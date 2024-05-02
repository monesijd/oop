import re
import urllib.request

class KSHS_Bot:

    def get_web_content(self):
        bot = urllib.request.urlopen('https://www.kshs.kh.edu.tw/view/index.php?WebID=269')
        self.content = bot.read().decode('utf8')
    
    def show_news(self):
        for each_news in re.findall(r'28016.+NowSubId=0">(.+)</a>', self.content):
            print(each_news)

bot = KSHS_Bot()
bot.get_web_content()
bot.show_news()



