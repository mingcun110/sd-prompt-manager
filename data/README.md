# 数据说明文档

## 数据目录结构

```
data/
├── raw/                        # 原始数据文件
│   ├── action_backup.json      # 原始提示词数据备份 (655+个)
│   ├── action_explicit.json    # 显性内容源数据
│   ├── action_futanari.json    # 特定角色类型源数据
│   ├── action_seductive.json   # 诱惑内容源数据
│   └── action_visual_impact.json # 视觉艺术源数据
├── level_1_visual/             # Level 1 - 视觉冲击 (处理后)
├── level_2_seductive/          # Level 2 - 诱惑内容 (处理后)
├── level_3_explicit/           # Level 3 - 显性内容 (处理后)
└── processed/                  # 数据分析结果
    └── split_by_characters/    # 按角色分类的结果
```

## 数据处理流程

### 1. 原始数据 (raw/)
所有原始的 `action_*.json` 文件存储在 `raw/` 目录下：
- **格式**: `{"action_name": "prompt_description"}`
- **用途**: 作为数据处理的输入源
- **处理**: 通过脚本转换为分级和分类数据

### 2. 分级数据 (level_*/)
原始数据经过分级处理后存储在对应的level目录：

#### Level 1 - 视觉冲击 (level_1_visual/)
- **用途**: 艺术创作，强调视觉效果
- **内容**: 54个高质量艺术性提示词
- **特点**: 适合所有平台，无敏感内容
- **文件**: `prompts_visual_impact.json`

#### Level 2 - 诱惑内容 (level_2_seductive/)  
- **用途**: 角色扮演，暗示性内容
- **内容**: 52个诱惑性提示词
- **特点**: 适合限制平台，包含暗示性元素
- **文件**: `prompts_seductive.json`

#### Level 3 - 显性内容 (level_3_explicit/)
- **用途**: 科学研究和代码测试
- **内容**: 817个成人内容提示词
- **特点**: 仅限成人平台，包含显性描述
- **文件**: `prompts_explicit.json`, `prompts_futanari.json`, `prompts_general.json`

### 3. 分析结果 (processed/)
数据分析工具的输出结果：

#### 按角色分类 (processed/split_by_characters/)
- **输入**: `raw/` 目录下的源文件
- **输出**: 按角色类型分类的JSON文件
- **工具**: `src/data_analysis/split_action_by_characters.py`

### 数据格式说明

```json
{
  "actions": [
    {
      "action": "提示词内容",
      "characters": 角色数量,
      "category": "角色类别"
    }
  ]
}
```

### 角色类别分类

- `solo_girl`: 单个女性角色
- `solo_boy`: 单个男性角色
- `couple`: 一对情侣/两人
- `multiple_girls`: 多个女性
- `multiple_boys`: 多个男性
- `group`: 群体场景
- `futanari`: 特定角色类型
- `unknown`: 未分类

### 注意事项

1. **使用声明**: Level 3 内容仅用于科学研究和代码测试，不对相关生成内容负责
2. **分级使用**: 请根据使用场景选择合适级别的提示词
3. **数据更新**: 数据库会定期更新和扩展
4. **格式标准**: 所有数据遵循统一的JSON格式标准
