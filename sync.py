import os
import sys
from datetime import datetime

def sync_to_github(message=None):
    # 默认提交信息：日期 + 自动同步
    if not message:
        message = f"Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    print("🚀 开始同步到 GitHub...")
    
    # 依次执行 Git 命令
    if os.system("git add .") != 0:
        print("❌ git add 失败")
        return
    
    if os.system(f'git commit -m "{message}"') != 0:
        print("⚠️  可能没有新改动需要提交")
        # 即使 commit 失败（比如没改动），也可以尝试 push
    
    result = os.system("git push origin main")
    
    if result == 0:
        print("✅ 同步成功！GitHub 绿点已更新。")
    else:
        print("❌ 推送失败，请检查网络或 GitHub 权限。")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    sync_to_github(msg)
