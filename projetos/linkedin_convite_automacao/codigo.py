import pyautogui 
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")


pyautogui.click(x=562, y=51)
pyautogui.write("https://www.linkedin.com/mynetwork/grow/")
pyautogui.press("enter")
time.sleep(3)



quantidade_add = 3

for qtd in range(quantidade_add):
    pyautogui.click(x=804, y=714)
    pyautogui.click(x=1026, y=708)
    pyautogui.click(x=1235, y=712)
    pyautogui.click(x=1444, y=709)
    pyautogui.scroll(-100)

    pyautogui.click(x=807, y=945)
    pyautogui.click(x=1019, y=949)
    pyautogui.click(x=1231, y=951)
    pyautogui.click(x=1460, y=951)

    pyautogui.click(x=93, y=50)
    time.sleep(3)









