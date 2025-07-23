# 开发文档

## 项目架构

本项目采用模块化设计，分为两个核心功能模块（功能1通过独立脚本实现）：

### 1. 批量任务提交 (根目录独立脚本)
`batch_action_generator.py` 作为独立的 SD WebUI 脚本实现。

**已实现功能：**
- SD WebUI 脚本集成
- 批量任务处理
- 进度监控和错误处理
- 灵活的提示词组合

**技术栈：**
- Python 3.8+
- Gradio (WebUI界面)
- SD WebUI Scripts API

### 2. 提示词库管理模块 (src/prompt_manager/)
提供完整的提示词数据库管理功能。

**计划功能：**
- 提示词CRUD操作
- 多级别分类管理
- 数据标准化处理
- 搜索和过滤引擎
- 导入导出工具
- 数据验证和清理

**技术栈：**
- SQLite/JSON (数据存储)
- Pandas (数据处理)
- RegEx (文本处理)
- JSON Schema (数据验证)

### 3. 数据分析模块 (src/data_analysis/)
提供深度分析和统计功能。

**已实现功能：**
- `split_action_by_characters.py`: 角色识别和分类

**计划功能：**
- 词频统计分析
- 使用趋势分析
- 内容质量评估
- 可视化报告生成
- 统计数据导出

**技术栈：**
- Matplotlib/Plotly (可视化)
- NumPy (数值计算)
- Scikit-learn (机器学习)
- WordCloud (词云生成)

## 开发规范

### 代码风格
- 遵循 PEP 8 Python 代码规范
- 使用类型注解 (Type Hints)
- 详细的文档字符串 (Docstrings)
- 单元测试覆盖

### 文件命名
- 使用小写字母和下划线
- 模块名称要能体现功能
- 配置文件使用 `.py` 或 `.json` 格式

### 数据格式
- JSON 作为主要数据交换格式
- 统一的数据结构标准
- 版本控制和向后兼容

## 部署说明

### 环境要求
- Python 3.8 或更高版本
- Stable Diffusion WebUI (可选)
- 足够的存储空间用于提示词库

### 安装步骤
1. 克隆项目仓库
2. 安装依赖包：`pip install -r requirements.txt`
3. 配置 `config/settings.py`
4. 运行初始化脚本

### 配置说明
主要配置项在 `config/settings.py` 中：
- SD WebUI API 地址和端口
- 数据库路径设置
- 批量处理参数
- 分析输出配置

## 扩展开发

### 添加新功能模块
1. 在对应的 `src/` 子目录中创建新模块
2. 更新 `__init__.py` 文件
3. 添加相应的测试用例
4. 更新文档

### 贡献指南
1. Fork 项目仓库
2. 创建功能分支
3. 提交代码并附上详细说明
4. 创建 Pull Request
5. 等待代码审查

## 许可证

本项目遵循 [LICENSE](../LICENSE) 文件中的许可证条款。
