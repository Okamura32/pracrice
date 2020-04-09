
import requests
from bs4 import BeautifulSoup

def Weather():
  response=requests.get('https://weather.yahoo.co.jp/weather/jp/20/4810/20201.html')

  html=response.text
  soup=BeautifulSoup(html,'html.parser')

  l=[]
  time=[]
  weth=[]
  temp=[]
  humi=[]
  preci=[]
  wind=[]

  for a in soup.select('''body > #wrapper > #contents > #contents-body > #main > div[class="yjw_main_md"] > 
  #yjw_pinpoint > #yjw_pinpoint_today > table[class="yjw_table2"] > tr > td >small'''):
    l.append(a.text)


  now=9
  time=l[1:now]
  del(l[:now])
  weth=l[1:now]
  del(l[:now])
  temp=l[1:now]
  del(l[:now])
  humi=l[1:now]
  del(l[:now])
  preci=l[1:now]
  del(l[:now])
  wind=l

  l=[]
  ans=""
  # for i in range(len(time)):
  #   l.append(str(time[i])+":"+"天気は"+str(weth[i])+":"+"気温は"+str(temp[i])+"℃")
    # print(time[i],":"+" 天気は",weth[i],":","気温 は",temp[i],"℃")
  temp=[int(x) for x in temp]
  max_temp=max(temp)
  min_temp=min(temp)
  cloud=weth.count("曇り")
  sunny=weth.count("晴れ")
  rainy=weth.count("雨")
  max_weth=max(cloud,sunny,rainy)

  today=""
  count=0
  if cloud==max_weth:
    today="曇り"
    count=1
  if sunny==max_weth:
    if count==1:
      today+="または晴れ"
    else:
      today="晴れ"
      count=1
  if rainy==max_weth:
    if count==1:
      today+="雨"
    else:
      today="雨"



  ans="最高気温は"+str(max_temp)+"℃ "+" 最低気温は"+str(min_temp)+"℃ "+" 多分"+today
  return ans


  
