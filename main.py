# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import time
import pyautogui
import pyperclip

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def click_l():		#当前位置左键单击
    x,y=pyautogui.position()
    pyautogui.click(x,y,button="left")

def click_r():		#当前位置右键单击
    x,y=pyautogui.position()
    pyautogui.click(x,y,button="right")

def keydown():#按下
    pyautogui.keyDown('enter')

def keyup(): #弹起
    pyautogui.keyUp('enter')

def hotkey(*key):#热键 如ctrl+v _ hotkey("ctrl","v")
    pyautogui.hotkey(*key)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    click_l()

    for i in [1, 2, 3, 4, 5]:
        pyperclip.copy(i)
        # pyperclip.paste()
        hotkey("ctrl", "v")
        keydown()
        keyup()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
