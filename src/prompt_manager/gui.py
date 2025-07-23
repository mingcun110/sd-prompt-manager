#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gradio用户界面
提供提示词管理的Web界面
"""

import gradio as gr
import os
from typing import List, Tuple
from .data_manager import PromptDataManager


class PromptManagerGUI:
    """提示词管理器GUI"""
    
    def __init__(self):
        self.data_manager = PromptDataManager()
        self.selected_prompt_ids = []
        
        # 级别选项
        self.level_options = ["level_1_visual", "level_2_seductive", "level_3_explicit"]
        
        # 当前页面状态
        self.current_page = 1
        self.current_search_query = ""
        self.current_level_filter = ""
        self.current_tag_filter = []
    
    def create_interface(self):
        """创建Gradio界面"""
        with gr.Blocks(title="提示词管理器", theme=gr.themes.Soft()) as interface:
            gr.Markdown("# 🎨 Stable Diffusion 提示词管理器")
            
            with gr.Tabs():
                # 第一页：词条管理
                with gr.TabItem("📚 词条管理"):
                    self._create_management_tab()
                
                # 第二页：统计分析（预留）
                with gr.TabItem("📊 统计分析"):
                    self._create_analytics_tab()
        
        return interface
    
    def _create_management_tab(self):
        """创建词条管理标签页"""
        
        # 顶部：数据导入区域
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 📥 数据导入")
                import_file = gr.File(
                    label="选择JSON文件",
                    file_types=[".json"],
                    file_count="single"
                )
                with gr.Row():
                    import_level = gr.Dropdown(
                        choices=[""] + self.level_options,
                        label="指定级别（留空自动推断）",
                        value="",
                        allow_custom_value=False,
                        scale=2
                    )
                    import_btn = gr.Button("导入数据", variant="primary", scale=1)
                import_status = gr.Textbox(label="导入状态", interactive=False)
        
        # 分割线
        gr.Markdown("---")
        
        # 中部：搜索/筛选区域
        with gr.Row():
            search_query = gr.Textbox(
                label="🔍 搜索",
                placeholder="搜索词条名称或内容...",
                scale=3
            )
            level_filter = gr.Dropdown(
                choices=[""] + self.level_options,
                label="级别筛选",
                value="",
                scale=1
            )
            tag_filter = gr.Dropdown(
                choices=self._get_all_tags(),
                label="标签筛选",
                multiselect=True,
                scale=2
            )
            search_btn = gr.Button("搜索", variant="primary", scale=1)
        
        # 批量操作区域
        with gr.Row():
            with gr.Column(scale=2):
                selected_info = gr.Textbox(
                    label="已选择的词条",
                    value="未选择任何词条",
                    interactive=False
                )
            with gr.Column(scale=1):
                batch_level_update = gr.Dropdown(
                    choices=[""] + self.level_options,
                    label="批量修改级别",
                    value=""
                )
                batch_level_btn = gr.Button("应用级别", size="sm")
            with gr.Column(scale=1):
                batch_tag_update = gr.Dropdown(
                    choices=self._get_all_tags(),
                    label="批量修改标签",
                    multiselect=True
                )
                batch_tag_mode = gr.Radio(
                    choices=["replace", "add", "remove"],
                    label="标签操作",
                    value="add"
                )
                batch_tag_btn = gr.Button("应用标签", size="sm")
            with gr.Column(scale=1):
                batch_delete_btn = gr.Button("批量删除", variant="stop", size="sm")
        
        # 分割线
        gr.Markdown("---")
        
        # 主体：词条列表和详情编辑
        with gr.Row():
            with gr.Column(scale=2):
                # 词条列表
                prompt_list = gr.Dataframe(
                    headers=["选择", "ID", "名称", "级别", "标签", "创建时间"],
                    datatype=["bool", "number", "str", "str", "str", "str"],
                    label="词条列表",
                    interactive=True,
                    wrap=True,
                    max_height=400
                )
                
                # 分页控制
                with gr.Row():
                    prev_page_btn = gr.Button("⬅️ 上一页", size="sm")
                    page_info = gr.Textbox(
                        value="第 1 页，共 1 页",
                        interactive=False,
                        scale=2
                    )
                    next_page_btn = gr.Button("下一页 ➡️", size="sm")
                    page_size_selector = gr.Dropdown(
                        choices=[20, 50, 100],
                        value=50,
                        label="每页显示",
                        scale=1
                    )
            
            with gr.Column(scale=1):
                # 词条详情编辑
                gr.Markdown("### ✏️ 词条编辑")
                
                edit_prompt_id = gr.Number(
                    label="词条ID",
                    visible=False
                )
                edit_name = gr.Textbox(
                    label="名称",
                    placeholder="输入词条名称..."
                )
                edit_content = gr.Textbox(
                    label="内容",
                    placeholder="输入提示词内容...",
                    lines=6
                )
                edit_level = gr.Dropdown(
                    choices=self.level_options,
                    label="级别",
                    value="level_1_visual"
                )
                edit_tags = gr.Dropdown(
                    choices=self._get_all_tags(),
                    label="标签",
                    multiselect=True,
                    allow_custom_value=True
                )
                
                with gr.Row():
                    add_btn = gr.Button("添加词条", variant="primary")
                    update_btn = gr.Button("更新词条", variant="secondary")
                    delete_btn = gr.Button("删除词条", variant="stop")
                
                edit_status = gr.Textbox(label="操作状态", interactive=False)
        
        # 分割线
        gr.Markdown("---")
        
        # 底部：数据导出区域
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 📤 数据导出")
                with gr.Row():
                    export_level_filter = gr.Dropdown(
                        choices=[""] + self.level_options,
                        label="按级别筛选（留空导出全部）",
                        value="",
                        scale=1
                    )
                    export_tag_filter = gr.Dropdown(
                        choices=self._get_all_tags(),
                        label="按标签筛选",
                        multiselect=True,
                        scale=2
                    )
                    export_format = gr.Radio(
                        choices=["full", "batch_compatible"],
                        label="导出格式",
                        value="full",
                        info="full: 完整格式, batch_compatible: 兼容批量脚本格式",
                        scale=1
                    )
                    export_btn = gr.Button("导出数据", variant="secondary", scale=1)
                export_status = gr.Textbox(label="导出状态", interactive=False)
        
        # 事件绑定
        self._bind_events(
            # 导入导出
            import_btn, import_file, import_level, import_status,
            export_btn, export_level_filter, export_tag_filter, export_format, export_status,
            
            # 搜索筛选
            search_btn, search_query, level_filter, tag_filter,
            
            # 词条列表和分页
            prompt_list, prev_page_btn, next_page_btn, page_info, page_size_selector,
            
            # 词条编辑
            edit_prompt_id, edit_name, edit_content, edit_level, edit_tags,
            add_btn, update_btn, delete_btn, edit_status,
            
            # 批量操作
            selected_info, batch_level_update, batch_level_btn,
            batch_tag_update, batch_tag_mode, batch_tag_btn, batch_delete_btn
        )
    
    def _create_analytics_tab(self):
        """创建统计分析标签页（预留）"""
        gr.Markdown("## 📊 统计分析功能")
        gr.Markdown("此功能将在后续版本中实现，敬请期待...")
        
        # 显示基本统计信息
        stats = self.data_manager.get_statistics()
        
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 📈 基本统计")
                gr.Markdown(f"- **词条总数**: {stats['total_prompts']}")
                
                if stats['level_distribution']:
                    gr.Markdown("#### 级别分布:")
                    for level, count in stats['level_distribution'].items():
                        gr.Markdown(f"- {level}: {count}")
            
            with gr.Column():
                if stats['tag_distribution']:
                    gr.Markdown("#### 标签分布 (Top 10):")
                    sorted_tags = sorted(stats['tag_distribution'].items(), 
                                       key=lambda x: x[1], reverse=True)[:10]
                    for tag, count in sorted_tags:
                        gr.Markdown(f"- {tag}: {count}")
    
    def _get_all_tags(self) -> List[str]:
        """获取所有标签"""
        return self.data_manager.get_all_tags()
    
    def _bind_events(self, *components):
        """绑定所有事件"""
        (import_btn, import_file, import_level, import_status,
         export_btn, export_level_filter, export_tag_filter, export_format, export_status,
         search_btn, search_query, level_filter, tag_filter,
         prompt_list, prev_page_btn, next_page_btn, page_info, page_size_selector,
         edit_prompt_id, edit_name, edit_content, edit_level, edit_tags,
         add_btn, update_btn, delete_btn, edit_status,
         selected_info, batch_level_update, batch_level_btn,
         batch_tag_update, batch_tag_mode, batch_tag_btn, batch_delete_btn) = components
        
        # 导入数据
        import_btn.click(
            fn=self._import_data,
            inputs=[import_file, import_level],
            outputs=[import_status, prompt_list, page_info]
        )
        
        # 导出数据
        export_btn.click(
            fn=self._export_data,
            inputs=[export_level_filter, export_tag_filter, export_format],
            outputs=[export_status]
        )
        
        # 搜索
        search_btn.click(
            fn=self._search_prompts,
            inputs=[search_query, level_filter, tag_filter, page_size_selector],
            outputs=[prompt_list, page_info]
        )
        
        # 分页
        prev_page_btn.click(
            fn=self._prev_page,
            inputs=[search_query, level_filter, tag_filter, page_size_selector],
            outputs=[prompt_list, page_info]
        )
        
        next_page_btn.click(
            fn=self._next_page,
            inputs=[search_query, level_filter, tag_filter, page_size_selector],
            outputs=[prompt_list, page_info]
        )
        
        # 词条编辑
        add_btn.click(
            fn=self._add_prompt,
            inputs=[edit_name, edit_content, edit_level, edit_tags],
            outputs=[edit_status, prompt_list, page_info, edit_name, edit_content, edit_tags]
        )
        
        update_btn.click(
            fn=self._update_prompt,
            inputs=[edit_prompt_id, edit_name, edit_content, edit_level, edit_tags],
            outputs=[edit_status, prompt_list]
        )
        
        delete_btn.click(
            fn=self._delete_prompt,
            inputs=[edit_prompt_id],
            outputs=[edit_status, prompt_list, page_info, edit_prompt_id, edit_name, edit_content, edit_tags]
        )
        
        # 批量操作
        batch_level_btn.click(
            fn=self._batch_update_level,
            inputs=[prompt_list, batch_level_update],
            outputs=[edit_status, prompt_list]
        )
        
        batch_tag_btn.click(
            fn=self._batch_update_tags,
            inputs=[prompt_list, batch_tag_update, batch_tag_mode],
            outputs=[edit_status, prompt_list]
        )
        
        batch_delete_btn.click(
            fn=self._batch_delete,
            inputs=[prompt_list],
            outputs=[edit_status, prompt_list, page_info]
        )
        
        # 选择词条时更新编辑区域
        prompt_list.select(
            fn=self._select_prompt,
            inputs=[prompt_list],
            outputs=[edit_prompt_id, edit_name, edit_content, edit_level, edit_tags, selected_info]
        )
    
    def _import_data(self, file_info, level: str) -> Tuple[str, List[List], str]:
        """导入数据"""
        if not file_info:
            return "请选择要导入的文件", [], "第 1 页，共 1 页"
        
        try:
            result = self.data_manager.import_from_json(file_info.name, level or None)
            
            if result["success"]:
                status = f"导入成功！导入 {result['imported']} 条，跳过 {result['skipped']} 条"
                # 刷新列表
                prompt_data, page_info = self._get_prompt_list()
                return status, prompt_data, page_info
            else:
                return f"导入失败：{result['error']}", [], "第 1 页，共 1 页"
        
        except Exception as e:
            return f"导入失败：{str(e)}", [], "第 1 页，共 1 页"
    
    def _export_data(self, level_filter: str, tag_filter: List[str], format_type: str) -> str:
        """导出数据"""
        try:
            # 生成文件名
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if format_type == "batch_compatible":
                filename = f"prompts_batch_{timestamp}.json"
            else:
                filename = f"prompts_full_{timestamp}.json"
            
            file_path = os.path.join(self.data_manager.export_dir, filename)
            
            # 导出
            success = self.data_manager.export_to_json(
                file_path, 
                level=level_filter or None,
                tags=tag_filter or None,
                format_type=format_type
            )
            
            if success:
                return f"导出成功！文件保存至：{file_path}"
            else:
                return "导出失败"
        
        except Exception as e:
            return f"导出失败：{str(e)}"
    
    def _search_prompts(self, query: str, level: str, tags: List[str], 
                       page_size: int) -> Tuple[List[List], str]:
        """搜索提示词"""
        self.current_page = 1
        self.current_search_query = query
        self.current_level_filter = level
        self.current_tag_filter = tags
        
        return self._get_prompt_list(page_size)
    
    def _get_prompt_list(self, page_size: int = 50) -> Tuple[List[List], str]:
        """获取提示词列表"""
        result = self.data_manager.search_prompts(
            query=self.current_search_query,
            level=self.current_level_filter,
            tags=self.current_tag_filter,
            page=self.current_page,
            page_size=page_size
        )
        
        # 转换为表格数据
        table_data = []
        for prompt in result["prompts"]:
            table_data.append([
                False,  # 选择框
                prompt["id"],
                prompt["name"],
                prompt["level"],
                ", ".join(prompt["tags"]),
                prompt["created_time"][:16]  # 只显示日期和时间
            ])
        
        page_info = f"第 {result['page']} 页，共 {result['total_pages']} 页（总计 {result['total']} 条）"
        
        return table_data, page_info
    
    def _prev_page(self, query: str, level: str, tags: List[str], 
                   page_size: int) -> Tuple[List[List], str]:
        """上一页"""
        if self.current_page > 1:
            self.current_page -= 1
        return self._get_prompt_list(page_size)
    
    def _next_page(self, query: str, level: str, tags: List[str], 
                   page_size: int) -> Tuple[List[List], str]:
        """下一页"""
        # 先获取当前结果以检查是否有下一页
        result = self.data_manager.search_prompts(
            query=self.current_search_query,
            level=self.current_level_filter,
            tags=self.current_tag_filter,
            page=self.current_page,
            page_size=page_size
        )
        
        if self.current_page < result["total_pages"]:
            self.current_page += 1
        
        return self._get_prompt_list(page_size)
    
    def _add_prompt(self, name: str, content: str, level: str, 
                   tags: List[str]) -> Tuple[str, List[List], str, str, str, List[str]]:
        """添加提示词"""
        try:
            if not name or not content:
                return "名称和内容不能为空", [], "第 1 页，共 1 页", name, content, tags
            
            self.data_manager.add_prompt(name, content, level, tags)
            
            # 刷新列表
            prompt_data, page_info = self._get_prompt_list()
            
            return "添加成功！", prompt_data, page_info, "", "", []
        
        except Exception as e:
            return f"添加失败：{str(e)}", [], "第 1 页，共 1 页", name, content, tags
    
    def _update_prompt(self, prompt_id: int, name: str, content: str, 
                      level: str, tags: List[str]) -> Tuple[str, List[List]]:
        """更新提示词"""
        try:
            if not prompt_id:
                return "请先选择要更新的词条", []
            
            success = self.data_manager.update_prompt(
                prompt_id,
                name=name,
                content=content,
                level=level,
                tags=tags
            )
            
            if success:
                # 刷新列表
                prompt_data, _ = self._get_prompt_list()
                return "更新成功！", prompt_data
            else:
                return "更新失败", []
        
        except Exception as e:
            return f"更新失败：{str(e)}", []
    
    def _delete_prompt(self, prompt_id: int) -> Tuple[str, List[List], str, int, str, str, List[str]]:
        """删除提示词（带确认）"""
        try:
            if not prompt_id:
                return "请先选择要删除的词条", [], "第 1 页，共 1 页", 0, "", "", []
            
            # 这里应该显示确认对话框，但Gradio的限制使得需要用户手动确认
            # 实际删除操作
            success = self.data_manager.delete_prompt(prompt_id)
            
            if success:
                # 刷新列表
                prompt_data, page_info = self._get_prompt_list()
                return "删除成功！", prompt_data, page_info, 0, "", "", []
            else:
                return "删除失败", [], "第 1 页，共 1 页", prompt_id, "", "", []
        
        except Exception as e:
            return f"删除失败：{str(e)}", [], "第 1 页，共 1 页", prompt_id, "", "", []
    
    def _select_prompt(self, prompt_list_data) -> Tuple[int, str, str, str, List[str], str]:
        """选择提示词时更新编辑区域"""
        if prompt_list_data is None or len(prompt_list_data) == 0:
            return 0, "", "", "level_1_visual", [], "未选择任何词条"
        
        # 获取选中的行
        selected_rows = []
        for i, row in enumerate(prompt_list_data):
            if len(row) > 0 and row[0]:  # 选择框为True
                selected_rows.append(row)
        
        if not selected_rows:
            return 0, "", "", "level_1_visual", [], "未选择任何词条"
        
        # 更新选择状态信息
        selected_info = f"已选择 {len(selected_rows)} 个词条"
        
        # 如果只选择了一个，填充编辑区域
        if len(selected_rows) == 1:
            row = selected_rows[0]
            if len(row) >= 6:  # 确保行有足够的列
                prompt_id = int(row[1])
                prompt = self.data_manager.get_prompt_by_id(prompt_id)
                
                if prompt:
                    return (prompt_id, prompt["name"], prompt["content"], 
                           prompt["level"], prompt["tags"], selected_info)
        
        return 0, "", "", "level_1_visual", [], selected_info
    
    def _batch_update_level(self, prompt_list_data, new_level: str) -> Tuple[str, List[List]]:
        """批量更新级别"""
        try:
            if not new_level:
                return "请选择要更新的级别", []
            
            # 获取选中的词条ID
            selected_ids = []
            if prompt_list_data:
                for row in prompt_list_data:
                    if len(row) > 0 and row[0]:  # 选择框为True
                        selected_ids.append(int(row[1]))
            
            if not selected_ids:
                return "请先选择要更新的词条", []
            
            updated_count = self.data_manager.batch_update_level(selected_ids, new_level)
            
            # 刷新列表
            prompt_data, _ = self._get_prompt_list()
            
            return f"批量更新成功！更新了 {updated_count} 个词条的级别", prompt_data
        
        except Exception as e:
            return f"批量更新失败：{str(e)}", []
    
    def _batch_update_tags(self, prompt_list_data, new_tags: List[str], 
                          mode: str) -> Tuple[str, List[List]]:
        """批量更新标签"""
        try:
            if not new_tags:
                return "请选择要操作的标签", []
            
            # 获取选中的词条ID
            selected_ids = []
            if prompt_list_data:
                for row in prompt_list_data:
                    if len(row) > 0 and row[0]:  # 选择框为True
                        selected_ids.append(int(row[1]))
            
            if not selected_ids:
                return "请先选择要更新的词条", []
            
            updated_count = self.data_manager.batch_update_tags(selected_ids, new_tags, mode)
            
            # 刷新列表
            prompt_data, _ = self._get_prompt_list()
            
            mode_text = {"replace": "替换", "add": "添加", "remove": "移除"}[mode]
            return f"批量{mode_text}标签成功！更新了 {updated_count} 个词条", prompt_data
        
        except Exception as e:
            return f"批量更新标签失败：{str(e)}", []
    
    def _batch_delete(self, prompt_list_data) -> Tuple[str, List[List], str]:
        """批量删除（带确认）"""
        try:
            # 获取选中的词条ID
            selected_ids = []
            if prompt_list_data:
                for row in prompt_list_data:
                    if len(row) > 0 and row[0]:  # 选择框为True
                        selected_ids.append(int(row[1]))
            
            if not selected_ids:
                return "请先选择要删除的词条", [], "第 1 页，共 1 页"
            
            # 这里应该显示确认对话框
            deleted_count = self.data_manager.delete_prompts_batch(selected_ids)
            
            # 刷新列表
            prompt_data, page_info = self._get_prompt_list()
            
            return f"批量删除成功！删除了 {deleted_count} 个词条", prompt_data, page_info
        
        except Exception as e:
            return f"批量删除失败：{str(e)}", [], "第 1 页，共 1 页"


def create_app():
    """创建并返回Gradio应用"""
    gui = PromptManagerGUI()
    return gui.create_interface()


if __name__ == "__main__":
    app = create_app()
    app.launch(share=False, server_name="127.0.0.1", server_port=7860)
