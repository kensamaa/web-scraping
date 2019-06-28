
import requests
#import urllib3
import urllib
from bs4 import BeautifulSoup as soup

url ='https://www.avito.ma/fr/casablanca/téléphones-à_vendre'
response = requests.get(url)
page_soup = soup(response.text, "html.parser")#get the html page

containers=page_soup.find_all('div',{"class":"item li-hover"})#the div in the web that has the info abt each product
#print( "how many  ",len(containers))#how many products

filename="products.csv"
f=open(filename,"w")
headers=("name, price\n")
f.write(headers)
for container in containers:#show all names
    name=container.a.div.div.img["title"]
    print("name : "+name)  
    try:#some products dont have prices
        '''<div class="item-price" style="margin-top: -91px;">
        <span class="mrs fs14">
            <span class="price_value" dir="ltr">1 600</span>
            DH
        </span>'''
        priceContainer=container.find_all('div',{"class":"item-price"})#fetch prices depend on div
        price=priceContainer[0].span.span.text.strip()
        print("price : "+price+" dh")
        f.write(name.replace(",","/")+","+price+"\n")
    except:
        print("no price")
    
    print("+++++++++++++++++")
f.close()
 
