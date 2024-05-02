import re
import urllib.request


# 把網站的內容撈回來
def fetch_kshs_web_content():
    bot = urllib.request.urlopen('https://www.kshs.kh.edu.tw/view/index.php?WebID=269')
    content = bot.read().decode('utf8')
    return content

# 用正規表示式把最新消息的標題撈出來
def fetch_kshs_news(content):
    for each_news in re.findall(r'28016.+NowSubId=0">(.+)</a>', content):
        print(each_news)


content = fetch_kshs_web_content()
fetch_kshs_news(content)
