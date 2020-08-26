import pyautogui as pg
import pyperclip as pc
import time
from python_imagesearch.imagesearch import imagesearch_count

#pg.moveTo(pg.locateCenterOnScreen('zoom_name.png'))
#time.sleep(1)
#pg.click(pg.locateCenterOnScreen('zoom2.png'))
#time.sleep(1)
#pg.doubleClick(pg.locateCenterOnScreen('chat.png'))
#time.sleep(1)
f=open('text.txt','w',encoding='utf-8')
while True:
    count = imagesearch_count("check.png")
    if(count>=5):
        f.write('count = '+str(count))
        break
    else:
        f.write('count = '+str(count)+'\n')
    time.sleep(10)
f.close()
pg.moveTo(pg.locateCenterOnScreen('msg.png'))
pg.click()
time.sleep(1)
pc.copy('출석합니다!')
pg.hotkey("ctrl", "v")
time.sleep(1)
pg.typewrite(['enter'])
