本项目致力于开发一个专业的提示词管理器，专门用于管理 Stable Diffusion WebUI 的绘图提示词。

## 核心功能

### 1. 批量任务提交
以脚本形式实现多组提示词的批量提交，提高绘图任务执行效率。

### 2. 提示词库管理
构建完整的提示词数据库，支持词条的增加、删除、修改和查询操作。

#### 2.1 技术选型
- **UI框架**：Gradio（提供直观的Web界面）
- **数据存储**：JSON格式（轻量化，易于管理和调试）

#### 2.2 核心功能
- **数据导入**：支持导入JSON格式的提示词词条文件
- **词条管理**：
  - 直接添加新词条
  - 根据名称/内容搜索词条（支持模糊匹配）
  - 按level和tags筛选搜索
  - 修改现有词条内容
  - 删除指定词条
  - 批量操作（批量删除、批量修改level/tags）
- **数据导出**：按条件筛选导出为JSON格式文件（支持按level、tags筛选）
- **重复处理**：导入时自动重命名重复词条（name_1、name_2等）
- **界面功能**：分页显示、词条内容展示

#### 2.3 数据结构设计
```json
{
  "prompts": [
    {
      "id": "unique_id",
      "name": "词条名称",
      "content": "提示词内容",
      "level": "level_1_visual|level_2_seductive|level_3_explicit",
      "tags": ["solo_girl", "couple", "multiple_girls", "custom_tag"],
      "created_time": "创建时间",
      "updated_time": "更新时间"
    }
  ]
}
```

**与现有数据的适配说明**：
- **level字段**：对应项目中的三个级别（level_1_visual、level_2_seductive、level_3_explicit）
- **tags字段**：使用split_action_by_characters.py脚本识别的类别作为标签（solo_girl、solo_boy、couple、multiple_girls、multiple_boys、group、futanari、unknown），同时支持用户自定义标签
- **与batch_action_generator.py的兼容**：新的数据结构可以导出为原有的简单键值对格式（name: content）供批量脚本使用

#### 2.4 技术实现细节
1. **数据存储**：
   - 主数据库文件：`data/database/prompts_database.json`
   - 备份目录：`data/database/backups/`（后续实现自动备份功能）
   - 导出文件：`data/exports/`

2. **数据导入**：
   - 主要从`data/raw/level_*/`目录导入标准格式：`{"action_name": "action_content"}`
   - level信息根据文件路径自动推断（level_1_visual、level_2_seductive、level_3_explicit）
   - tags自动识别：使用split_action_by_characters.py的逻辑自动分析内容并添加相应标签
   - 后续支持用户手动指定level的功能

3. **ID生成**：使用自增数字（1, 2, 3...）

4. **标签系统**：
   - 预定义标签：基于split_action_by_characters.py的分类结果
   - 可用标签：solo_girl、solo_boy、couple、multiple_girls、multiple_boys、group、futanari、unknown
   - 支持用户自定义标签和标签编辑

5. **导出兼容性**：
   - 可导出为batch_action_generator.py兼容的格式：`{"action_name": "action_content"}`
   - 不集成批量生成功能，仅提供数据导出

6. **UI布局设计**：
   - **第一页：词条管理**（主要功能页面）
     - 顶部：数据导入功能
     - 中部：搜索/筛选区域 + 批量操作按钮
     - 主体：词条列表（分页显示）
     - 右侧：词条详情编辑区域
     - 底部：数据导出功能
     - 删除操作：提供二次确认对话框（单个删除和批量删除）
   - **第二页：统计分析**（预留页面，功能3后续实现）

7. **性能优化**：
   - 分页显示（每页50条，可配置）
   - 搜索索引优化
   - 大数据集支持（预计支持10000+词条）

### 3. 数据分析与统计
对提示词库进行深度分析，包括：
- 类别统计分析
- 词频分析报告
- 使用趋势展示

此外，本项目还提供一个多级别提示词库（涉及NSFW），仅用于科学研究和代码测试，不对相关生成内容负责。

## 实现方案
- **功能1**：基于 Stable Diffusion WebUI 脚本框架实现
- **功能2**：采用Gradio框架开发Web UI界面，使用JSON格式存储数据，提供完整的CRUD操作
- **功能3**：基于功能2的数据基础，提供数据分析与可视化功能

本项目使用 uv 管理依赖。