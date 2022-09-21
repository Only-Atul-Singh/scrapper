import requests #to deal with http requests
from bs4 import BeautifulSoup #to parse html

# create a request
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')

# find relevent part and stored in a list
jobss = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
for jobs in jobss:
    jd = jobs.find('span',class_="sim-posted").text
    if 'few' in jd:

        # finding Compeny name
        cname = jobs.find('h3',class_="joblist-comp-name").text.replace(' ','')

        # finding all the skills Required
        skill = jobs.find('span',class_="srp-skills").text.replace(' ','')

        # finding links of the Compeny
        link = jobs.find('a')

        print(f"Compeny Name : {cname.strip()}")
        print(f"Required Skills : {skill.strip()}")
        print(f"More Info : {link['href']}")
        print('  ')
        print(100*'-')
        print('  ')