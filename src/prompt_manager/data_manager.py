#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提示词数据管理器
负责提示词数据的增删改查、导入导出等核心功能
"""

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from collections import defaultdict


class PromptDataManager:
    """提示词数据管理器"""
    
    def __init__(self, database_path: str = "data/database/prompts_database.json"):
        self.database_path = database_path
        self.backup_dir = "data/database/backups"
        self.export_dir = "data/exports"
        
        # 确保目录存在
        Path(self.database_path).parent.mkdir(parents=True, exist_ok=True)
        Path(self.backup_dir).mkdir(parents=True, exist_ok=True)
        Path(self.export_dir).mkdir(parents=True, exist_ok=True)
        
        # 预定义标签
        self.predefined_tags = [
            "solo_girl", "solo_boy", "couple", "multiple_girls", 
            "multiple_boys", "group", "futanari", "unknown"
        ]
        
        # 加载数据
        self.data = self._load_database()
    
    def _load_database(self) -> Dict[str, Any]:
        """加载数据库"""
        if os.path.exists(self.database_path):
            try:
                with open(self.database_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 确保数据结构正确
                    if "prompts" not in data:
                        data = {"prompts": [], "next_id": 1}
                    if "next_id" not in data:
                        # 如果没有next_id，根据现有数据计算
                        max_id = 0
                        for prompt in data["prompts"]:
                            if isinstance(prompt.get("id"), int):
                                max_id = max(max_id, prompt["id"])
                        data["next_id"] = max_id + 1
                    return data
            except (json.JSONDecodeError, Exception) as e:
                print(f"加载数据库失败: {e}，创建新的数据库")
                return {"prompts": [], "next_id": 1}
        else:
            return {"prompts": [], "next_id": 1}
    
    def _save_database(self) -> bool:
        """保存数据库"""
        try:
            # 创建备份
            if os.path.exists(self.database_path):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = os.path.join(self.backup_dir, f"backup_{timestamp}.json")
                shutil.copy2(self.database_path, backup_file)
            
            # 保存数据
            with open(self.database_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存数据库失败: {e}")
            return False
    
    def analyze_character_count(self, content: str) -> Tuple[int, int, str]:
        """
        分析内容中的人物数量信息（复用split_action_by_characters.py的逻辑）
        返回: (girls_count, boys_count, category)
        """
        if not content:
            return 0, 0, "unknown"
        
        text = content.lower()
        
        girls_count = 0
        boys_count = 0
        
        # 匹配具体数字的女性关键词
        female_patterns = [
            r'(\d+)\s*(?:girl|woman|women)',
            r'(\d+)(?:girl|woman|women)',
        ]
        
        for pattern in female_patterns:
            matches = re.findall(pattern, text)
            if matches:
                girls_count = max(girls_count, max([int(x) for x in matches]))
        
        # 匹配具体数字的男性关键词
        male_patterns = [
            r'(\d+)\s*(?:boy|man|men)',
            r'(\d+)(?:boy|man|men)',
        ]
        
        for pattern in male_patterns:
            matches = re.findall(pattern, text)
            if matches:
                boys_count = max(boys_count, max([int(x) for x in matches]))
        
        # 检查multiple关键词
        if any(phrase in text for phrase in ['multiple girls', 'multiple women']):
            girls_count = max(girls_count, 2)
        if any(phrase in text for phrase in ['multiple boys', 'multiple men']):
            boys_count = max(boys_count, 2)
        
        # 检查特殊情况
        if '3+boys' in text or '6+boys' in text:
            boys_count = max(boys_count, 3)
        
        # 检查无空格的数字+关键词组合
        if '2girls' in text or '2women' in text:
            girls_count = max(girls_count, 2)
        if '3girls' in text or '3women' in text:
            girls_count = max(girls_count, 3)
        if '2boys' in text or '2men' in text:
            boys_count = max(boys_count, 2)
        if '3boys' in text or '3men' in text:
            boys_count = max(boys_count, 3)
        
        # 检查复数形式
        if girls_count == 0 and boys_count == 0:
            if 'women' in text and 'men' in text:
                girls_count = 2
                boys_count = 2
            elif 'women' in text:
                girls_count = 2
            elif 'men' in text and not any(fw in text.lower() for fw in ['woman', 'female']):
                boys_count = 2
        
        # 检查通用的女性词汇
        if girls_count == 0:
            female_words = ['woman', 'female', 'girl']
            for word in female_words:
                word_variants = [word, word.title(), word.upper()]
                for variant in word_variants:
                    if variant in text:
                        girls_count = 1
                        break
                if girls_count > 0:
                    break
        
        # 检查通用的男性词汇
        if boys_count == 0:
            male_words = ['man', 'male', 'boy']
            for word in male_words:
                word_variants = [word, word.title(), word.upper()]
                for variant in word_variants:
                    if variant in text:
                        boys_count = 1
                        break
                if boys_count > 0:
                    break
        
        # 检查solo
        if 'solo' in text and girls_count == 0 and boys_count == 0:
            girls_count = 1
        
        # 检查futanari
        if 'futanari' in text or 'futa' in text:
            return girls_count, boys_count, "futanari"
        
        # 通过身体部位推断性别
        if girls_count == 0 and boys_count == 0:
            female_body_parts = ['pussy', 'vagina', 'vaginal', 'breasts', 'nipples', 'clitoris']
            male_body_parts = ['penis', 'testicles', 'cock', 'dick']
            
            has_female_parts = any(part in text for part in female_body_parts)
            has_male_parts = any(part in text for part in male_body_parts)
            
            if has_female_parts and has_male_parts:
                girls_count = 1
                boys_count = 1
            elif has_female_parts:
                girls_count = 1
            elif has_male_parts and not has_female_parts:
                boys_count = 1
        
        # 检查特定的性行为描述
        if girls_count == 0 and boys_count == 0:
            couple_activities = ['hetero', 'after sex', 'creampie', 'cumshot']
            if any(activity in text for activity in couple_activities):
                girls_count = 1
                boys_count = 1
            
            solo_activities = ['masturbation', 'solo']
            if any(activity in text for activity in solo_activities):
                girls_count = 1
            
            oral_activities = ['fellatio', 'blowjob', 'deepthroat']
            if any(activity in text for activity in oral_activities):
                girls_count = 1
                boys_count = 1
            
            manual_activities = ['handjob', 'hand job']
            if any(activity in text for activity in manual_activities):
                girls_count = 1
                boys_count = 1
        
        # 确定类别
        if girls_count == 0 and boys_count == 0:
            return 0, 0, "unknown"
        elif girls_count == 1 and boys_count == 0:
            return girls_count, boys_count, "solo_girl"
        elif girls_count == 0 and boys_count == 1:
            return girls_count, boys_count, "solo_boy"
        elif girls_count == 1 and boys_count == 1:
            return girls_count, boys_count, "couple"
        elif girls_count > 1 and boys_count == 0:
            return girls_count, boys_count, "multiple_girls"
        elif girls_count == 0 and boys_count > 1:
            return girls_count, boys_count, "multiple_boys"
        elif girls_count > 1 or boys_count > 1:
            return girls_count, boys_count, "group"
        else:
            return girls_count, boys_count, "unknown"
    
    def add_prompt(self, name: str, content: str, level: str, tags: List[str] = None) -> Dict[str, Any]:
        """添加新的提示词"""
        if not name or not content:
            raise ValueError("名称和内容不能为空")
        
        # 检查重复名称并自动重命名
        original_name = name
        counter = 1
        while self.get_prompt_by_name(name):
            name = f"{original_name}_{counter}"
            counter += 1
        
        # 如果没有提供tags，自动分析
        if tags is None:
            _, _, auto_tag = self.analyze_character_count(content)
            tags = [auto_tag] if auto_tag != "unknown" else []
        
        prompt = {
            "id": self.data["next_id"],
            "name": name,
            "content": content,
            "level": level,
            "tags": tags or [],
            "created_time": datetime.now().isoformat(),
            "updated_time": datetime.now().isoformat()
        }
        
        self.data["prompts"].append(prompt)
        self.data["next_id"] += 1
        
        if self._save_database():
            return prompt
        else:
            # 如果保存失败，回滚
            self.data["prompts"].pop()
            self.data["next_id"] -= 1
            raise Exception("保存失败")
    
    def update_prompt(self, prompt_id: int, **kwargs) -> bool:
        """更新提示词"""
        prompt = self.get_prompt_by_id(prompt_id)
        if not prompt:
            return False
        
        # 更新字段
        for key, value in kwargs.items():
            if key in ["name", "content", "level", "tags"]:
                prompt[key] = value
        
        prompt["updated_time"] = datetime.now().isoformat()
        return self._save_database()
    
    def delete_prompt(self, prompt_id: int) -> bool:
        """删除提示词"""
        for i, prompt in enumerate(self.data["prompts"]):
            if prompt["id"] == prompt_id:
                self.data["prompts"].pop(i)
                return self._save_database()
        return False
    
    def delete_prompts_batch(self, prompt_ids: List[int]) -> int:
        """批量删除提示词，返回成功删除的数量"""
        deleted_count = 0
        self.data["prompts"] = [
            prompt for prompt in self.data["prompts"] 
            if prompt["id"] not in prompt_ids or (deleted_count := deleted_count + 1, False)[1]
        ]
        
        if self._save_database():
            return len(prompt_ids)
        return 0
    
    def get_prompt_by_id(self, prompt_id: int) -> Optional[Dict[str, Any]]:
        """根据ID获取提示词"""
        for prompt in self.data["prompts"]:
            if prompt["id"] == prompt_id:
                return prompt
        return None
    
    def get_prompt_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """根据名称获取提示词"""
        for prompt in self.data["prompts"]:
            if prompt["name"] == name:
                return prompt
        return None
    
    def search_prompts(self, query: str = "", level: str = "", tags: List[str] = None, 
                      page: int = 1, page_size: int = 50) -> Dict[str, Any]:
        """搜索提示词"""
        results = []
        
        for prompt in self.data["prompts"]:
            # 文本搜索
            if query:
                if (query.lower() not in prompt["name"].lower() and 
                    query.lower() not in prompt["content"].lower()):
                    continue
            
            # 级别筛选
            if level and prompt["level"] != level:
                continue
            
            # 标签筛选
            if tags:
                if not any(tag in prompt["tags"] for tag in tags):
                    continue
            
            results.append(prompt)
        
        # 分页
        total = len(results)
        start = (page - 1) * page_size
        end = start + page_size
        page_results = results[start:end]
        
        return {
            "prompts": page_results,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size
        }
    
    def get_all_tags(self) -> List[str]:
        """获取所有使用过的标签"""
        all_tags = set(self.predefined_tags)
        for prompt in self.data["prompts"]:
            all_tags.update(prompt.get("tags", []))
        return sorted(list(all_tags))
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        total_prompts = len(self.data["prompts"])
        
        # 按级别统计
        level_stats = defaultdict(int)
        for prompt in self.data["prompts"]:
            level_stats[prompt["level"]] += 1
        
        # 按标签统计
        tag_stats = defaultdict(int)
        for prompt in self.data["prompts"]:
            for tag in prompt.get("tags", []):
                tag_stats[tag] += 1
        
        return {
            "total_prompts": total_prompts,
            "level_distribution": dict(level_stats),
            "tag_distribution": dict(tag_stats)
        }
    
    def import_from_json(self, file_path: str, level: str = None) -> Dict[str, Any]:
        """从JSON文件导入数据"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 如果没有指定level，尝试从文件路径推断
            if not level:
                if "level_1_visual" in file_path:
                    level = "level_1_visual"
                elif "level_2_seductive" in file_path:
                    level = "level_2_seductive"
                elif "level_3_explicit" in file_path:
                    level = "level_3_explicit"
                else:
                    level = "level_1_visual"  # 默认级别
            
            imported_count = 0
            skipped_count = 0
            
            for name, content in data.items():
                if not content or content.strip() == "":
                    skipped_count += 1
                    continue
                
                try:
                    self.add_prompt(name, content, level)
                    imported_count += 1
                except Exception as e:
                    print(f"导入词条 '{name}' 失败: {e}")
                    skipped_count += 1
            
            return {
                "success": True,
                "imported": imported_count,
                "skipped": skipped_count,
                "total": len(data)
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def export_to_json(self, file_path: str, level: str = None, tags: List[str] = None, 
                      format_type: str = "full") -> bool:
        """导出数据到JSON文件"""
        try:
            # 获取要导出的数据
            export_data = []
            for prompt in self.data["prompts"]:
                # 级别筛选
                if level and prompt["level"] != level:
                    continue
                
                # 标签筛选
                if tags and not any(tag in prompt["tags"] for tag in tags):
                    continue
                
                export_data.append(prompt)
            
            # 根据格式类型准备数据
            if format_type == "batch_compatible":
                # 导出为batch_action_generator.py兼容格式
                output = {prompt["name"]: prompt["content"] for prompt in export_data}
            else:
                # 导出完整格式
                output = {"prompts": export_data}
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(output, f, ensure_ascii=False, indent=2)
            
            return True
        
        except Exception as e:
            print(f"导出失败: {e}")
            return False
    
    def batch_update_level(self, prompt_ids: List[int], new_level: str) -> int:
        """批量更新级别"""
        updated_count = 0
        for prompt_id in prompt_ids:
            if self.update_prompt(prompt_id, level=new_level):
                updated_count += 1
        return updated_count
    
    def batch_update_tags(self, prompt_ids: List[int], new_tags: List[str], mode: str = "replace") -> int:
        """批量更新标签
        mode: "replace" 替换, "add" 添加, "remove" 移除
        """
        updated_count = 0
        for prompt_id in prompt_ids:
            prompt = self.get_prompt_by_id(prompt_id)
            if not prompt:
                continue
            
            current_tags = prompt.get("tags", [])
            
            if mode == "replace":
                updated_tags = new_tags
            elif mode == "add":
                updated_tags = list(set(current_tags + new_tags))
            elif mode == "remove":
                updated_tags = [tag for tag in current_tags if tag not in new_tags]
            else:
                continue
            
            if self.update_prompt(prompt_id, tags=updated_tags):
                updated_count += 1
        
        return updated_count
