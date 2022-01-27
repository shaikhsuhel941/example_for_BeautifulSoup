from bs4 import BeautifulSoup as bs
import requests

# <img style="height:auto;" alt="" width="260" height="260" class="avatar avatar-user width-full border color-bg-default" src="https://avatars.githubusercontent.com/u/97778625?v=4">

user_name = input('Enter your github user_name : ')
url = f"https://github.com/{user_name}"
source_code = requests.get(url).text
soup = bs(source_code, 'lxml')
profile_img = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_img)
