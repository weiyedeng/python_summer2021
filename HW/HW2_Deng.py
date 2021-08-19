# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:58:21 2021

@author: Rex DENG
"""
from bs4 import BeautifulSoup
import urllib
import csv
import os
import time

os.chdir('E:/mine/academics_career/Website/python_summer2021/HW')
with open ('biden_address.csv', 'w', newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames = ("Date", "Title", "Texts", "Footnote", "Citation")) # define colnames
    w.writeheader() # write the header into csv
    web_url="https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks"
    
    addresses = {} # create an empty dict
    j = 0
    for i in range(1):
        if i > 0:
            each_page_url = web_url + "?page=" + str(i)
        else:
            each_page_url = web_url # get the web address of each page
        each_page = urllib.request.urlopen(each_page_url) # read the web address of each page with urllib
        soup = BeautifulSoup(each_page.read(), features="lxml") # open each page with soup
        title_urls = soup.find_all('div', class_ = 'field-title') # get all the links 
        for url in title_urls:
            latter_url = url.find('a')["href"] # get the second part of url for each address/remark
            address_url = "https://www.presidency.ucsb.edu" + latter_url # get the complete url for each address/remark
            each_address = urllib.request.urlopen(address_url) # read the url for each
            address_soup = BeautifulSoup(each_address.read().decode('utf-8'), features="lxml") # open each address/remark in each page with soup
            if address_soup.find('h3', class_ = "diet-title").text == 'Joseph R. Biden': # get only Biden's addresses/remarks
                addresses["Date"] = address_soup.find('span', class_ = 'date-display-single').text.strip('\n') # get the date in each address/remark
                addresses["Title"] = address_soup.find('div', class_ = 'field-ds-doc-title').text.strip('\n') # get the title
                addresses["Texts"] = address_soup.find('div', class_ = 'field-docs-content').text.strip('\n') # get the content
                try:
                    addresses["Footnote"] = address_soup.find('div', class_ = 'field-docs-footnote').text.strip('\n') # get the footnote if no error
                except:
                    addresses["Footnote"] = "NA" # if nothing then NA
                try:
                    addresses["Citation"] = address_soup.find('div', class_ = 'field-prez-document-citation').text.strip('\n') # get the citation
                except:
                    addresses["Citation"] = "NA" # if nothing then NA
                w.writerow(addresses)
                j += 1
                print(j) # counter
                time.sleep(1) # be polite
            else:
                break
            if j == 9:
                break
            

            
i = 1
each_page_url = web_url + "?page=" + str(i) # get the web address of each page
each_page = urllib.request.urlopen(each_page_url) # read the web address of each page with urllib
soup = BeautifulSoup(each_page.read(), features="lxml") # open each page with soup
title_links = soup.find_all('div', class_ = 'field-title')

for url in title_links:
    latter_url = url.find('a')["href"]
    remark_url = "https://www.presidency.ucsb.edu" + latter_url
each_remark = urllib.request.urlopen(remark_url)
address_soup = BeautifulSoup(each_remark.read(), features="lxml")
print(address_soup.find('span', class_ = 'date-display-single').text.strip('\n'))
print(address_soup.find('div', class_ = 'field-ds-doc-title').text.strip('\n'))
print(address_soup.find('div', class_ = 'field-docs-content').text.strip('\n'))
print(address_soup.find('div', class_ = 'field-docs-footnote').text)
print(address_soup.find('h3', class_ = "diet-title").text)
print(address_soup.find('div', class_ = 'field-prez-document-citation').text.strip('\n'))


# =============================================================================
# with open('iceland_test.csv', 'w') as f: # set up with the writer
#   w = csv.DictWriter(f, fieldnames = ("name", "party", "phone")) # define column names
#   w.writeheader() # write the header
#   web_address='https://www.althingi.is/altext/cv/en/' # the web address
#   web_page = urllib.request.urlopen(web_address) # open the web page
#   soup = BeautifulSoup(web_page.read()) # soup the web page
#   all_members = soup.find_all('tr') # find the list of names and parties
#   for i in range(1,3): # for members 1 and 2 (member 0 is just the table heading)
#     try:
#       member = {} ## empty dictionary to fill in
#       member_i = all_members[i].find_all('td') # subset lower to each individual item
#       member["name"] = member_i[0].text # member's name
#       member['party'] =  member_i[1].text # member's party
#       inner_page_url = web_address + member_i[0].a['href'] # get the extension to their personal page
#       inner_page = urllib.request.urlopen(inner_page_url) # open the personal page
#       inner_soup = BeautifulSoup(inner_page.read()) # soup the personal page
#       member['phone'] = inner_soup.find('a', {'class' : 'tel'}).text # get phone number
#     except:
#       member['name'] = 'NA'
#       member['party'] = 'NA'
#       member['phone'] = 'NA'
#     w.writerow(member) # write the row for this specific member
#     time.sleep(random.uniform(1, 5)) # be polite, sleep!
# =============================================================================


# =============================================================================
# with open("washu_faculty.csv", "w") as f:
#     # 
#     w = csv.DictWriter(f, fieldnames= ("Name", "Title", "E-mail", "Webpage", "Specialization") )
#     w.writeheader()
#     web_address = 'https://polisci.wustl.edu/people/88/all'
#     web_page = urllib.request.urlopen(web_address)
#     soup = BeautifulSoup(web_page.read(), features="lxml") 
#     s = soup.find_all("a", class_="card")
#     faculty = {} # dict
#     for i in s:
#         faculty["Name"] = i.h3.text
#         faculty["Title"] = i.find(class_ = "dept").text
#         if i["href"][0] == '/':
#             webpage = "https://polisci.wustl.edu" + i["href"]
#         else: 
#             webpage = i["href"]
#         new_page = urllib.request.urlopen(webpage)
#         new_soup = BeautifulSoup(new_page.read(), features = "lxml")
#         try: 
#             faculty["E-mail"] = new_soup.find(class_ = "detail contact").find("a").text
#         except: 
#             faculty["E-mail"] = "N/A"
#         try: 
#             faculty["Webpage"] = new_soup.find(class_ = "links").find("a")["href"]
#         except:
#             faculty["Webpage"] = "N/A"
#         try: 
#             faculty["Specialization"] = new_soup.find(class_ = "post-excerpt").text
#         except: 
#             faculty["Specialization"] =  "N/A"
#         w.writerow(faculty)
#         time.sleep(random.uniform(1, 5))
# =============================================================================
