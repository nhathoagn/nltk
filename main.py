# # import libraries
# from builtins import list
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# # specify the url
# url = "https://www.bbc.com/sport/football/46897172"
#
# # Connect to the website and return the html to the variable ‘page’
# try:
#     page = urlopen(url)
# except:
#     print("Error opening the URL")
#
# # parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(page, 'html.parser')
# print(soup)
# # Take out the <div> of name and get its value
# # content = soup.find('div', {"class": "story-body sp-story-body gel-body-copy"})
#
# # article = ''
# # for i in content.findAll('p'):
# #     article = article + ' ' +  i.text
# # print(article)
# #
# # # Saving the scraped text
# # with open('scraped_text.txt', 'w') as file:
# #     file.write(article)
from bs4 import BeautifulSoup
import requests

url="https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify()) # print the parsed data of html

for link in soup.find_all("p"):
    # print("Inner Text: {}".format(link.text))
    # print("Title: {}".format(link.get("title")))
    # print("href: {}".format(link.get("href")))
     print(link)