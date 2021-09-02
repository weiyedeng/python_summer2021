
#%% SETUP
import re
from weibo_scraper import get_weibo_profile
from weibo_scraper import  get_weibo_tweets_by_name
from weibo_scraper import  get_formatted_weibo_tweets_by_name
import csv

result_iterator = get_formatted_weibo_tweets_by_name(name='嘻红豆', pages=1)
people_tweets = get_weibo_tweets_by_name(name='人民日报', pages=2)

for tweet in people_tweets:
    print(tweet)

tweet['mblog']['page_info']
tweet['mblog']['reposts_count']
tweet['mblog']['attitudes_count']
tweet['mblog']['text']
sample = 'I am from 美国。We should be friends. 朋友。'
re.findall(r'[\u4e00-\u9fff|\d]+',tweet['mblog']['text'])

# Get hashtags
re.findall(r'#.*?#',tweet['mblog']['text'])

with open ('people_daily.csv', 'w', newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames = ("ID", "Created_at", "Title", "Text", "Hashtags", "Reposts_Count", "Comments_Count", "Attitudes_Count", "type", "Video_Play_Count")) # define colnames
    
    
# =============================================================================
#     addresses = {} # create an empty dict
#     j = 0
#     for i in range(22):
#         if i > 0:
#             each_page_url = web_url + "?page=" + str(i)
#         else:
#             each_page_url = web_url # get the web address of each page
#             # alternatively, we can also do selenium to scroll down and choose next page, but making use of the 
#             # patterns of the page urls here is more efficient
#         each_page = urllib.request.urlopen(each_page_url) # read the web address of each page with urllib
#         soup = BeautifulSoup(each_page.read(), features="lxml") # open each page with soup
#         title_urls = soup.find_all('div', class_ = 'field-title') # get all the links 
#         for url in title_urls:
#             latter_url = url.find('a')["href"] # get the second part of url for each address/remark
#             address_url = "https://www.presidency.ucsb.edu" + latter_url # get the complete url for each address/remark
#             each_address = urllib.request.urlopen(address_url) # read the url for each
#             address_soup = BeautifulSoup(each_address.read().decode('utf-8'), features="lxml") # open each address/remark in each page with soup
#             if address_soup.find('h3', class_ = "diet-title").text != 'Donald J. Trump': # get only Biden's addresses/remarks; can also check dates after Jan 20
#                 addresses["Date"] = address_soup.find('span', class_ = 'date-display-single').text.strip('\n') # get the date in each address/remark
#                 addresses["Title"] = address_soup.find('div', class_ = 'field-ds-doc-title').text.strip('\n') # get the title
#                 addresses["Texts"] = address_soup.find('div', class_ = 'field-docs-content').text.strip('\n') # get the content
#                 try:
#                     addresses["Footnote"] = address_soup.find('div', class_ = 'field-docs-footnote').text.strip('\n') # get the footnote if no error
#                 except:
#                     addresses["Footnote"] = "NA" # if nothing then NA
#                 try:
#                     addresses["Citation"] = address_soup.find('div', class_ = 'field-prez-document-citation').text.strip('\n') # get the citation
#                 except:
#                     addresses["Citation"] = "NA" # if nothing then NA
#                 w.writerow(addresses)
#                 j += 1
#                 print(j) # counter
#                 time.sleep(random.uniform(1, 5)) # be polite
#             else:
#                 break
# =============================================================================


