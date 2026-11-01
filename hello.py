"""一个最小的示例程序，用来练习 Git 和 GitHub。"""

import sys


def greet(name: str) -> str:
    """返回一句问候。"""
    return f"你好，{name}！欢迎来到 GitHub。"


if __name__ == "__main__":
    # 用法：python hello.py 小明
    # 不传参数时默认问候"世界"
    name = sys.argv[1] if len(sys.argv) > 1 else "世界"
    print(greet(name))
