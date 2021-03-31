# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:32:31 2021

@author: ALI
"""
from selenium import webdriver
import os
import urllib
import time

path = r'C:\Program Files\chromedriver.exe'

url_prefix = "https://www.google.com.sg/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591"

topics =[]

save_folder = 'Images'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    
    topics.append("cat")
    topics.append("dog")
    topics.append("car")
    topics.append("cycle")
    topics.append("bike")
    
    n_images = 5
    
    
    download_images(topics,n_images)
    
def download_images(topics,n_images):
    
    
    
    
    path = 'C:/Program Files/chromedriver/chromedriver.exe'
    
    driver = webdriver.Chrome(path)
    
    for topic in topics:
        search_url = url_prefix+topic+url_postfix
        #print(search_url)
        
        driver.get(search_url)
        
        value = 0
        for i in range(3):
            driver.execute_script("scrollBy("+ str(value) +",+1000);")
            value += 1000
            time.sleep(1)
        
        elem1 = driver.find_element_by_id('islmp')
        sub = elem1.find_elements_by_tag_name('img')
        
        count=0
        for j,i in enumerate(sub):
            if j < n_images:
                src = i.get_attribute('src')                         
                try:
                    if src != None:
                        src  = str(src)
                        print(src)
                        
                        urllib.request.urlretrieve(src, os.path.join(save_folder, topic+str(count)+'.jpg'))
                        count += 1
                    else:
                        raise TypeError
                except Exception as e:              #catches type error along with other errors
                    print(f'fail with error {e}')
        
    driver.close()
    
if __name__ == "__main__":
    main()
