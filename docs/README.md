# Stable Diffusion WebUI 提示词管理器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

专业的提示词管理解决方案，专门为 Stable Diffusion WebUI 设计。

## 🎯 核心理念

本项目致力于提供一个完整的提示词管理生态系统，帮助用户更高效地管理和使用 Stable Diffusion 提示词。

### 三大核心功能

1. **📋 批量任务提交** - 自动化批量处理，提高工作效率
2. **🗄️ 提示词库管理** - 完整的数据库操作，灵活的分类管理  
3. **📊 数据分析统计** - 深度分析工具，洞察使用趋势

## 🗂️ 项目结构

```
sd-prompt-manager/
├── 📁 src/                 # 核心源代码
│   ├── batch_submit/       # 批量任务提交模块
│   ├── prompt_manager/     # 提示词库管理模块
│   └── data_analysis/      # 数据分析模块
├── 📁 data/                # 数据存储
│   ├── action_*.json       # 原始数据文件
│   └── prompts/           # 分级提示词库
├── 📁 config/              # 配置文件
├── 📁 docs/                # 项目文档
└── 📁 scripts/            # 实用工具脚本
```

## 🚀 快速开始

### 环境准备
```bash
# 克隆项目
git clone https://github.com/your-username/sd-prompt-manager.git
cd sd-prompt-manager

# 安装依赖 (待实现)
pip install -r requirements.txt
```

### 基础使用
```python
# 导入核心模块
from src.data_analysis import analyze_character_count

# 分析提示词角色信息
girls, boys, category = analyze_character_count("1girl, solo, fantasy art")
print(f"识别结果: {category}")  # 输出: solo_girl
```

## 📊 数据库概览

### 多级别提示词库
- **🟢 Level 1** - 视觉艺术 (54个提示词)
- **🟡 Level 2** - 诱惑内容 (52个提示词)  
- **🔴 Level 3** - 显性内容 (817个提示词，科研用途)

### 智能分类系统
支持8种角色类别的自动识别：`solo_girl`, `solo_boy`, `couple`, `group` 等

## 📖 文档导航

- 📋 [开发文档](docs/DEVELOPMENT.md) - 架构设计和开发规范
- 📊 [数据说明](data/README.md) - 数据结构和格式规范
- ⚙️ [配置说明](config/settings.py) - 系统配置参数

## 🤝 贡献指南

我们欢迎社区贡献！请查看 [DEVELOPMENT.md](docs/DEVELOPMENT.md) 了解详细的贡献流程。

## ⚠️ 使用声明

本项目包含的多级别提示词库（包括NSFW内容）仅用于科学研究和代码测试目的。我们不对使用本项目生成的任何内容承担责任。请用户根据所在地区的法律法规和使用场景合理选择合适级别的内容。

## 📄 许可证

本项目采用 MIT 许可证 - 详情请查看 [LICENSE](LICENSE) 文件。

---
<div align="center">
  <sub>Built with ❤️ for the Stable Diffusion community</sub>
</div>
