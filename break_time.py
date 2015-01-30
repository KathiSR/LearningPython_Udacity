import webbrowser
import time
url = "https://www.youtube.com/watch?v=p2PGNA2u_HI"

total_breaks = 3
break_count = 0

print("this program started on" + time.ctime())
while (break_count < 3):
    time.sleep(10)
    webbrowser.open(url)
    break_count = break_count + 1

