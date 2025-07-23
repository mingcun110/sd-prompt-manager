# API接口文档

## 📡 WAI-NSFW 提示词库 API 规范

### 版本信息
- **API版本**: v1.0
- **文档版本**: 2025.01.23
- **兼容性**: Python 3.8+
- **总内容量**: 923个提示词

---

## 🔗 核心接口

### 1. 获取分类内容

#### 获取视觉冲击内容（低风险）
```python
def get_visual_prompts():
    """
    获取艺术性视觉冲击提示词
    风险等级: 低
    内容数量: 54个
    适用平台: 通用平台
    """
    with open('prompts/level_1_visual/prompts_visual_impact.json', 'r') as f:
        return json.load(f)

# 返回格式
{
    "actions": [
        {
            "action": "neon-lit laboratory experiment",
            "characters": 1,
            "category": "solo_girl", 
            "intensity": "visual",
            "themes": ["science", "neon", "artistic"]
        }
    ]
}
```

#### 获取诱惑内容（中风险）
```python
def get_seductive_prompts():
    """
    获取诱惑性提示词
    风险等级: 中
    内容数量: 52个
    适用平台: 限制平台
    """
    with open('prompts/level_2_seductive/prompts_seductive.json', 'r') as f:
        return json.load(f)
```

#### 获取显性内容（高风险）
```python
def get_explicit_prompts(category=None):
    """
    获取显性成人内容
    风险等级: 高
    内容数量: 817个
    适用平台: 成人平台
    
    参数:
    - category: 'general'|'futanari'|'explicit'|None（全部）
    """
    if category:
        file_path = f'prompts/level_3_explicit/prompts_{category}.json'
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        # 合并所有显性内容
        all_content = {"actions": []}
        for cat in ['general', 'futanari', 'explicit']:
            with open(f'prompts/level_3_explicit/prompts_{cat}.json', 'r') as f:
                data = json.load(f)
                all_content["actions"].extend(data["actions"])
        return all_content
```

### 2. 智能分类接口

#### 按角色数量分类
```python
def classify_by_characters(min_chars=1, max_chars=10):
    """
    按角色数量过滤内容
    
    参数:
    - min_chars: 最小角色数
    - max_chars: 最大角色数
    
    返回: 过滤后的内容列表
    """
    from split_action_by_characters import classify_action
    
    results = {
        "solo_girl": [],
        "solo_boy": [], 
        "couple": [],
        "multiple_girls": [],
        "multiple_boys": [],
        "group": [],
        "futanari": [],
        "unknown": []
    }
    
    # 处理逻辑...
    return results
```

#### 内容安全检查
```python
def safety_check(content, platform_type="general"):
    """
    内容安全性检查
    
    参数:
    - content: 待检查的内容
    - platform_type: "general"|"restricted"|"adult"
    
    返回:
    {
        "safe": bool,
        "risk_level": "low"|"medium"|"high", 
        "recommendations": [...]
    }
    """
    risk_keywords = {
        "high": ["explicit", "nude", "sex"],
        "medium": ["seductive", "suggestive", "revealing"],
        "low": ["artistic", "aesthetic", "visual"]
    }
    
    # 检查逻辑...
    return safety_result
```

### 3. 随机内容生成

#### 获取随机提示词
```python
def get_random_prompt(intensity="any", character_count="any", category="any"):
    """
    获取随机提示词
    
    参数:
    - intensity: "visual"|"seductive"|"explicit"|"any"
    - character_count: 数字或"any"
    - category: "solo_girl"|"couple"|"group"等或"any"
    
    返回: 单个随机提示词对象
    """
    import random
    
    # 根据条件过滤
    candidates = filter_prompts(intensity, character_count, category)
    
    if candidates:
        return random.choice(candidates)
    else:
        return None
```

#### 批量随机生成
```python
def generate_prompt_batch(count=5, **filters):
    """
    批量生成随机提示词
    
    参数:
    - count: 生成数量
    - **filters: 过滤条件
    
    返回: 提示词列表
    """
    results = []
    for _ in range(count):
        prompt = get_random_prompt(**filters)
        if prompt and prompt not in results:
            results.append(prompt)
    
    return results
```

### 4. 统计分析接口

#### 获取内容统计
```python
def get_content_statistics():
    """
    获取内容库统计信息
    
    返回:
    {
        "total_prompts": 923,
        "by_intensity": {
            "visual": 54,
            "seductive": 52, 
            "explicit": 817
        },
        "by_category": {
            "solo_girl": 655,
            "couple": 110,
            "futanari": 52,
            ...
        },
        "classification_accuracy": 90.7
    }
    """
    # 统计逻辑...
    return statistics
```

