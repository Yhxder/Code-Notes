import os
import sys
from datetime import datetime

def update_progress():
    """自动数文件并更新 README 进度条"""
    try:
        # 计算 Luogu 目录下的 cpp 文件数
        count = len([f for f in os.listdir('./Luogu') if f.endswith('.cpp')])
        target = 100  # 设定第一阶段目标为 100 题
        progress = min(100, count)

        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 寻找并替换进度条链接
        import re
        new_content = re.sub(r'geps.dev/progress/\d+', f'geps.dev/progress/{progress}', content)
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"📊 进度已更新：目前已完成 {count} 道题目")
    except Exception as e:
        print(f"⚠️ 进度更新失败: {e}")

def sync_to_github(message=None):
    # 先更新进度条
    update_progress()
    
    if not message:
        message = f"Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    print("🚀 开始同步到 GitHub...")
    os.system("git add .")
    os.system(f'git commit -m "{message}"')
    result = os.system("git push origin main")
    
    if result == 0:
        print("✅ 同步成功！")
    else:
        print("❌ 同步失败，请检查网络。")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    sync_to_github(msg)
