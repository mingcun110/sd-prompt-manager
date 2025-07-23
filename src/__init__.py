"""
Stable Diffusion WebUI 提示词管理器

本项目实现了完整的提示词管理生态系统，包括：
1. 批量任务提交 - 独立脚本 batch_action_generator.py（项目根目录）
2. 提示词库管理 - 完整的数据库操作（规划中）
3. 数据分析与统计 - 深度分析和统计功能

注意：功能1通过根目录的独立脚本实现，无需模块导入。
"""

__version__ = "1.0.0"
__author__ = "SD Prompt Manager Team"

# 模块导入
from . import prompt_manager  
from . import data_analysis

__all__ = [
    "prompt_manager", 
    "data_analysis"
]
