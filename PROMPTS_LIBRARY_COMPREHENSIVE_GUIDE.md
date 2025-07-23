# 词条库全面指南与文件组织说明

## 📋 项目概览

本文档是 WAI-NSFW-illustrious-character-select 项目中所有词条文件的完整指南，涵盖内容分类、使用场景、强度级别和技术规范。

---

## 🎯 内容分级体系

### **Level 1: 大胆视觉表现** 🎨
**目标**: 强烈视觉冲击，隐含诱惑元素  
**特点**: 艺术性主导，需深度观察发现隐含内容  
**用途**: 视觉艺术创作，色彩实验，情绪表达

### **Level 2: 隐含色情内容** 💋
**目标**: 诱惑暗示，擦边球内容  
**特点**: 高度性暗示但不直接暴露  
**用途**: 软色情创作，诱惑性场景，性感展示

### **Level 3: 明显色情内容** 🔥
**目标**: 直接性内容，强烈性刺激  
**特点**: 明确性器官描述，激发性欲  
**用途**: 硬色情创作，成人娱乐，自慰素材

---

## 📚 词条文件详细说明

### **Level 1: 大胆视觉表现类**

#### `prompts_visual_impact.json` 
- **原名**: `action_visual_impact.json`
- **词条数量**: 54个
- **内容强度**: ⭐⭐☆☆☆ (视觉导向)
- **主要特色**:
  - 🌈 **强烈色彩主题**: 每个词条都有明确的颜色基调
  - 🔬 **科学美学**: 物理、化学现象的艺术化表达
  - 🎭 **隐含诱惑**: 表面艺术，深层性暗示
  - 💫 **情绪冲击**: 第一眼强烈印象，细看发现内涵

**典型词条示例**:
```json
"neon temptation 1": "1girl,neon lighting,electric blue and hot pink,cyberpunk aesthetic,glowing eyes,metallic bodysuit,holographic reflections,artificial enhancement"

"blood moon ritual 1": "1girl,crimson red dominance,gothic atmosphere,dark ceremonial,blood-red lips,pale contrasting skin,ritual positioning,occult symbolism"

"golden hour fever 1": "1girl,intense golden light,warm amber tones,sweat glistening,heat wave distortion,burning passion,molten gold aesthetic,desire incarnate"
```

**分类分布**:
- 霓虹科技风: 8个
- 自然元素风: 12个  
- 物理现象风: 16个
- 神秘哥特风: 6个
- 科学美学风: 6个

---

### **Level 2: 隐含色情内容类**

#### `prompts_seductive.json`
- **原名**: `action_seductive.json`
- **词条数量**: 52个
- **内容强度**: ⭐⭐⭐⭐☆ (诱惑导向)
- **主要特色**:
  - 💋 **高诱惑性**: 擦边但不越界的性感内容
  - 👗 **服装重点**: 湿身、紧身、半裸、内衣等
  - 🏠 **生活场景**: 浴室、卧室、厨房、办公室等
  - 🎪 **角色扮演**: 护士、女仆、教师、秘书等

**典型词条示例**:
```json
"wet clothing 1": "1girl,soaking wet,white shirt,completely transparent,nipples clearly visible,water dripping,erotic"

"partial undress 1": "1girl,shirt half open,breasts partially exposed,nipple slip,accidental nudity,erotic undressing"

"office flirt 1": "1girl,tight business suit,buttons straining,professional but sexy,workplace seduction,formal erotica"
```

**分类分布**:
- 姿态诱惑: 6个
- 服装诱惑: 12个
- 场景诱惑: 18个
- 职业角色: 8个
- 暴露展示: 4个

---

### **Level 3: 明显色情内容类**

#### `prompts_general.json`
- **原名**: `action_backup.json` (原始通用)
- **词条数量**: 655个
- **内容强度**: ⭐⭐⭐☆☆ (通用成人)
- **主要特色**:
  - 📊 **数量最多**: 涵盖各种基础成人场景
  - 🎯 **分类全面**: 从温和到激烈的完整梯度
  - 💼 **经典内容**: 经过验证的标准成人词条
  - 🔄 **向下兼容**: 与现有系统完全兼容

