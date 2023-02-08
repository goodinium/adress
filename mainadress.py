import os    
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
scr = os.path.abspath(__file__)
dir = os.path.split(scr)[0]
file=open(fr'{dir}\city.txt',encoding='utf-8')
import pyperclip
file=open(r'C:\Users\Vadim\Desktop\py\adres\city.txt',encoding='utf-8')
gorf=file.readlines()
for g in gorf:
    os.environ['MOZ_HEADLESS']='1'
    brow=webdriver.Firefox()
    sleep(1)
    brow.get(url=f"https://yandex.ru/maps/194/saratov/search/больница%20{g}/")
    sleep(1)
    print(g)
    sleep(1)
    et=brow.find_elements(By.CLASS_NAME, "search-business-snippet-view__address")
    for i in et:
        print(repr(i.text.encode("utf-8")))
        adres=i.text
    sleep(1)
    brow.quit()
    sleep(1)