# 🚀 快速入门指南

## 欢迎使用 WAI-NSFW 提示词库！

这是一个包含 **923个高质量提示词** 的专业内容库，采用 **3级风险分类** 系统，确保在不同平台上的安全使用。

---

## ⚡ 60秒快速开始

### 1. 选择您的使用场景（30秒）

| 🎨 创作类型 | 📁 使用文件 | ⚠️ 风险等级 | 🌐 适用平台 |
|------------|------------|-------------|------------|
| **艺术创作** | `prompts/level_1_visual/` | 🟢 低风险 | 所有平台 |
| **角色扮演** | `prompts/level_2_seductive/` | 🟡 中风险 | 限制平台 |
| **成人内容** | `prompts/level_3_explicit/` | 🔴 高风险 | 成人平台 |

### 2. 立即开始使用（30秒）

```python
# 🎨 艺术创作（最安全）
import json
with open('prompts/level_1_visual/prompts_visual_impact.json', 'r') as f:
    visual_prompts = json.load(f)
    
# 获取一个随机提示词
import random
random_prompt = random.choice(visual_prompts['actions'])
print(f"🎨 推荐提示词: {random_prompt['action']}")
```

---

## 📚 详细使用指南

### 🟢 Level 1: 视觉冲击内容（推荐新手）

**特点**: 艺术性强，视觉冲击力大，无显性内容
**数量**: 54个精选提示词
**适用**: 艺术创作、视觉设计、通用平台

```python
# 获取科幻主题的视觉内容
visual_sci_fi = [p for p in visual_prompts['actions'] 
                if 'science' in p.get('themes', [])]
```

**示例提示词**:
- `neon-lit laboratory experiment, glowing test tubes`
- `holographic data visualization floating in space`
- `crystalline structure formation in macro photography`

### 🟡 Level 2: 诱惑内容（适合有经验用户）

**特点**: 暗示性强，诱惑元素，无直接显性内容
**数量**: 52个精心设计提示词
**适用**: 角色扮演、情感表达、限制平台

```python
# 加载诱惑内容
with open('prompts/level_2_seductive/prompts_seductive.json', 'r') as f:
    seductive_prompts = json.load(f)
    
# 按角色类型筛选
couple_content = [p for p in seductive_prompts['actions'] 
                 if p['category'] == 'couple']
```

**示例场景**:
- 办公室角色扮演
- 湿衣诱惑场景
- 暗示性姿态表现

### 🔴 Level 3: 显性内容（仅限成人平台）

**特点**: 直接成人内容，需要年龄验证
**数量**: 817个专业提示词
**分类**: 通用(655) + 双性(52) + 显性(110)

```python
# ⚠️ 仅在确认合规后使用
# 年龄验证和平台检查必须先完成

if user_age >= 18 and platform_allows_adult_content:
    with open('prompts/level_3_explicit/prompts_general.json', 'r') as f:
        explicit_content = json.load(f)
```

---

## 🛠️ 智能分类工具

### 自动角色识别

```python
# 使用内置分类脚本
python split_action_by_characters.py

# 结果将保存在 prompts/processed/split_by_characters/
```

**分类结果**:
- `solo_girl` - 单女性角色 (685个)
- `couple` - 情侣角色 (145个) 
- `solo_boy` - 单男性角色 (30个)
- `group` - 群体场景 (等等...)

### 按需筛选

```python
def get_prompts_by_filter(character_count=None, category=None, intensity=None):
    """
    智能筛选提示词
    
    参数:
    - character_count: 1, 2, "3+", None(任意)
    - category: "solo_girl", "couple", "group", None
    - intensity: "visual", "seductive", "explicit", None
    """
    # 筛选逻辑...
    return filtered_prompts

# 使用示例
romantic_couple = get_prompts_by_filter(
    character_count=2,
    category="couple", 
    intensity="seductive"
)
```

---

## 🎯 常用场景示例

### 场景1: 艺术创作项目
```python
# 获取具有强烈视觉冲击的艺术提示词
def get_artistic_inspiration(theme="any"):
    visual_content = load_visual_prompts()
    
    if theme != "any":
        filtered = [p for p in visual_content['actions'] 
                   if theme in p.get('themes', [])]
        return filtered
    
    return visual_content['actions']

# 使用
neon_art = get_artistic_inspiration("neon")
gothic_art = get_artistic_inspiration("gothic")
```

