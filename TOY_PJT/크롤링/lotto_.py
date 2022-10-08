import requests


for nums in range(1036):
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={nums}"
    response = requests.get(url).json()


# url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1024'
# response = requests.get(url).json()


print(response)
