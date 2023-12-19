from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import requests
from time import sleep
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import TimeoutException
import csv



linkedIn_profiles = []
with open("linkedIn_users.txt") as file:
    for line in file:
        linkedIn_profiles.append(line.strip())


filename = "linkedIn_data.csv"
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    fields = ['Company Name', 'Industries', 'Website', 'Specialties', 'Size', 'Headquarters', 'OrganizationType', 'FoundedOn', 'Followers', 'Branches', 'Employees'] 
    csvwriter.writerow(fields)
    for linkedIn_url in linkedIn_profiles:
        options = Options() 
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(linkedIn_url)

        src = driver.page_source
        soup = BeautifulSoup(src, 'html.parser')
        driver.close()

        try:
            fields[0] = soup.find("h1", {"class": "top-card-layout__title"}).get_text().strip()
        except:
            fields[0] = 'None'
            
        try:
            industries_data = soup.find("div", {"data-test-id": "about-us__industry"})
            fields[1] = industries_data.find("dd", {"class": "overflow-hidden"}).get_text().strip()
        except:
            fields[1] = 'None'

        try:
            website_data = soup.find("div", {"data-test-id": "about-us__website"})
            fields[2] = website_data.find("a", {"class": "link-no-visited-state"}).get_text().strip()
        except:
            fields[2] = 'None'

        try:
            specialties_data = soup.find("div", {"data-test-id": "about-us__specialties"})
            fields[3] = specialties_data.find("dd", {"class": "overflow-hidden"}).get_text().strip()
        except:
            fields[3] = 'None'

        try:
            size_data = soup.find("div", {"data-test-id": "about-us__size"})
            fields[4] = size_data.find("dd", {"class": "overflow-hidden"}).get_text().strip()
        except:
            fields[4] = 'None'

        try:
            headquarters_data = soup.find("div", {"data-test-id": "about-us__headquarters"})
            fields[5] = headquarters_data.find("dd", {"class": "overflow-hidden"}).get_text().strip()
        except:
            fields[5] = 'None'

        try:
            org_type_data = soup.find("div", {"data-test-id": "about-us__organizationType"})
            fields[6] = org_type_data.find("dd", {"class": "overflow-hidden"}).get_text().strip()
        except:
            fields[6] = 'None'

        try:
            founded_on_data = soup.find("div", {"data-test-id": "about-us__foundedOn"})
            fields[7] = founded_on_data.find("dd", {"class": "overflow-hidden"}).get_text().strip()
        except:
            fields[7] = 'None'

        try:
            followers_data = soup.find_all("div", {"data-test-id": "main-feed-activity-card__entity-lockup"})
            fields[8] = followers_data[1].find("p", {"class": "text-color-text-low-emphasis"}).get_text().strip()
        except:
            fields[8] = 'None'

        try:
            branches_data = soup.find_all("li", {'class': 'papabear:odd:w-[calc(50%-16px)]'})
            branches = []
            for address in branches_data:
                temp_addresses = address.find("div")
                location = temp_addresses.get_text().strip().replace("  ", "").replace("\n\n", ", ").replace("\n", "")
                branches.append(location)
            fields[9] = '  ;  '.join(branches)
        except:
            fields[9] = 'None'

        try:
            employees_data = soup.find_all("h3", {'class': 'base-main-card__title'})
            employees = [emp.get_text().strip() for emp in employees_data]
            fields[10] = ', '.join(employees)
        except:
            fields[10] = 'None'

        print('Fields : ', fields)
        csvwriter.writerow(fields)
        sleep(5)