#### 内容质量分析
```python
def analyze_content_quality(sample_size=100):
    """
    分析内容质量指标
    
    返回:
    {
        "vocabulary_diversity": float,
        "content_originality": float,
        "category_balance": float,
        "quality_score": float
    }
    """
    # 质量分析逻辑...
    return quality_metrics
```

---

## 🛡️ 安全和合规

### 内容分级系统
```python
CONTENT_RATINGS = {
    "G": {  # General - 通用
        "allowed_files": ["prompts_visual_impact.json"],
        "age_requirement": 0,
        "platform_restrictions": None
    },
    "PG-13": {  # Parental Guidance - 家长指导  
        "allowed_files": ["prompts_seductive.json"],
        "age_requirement": 13,
        "platform_restrictions": ["social_media_limited"]
    },
    "R": {  # Restricted - 限制级
        "allowed_files": ["prompts_general.json"],
        "age_requirement": 18,
        "platform_restrictions": ["adult_platforms_only"]
    },
    "X": {  # Adults Only - 仅限成人
        "allowed_files": ["prompts_explicit.json", "prompts_futanari.json"],
        "age_requirement": 21,
        "platform_restrictions": ["verified_adult_platforms"]
    }
}
```

### 访问控制
```python
def verify_access(user_age, platform_type, requested_content):
    """
    验证用户访问权限
    
    参数:
    - user_age: 用户年龄
    - platform_type: 平台类型
    - requested_content: 请求的内容级别
    
    返回: 访问许可状态
    """
    # 权限验证逻辑...
    return access_granted
```

---

## 📊 使用示例

### 基础使用
```python
# 获取低风险内容
visual_content = get_visual_prompts()
print(f"获取到 {len(visual_content['actions'])} 个视觉冲击提示词")

# 随机获取一个情侣类内容
couple_prompt = get_random_prompt(
    intensity="seductive",
    category="couple"
)
print(f"随机情侣提示词: {couple_prompt['action']}")
```

### 高级使用
```python
# 智能内容推荐
def recommend_content(user_preferences):
    """基于用户偏好推荐内容"""
    
    # 安全检查
    if not verify_access(user_preferences["age"], 
                        user_preferences["platform"],
                        user_preferences["intensity"]):
        return {"error": "访问被拒绝"}
    
    # 生成推荐
    recommendations = generate_prompt_batch(
        count=10,
        intensity=user_preferences["intensity"],
        category=user_preferences["preferred_category"]
    )
    
    return {
        "recommendations": recommendations,
        "total_available": len(get_content_by_filters(**user_preferences))
    }
```

### 批量处理
```python
# 批量内容处理
def process_content_batch(content_list, operations):
    """
    批量处理内容
    
    参数:
    - content_list: 内容列表
    - operations: 操作列表 ["validate", "classify", "filter"]
    """
    results = []
    
    for content in content_list:
        processed = content.copy()
        
        if "validate" in operations:
            processed["validation"] = safety_check(content)
            
        if "classify" in operations:
            processed["classification"] = classify_by_characters(content)
            
        if "filter" in operations:
            processed["filtered"] = apply_content_filters(content)
            
        results.append(processed)
    
    return results
```

---

## 🔧 错误处理

### 错误代码
```python
ERROR_CODES = {
    1001: "内容文件不存在",
    1002: "JSON格式错误", 
    1003: "访问权限不足",
    1004: "内容类别无效",
    1005: "年龄验证失败",
    2001: "分类算法错误",
    2002: "统计计算失败",
    3001: "平台限制违规",
    3002: "内容安全检查失败"
}
```

### 异常处理示例
```python
try:
    content = get_explicit_prompts("invalid_category")
except FileNotFoundError:
    return {"error": ERROR_CODES[1001]}
except json.JSONDecodeError:
    return {"error": ERROR_CODES[1002]}
except PermissionError:
    return {"error": ERROR_CODES[1003]}
```

---

## 📞 技术支持

### API支持
- **响应时间**: 通常 < 100ms
- **并发限制**: 建议 < 1000 req/min  
- **缓存策略**: 推荐本地缓存静态内容
- **错误重试**: 指数退避算法

### 联系方式
- **技术文档**: 参考 `COMPREHENSIVE_TECHNICAL_REPORT.md`
- **使用指南**: 参考 `PROMPTS_LIBRARY_COMPREHENSIVE_GUIDE.md`
- **部署问题**: 参考 `DEPLOYMENT_CHECKLIST.md`

---
*API文档版本 v1.0 - 2025年1月23日更新*