### 场景2: 角色扮演游戏
```python
# 为RPG生成角色互动场景
def generate_rpg_scenario(characters=2, intensity="seductive"):
    if intensity == "seductive":
        prompts = load_seductive_prompts()
    elif intensity == "visual":
        prompts = load_visual_prompts()
    
    # 按角色数筛选
    suitable = [p for p in prompts['actions'] 
               if p['characters'] == characters]
    
    return random.choice(suitable) if suitable else None

# 使用
scenario = generate_rpg_scenario(characters=2, intensity="seductive")
print(f"RPG场景: {scenario['action']}")
```

### 场景3: 内容创作平台
```python
# 为内容平台提供安全的提示词推荐
def get_platform_safe_content(platform_rating="PG"):
    content_map = {
        "G": load_visual_prompts(),      # 通用级别
        "PG": load_seductive_prompts(),  # 家长指导  
        "R": load_explicit_prompts()     # 限制级别
    }
    
    if platform_rating in content_map:
        return content_map[platform_rating]
    else:
        return load_visual_prompts()  # 默认最安全

# 使用
safe_content = get_platform_safe_content("G")
```

---

## 🔧 高级功能

### 批量处理
```python
# 批量生成多样化内容
def generate_diverse_batch(count=10):
    results = []
    
    # 从不同级别随机选择
    levels = ['visual', 'seductive', 'explicit']
    
    for _ in range(count):
        level = random.choice(levels[:2])  # 排除高风险内容
        if level == 'visual':
            prompt = random.choice(load_visual_prompts()['actions'])
        else:
            prompt = random.choice(load_seductive_prompts()['actions'])
        
        results.append(prompt)
    
    return results
```

### 内容验证
```python
def validate_content_safety(prompt_text, target_platform="general"):
    """
    验证内容是否适合目标平台
    
    返回: {"safe": bool, "recommendations": [...]}
    """
    risk_indicators = {
        "high": ["explicit", "nude", "sex"],
        "medium": ["seductive", "revealing", "intimate"], 
        "low": ["artistic", "aesthetic", "creative"]
    }
    
    # 检查风险指标...
    return safety_assessment
```

---

## 🆘 常见问题解答

### Q: 如何确保内容合规？
**A**: 始终从最低风险级别开始，检查平台政策，确保有适当的年龄验证机制。

### Q: 可以修改提示词吗？  
**A**: 可以！所有内容都是开源的，您可以根据需要修改和扩展。

### Q: 如何获得更多内容？
**A**: 可以使用 `split_action_by_characters.py` 脚本分析现有内容，或者参考我们的扩展指南。

### Q: 遇到技术问题怎么办？
**A**: 查看 `COMPREHENSIVE_TECHNICAL_REPORT.md` 了解详细技术信息，或检查 `DEPLOYMENT_CHECKLIST.md` 排除常见问题。

---

## 📞 获取帮助

### 📖 文档资源
- **📋 部署清单**: `DEPLOYMENT_CHECKLIST.md`
- **🔧 技术报告**: `COMPREHENSIVE_TECHNICAL_REPORT.md`  
- **📚 完整指南**: `PROMPTS_LIBRARY_COMPREHENSIVE_GUIDE.md`
- **🔌 API文档**: `API_DOCUMENTATION.md`

### 🚨 紧急支持
- **内容问题**: 立即切换到 Level 1 (视觉) 内容
- **技术故障**: 使用 `legacy/` 目录中的备份文件
- **合规问题**: 暂停使用，查看平台政策

---

## 🎉 开始您的创作之旅！

现在您已经掌握了基础知识，选择适合您的内容级别，开始创作吧！

```python
# 🎨 立即开始 - 获取您的第一个提示词
import json, random

# 选择安全的视觉冲击内容
with open('prompts/level_1_visual/prompts_visual_impact.json', 'r') as f:
    content = json.load(f)

first_prompt = random.choice(content['actions'])
print(f"🎨 您的创作提示词: {first_prompt['action']}")
print(f"👥 角色数量: {first_prompt['characters']}")  
print(f"📂 分类: {first_prompt['category']}")

print("\n🚀 创作愉快！")
```

---
*快速入门指南 - 让创作变得简单安全*
