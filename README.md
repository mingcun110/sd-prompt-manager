# 🎨 Stable Diffusion WebUI 提示词管理器

## 📊 项目概览

专业的提示词管理器，专门用于管理 Stable Diffusion WebUI 的绘图提示词，包括批量任务提交、提示词库管理和数据分析功能。

## 🎯 核心功能

### 1. 📋 批量任务提交
以脚本形式实现多组提示词的批量提交，提高绘图任务执行效率。
- **状态**: ✅ 已完全实现
- **文件**: `batch_action_generator.py` (根目录，下载即用)
- **特性**: 支持批量提示词处理、自动化任务队列管理、与 SD WebUI 集成

### 2. 🗄️ 提示词库管理
构建完整的提示词数据库，支持词条的增加、删除、修改和查询操作。
- **状态**: 🚧 规划中
- **数据**: 923个分级提示词（Level 1-3），仅NSFW内容用于科学研究和代码测试
- **特性**: 标准化数据格式、灵活的查询和过滤功能

### 3. 📊 数据分析与统计
对提示词库进行深度分析，包括：
- **状态**: 🔄 部分实现
- **已有**: 角色识别和分类
- **规划**: 类别统计分析、词频分析报告、使用趋势展示

## 🚀 快速开始

### ⚙️ 环境设置

建议使用 [uv](https://github.com/astral-sh/uv) 进行依赖管理，以获得更快的包管理体验。

```bash
uv venv .venv # 创建虚拟环境
source .venv/bin/activate  # 激活虚拟环境
uv sync                   # 安装所有基础依赖
```

### 📋 功能1：批量任务提交（立即可用）

**一键使用步骤**：

1. **下载脚本**
   ```bash
   # 下载批量脚本到本地
   wget https://raw.githubusercontent.com/your-username/sd-prompt-manager/main/batch_action_generator.py
   ```

2. **安装到 SD WebUI**
   ```bash
   # 复制到您的 Stable Diffusion WebUI scripts 目录
   cp batch_action_generator.py /path/to/stable-diffusion-webui/scripts/
   ```

3. **使用脚本**
   - 重启 Stable Diffusion WebUI
   - 在界面底部的 "Scripts" 下拉菜单中选择 "Batch Action Generator"
   - 设置 JSON 文件路径：`data/raw/action_backup.json` (推荐，655+ 动作)
   - 配置参数后点击 "Generate" 开始批量生成

## 📊 数据库概览

- **🟢 Level 1** - 正常视觉艺术 (54个提示词，适合所有平台)
- **🟡 Level 2** - 擦边内容 (52个提示词，适合限制平台)  
- **🔴 Level 3** - NSFW内容 (817个提示词，仅限成人平台，科研用途)
  - 👩 单女性:     685个 (74.2%)
  - 💑 情侣:       145个 (15.7%) 
  - 👨 单男性:      30个 (3.3%)
  - 👥 群体:        35个 (3.8%)
  - 🌟 其他类型:    28个 (3.0%)

数据库来源：
> 1. https://github.com/lanner0403/WAI-NSFW-illustrious-character-select
> 2. 由 Claude Sonnet 4 等LLM生成

## 📁 项目结构

```
sd-prompt-manager/
├── batch_action_generator.py   # 📋 功能1: SD WebUI 批量脚本 (下载即用)
├── src/                        # 源代码目录
│   ├── prompt_manager/         # 提示词库管理模块（规划中）
│   └── data_analysis/          # 数据分析模块
│       └── split_action_by_characters.py  # 角色识别脚本
├── data/                       # 数据目录
│   ├── raw/                   # 原始数据 (action_*.json)
│   ├── level_1_visual/        # Level 1 - 视觉冲击 (54个)
│   ├── level_2_seductive/     # Level 2 - 诱惑内容 (52个)
│   ├── level_3_explicit/      # Level 3 - 显性内容 (817个)
│   └── processed/             # 数据分析结果
│       └── split_by_characters/  # 角色分类结果
├── config/                     # 配置文件
├── docs/                       # 文档目录
│   ├── USER_GUIDE.md          # 完整使用指南
│   └── DEVELOPMENT.md         # 开发文档
└── scripts/                   # 实用脚本

```

## 🤝 贡献指南

我们欢迎社区贡献！请查看 [开发文档](docs/DEVELOPMENT.md) 了解详细的贡献流程。

## ⚠️ 使用声明

本项目包含的多级别提示词库（包括NSFW内容）仅用于科学研究和代码测试目的。我们不对使用本项目生成的任何内容承担责任。请用户根据所在地区的法律法规和使用场景合理选择合适级别的内容。

## 📄 许可证

本项目采用 MIT 许可证 - 详情请查看 [LICENSE](LICENSE) 文件。