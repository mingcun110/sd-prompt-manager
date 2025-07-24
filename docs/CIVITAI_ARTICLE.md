# SD WebUI 提示词管理器 - 让你的创作更高效

## 项目介绍

每天用SD WebUI画图的时候，是不是经常要重复输入相同的提示词？你的提示词是不是散落在各种txt文件里，需要的时候找不到？

我开发这个提示词管理器就是为了解决这些烦人的问题。这个工具专门为Stable Diffusion WebUI设计，主要有两个核心功能：**批量任务提交**和**提示词库管理**，同时提供了900+的提示词。

## 能解决什么问题？

### 重复工作太烦人
以前每次画图都要重新输入提示词，现在可以批量提交多组提示词，一次性生成很多变体。

### 提示词管理混乱
以前提示词到处都是，txt文件、笔记软件里一堆，现在有统一的网页界面管理，还能搜索。

### 内置丰富提示词库
项目里内置了900多个分好级别的提示词，创作没灵感的时候可以参考。

## 主要功能介绍

### 功能1：批量任务提交（立即可用）

这是项目的核心功能之一，就一个脚本文件解决批量生成的问题。

下载 `batch_action_generator.py` 这个文件，复制到你的 SD WebUI 的 `scripts/` 目录里，重启WebUI就能用了。

**主要特点：**
- 支持导入JSON格式的提示词批次
- 可以设置不同的采样器、步数、CFG等参数组合
- 有进度条显示，出错会自动重试
- 结果自动保存

**举个例子：**
```json
{
  "prompt_1": "masterpiece, 1girl, portrait, detailed face",
  "prompt_2": "landscape, mountains, sunset, cinematic", 
  "prompt_3": "anime style, cute girl, school uniform"
}
```
导入后会自动为每个提示词生成多个变体，不用你一个个手动操作。

### 功能2：提示词库管理（完整系统）

这是一个完整的提示词数据库管理系统，包含900+内置提示词。

启动方法：运行 `uv run python prompt_manager_app.py`
然后打开浏览器访问 `http://127.0.0.1:7861`

**主要功能：**
- **智能导入**：自动识别提示词的级别和标签
- **强大搜索**：可以按名称、内容、标签搜索
- **标签系统**：自动识别人物数量和场景类型
- **批量操作**：可以批量修改、删除、导出
- **自动备份**：数据安全有保障
- **格式兼容**：导出的格式可以直接用于批量脚本

**内置提示词分级：**
- **Level 1 (Visual)**: 54个视觉冲击类提示词
- **Level 2 (Seductive)**: 52个诱惑类提示词
- **Level 3 (Explicit)**: 817个显性内容类提示词

**自动标签系统：**
- `solo_girl` / `solo_boy`：单人场景
- `couple`：双人场景
- `multiple_girls` / `multiple_boys`：多人场景
- `group`：群体场景
- `futanari`：特殊类别
- 支持自定义标签

## 怎么使用？

### 快速上手（5分钟搞定）

1. **下载项目**
   ```bash
   git clone https://github.com/mingcun110/sd-prompt-manager.git
   cd sd-prompt-manager
   ```

2. **使用批量功能**
   ```bash
   # 把批量脚本复制到SD WebUI
   cp batch_action_generator.py /path/to/stable-diffusion-webui/scripts/
   # 重启SD WebUI，在Scripts选项卡就能看到新功能
   ```

3. **启动提示词管理界面**
   ```bash
   # 安装依赖并启动
   uv run python prompt_manager_app.py
   # 浏览器打开 http://127.0.0.1:7861
   ```

### 进阶用法

**提示词库管理：**
- 导入你现有的提示词（支持JSON格式）
- 使用搜索和标签功能整理提示词
- 按需求导出提示词用于批量生成

**批量任务：**
- 准备JSON格式的提示词文件
- 在SD WebUI的Scripts选项卡选择批量脚本
- 设置参数后一键批量生成

## 未来开发计划

后续主要会完善数据分析功能，包括词频统计、使用趋势分析等，同时扩充提示词数据库的内容。项目会持续更新，有问题或建议可以在GitHub提交Issue。

### 项目地址

- **GitHub**: [sd-prompt-manager](https://github.com/mingcun110/sd-prompt-manager)

## 相关资源

- **使用指南**: [USER_GUIDE.md](docs/USER_GUIDE.md)
- **开发文档**: [DEVELOPMENT.md](docs/DEVELOPMENT.md)

## 重要说明

项目里包含的示例提示词仅用于技术测试和研究。使用这些提示词生成的内容，我不承担任何责任。请确保你的使用符合当地法律和平台规则。

在Civitai等平台分享作品时，记得选择合适的内容级别标记，遵守社区规则。

---

**希望这个工具能让你的AI绘画更高效！欢迎下载试用！**
