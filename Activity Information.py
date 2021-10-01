import requests
from bs4 import BeautifulSoup
import pandas as pd
arr = []
url = 'https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx'
html = requests.get(url)
html.encoding = 'utf8'
cl = []
idx = ["活動名稱","主辦單位","活動日期","報名時間","認證時數"]
sp = BeautifulSoup(html.text, 'lxml')
for i in range (0,5):
    arr.append([])
    for j in range (10):
        if(i==0):
            data = sp.find(id = "BodyContent_gvActs_lblGv_act_name_"+str(j))
            if data is None:
                break
            arr[i].append(data.text)
            cl.append(j+1)
        if(i==1):
            data = sp.find(id = "BodyContent_gvActs_lblGv_act_unit_"+str(j))
            if data is None:
                break
            arr[i].append(data.text)
        if(i==2):
            data = sp.find(id = "BodyContent_gvActs_lblGv_act_dt_"+str(j))
            if data is None:
                break
            arr[i].append(data.text)
        if(i==3):
            data = sp.find(id = "BodyContent_gvActs_lblGv_reg_dt_"+str(j))
            if data is None:
                break
            arr[i].append(data.text)
        if(i==4):
            data = sp.find(id = "BodyContent_gvActs_lblGv_xsl_check_"+str(j))
            if data is None:
                break
            arr[i].append(data.text)
    
arr2 = pd.DataFrame(arr,columns = cl, index = idx)
arr2
