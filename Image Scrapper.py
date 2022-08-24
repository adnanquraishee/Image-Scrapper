# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 02:09:52 2022

@author: adnan
"""
from selenium import webdriver
import os
import urllib
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


topic = input("Name of Celebrity: ")
n_images = int(input('No of images you want: '))

path = 'C:\Program Files (x86)\Scraping\chromedriver.exe'

url_prefix = "https://www.google.com/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591"

save_folder = topic

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    download_images()
    
def download_images():
    
    search_url = url_prefix+topic+url_postfix
    #print(search_url)
    
    path = r'C:/Program Files (x86)/Scraping/chromedriver.exe'
    
    s=Service(path)
    browser = webdriver.Chrome(service=s)
    browser.get(search_url)
    
    value = 0
    for i in range(3):
        browser.execute_script("scrollBy("+ str(value) +",+1000);")
        value += 1000
        time.sleep(1)
    
    elem1 = browser.find_element(By.ID, 'islmp')
    sub = elem1.find_elements(By.TAG_NAME, 'img')
    
    j=0
    for j,i in enumerate(sub):
        if j < n_images:
            src = i.get_attribute('src')                         
            try:
                if src != None:
                    src  = str(src)
                    print(src)
                    
                    urllib.request.urlretrieve(src, os.path.join(save_folder, topic+str(j)+'.jpg'))
                else:
                    raise TypeError
            except Exception as e:              #catches type error along with other errors
                print(f'fail with error {e}')
    
    browser.close()
    
if __name__ == "__main__":
    main()

