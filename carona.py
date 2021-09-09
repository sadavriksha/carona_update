from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(
       title = title,
       message = message,
       app_icon = "add path"
       timeout = 15
    )

def getdata(url):
    r = requests.get(url)
    return r.text

if __name__=="__main__" :
     #notifyMe("sada" , "lets stop the spread of vrious") 
     myhtmldata = getdata('https://www.mohfw.gov.in/')
     soup = BeautifulSoup(myhtmldata,'html.parser')
     mydatastr = ""

     for tr in soup.find_all('tboby')[1].find_all('tr'):
         mydatastr += tr.get_text()
         mydatastr = mydatastr[1:]
         itenlist = mydatastr.split("\n\n")

         states = ['Chandigarh','Telengana','Uttar Pradesh']
         for item in itenlist[0:22]:
             datalist = item.split('\n')
             if datalist[1] in states:
                 nTitle = 'case of covid-19'
                 ntext = f"state {datalist[1]}\nindian : {datalist[2] & foregin : {datalist[3]}\nCured : {datalist[4]}\nDeaths : {datalist[5]}"
                 notifyMe(nTitle,ntext)
                 time.sleep(2)
     time.sleep(10)

