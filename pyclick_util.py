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

def move(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.1)

def move_pos(pos):
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(0.1)

def click_l_pos(pos, t=0.1):
    move_pos(pos)
    pyautogui.click(pos[0], pos[1], button="left")
    time.sleep(t)