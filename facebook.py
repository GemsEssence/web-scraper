from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
import random
import requests
import re
import csv
from time import sleep



def validate_phone_number(txt):
    validate_phone_number_pattern = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    return bool(re.match(validate_phone_number_pattern, txt))


def validate_emails(txt):
    validate_email_pattern = "[a-z0-9.]+@[a-z]+\.[a-z]{2,3}"
    return bool(re.match(validate_email_pattern, txt))


def create_empty_entry():
    return [{"email": None, "number": None, "address": None}]


def fetch_facebook_data(facebookUrl):
    entry_list=[]
    entry_dict={} 
    try:
        # For Firefox
        options = Options() 
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

        url = facebookUrl.replace('\n', '')
        driver.get(url)
        
        src = driver.page_source
        soup = BeautifulSoup(src, 'html.parser')
        driver.close()
    except:
        return create_empty_entry()


    try:    
        items = soup.find_all('div',{'class':'x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x1qjc9v5 xozqiw3 x1q0g3np x1pi30zi x1swvt13 xyamay9 xykv574 xbmpl8g x4cne27 xifccgj'})[1] 
        allDetails = items.find_all("div",{"class":"x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1nhvcw1 x1qjc9v5 xozqiw3 x1q0g3np xyamay9 xykv574 xbmpl8g x4cne27 xifccgj"})
        for contact in allDetails: 
            checkaddress = len(contact.text.split(",")) 
            if(checkaddress>2): 
                try: 
                    entry_dict["address"]=contact.text 
                except: 
                    entry_dict["address"]=None 

            checknumber = validate_phone_number(contact.text) 
            if checknumber: 
                try: 
                    entry_dict["number"]=contact.text 
                except: 
                    entry_dict["number"]=None 

            checkemail = validate_emails(contact.text)
            if checkemail: 
                try: 
                    entry_dict["email"]=contact.text 
                except: 
                    entry_dict["email"]=None 
        entry_list.append(entry_dict)
        
    except:
        try:
            allDetails = soup.find_all("span",{"class":"x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x6prxxf xvq8zen xo1l8bm xzsf02u"}) 
            for contact in allDetails: 
                checkaddress = len(contact.text.split(",")) 
                if(checkaddress>2): 
                    try: 
                        entry_dict["address"]=contact.text 
                    except: 
                        entry_dict["address"]=None 

                checknumber = validate_phone_number(contact.text) 
                if checknumber: 
                    try: 
                        entry_dict["number"]=contact.text 
                    except: 
                        entry_dict["number"]=None 

            allDetails = soup.find_all("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1fey0fg"}) 
            for contact in allDetails: 
                checkemail = validate_emails(contact.text)
                if checkemail: 
                    try: 
                        entry_dict["email"]=contact.text 
                    except: 
                        entry_dict["email"]=None 

            entry_list.append(entry_dict)
        except:
            entry_dict["email"]=None 
            entry_dict["number"]=None 
            entry_dict["address"]=None 
            entry_list.append(entry_dict)
    
    return entry_list


def driver():
    facebook_profiles = []
    with open("facebook_users.txt") as file:
        for line in file:
            facebook_profiles.append(line.strip())

    filename = "facebook_data.csv"
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        fields = ['Facebook Url', 'Email', 'Number', 'Address'] 
        csvwriter.writerow(fields)
        for facebook_url in facebook_profiles:
            facebook_data = fetch_facebook_data(facebook_url)
            fields[0] = facebook_url
            try:
                fields[1] = facebook_data[0]['email']
            except:
                fields[1] = 'None'

            try:
                fields[2] = facebook_data[0]['number']
            except:
                fields[2] = 'None'

            try:
                fields[3] = facebook_data[0]['address']
            except:
                fields[3] = 'None'
            csvwriter.writerow(fields)
            sleep(5)


driver()