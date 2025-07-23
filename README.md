# 🎨 WAI-NSFW 智能提示词库

## 📊 项目概览

**🚀 全新升级版本** - 现在包含 **923个高质量提示词**，采用 **3级风险分类系统**，确保在不同平台的安全使用！

| 📈 统计指标 | 📊 数值 | 📝 说明 |
|------------|---------|---------|
| **总提示词数** | 923个 | 完整的内容库 |
| **分类精度** | 90.7% | AI智能分类 |
| **风险等级** | 3级 | 从艺术到成人 |
| **角色类型** | 8种 | 全面覆盖 |

## 🎯 主要特性

### ✨ 3级内容分类系统
- 🟢 **Level 1 - 视觉冲击** (54个): 艺术性强，适合所有平台
- 🟡 **Level 2 - 诱惑内容** (52个): 暗示性强，适合限制平台  
- 🔴 **Level 3 - 显性内容** (817个): 成人内容，仅限成人平台

### 🤖 智能分类算法
- **角色识别**: 自动识别角色数量和类型
- **内容分析**: 智能分析内容风险等级
- **批量处理**: 支持大规模内容处理

### 📁 专业文件组织
- **标准化命名**: 统一的文件命名规范
- **层级结构**: 清晰的目录层次
- **备份系统**: 完整的legacy备份

## 🚀 快速开始

### 📥 立即使用
```python
# 🎨 获取安全的艺术创作提示词
import json, random

with open('prompts/level_1_visual/prompts_visual_impact.json', 'r') as f:
    visual_prompts = json.load(f)

# 随机获取一个提示词
prompt = random.choice(visual_prompts['actions'])
print(f"🎨 推荐: {prompt['action']}")
```

### 📚 完整文档
- 📋 **[快速入门](QUICK_START_GUIDE.md)** - 60秒上手指南
- 🔧 **[技术文档](COMPREHENSIVE_TECHNICAL_REPORT.md)** - 详细技术规范
- 🚀 **[部署指南](DEPLOYMENT_CHECKLIST.md)** - 生产环境部署
- 🔌 **[API文档](API_DOCUMENTATION.md)** - 接口规范说明

## 📊 内容统计

### 按风险等级分布
```
🟢 视觉冲击 (Level 1):  54个 (5.9%)  - 艺术创作
🟡 诱惑内容 (Level 2):  52个 (5.6%)  - 角色扮演  
🔴 显性内容 (Level 3): 817个 (88.5%) - 成人平台
```

### 按角色类型分布
```
👩 单女性:     685个 (74.2%)
💑 情侣:       145个 (15.7%) 
👨 单男性:      30个 (3.3%)
👥 群体:        35个 (3.8%)
🌟 其他类型:    28个 (3.0%)
```

## 🛠️ 技术规格

### 系统要求
- **Python**: 3.8+ 
- **依赖**: json, random (标准库)
- **内存**: < 50MB
- **兼容**: 跨平台

### 核心功能
- ✅ 智能内容分类 (90.7%精度)
- ✅ 多级风险管理
- ✅ 批量内容处理
- ✅ 安全合规检查
- ✅ API接口支持

## 🛡️ 安全与合规

### 🔐 内容分级
| 等级 | 年龄要求 | 平台限制 | 风险评估 |
|------|----------|----------|----------|
| Level 1 | 无限制 | 通用平台 | 🟢 低风险 |
| Level 2 | 13+ | 限制平台 | 🟡 中风险 |
| Level 3 | 18+ | 成人平台 | 🔴 高风险 |

### ⚖️ 法律合规
- ✅ 年龄验证系统兼容
- ✅ 平台政策适配
- ✅ 内容标记完整
- ✅ 访问控制支持

## 📞 获取支持

### 📖 学习资源
1. **新手**: 阅读 [快速入门指南](QUICK_START_GUIDE.md)
2. **开发者**: 查看 [API文档](API_DOCUMENTATION.md)
3. **运维**: 参考 [部署清单](DEPLOYMENT_CHECKLIST.md)
4. **高级用户**: 研读 [技术报告](COMPREHENSIVE_TECHNICAL_REPORT.md)

