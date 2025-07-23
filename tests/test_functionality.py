#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提示词管理器功能测试
"""

import sys
import os
from pathlib import Path

# 添加src路径
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from prompt_manager.data_manager import PromptDataManager

def test_basic_functionality():
    """测试基本功能"""
    print("🧪 开始测试提示词管理器基本功能...")
    
    # 创建测试数据库
    test_db_path = "data/database/test_prompts.json"
    manager = PromptDataManager(test_db_path)
    
    print("✅ 数据管理器初始化成功")
    
    # 测试添加词条
    try:
        prompt = manager.add_prompt(
            name="测试词条",
            content="1girl, beautiful, masterpiece",
            level="level_1_visual",
            tags=["solo_girl"]
        )
        print("✅ 添加词条测试通过")
        print(f"   - ID: {prompt['id']}")
        print(f"   - 名称: {prompt['name']}")
        print(f"   - 标签: {prompt['tags']}")
    except Exception as e:
        print(f"❌ 添加词条测试失败: {e}")
        return False
    
    # 测试搜索
    try:
        result = manager.search_prompts(query="测试", page_size=10)
        print("✅ 搜索功能测试通过")
        print(f"   - 找到 {result['total']} 个结果")
    except Exception as e:
        print(f"❌ 搜索功能测试失败: {e}")
        return False
    
    # 测试标签识别
    try:
        girls_count, boys_count, category = manager.analyze_character_count("2girls, 1boy, sex")
        print("✅ 标签识别测试通过")
        print(f"   - 女性数量: {girls_count}")
        print(f"   - 男性数量: {boys_count}")
        print(f"   - 分类: {category}")
    except Exception as e:
        print(f"❌ 标签识别测试失败: {e}")
        return False
    
    # 测试导出
    try:
        export_path = "data/exports/test_export.json"
        success = manager.export_to_json(export_path, format_type="batch_compatible")
        if success:
            print("✅ 导出功能测试通过")
            print(f"   - 导出文件: {export_path}")
        else:
            print("❌ 导出功能测试失败")
            return False
    except Exception as e:
        print(f"❌ 导出功能测试失败: {e}")
        return False
    
    # 清理测试文件
    try:
        if os.path.exists(test_db_path):
            os.remove(test_db_path)
        if os.path.exists(export_path):
            os.remove(export_path)
        print("✅ 测试文件清理完成")
    except Exception as e:
        print(f"⚠️ 清理测试文件时出现警告: {e}")
    
    print("\n🎉 所有测试通过！提示词管理器功能正常。")
    return True

def test_import_functionality():
    """测试导入功能"""
    print("\n🧪 测试数据导入功能...")
    
    # 创建测试数据文件
    test_data = {
        "test_action_1": "1girl, solo, beautiful",
        "test_action_2": "2girls, multiple girls, friendship",
        "test_action_3": "1boy, 1girl, couple, romance"
    }
    
    test_file = "data/test_import.json"
    try:
        import json
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        
        # 测试导入
        manager = PromptDataManager("data/database/test_import.json")
        result = manager.import_from_json(test_file, "level_1_visual")
        
        if result["success"]:
            print("✅ 数据导入测试通过")
            print(f"   - 导入成功: {result['imported']} 条")
            print(f"   - 跳过: {result['skipped']} 条")
        else:
            print(f"❌ 数据导入测试失败: {result.get('error', '未知错误')}")
            return False
        
        # 清理测试文件
        os.remove(test_file)
        os.remove("data/database/test_import.json")
        print("✅ 导入测试文件清理完成")
        
    except Exception as e:
        print(f"❌ 数据导入测试失败: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 提示词管理器功能测试")
    print("=" * 50)
    
    # 确保目录存在
    os.makedirs("data/database", exist_ok=True)
    os.makedirs("data/exports", exist_ok=True)
    
    success = True
    success &= test_basic_functionality()
    success &= test_import_functionality()
    
    if success:
        print("\n🎉 所有测试通过！系统运行正常。")
        print("💡 您现在可以运行 'uv run python prompt_manager_app.py' 启动应用。")
    else:
        print("\n❌ 部分测试失败，请检查系统配置。")
        sys.exit(1)
