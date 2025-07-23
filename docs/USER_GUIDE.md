# 📖 提示词管理器使用指南

本指南介绍如何使用 Stable Diffusion WebUI 提示词管理器的各项功能。

## 🎯 核心功能概览

根据 `mainidea.md` 的设计，本项目提供三大核心功能：

### 1. 📋 批量任务提交
**已实现** - 使用根目录的 `batch_action_generator.py` 独立脚本
- **功能**: 批量处理多组提示词，提高绘图效率
- **实现**: SD WebUI 脚本插件
- **使用**: 下载脚本文件，复制到 WebUI scripts/ 目录

### 2. 🗄️ 提示词库管理
**已实现** - 基于Gradio的Web UI管理系统
- **功能**: 词条的增加、删除、修改和查询
- **数据**: 支持导入现有的分级提示词数据
- **格式**: 标准化 JSON 数据

## 快速开始

### 1. 启动应用
```bash
# 确保在项目根目录下
cd /path/to/sd-prompt-manager

# 启动应用
uv run python prompt_manager_app.py
```

应用将在 `http://127.0.0.1:7861` 启动

### 2. 界面介绍

应用包含两个主要页面：

#### 📚 词条管理页面
- **数据导入/导出区域**（顶部）
- **搜索/筛选区域**（中部）
- **批量操作区域**（中部）
- **词条列表**（左侧）
- **词条编辑区域**（右侧）

#### 📊 统计分析页面
- 显示基本统计信息（当前版本）
- 后续将添加详细的数据分析功能

## 主要功能

### 数据导入
1. 点击"选择JSON文件"按钮上传文件
2. 选择级别或留空自动推断（基于文件路径）
3. 点击"导入数据"按钮
4. 系统会自动识别重复词条并重命名
5. 导入时会自动分析内容并添加相应标签

**支持的文件格式**：
```json
{
  "action_name": "action_content",
  "another_action": "another_content"
}
```

### 词条管理

#### 添加词条
1. 在右侧编辑区域填写词条信息
2. 点击"添加词条"按钮

#### 搜索词条
1. 在搜索框输入关键词（支持名称和内容搜索）
2. 使用级别和标签下拉框进行筛选
3. 点击"搜索"按钮

#### 编辑词条
1. 在词条列表中选择一个词条（点击选择框）
2. 词条信息会自动填入右侧编辑区域
3. 修改信息后点击"更新词条"

#### 删除词条
1. 选择要删除的词条
2. 点击"删除词条"按钮（单个删除）
3. 或使用"批量删除"功能

### 批量操作

#### 批量选择
- 在词条列表中勾选多个词条的选择框

#### 批量修改级别
1. 选择多个词条
2. 在"批量修改级别"下拉框选择新级别
3. 点击"应用级别"

#### 批量修改标签
1. 选择多个词条
2. 在"批量修改标签"中选择标签
3. 选择操作模式：
   - **replace**: 替换现有标签
   - **add**: 添加新标签
   - **remove**: 移除指定标签
4. 点击"应用标签"

### 数据导出

#### 导出格式
- **full**: 完整格式（包含所有字段）
- **batch_compatible**: 兼容批量脚本格式

#### 筛选导出
1. 选择要导出的级别（可选）
2. 选择要导出的标签（可选）
3. 选择导出格式
4. 点击"导出数据"

导出的文件会保存在 `data/exports/` 目录下

## 数据结构

### 内部数据格式
```json
{
  "prompts": [
    {
      "id": 1,
      "name": "词条名称",
      "content": "提示词内容",
      "level": "level_1_visual",
      "tags": ["solo_girl", "custom_tag"],
      "created_time": "2025-01-23T14:30:00",
      "updated_time": "2025-01-23T14:30:00"
    }
  ]
}
```

### 级别说明
- `level_1_visual`: 视觉级别
- `level_2_seductive`: 诱惑级别
- `level_3_explicit`: 明示级别

### 预定义标签
- `solo_girl`: 单个女性
- `solo_boy`: 单个男性
- `couple`: 一男一女
- `multiple_girls`: 多个女性
- `multiple_boys`: 多个男性
- `group`: 群体
- `futanari`: 扶他
- `unknown`: 未知

## 文件目录结构

```
data/
├── database/
│   ├── prompts_database.json    # 主数据库文件
│   └── backups/                 # 自动备份目录
├── exports/                     # 导出文件目录
└── raw/                        # 原始数据目录
    ├── level_1_visual/
    ├── level_2_seductive/
    └── level_3_explicit/
```

## 注意事项

1. **数据安全**: 每次保存时会自动创建备份
2. **重复处理**: 导入时重复词条会自动重命名（name_1, name_2...）
3. **标签自动识别**: 导入时会根据内容自动分析并添加标签
4. **分页显示**: 默认每页显示50条，可在页面底部调整
5. **搜索功能**: 支持模糊匹配，搜索词条名称和内容

## 故障排除

### 启动失败
```bash
# 检查依赖是否安装
uv sync

# 手动安装Gradio
uv add gradio
```

### 端口被占用
修改 `prompt_manager_app.py` 中的端口号：
```python
server_port=7862  # 改为其他端口
```

### 数据导入失败
- 检查JSON文件格式是否正确
- 确保文件编码为UTF-8
- 查看控制台错误信息

## 开发信息

- **框架**: Gradio
- **数据存储**: JSON
- **Python版本**: >=3.10
- **依赖管理**: uv

更多技术细节请参考项目文档。

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