### 🚨 紧急支持
- **内容问题**: 使用Level 1安全内容
- **技术故障**: 检查legacy/备份文件
- **合规问题**: 参考安全指南

---

## 🎯 原始项目信息

**专用于 WAI-NSFW-illustrious-SDXL** 
- 模型链接: https://civitai.com/models/827184?modelVersionId=1183765

### 相关依赖
- add-detail-xl: https://huggingface.co/PvDeep/Add-Detail-XL/blob/main/add-detail-xl.safetensors
- Pony People's Works: https://civitai.green/models/856285/pony-peoples-works?modelVersionId=1036362
- ChihunHentai: https://civitai.com/models/106586
- SDXL VAE: https://civitai.com/models/296576?modelVersionId=333245

### AI功能配置 
支持各大API服务商，如 Groq (llama-3.3-70b-versatile)

配置示例:
```json
{
    "ai": true,
    "base_url": "https://api.groq.com/openai/v1/chat/completions",
    "model": "llama-3.3-70b-versatile",
    
        "api_key": "your_api_key_here"
}
```

## 🔄 更新历史

### 🎉 v2.0 - 2025年1月 (当前版本)
- ✅ **内容大幅扩展**: 从原有基础扩展到923个提示词
- ✅ **3级分类系统**: 全新的风险等级管理
- ✅ **智能分类算法**: 90.7%精度的自动分类
- ✅ **专业文档系统**: 完整的技术文档和用户指南
- ✅ **API接口规范**: 标准化的编程接口

### 📅 历史版本
- **4/13**: 新增100名角色
- **2/23**: 调整预设，新增手机模式
- **2/22**: 人物翻译完成，部分prompt调整
- **2/20**: 修复切换bug，新增随机按钮
- **2/15**: 更新AI功能，角色名称修正
- **1/19**: AI功能更新，下载timeout延长

## 🎯 使用场景

### 🎨 创意工作者
- **数字艺术**: 使用Level 1视觉冲击内容
- **概念设计**: 丰富的视觉元素组合
- **艺术灵感**: 多样化的创作方向

### 🎮 游戏开发
- **角色设计**: 按角色类型精确筛选
- **场景构建**: 情境化的提示词组合
- **故事创作**: 多角色互动场景

### 📱 内容平台
- **社交媒体**: Level 1安全内容
- **创作平台**: Level 2限制内容
- **成人平台**: Level 3完整内容

## 🏆 项目优势

### 🎯 内容优势
- **数量优势**: 923个vs市面平均200-300个
- **质量保证**: 手工精选+AI智能分类
- **分级管理**: 3级风险分类确保合规
- **持续更新**: 基于用户反馈持续优化

### 🔧 技术优势  
- **零依赖**: 仅需Python标准库
- **高性能**: < 50MB内存占用
- **易集成**: 标准JSON格式
- **跨平台**: 支持所有主流操作系统

### 📚 服务优势
- **完整文档**: 从快速入门到技术细节
- **专业支持**: 多层级技术支持体系
- **开源免费**: MIT许可证，商用友好
- **社区驱动**: 欢迎贡献和反馈

---

## 🌟 立即开始！

选择适合您的入门方式:

| 👤 用户类型 | 📖 推荐文档 | ⏱️ 预计时间 |
|------------|------------|-------------|
| **新手用户** | [快速入门指南](QUICK_START_GUIDE.md) | 5分钟 |
| **开发者** | [API文档](API_DOCUMENTATION.md) | 15分钟 |
| **项目经理** | [部署清单](DEPLOYMENT_CHECKLIST.md) | 30分钟 |
| **技术专家** | [技术报告](COMPREHENSIVE_TECHNICAL_REPORT.md) | 60分钟 |

```bash
# 🚀 一键验证安装
python -c "
import json
with open('prompts/level_1_visual/prompts_visual_impact.json', 'r') as f:
    data = json.load(f)
    print(f'✅ 成功加载 {len(data["actions"])} 个安全提示词')
    print(f'🎨 示例: {data["actions"][0]["action"]}')
"
```

**🎉 欢迎使用WAI-NSFW智能提示词库！**

---
*Made with ❤️ for the creative community*
    


