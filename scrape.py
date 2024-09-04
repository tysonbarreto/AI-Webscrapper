import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_website(website):
    print("Launching chrome browser...")
    
    chrome_driver_path = "./resource/chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    with driver:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        #time.sleep(10)
        return html

def extract_cleaned_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        content = str(body_content)
    else:
        content =''
        
    soup = BeautifulSoup(content, 'html.parser')
    content_list = [i.getText('\n')  for i in soup]
    content = '\n'.join(content_list[0].splitlines())
    return content
#[content[i:i+max_length] for i in range(0, len(content), max_length)]

def get_chunks(content, max_length=6000):
    return [content[i:i+max_length] for i in range(0, len(content), max_length)]