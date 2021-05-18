
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('D:/CODE/intern/chromedriver')
import time

url =['https://vnexpress.net/the-thao']


def crawlImg(url):
    driver.get(url)
    time.sleep(15)
    eleList = driver.find_elements_by_tag_name("article")
    listOfImage = []
    index = 0
    i = 1
    o = 1
    try: 
        while eleList:
            ele = eleList.pop()
            #urlI = "/html/body/section[" + str(i) +"]/div/div/div/article/div/a/picture/img"
            urlI = "/html/body/section[6]/div/div[1]/article["+str(i)+"]/div/a/picture/img"
            
            urlAbstract = ele.find_element(By.XPATH,urlI).get_attribute('src')
            print(i,'.',urlAbstract)
            listOfImage.append(urlAbstract)
            i+=1
            # if(i>10):
            #     break
    except:
        pass
    j = 1
    while listOfImage:
        link = listOfImage.pop()
        print(link)
        img = Image.open(requests.get(link, stream=True).raw)
        filename = "hinh"+str(j)+".jpg"
        img.save('D:/CODE/intern/thethao/'+filename ,'')
        j+=1


try:
    for i in range(0,len(url)):
        print(i)
        crawlImg(url[i])

finally:
    driver.close()
    driver.quit()