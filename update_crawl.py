import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import time

url = 'https://vnexpress.net/bong-da'
def cr(url,filename):
    driver.get(url)
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for k in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(k))
    listOfImage = []
    i = 1
    


    # eleList = driver.find_element_by_tag_name("article")
    # print(eleList)
    # ele = eleList
    try:
        while(i<34):
            if i==6 or i==13 or i ==20 or i==27:
                i+=1
            urlI = "/html/body/section[5]/div/div[1]/div[2]/article["+str(i)+"]/div/a/picture/img"
            
            urlAbstract = driver.find_element(By.XPATH,urlI).get_attribute('src')
            if(urlAbstract):
                print(i,'.',urlAbstract)
                listOfImage.append(urlAbstract)

                print(urlAbstract)
                i+=1
            else:
                i+=1

                
    except:
        pass
    j = 1
    while listOfImage:
        link = listOfImage.pop()
        print(link)
        img = Image.open(requests.get(link, stream=True).raw)
        filename1 = filename+"hinh"+str(j)+".png"
        img.save('./xe_train/'+filename1 ,'')
        j+=1
p = 1
url = 'https://vnexpress.net/bong-da'
filename = "page"+str(p)
cr(url,filename)
while(p<20):   
    p+=1
    url = 'https://vnexpress.net/bong-da-p'
    url+=str(p)
    filename = "page"+str(p)
    cr(url,filename)

driver.close()
driver.quit