from selenium import webdriver
from selenium.webdriver.common.by import By
import json

browser = webdriver.Chrome()
browser.get('https://www.audible.in/adblbestsellers')

books_dic = []

last_page_number = int(browser.find_elements(By.CSS_SELECTOR,'.bc-link.refinementFormLink.pageNumberElement.bc-color-link')[1].text)

for _ in range(1,last_page_number):
    book_list = browser.find_elements(By.CSS_SELECTOR, ".bc-col-responsive.bc-col-6")


    for item in book_list:

        book_name = item.find_element(By.CSS_SELECTOR,'h3 a').text
        # print(book_name)
        temp_author_name = item.find_element(By.CSS_SELECTOR,'.bc-list-item.authorLabel a').text # if someting is in list then we cant convert it into text

        link = item.find_element(By.CSS_SELECTOR,'h3 a.bc-link.bc-color-link').get_attribute('href')


        books_dic.append({

            "Title" :book_name.replace('\u2019', ''),
            "author_name" :temp_author_name.replace('\u00e9',''),
            "Link" :link
        })

    next_page = browser.find_element(By.CSS_SELECTOR,'.bc-button.bc-button-secondary.nextButton.refinementFormButton.bc-button-small.bc-button-inline')
    next_page.click()

with open('Audible_Data_Final.json','w') as j:
    json.dump(books_dic,j, indent = 3)
