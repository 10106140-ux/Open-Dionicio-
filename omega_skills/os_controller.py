# omega_skills/os_controller.py
import pyautogui
import time

def automate_ui_task(task_description, target_app):
    # Abrir app (lógica nativa)
    time.sleep(2)
    pyautogui.typewrite(task_description["text"], interval=0.05)
    pyautogui.press("enter")
    return "UI Task completada."
