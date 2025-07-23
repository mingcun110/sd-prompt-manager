# 📖 使用指南

本指南介绍如何使用 Stable Diffusion WebUI 提示词管理器的各项功能。

## 🎯 核心功能概览

根据 `mainidea.md` 的设计，本项目提供三大核心功能：

### 1. 📋 批量任务提交
**已实现** - 使用根目录的 `batch_action_generator.py` 独立脚本
- **功能**: 批量处理多组提示词，提高绘图效率
- **实现**: SD WebUI 脚本插件
- **使用**: 下载脚本文件，复制到 WebUI scripts/ 目录

### 2. 🗄️ 提示词库管理
**规划中** - 提示词数据库管理系统
- **功能**: 词条的增加、删除、修改和查询
- **数据**: 923个分级提示词
- **格式**: 标准化 JSON 数据

### 3. 📊 数据分析与统计
**部分实现** - 角色识别分类工具
- **功能**: 类别统计、词频分析、使用趋势
- **已有**: 角色数量识别算法
- **规划**: 可视化报告、统计导出

---

## 🚀 快速开始

### 前置条件
- Python 3.8+
- Stable Diffusion WebUI（功能1需要）
- 基本的命令行操作知识

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/your-username/sd-prompt-manager.git
   cd sd-prompt-manager
   ```

2. **验证数据完整性**
   ```bash
   # 检查数据文件是否完整
   ls data/raw/
   ls data/level_*/
   ```

---

## 📋 功能1：批量任务提交

### 配置步骤

1. **下载脚本**
   ```bash
   # 直接下载单个脚本文件
   wget https://raw.githubusercontent.com/your-username/sd-prompt-manager/main/batch_action_generator.py
   ```

2. **复制脚本到 WebUI**
   ```bash
   cp batch_action_generator.py /path/to/stable-diffusion-webui/scripts/
   ```

3. **重启 WebUI**
   重启 Stable Diffusion WebUI 以加载脚本

4. **验证安装**
   在 WebUI 的 Scripts 下拉菜单中查找 "Batch Action Generator"

### 使用方法

1. **基础设置**
   - JSON 文件路径: `data/raw/action_backup.json`（推荐）
   - 启用不同种子: ✅ 
   - 包含动作名称: ✅

2. **提示词组合**
   - 位置选择: "end"（原始提示词 + 动作）
   - 可选前缀: `masterpiece, high quality, `
   - 可选后缀: `, professional photography`

3. **开始批量生成**
   - 预览动作: 点击 "Load and Preview Actions"
   - 设置生成参数（分辨率、步数等）
   - 点击 "Generate" 开始

### 推荐 JSON 文件

| 文件 | 用途 | 动作数量 | 适用场景 |
|------|------|----------|----------|
| `action_backup.json` | 通用 | 655+ | 日常批量生成 |
| `action_visual_impact.json` | 艺术 | 54 | 视觉艺术创作 |
| `action_seductive.json` | 角色扮演 | 52 | 限制平台内容 |

---

## 📊 功能3：数据分析

### 角色识别分类

使用 `split_action_by_characters.py` 对提示词进行角色分析：

1. **运行分析**
   ```bash
   cd sd-prompt-manager
   python src/data_analysis/split_action_by_characters.py
   ```

2. **查看结果**
   ```bash
   ls data/processed/split_by_characters/
   ```

3. **结果文件**
   - `action_solo_girl.json`: 单女性动作
   - `action_couple.json`: 情侣动作
   - `action_group.json`: 群体动作
   - `split_summary.json`: 分析总览
   - `analysis_details.json`: 详细分析数据

### 支持的角色类别

- `solo_girl`: 单个女性角色
- `solo_boy`: 单个男性角色
- `couple`: 一男一女
- `multiple_girls`: 多个女性
- `multiple_boys`: 多个男性
- `group`: 群体场景
- `futanari`: 特定角色类型
- `unknown`: 未识别类型

---

## 🗄️ 数据库管理

### 数据结构

```
data/
├── raw/                     # 原始数据
│   ├── action_backup.json   # 主要数据源 (655+)
│   ├── action_explicit.json # 显性内容
│   └── ...                  # 其他分类数据
├── level_1_visual/          # Level 1: 视觉艺术 (54)
├── level_2_seductive/       # Level 2: 诱惑内容 (52)
├── level_3_explicit/        # Level 3: 成人内容 (817)
└── processed/               # 分析结果
    └── split_by_characters/ # 角色分类结果
```

### 数据格式

**原始格式 (raw/*.json)**:
```json
{
  "action_name": "prompt description"
}
```

**分级格式 (level_*/*.json)**:
```json
{
  "actions": [
    {
      "action": "prompt content",
      "characters": 1,
      "category": "solo_girl"
    }
  ]
}
```

### 使用建议

1. **开发测试**: 使用 `level_1_visual/` 的安全内容
2. **艺术创作**: 使用 `action_visual_impact.json`
3. **批量处理**: 使用 `action_backup.json`
4. **分析研究**: 使用 `processed/` 下的分类数据

---

## 📝 配置说明

### 系统配置 (`config/settings.py`)

```python
# SD WebUI API 配置
SD_WEBUI_HOST = "127.0.0.1"
SD_WEBUI_PORT = 7860

# 数据路径配置
DATABASE_PATH = "data/"
PROMPTS_DATABASE = "prompts/"

# 分析配置
ANALYSIS_OUTPUT_PATH = "docs/reports/"
```

### 环境变量

可选的环境变量配置：
```bash
export SD_WEBUI_URL="http://localhost:7860"
export PROMPT_DATA_PATH="/path/to/data"
```

---

## ⚠️ 注意事项

### 内容分级使用

1. **Level 1 (视觉艺术)**: 适合所有平台，无限制
2. **Level 2 (诱惑内容)**: 适合限制平台，需谨慎使用
3. **Level 3 (成人内容)**: 仅限科研和测试，请遵守当地法规

### 性能建议

1. **批量生成**: 根据显存调整批次大小
2. **数据分析**: 大文件处理可能需要较长时间
3. **文件路径**: 使用绝对路径避免错误

### 故障排除

1. **脚本未显示**: 检查文件是否正确复制到 scripts/ 目录
2. **JSON 格式错误**: 使用预览功能验证文件格式
3. **路径错误**: 确认文件路径相对于正确的工作目录

---

## 📚 进阶使用

### 自定义 JSON 文件

创建自己的动作文件：
```json
{
  "my_action_1": "detailed prompt description",
  "my_action_2": "another creative prompt"
}
```

### Python API 使用

```python
from src.data_analysis import analyze_character_count

# 分析单个提示词
girls, boys, category = analyze_character_count("1girl, solo, fantasy")
print(f"类别: {category}")  # 输出: solo_girl
```

### 批量数据处理

```python
# 自定义输入文件和输出目录
from src.data_analysis.split_action_by_characters import split_action_json

input_files = ["data/raw/action_backup.json"]
output_dir = "my_analysis_results"
categories = split_action_json(input_files, output_dir)
```

---

## 🔗 相关链接

- [批量任务详细指南](src/batch_submit/README.md)
- [数据结构说明](data/README.md)
- [开发文档](docs/DEVELOPMENT.md)
- [项目主页](README.md)

---

## 🤝 获得帮助

遇到问题时的解决途径：

1. **查看文档**: 先查阅相关的 README 文件
2. **检查配置**: 验证路径和设置是否正确
3. **测试环境**: 使用小数据集验证功能
4. **社区支持**: 在 GitHub Issues 中寻求帮助

---

<div align="center">
  <sub>📖 详细的使用指南，助您快速掌握所有功能</sub>
</div>
