import json
import os
import copy
import modules.scripts as scripts
import gradio as gr

from modules import errors
from modules.processing import Processed, process_images
from modules.shared import state


class Script(scripts.Script):
    def title(self):
        return "Batch Action Generator"

    def ui(self, is_img2img):
        # Action JSON file path input
        action_file_path = gr.Textbox(
            label="Action JSON file path",
            value="scripts/action.json",
            placeholder="Enter the path to your action.json file",
            elem_id=self.elem_id("action_file_path"),
        )

        # Options for batch processing
        with gr.Row():
            iterate_seed = gr.Checkbox(
                label="Use different seed for each action",
                value=True,
                elem_id=self.elem_id("iterate_seed"),
            )
            include_action_name = gr.Checkbox(
                label="Include action name in filename",
                value=True,
                elem_id=self.elem_id("include_action_name"),
            )

        # Prompt combination options
        prompt_position = gr.Radio(
            ["start", "end", "replace"],
            label="Action prompt position",
            value="end",
            info="start: action + original prompt, end: original prompt + action, replace: use only action prompt",
            elem_id=self.elem_id("prompt_position"),
        )

        # Additional prompt prefix/suffix
        with gr.Row():
            prompt_prefix = gr.Textbox(
                label="Prompt prefix (added before everything)",
                placeholder="e.g., 'masterpiece, high quality, '",
                elem_id=self.elem_id("prompt_prefix"),
            )
            prompt_suffix = gr.Textbox(
                label="Prompt suffix (added after everything)",
                placeholder="e.g., ', professional photography'",
                elem_id=self.elem_id("prompt_suffix"),
            )

        # Preview loaded actions
        action_preview = gr.Textbox(
            label="Loaded actions preview",
            lines=5,
            interactive=False,
            elem_id=self.elem_id("action_preview"),
        )

        # Load button to preview actions
        load_actions_btn = gr.Button(
            "Load and Preview Actions", elem_id=self.elem_id("load_actions_btn")
        )

        def load_actions_preview(file_path):
            try:
                if not os.path.exists(file_path):
                    return f"Error: File '{file_path}' not found."

                with open(file_path, "r", encoding="utf-8") as f:
                    actions = json.load(f)

                if not isinstance(actions, dict):
                    return "Error: Invalid JSON format. Expected a dictionary."

                preview_text = f"Found {len(actions)} actions:\n\n"
                for i, (action_name, action_prompt) in enumerate(actions.items(), 1):
                    preview_text += f"{i}. {action_name}:\n   {action_prompt[:100]}{'...' if len(action_prompt) > 100 else ''}\n\n"

                return preview_text

            except json.JSONDecodeError as e:
                return f"Error: Invalid JSON format - {str(e)}"
            except Exception as e:
                return f"Error: {str(e)}"

        load_actions_btn.click(
            fn=load_actions_preview,
            inputs=[action_file_path],
            outputs=[action_preview],
            show_progress=False,
        )

        return [
            action_file_path,
            iterate_seed,
            include_action_name,
            prompt_position,
            prompt_prefix,
            prompt_suffix,
        ]

    def run(
        self,
        p,
        action_file_path,
        iterate_seed,
        include_action_name,
        prompt_position,
        prompt_prefix,
        prompt_suffix,
    ):
        # Load actions from JSON file
        try:
            if not os.path.exists(action_file_path):
                raise FileNotFoundError(f"Action file '{action_file_path}' not found.")

            with open(action_file_path, "r", encoding="utf-8") as f:
                actions = json.load(f)

            if not isinstance(actions, dict):
                raise ValueError("Invalid JSON format. Expected a dictionary.")

        except Exception as e:
            errors.report(f"Error loading action file: {str(e)}", exc_info=True)
            return Processed(p, [], p.seed, f"Error loading action file: {str(e)}")

        if not actions:
            return Processed(p, [], p.seed, "No actions found in the file.")

        # Disable grid saving for batch processing
        p.do_not_save_grid = True

        # Calculate total job count
        job_count = len(actions) * p.n_iter
        print(f"Will process {len(actions)} actions in {job_count} jobs.")

        # Set up job tracking
        state.job_count = job_count

        # Initialize result collections
        all_images = []
        all_prompts = []
        all_infotexts = []

        # Process each action
        for action_index, (action_name, action_prompt) in enumerate(actions.items(), 1):
            state.job = f"Action {action_index}/{len(actions)}: {action_name}"

            # Create a copy of the processing parameters
            copy_p = copy.copy(p)

            # Build the final prompt
            final_prompt = ""

            # Add prefix if specified
            if prompt_prefix.strip():
                final_prompt += prompt_prefix.strip() + " "

            # Combine prompts based on position setting
            if prompt_position == "replace":
                final_prompt += action_prompt
            elif prompt_position == "start":
                final_prompt += action_prompt
                if p.prompt.strip():
                    final_prompt += " " + p.prompt.strip()
            else:  # end
                if p.prompt.strip():
                    final_prompt += p.prompt.strip() + " "
                final_prompt += action_prompt

            # Add suffix if specified
            if prompt_suffix.strip():
                final_prompt += " " + prompt_suffix.strip()

            copy_p.prompt = final_prompt.strip()

            # Set up filename if include_action_name is enabled
            if include_action_name:
                # Clean action name for filename
                clean_action_name = "".join(
                    c for c in action_name if c.isalnum() or c in (" ", "-", "_")
                ).rstrip()
                clean_action_name = clean_action_name.replace(" ", "_")

                # We'll add the action name to the info text instead of modifying paths
                # to avoid filesystem issues

            # Adjust seed for iteration
            if iterate_seed and action_index > 1:
                if copy_p.seed != -1:
                    copy_p.seed = copy_p.seed + (action_index - 1) * 1000

            try:
                # Process the images for this action
                proc = process_images(copy_p)

                # Add action name to info text if requested
                if include_action_name:
                    modified_infotexts = []
                    for info in proc.infotexts:
                        modified_info = f"Action: {action_name}\n{info}"
                        modified_infotexts.append(modified_info)
                    proc.infotexts = modified_infotexts

                # Collect results
                all_images.extend(proc.images)
                all_prompts.extend(proc.all_prompts)
                all_infotexts.extend(proc.infotexts)

                print(
                    f"Completed action '{action_name}' - Generated {len(proc.images)} images"
                )

            except Exception as e:
                error_msg = f"Error processing action '{action_name}': {str(e)}"
                errors.report(error_msg, exc_info=True)
                print(error_msg)
                continue

        # Create final processed result
        if all_images:
            result_info = f"Batch processing completed. Generated {len(all_images)} images from {len(actions)} actions."
            return Processed(
                p,
                all_images,
                p.seed,
                result_info,
                all_prompts=all_prompts,
                infotexts=all_infotexts,
            )
        else:
            return Processed(
                p, [], p.seed, "No images were generated. Check the console for errors."
            )