#### `prompts_futanari.json`
- **原名**: `action_futanari.json`
- **词条数量**: 52个
- **内容强度**: ⭐⭐⭐⭐☆ (专门特化)
- **主要特色**:
  - 🎭 **角色多样性**: 涵盖学生、护士、女仆、精灵、恶魔等
  - 🌟 **场景丰富性**: 办公室、学校、医院、魔法世界等
  - 🔮 **幻想元素**: 变身、触手、魔法、科幻等特殊题材
  - ⚡ **动作层次**: 从温和到极端的完整梯度

#### `prompts_explicit.json`
- **原名**: `action_explicit.json`
- **词条数量**: 110个
- **内容强度**: ⭐⭐⭐⭐⭐ (极限成人)
- **主要特色**:
  - 🔥 **最高强度**: 最直接和露骨的性内容
  - 💥 **专门设计**: 针对性欲激发和自慰需求
  - 🎯 **补强作用**: 专门补充数量不足的分类
  - 🌈 **场景多样**: 各种极端和幻想场景

**分类分布**:
- 群体性爱场景: 40个
- 男性自慰场景: 20个
- 多男性群体: 20个
- 多女性群体: 30个

---

## 🗂️ 文件重新组织方案

### **新的命名规范**
```
prompts_[类型]_[强度级别].json
```

### **统一文件结构**
```
prompts/
├── level_1_visual/
│   └── prompts_visual_impact.json      (54词条) - 大胆视觉表现
├── level_2_seductive/
│   └── prompts_seductive.json          (52词条) - 隐含色情诱惑
├── level_3_explicit/
│   ├── prompts_general.json            (655词条) - 通用成人内容
│   ├── prompts_futanari.json           (52词条) - 扶他专门内容
│   └── prompts_explicit.json          (110词条) - 极限成人内容
└── processed/
    ├── split_by_characters/            (按人物数量分类的结果)
    ├── analysis_reports/               (各种分析报告)
    └── statistics/                     (统计数据)
```

### **备份与兼容性**
```
legacy/
├── action.json                         (原始文件，供scripts使用)
├── character.json                      (角色文件，保持不变)
└── settings.json                       (设置文件，保持不变)
```

---

## 📊 数量统计总览

### **按强度级别分布**
| 级别 | 类型 | 文件数 | 词条总数 | 百分比 |
|------|------|--------|----------|--------|
| Level 1 | 大胆视觉 | 1 | 54 | 5.9% |
| Level 2 | 隐含色情 | 1 | 52 | 5.7% |
| Level 3 | 明显色情 | 3 | 817 | 88.4% |
| **总计** | **全部** | **5** | **923** | **100%** |

### **按人物类型分布** (Level 3处理后)
| 类型 | 数量 | 百分比 | 状态 |
|------|------|--------|------|
| Solo Girl (单女) | 300 | 36.7% | ✅ 充足 |
| Couple (情侣) | 243 | 29.7% | ✅ 充足 |
| Futanari (扶他) | 58 | 7.1% | ✅ 丰富 |
| Group (群体) | 44 | 5.4% | ⚠️ 可扩展 |
| Multiple Girls (多女) | 40 | 4.9% | ⚠️ 可扩展 |
| Solo Boy (单男) | 30 | 3.7% | ⚠️ 可扩展 |
| Multiple Boys (多男) | 25 | 3.1% | ⚠️ 可扩展 |
| Unknown (未识别) | 76 | 9.3% | 🔧 需优化 |

---

## 🎯 使用场景指南

### **内容创作者选择指南**

#### 🎨 **艺术创作场景**
**推荐**: `prompts_visual_impact.json`
- 适用于: 概念艺术、色彩实验、情绪表达
- 特点: 强烈视觉冲击，艺术性主导
- 风险: 低，主要是视觉艺术

