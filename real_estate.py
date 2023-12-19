import requests 
from bs4 import BeautifulSoup 
import csv


# Making a GET request 
r = requests.get('https://housing.com/in/buy/searches/P3fo3o3llgtfbceum_38f9yfbk7p3m2h1fZ3') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
    
cards = soup.find_all("div", {"class": "_mkh2mm _9s1txw _ar1bp4 _fc1yb4 _axkb7n _l8bsq7 _vy1x30 _gdnqedxx _ft8m16eo"})


filename = "real_estate.csv"
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    fields = ['Title', 'Location', 'Price', 'Area(in sq ft.)', 'Average Price', 'Number of rooms', 'EMI', 'Contact'] 
    csvwriter.writerow(fields)

    for individual_card in cards:   
        # Title    
        try:
            fields[0] = individual_card.find("h2", {"class": "_gi182v _1u71grho _7s5wglyw"}).get_text().strip()
        except:
            fields[0] = 'None'

        # Location
        try:
            fields[1] = individual_card.find("a", {"class": "link last-link _18uq1994 _ot7i1994"}).get_text().strip()
        except:
            fields[1] = 'None'

        # Price
        try:
            fields[2] = individual_card.find("div", {"class": "_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh"}).get_text().strip()
        except:
            fields[2] = 'None'

        # Area(in sq ft.)
        try:
            data = individual_card.find_all("div", {"class": "_sq1l2s _vv1q9c _ks15vq _vy1ipv _7ltvct _g3dlk8 _c81fwx _cs1nn1 value"})
            fields[3] = data[2].get_text().strip()
        except:
            fields[3] = 'None'

        # Average Price
        try:
            fields[4] = data[1].get_text().strip()
        except:
            fields[4] = 'None'

        # Number of rooms
        try:
            no_of_rooms = individual_card.find("h3", {"class": "_sq1l2s _vv1q9c _ks15vq _5vy24jg8 _blas14la _csbfng _g3dlk8 _c81fwx _h3ftgi"}).get_text()
            fields[5] = no_of_rooms.split('for sale in', 1)[0].strip()
        except:
            fields[5] = 'None'

        # EMI
        try:
            fields[6] = individual_card.find("span", {"class": "_9jtlke _l881bl _gzftgi _7l1994 _c81fwx _g3dlk8"}).get_text().strip()
        except:
            fields[6] = 'None'
        
        # Contact
        try:
            fields[7] = individual_card.find("div", {"class": "css-wni7av"}).get_text().strip()
        except:
            fields[7] = 'None'

        csvwriter.writerow(fields)
