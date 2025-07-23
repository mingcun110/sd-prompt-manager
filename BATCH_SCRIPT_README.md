# 📋 Batch Action Generator

**SD WebUI 批量任务提交脚本** - 实现 `mainidea.md` 功能1

## 🚀 一键使用

### 安装步骤

1. **下载此脚本**
   ```bash
   # 方式1: 直接下载
   wget https://raw.githubusercontent.com/your-username/sd-prompt-manager/main/batch_action_generator.py
   
   # 方式2: 克隆整个项目后复制
   git clone https://github.com/your-username/sd-prompt-manager.git
   cp sd-prompt-manager/batch_action_generator.py .
   ```

2. **复制到 SD WebUI**
   ```bash
   cp batch_action_generator.py /path/to/stable-diffusion-webui/scripts/
   ```

3. **重启 WebUI** 并在 Scripts 中选择 "Batch Action Generator"

## ⚙️ 使用配置

### 推荐 JSON 文件

| 文件 | 动作数量 | 适用场景 | 相对路径 |
|------|----------|----------|----------|
| `action_backup.json` | 655+ | 通用批量生成 | `data/raw/action_backup.json` |
| `action_visual_impact.json` | 54 | 艺术创作 | `data/raw/action_visual_impact.json` |
| `action_seductive.json` | 52 | 角色扮演 | `data/raw/action_seductive.json` |

### 基础设置

- **JSON 文件路径**: 设置为上述推荐路径之一
- **Use different seed**: ✅ 推荐启用
- **Include action name**: ✅ 推荐启用
- **Prompt position**: 选择 "end" (原始提示词 + 动作)

### 高级选项

- **Prefix**: 例如 `masterpiece, high quality, `
- **Suffix**: 例如 `, professional photography`

## 📊 功能特性

- ✅ 支持批量处理 JSON 格式的动作文件
- ✅ 灵活的提示词组合模式（前置/后置/替换）
- ✅ 自动种子管理，确保每个动作产生不同结果
- ✅ 进度跟踪和错误处理
- ✅ 动作名称自动记录到图片元数据

## 🗂️ JSON 文件格式

```json
{
  "action_name_1": "detailed prompt description",
  "action_name_2": "another prompt description"
}
```

## 📖 详细文档

- [完整使用指南](docs/USER_GUIDE.md)
- [项目主页](README.md)
- [数据说明](data/README.md)

---

**注意**: 此脚本是独立工具，仅需下载此单个文件即可使用。无需安装整个项目。
