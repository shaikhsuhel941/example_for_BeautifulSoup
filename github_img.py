from bs4 import BeautifulSoup as bs
import requests

user_name = input('Enter your github user_name : ')
url = f"https://github.com/{user_name}"
source_code = requests.get(url).text
soup = bs(source_code, 'lxml')
profile_img = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_img)
