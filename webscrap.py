from urllib import request
from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
    soup  = BeautifulSoup(html_text, 'lxml') 
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        post_date = job.find('span', class_='sim-posted').span.text
        if 'month' not in post_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            if '(MoreJobs)' not in company_name:
                key_skills = job.find('span', class_="srp-skills").text.replace(' ','')
                with open('C:\\Users\\user\\Desktop\\Skills in Demand\\ScrapResults.txt', 'a') as f:
                    f.write(f"{key_skills.strip()},")
                    
                print(f'File Saved: {index}')

if __name__ == '__main__':
    if True:
        find_jobs()
        sleep_time = 1440
        print('Waiting for 1 day to run...')
        time.sleep(sleep_time)

