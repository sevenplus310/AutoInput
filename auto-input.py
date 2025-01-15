import pyautogui
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import keyboard


def perform_auto_input():
    root = Tk()
    root.withdraw()

    # 弹出文件选择对话框，选择 TXT 文件
    file_path = askopenfilename(
        title="选择一个TXT文件",
        filetypes=[("TXT files", "*.txt")]
    )

    if file_path:
        # 读取 TXT 文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()

        # 等待几秒钟以便你可以切换到目标输入框
        print("请在4秒内切换到目标输入框...")
        time.sleep(2)

        # 将 TXT 文件内容逐字输入到当前活动的输入框
        pyautogui.typewrite(text_content, interval=0.00001)
    else:
        print("哥们咋不选文件呢🤔")


print("按下 Ctrl + i 开始执行任务")

while True:
    if keyboard.is_pressed('ctrl+i'):
        perform_auto_input()
    elif keyboard.is_pressed('esc'):
        print("拜拜了您嘞~")
        break
