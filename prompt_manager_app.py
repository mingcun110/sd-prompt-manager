#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提示词管理器主启动脚本
"""

import sys
from pathlib import Path

# 将src目录添加到Python路径
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from prompt_manager.gui import create_app
    
    def main():
        """主函数"""
        print("🎨 启动 Stable Diffusion 提示词管理器...")
        print("=" * 50)
        
        # 检查并创建必要的目录
        directories = [
            "data/database",
            "data/database/backups", 
            "data/exports"
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"✓ 目录检查: {directory}")
        
        print("\n🚀 启动Web界面...")
        print("📡 服务地址: http://127.0.0.1:7861")
        print("🔗 在浏览器中打开上述地址来使用提示词管理器")
        print("\n按 Ctrl+C 停止服务")
        
        try:
            app = create_app()
            app.launch(
                share=False,
                server_name="127.0.0.1", 
                server_port=7861,
                show_api=False,
                quiet=False
            )
        except KeyboardInterrupt:
            print("\n👋 提示词管理器已停止")
        except Exception as e:
            print(f"\n❌ 启动失败: {e}")
            print("请检查依赖是否正确安装: pip install gradio")

    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"❌ 导入失败: {e}")
    print("\n🔧 请安装所需依赖:")
    print("pip install gradio")
    print("\n或使用 uv 安装:")
    print("uv add gradio")
    sys.exit(1)
