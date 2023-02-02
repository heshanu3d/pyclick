# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import time
import pyautogui
from pyclick_util import *

code = [
'APP666',
'HAPPY666',
'QQ888',
'QQXY888',
'vip666',
'VIP666',
'XY888',
'app666',
'bdvip666',
'douyin666',
'douyin777',
'douyin888',
'happy666',
'huhushengwei888',
'taptap666',
'xyzwgame666',]

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    btn1 = [856, 555]
    btn2 = [867, 639]
    btn3 = [925, 710]
    btn_new_hero = [960, 905]
    for i in code:
        click_l_pos(btn1, 0.5)
        click_l_pos(btn1, 0.5)
        click_l_pos(btn1, 0.5)
        pyperclip.copy(i)
        hotkey("ctrl", "v")
        click_l_pos(btn2, 0.5)
        click_l_pos(btn3, 1)
        click_l()
        if i == 'vip666':
            for j in range(0, 4):
                click_l_pos(btn_new_hero, 0.5)
