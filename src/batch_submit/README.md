# Batch Action Generator 使用指南

## 概述

`batch_action_generator.py` 是一个为 Stable Diffusion WebUI 设计的脚本，实现了 `mainidea.md` 中定义的**功能1: 批量任务提交**。该脚本允许用户批量处理多组提示词，大幅提高绘图任务的执行效率。

## 安装步骤

### 1. 复制脚本文件
将 `batch_action_generator.py` 复制到您的 Stable Diffusion WebUI 安装目录下的 `scripts/` 文件夹中：

```bash
# 示例路径
cp src/batch_submit/batch_action_generator.py /path/to/stable-diffusion-webui/scripts/
```

### 2. 重启 WebUI
重启 Stable Diffusion WebUI 以加载新脚本。

### 3. 验证安装
在 WebUI 界面的生成页面底部，找到 "Scripts" 下拉菜单，确认能看到 "Batch Action Generator" 选项。

## 使用方法

### 基础配置

1. **选择脚本**: 在 Scripts 下拉菜单中选择 "Batch Action Generator"

2. **设置 JSON 文件路径**: 
   - 默认路径：`scripts/action.json`
   - 您可以使用项目中的任何 action JSON 文件
   - 推荐路径：`data/raw/action_backup.json`（包含 655+ 个动作）

3. **配置批量选项**:
   - ✅ **Use different seed for each action**: 为每个动作使用不同的随机种子
   - ✅ **Include action name in filename**: 在文件名中包含动作名称

### 高级配置

#### 提示词组合模式
- **start**: 动作提示词 + 原始提示词
- **end**: 原始提示词 + 动作提示词 (推荐)
- **replace**: 仅使用动作提示词

#### 提示词增强
- **Prompt prefix**: 添加到所有提示词前面的内容
  - 示例：`masterpiece, high quality, `
- **Prompt suffix**: 添加到所有提示词后面的内容
  - 示例：`, professional photography`

### 操作流程

1. **预览动作**: 点击 "Load and Preview Actions" 按钮预览将要处理的动作
2. **设置参数**: 配置生成参数（分辨率、采样器、步数等）
3. **开始批量生成**: 点击 "Generate" 开始批量处理

## JSON 文件格式

脚本支持标准的 action JSON 格式：

```json
{
  "action_name_1": "detailed prompt description",
  "action_name_2": "another prompt description",
  "..."
}
```

### 推荐文件

项目提供了多个可用的 JSON 文件：

| 文件 | 位置 | 内容 | 推荐用途 |
|------|------|------|----------|
| `action_backup.json` | `data/raw/` | 655+ 基础动作 | 通用批量生成 |
| `action_visual_impact.json` | `data/raw/` | 视觉艺术风格 | 艺术创作 |
| `action_seductive.json` | `data/raw/` | 诱惑内容 | 角色扮演 |
| `action_explicit.json` | `data/raw/` | 成人内容 | 科研用途 |

## 实际应用示例

### 示例1：基础批量生成

```
原始提示词: "1girl, anime style"
JSON文件: data/raw/action_backup.json
组合模式: end
结果: "1girl, anime style, [动作描述]"
```

### 示例2：艺术风格批量生成

```
前缀: "masterpiece, best quality, "
原始提示词: "fantasy landscape"
JSON文件: data/raw/action_visual_impact.json
后缀: ", cinematic lighting"
结果: "masterpiece, best quality, fantasy landscape, [视觉冲击动作], cinematic lighting"
```

## 输出管理

### 文件命名
- 启用 "Include action name in filename" 时，生成的图片文件名将包含动作名称
- 便于后续整理和管理批量生成的结果

### 信息记录
- 每张图片的元数据中都会记录对应的动作名称
- 便于追踪和复现特定的生成结果

## 性能优化建议

1. **合理设置批次大小**: 根据显存容量调整单次生成的图片数量
2. **选择适当的动作文件**: 根据需求选择合适大小的 JSON 文件
3. **监控系统资源**: 批量生成时注意 GPU 和内存使用情况

## 故障排除

### 常见问题

1. **文件路径错误**
   - 确保 JSON 文件路径正确
   - 使用相对于 WebUI 根目录的路径

2. **JSON 格式错误**
   - 使用 "Load and Preview Actions" 验证文件格式
   - 确保 JSON 文件编码为 UTF-8

3. **内存不足**
   - 减少单次生成的图片数量
   - 选择较小的 JSON 文件

4. **脚本未显示**
   - 确认文件已正确复制到 scripts/ 目录
   - 重启 WebUI

### 错误信息解读

- `File not found`: JSON 文件路径不正确
- `Invalid JSON format`: JSON 文件格式错误
- `No actions found`: JSON 文件为空或格式不正确

## 技术细节

### 脚本特性
- **自动种子管理**: 可为每个动作生成不同的随机种子
- **进度跟踪**: 显示当前处理的动作和进度
- **错误处理**: 单个动作失败不会影响整个批次
- **内存优化**: 禁用网格保存以节省内存

### 兼容性
- 支持 txt2img 和 img2img 模式
- 兼容所有 WebUI 版本
- 支持所有采样器和模型

---

## 相关链接

- [项目主页](../../README.md)
- [数据说明](../../data/README.md)
- [开发文档](../../docs/DEVELOPMENT.md)