#### 💋 **软色情创作场景**  
**推荐**: `prompts_seductive.json`
- 适用于: 时尚摄影、诱惑艺术、性感展示
- 特点: 高度诱惑但不直接暴露
- 风险: 中等，需注意平台政策

#### 🔥 **成人娱乐场景**
**推荐**: `prompts_general.json` + `prompts_futanari.json` + `prompts_explicit.json`
- 适用于: 成人内容、情色艺术、私人用途
- 特点: 直接性内容，强烈刺激
- 风险: 高，仅限成人平台

### **技术开发者集成指南**

#### 🔧 **API设计建议**
```javascript
// 示例API调用
const promptConfig = {
  intensity_level: 1-3,        // 强度级别
  character_type: "solo_girl", // 人物类型  
  scene_category: "seductive", // 场景类别
  safety_filter: true         // 安全过滤
}
```

#### 📱 **应用集成方案**
- **分级访问**: 根据用户年龄和偏好限制访问级别
- **内容过滤**: 可选择性启用不同强度的内容
- **场景匹配**: 根据使用场景自动选择合适文件
- **安全机制**: 内置内容警告和年龄验证

---

## ⚖️ 内容责任与合规

### **使用声明**
- 🔞 **年龄限制**: Level 2和Level 3内容仅限18岁以上用户
- 📋 **平台政策**: 使用前请检查目标平台的内容政策
- 🛡️ **法律合规**: 确保在当地法律允许范围内使用
- 👥 **社会责任**: 避免在不适当的场合使用高强度内容

### **技术限制建议**
- ✅ **访问控制**: 实施年龄验证和用户同意机制
- ✅ **内容标记**: 为所有内容添加适当的警告标签
- ✅ **过滤选项**: 提供用户可控的内容过滤功能
- ✅ **审核机制**: 建立内容审核和举报机制

---

## 🚀 未来发展规划

### **短期目标** (1-3个月)
- [ ] 完成文件重组和命名标准化
- [ ] 建立自动化的内容分级系统
- [ ] 开发内容过滤和安全机制
- [ ] 创建用户友好的选择界面

### **中期目标** (3-6个月)
- [ ] 扩展Level 1视觉艺术类内容
- [ ] 优化分类算法，减少未识别内容
- [ ] 建立多语言支持系统
- [ ] 开发内容推荐算法

### **长期目标** (6-12个月)
- [ ] 建立用户生成内容系统
- [ ] 开发智能内容标签系统
- [ ] 集成AI内容生成辅助
- [ ] 建立内容质量评估体系

---

## 📝 技术规范

### **文件格式标准**
```json
{
  "词条名称": "1girl,标签1,标签2,标签3,描述性标签,场景标签,动作标签",
  "_metadata": {
    "version": "2.0",
    "intensity_level": 1-3,
    "character_count": "solo_girl|couple|group",
    "content_type": "visual|seductive|explicit",
    "creation_date": "2025-07-23",
    "last_updated": "2025-07-23"
  }
}
```

### **标签命名规范**
- **人物标签**: `1girl`, `1boy`, `multiple girls`, `multiple boys`
- **强度标签**: `mild`, `moderate`, `intense`, `explicit`
- **场景标签**: `indoor`, `outdoor`, `workplace`, `fantasy`
- **风格标签**: `realistic`, `anime`, `artistic`, `photographic`

### **质量控制标准**
- ✅ **标签一致性**: 使用标准化的标签词汇
- ✅ **描述准确性**: 确保描述与预期效果匹配
- ✅ **分类正确性**: 正确归类到对应的强度级别
- ✅ **技术兼容性**: 与现有生成系统兼容

---

*最后更新: 2025年7月23日*  
*文档版本: v3.0*  
*总词条数: 923个*  
*强度级别: 3个*  
*文件数量: 5个*
