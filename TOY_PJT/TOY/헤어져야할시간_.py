import time
import webbrowser
import os

# 17시59분이 되면 알람 울리기
while True:
    now = time.localtime()
    if now.tm_hour == 11 and now.tm_min == 44:
        url = "https://www.youtube.com/watch?v=lqFby1rSGyI"
        webbrowser.open(url)
        time.sleep(30)
        os.system("taskkill /im chrome.exe /f")
        break
    else:
        time.sleep(60) # 1분 대기 후 다시 검사 ctrl + c로 종료

