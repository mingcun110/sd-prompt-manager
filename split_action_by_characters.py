#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据人物数量将action.json拆分成多个文件的脚本
"""

import json
import os
import re
from collections import defaultdict
from pathlib import Path

def analyze_character_count(value_string):
    """
    分析字符串中的人物数量信息
    返回: (girls_count, boys_count, category)
    """
    if not value_string:
        return 0, 0, "unknown"
    
    # 转换为小写便于匹配
    text = value_string.lower()
    
    girls_count = 0
    boys_count = 0
    
    # 匹配具体数字的女性关键词 (支持空格分隔，如 "1 girl")
    female_patterns = [
        r'(\d+)\s*(?:girl|woman|women)',  # 1girl, 1 girl, 1woman, 1 woman
        r'(\d+)(?:girl|woman|women)',     # 1girl, 1woman (无空格)
    ]
    
    for pattern in female_patterns:
        matches = re.findall(pattern, text)
        if matches:
            girls_count = max(girls_count, max([int(x) for x in matches]))
    
    # 匹配具体数字的男性关键词 (支持空格分隔，如 "1 boy")
    male_patterns = [
        r'(\d+)\s*(?:boy|man|men)',  # 1boy, 1 boy, 1man, 1 man
        r'(\d+)(?:boy|man|men)',     # 1boy, 1man (无空格)
    ]
    
    for pattern in male_patterns:
        matches = re.findall(pattern, text)
        if matches:
            boys_count = max(boys_count, max([int(x) for x in matches]))
    
    # 检查multiple关键词
    if any(phrase in text for phrase in ['multiple girls', 'multiple women']):
        girls_count = max(girls_count, 2)  # multiple至少是2个
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
    
    # 检查复数形式（当没有数字时）
    if girls_count == 0 and boys_count == 0:
        if 'women' in text and 'men' in text:
            # 同时有男性和女性复数，表示群体
            girls_count = 2
            boys_count = 2
        elif 'women' in text:
            girls_count = 2
        elif 'men' in text and not any(fw in text.lower() for fw in ['woman', 'female']):
            boys_count = 2
    
    # 检查通用的女性词汇（包括大小写变体）
    if girls_count == 0:
        female_words = ['woman', 'female', 'girl']
        for word in female_words:
            # 检查各种大小写组合
            word_variants = [word, word.title(), word.upper()]
            for variant in word_variants:
                if variant in text:
                    girls_count = 1
                    break
    
    # 检查通用的男性词汇（包括大小写变体）
    if boys_count == 0:
        male_words = ['man', 'male', 'boy']
        for word in male_words:
            # 检查各种大小写组合，但要避免与女性词冲突
            word_variants = [word, word.title(), word.upper()]
            for variant in word_variants:
                if variant in text:
                    # 避免误识别包含女性词的情况
                    if not any(fw in text.lower() for fw in ['woman', 'female', 'girl']):
                        boys_count = 1
                        break
    
    # 检查solo (优先于单词识别)
    if 'solo' in text and girls_count == 0 and boys_count == 0:
        girls_count = 1
    
    # 检查futanari
    if 'futanari' in text or 'futa' in text:
        return girls_count, boys_count, "futanari"
    
    # 通过身体部位推断性别（当没有明确数字时）
    if girls_count == 0 and boys_count == 0:
        # 女性身体部位
        female_body_parts = ['pussy', 'vagina', 'vaginal', 'breasts', 'nipples', 'clitoris']
        male_body_parts = ['penis', 'testicles', 'cock', 'dick']
        
        has_female_parts = any(part in text for part in female_body_parts)
        has_male_parts = any(part in text for part in male_body_parts)
        
        if has_female_parts and has_male_parts:
            # 同时有男女性特征，可能是异性恋
            girls_count = 1
            boys_count = 1
        elif has_female_parts:
            girls_count = 1
        elif has_male_parts and not has_female_parts:
            # 只有男性部位且没有女性词汇
            boys_count = 1
    
    # 检查特定的性行为描述来推断人数
    if girls_count == 0 and boys_count == 0:
        # 一些明确的性行为通常涉及两个人
        couple_activities = ['hetero', 'after sex', 'creampie', 'cumshot']
        if any(activity in text for activity in couple_activities):
            girls_count = 1
            boys_count = 1
        
        # 一些明确的单人活动
        solo_activities = ['masturbation', 'solo']
        if any(activity in text for activity in solo_activities):
            girls_count = 1  # 默认假设为女性
        
        # 一些通常涉及口交的活动（通常是异性恋）
        oral_activities = ['fellatio', 'blowjob', 'deepthroat']
        if any(activity in text for activity in oral_activities):
            girls_count = 1
            boys_count = 1
        
        # 手工活动通常也涉及两人
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
        return girls_count, boys_count, "mixed"

def split_action_json(input_files=["action.json"], output_dir="split_actions"):
    """
    拆分action.json文件，支持多个输入文件
    input_files: 输入文件列表，默认为["action.json"]
    """
    # 合并所有输入文件的数据
    action_data = {}
    
    for input_file in input_files:
        if not os.path.exists(input_file):
            print(f"警告: 文件 {input_file} 不存在，跳过...")
            continue
            
        print(f"正在读取文件: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            file_data = json.load(f)
            
        # 检查是否有重复的键
        for key, value in file_data.items():
            if key in action_data:
                print(f"警告: 发现重复的动作名称 '{key}'，将使用来自 {input_file} 的版本")
            action_data[key] = value
            
        print(f"  从 {input_file} 读取了 {len(file_data)} 个动作")
    
    print(f"\n总计合并了 {len(action_data)} 个动作")
    
    # 创建输出目录
    Path(output_dir).mkdir(exist_ok=True)
    
    # 按类别分组
    categories = defaultdict(dict)
    
    # 统计信息
    stats = defaultdict(int)
    
    # 保存分析结果用于调试
    analysis_results = []
    
    print("正在分析动作数据...")
    for action_name, action_value in action_data.items():
        # 跳过空值项（如 "random": ""）
        if not action_value or action_value.strip() == "":
            print(f"  跳过空值项: {action_name}")
            continue
            
        girls_count, boys_count, category = analyze_character_count(action_value)
        
        # 添加到对应类别
        categories[category][action_name] = action_value
        stats[category] += 1
        # 保存分析结果
        analysis_results.append({
            "name": action_name,
            "value": action_value,
            "girls_count": girls_count,
            "boys_count": boys_count,
            "category": category
        })
        
        # 打印一些示例用于验证
        if len(categories[category]) <= 3:
            print(f"  {category}: {action_name} -> {action_value[:50]}...")
    
    # 输出统计信息
    print("\n=== 分类统计 ===")
    for category, count in sorted(stats.items()):
        print(f"{category}: {count} 个动作")
    
    # 保存分类文件
    print("\n正在保存分类文件...")
    
    # 创建文件名映射（更友好的文件名）
    filename_mapping = {
        "solo_girl": "action_solo_girl.json",
        "solo_boy": "action_solo_boy.json", 
        "couple": "action_couple.json",
        "multiple_girls": "action_multiple_girls.json",
        "multiple_boys": "action_multiple_boys.json",
        "group": "action_group.json",
        "mixed": "action_mixed.json",
        "futanari": "action_futanari.json",
        "unknown": "action_unknown.json"
    }
    
    for category, actions in categories.items():
        if not actions:  # 跳过空类别
            continue
            
        filename = filename_mapping.get(category, f"action_{category}.json")
        output_path = os.path.join(output_dir, filename)
        
        # 直接保存动作数据，不添加 _category_info
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(actions, f, ensure_ascii=False, indent=2)
        
        print(f"  保存 {filename}: {len(actions)} 个动作")
    
    # 保存详细分析结果
    analysis_path = os.path.join(output_dir, "analysis_details.json")
    with open(analysis_path, 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, ensure_ascii=False, indent=2)
    
    # 创建一个总览文件，包含详细的分类信息
    summary = {
        "split_info": {
            "input_files": input_files,
            "total_actions": len(action_data),
            "categories": dict(stats),
            "files": {cat: filename_mapping.get(cat, f"action_{cat}.json") 
                     for cat in categories.keys()}
        },
        "category_details": {
            category: {
                "category": category,
                "description": get_category_description(category),
                "count": len(actions),
                "filename": filename_mapping.get(category, f"action_{category}.json")
            }
            for category, actions in categories.items() if actions
        }
    }
    
    summary_path = os.path.join(output_dir, "split_summary.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"\n总览文件保存至: {summary_path}")
    print(f"详细分析保存至: {analysis_path}")
    print(f"所有分类文件保存在目录: {output_dir}")
    
    return categories

def analyze_unknown_actions(unknown_actions):
    """
    分析未识别的动作，寻找可能的改进点
    """
    print("\n=== 分析未识别动作 ===")
    
    # 统计各种模式
    patterns = {
        'contains_girl_variants': [],
        'contains_boy_variants': [],
        'contains_sex_terms': [],
        'contains_body_parts': [],
        'technical_terms': [],
        'truly_ambiguous': []
    }
    
    # 关键词集合
    girl_variants = ['girl', 'Girl', 'female', 'Female', 'woman', 'Woman', 'women', 'Women']
    boy_variants = ['boy', 'Boy', 'male', 'Male', 'man', 'Man', 'men', 'Men']
    sex_terms = ['sex', 'sexual', 'fucking', 'penetration', 'intercourse']
    body_parts = ['penis', 'pussy', 'vagina', 'breast', 'nipple', 'ass', 'anus']
    technical_terms = ['lora:', 'pov', 'close up', 'from behind', 'masturbation']
    
    for action_name, action_value in unknown_actions.items():
        if action_name == "_category_info":
            continue
            
        text = action_value.lower()
        original_text = action_value
        
        # 分类分析
        if any(variant.lower() in text for variant in girl_variants):
            patterns['contains_girl_variants'].append((action_name, original_text))
        elif any(variant.lower() in text for variant in boy_variants):
            patterns['contains_boy_variants'].append((action_name, original_text))
        elif any(term in text for term in sex_terms):
            patterns['contains_sex_terms'].append((action_name, original_text))
        elif any(term in text for term in body_parts):
            patterns['contains_body_parts'].append((action_name, original_text))
        elif any(term in text for term in technical_terms):
            patterns['technical_terms'].append((action_name, original_text))
        else:
            patterns['truly_ambiguous'].append((action_name, original_text))
    
    # 输出分析结果
    total_unknown = len([k for k in unknown_actions.keys() if k != "_category_info"])
    
    print(f"总计未识别动作: {total_unknown}")
    print("\n📊 模式分析:")
    
    for pattern_name, actions in patterns.items():
        if actions:
            print(f"\n🔍 {pattern_name}: {len(actions)} 个")
            # 显示前3个示例
            for i, (name, value) in enumerate(actions[:3]):
                print(f"  - {name}: {value[:60]}...")
            if len(actions) > 3:
                print(f"  ... 还有 {len(actions) - 3} 个")
    
    # 提供改进建议
    print("\n💡 改进建议:")
    
    if patterns['contains_girl_variants']:
        print(f"- 发现 {len(patterns['contains_girl_variants'])} 个包含女性词汇的动作需要改进规则")
    
    if patterns['contains_boy_variants']:
        print(f"- 发现 {len(patterns['contains_boy_variants'])} 个包含男性词汇的动作需要改进规则")
    
    if patterns['contains_sex_terms']:
        print(f"- {len(patterns['contains_sex_terms'])} 个包含性行为词汇，可能需要上下文分析")
    
    if patterns['contains_body_parts']:
        print(f"- {len(patterns['contains_body_parts'])} 个包含身体部位词汇，可通过部位推断性别")
    
    if patterns['technical_terms']:
        print(f"- {len(patterns['technical_terms'])} 个技术性描述，可能本身就不包含人物信息")
    
    if patterns['truly_ambiguous']:
        print(f"- {len(patterns['truly_ambiguous'])} 个真正难以分类的动作")
    
    return patterns

def get_category_description(category):
    """获取类别描述"""
    descriptions = {
        "solo_girl": "单个女性角色的动作",
        "solo_boy": "单个男性角色的动作",
        "couple": "一男一女的动作", 
        "multiple_girls": "多个女性角色的动作",
        "multiple_boys": "多个男性角色的动作",
        "group": "群体动作（多人）",
        "mixed": "混合性别的多人动作",
        "futanari": "扶他相关动作",
        "unknown": "未能识别人物数量的动作"
    }
    return descriptions.get(category, "其他类型动作")

def main():
    """主函数"""
    print("Action.json 人物数量分类工具")
    print("=" * 40)
    
    # 检查输入文件
    input_files = []
    
    # 检查指定的文件
    target_files = ["action.json", "action_futanari.json", "action_explicit.json"]
    
    for file_name in target_files:
        if os.path.exists(file_name):
            input_files.append(file_name)
            print(f"✅ 找到 {file_name}")
        else:
            print(f"⚠️  未找到 {file_name}")
    
    if not input_files:
        print("❌ 错误: 没有找到任何目标文件")
        return
    
    print(f"\n将处理以下文件: {', '.join(input_files)}")
    
    try:
        categories = split_action_json(input_files)
        
        # 分析未识别的动作
        if "unknown" in categories and categories["unknown"]:
            print("\n" + "=" * 50)
            analyze_unknown_actions(categories["unknown"])
        
        print("\n✅ 分类完成!")
    except Exception as e:
        print(f"\n❌ 错误: {e}")

if __name__ == "__main__":
    main()
