from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import wget
import time

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştır
# chrome_options.add_argument("--disable-gpu")  # GPU kullanımını devre dışı bırak (gereksiz hataları önlemek için)
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()
"""
twitter botumuzun yapabilecekleri
- Twitter hesabına giriş
- Tweetleri beğenme
- Tweet Paylaşma
- Takipçi değişimi hakkinda veri tutma
- Takipten Çıkan hesapları raporlama
- Takipçi analizi
- Hesaptan çıkış


Özellikler
----------
email : str
    user email for Twitter account
password : str
    user password for Twitter account
bot : WebDriver
    webdriver that carry out the automation tasks
is_logged_in : bool
    boolean to check if the user is logged in or not


Metotlar 
-------
login()
    logs user in based on email and password provided during initialisation
logout()
    logs user out
like_tweets(cycles: int)
    loops over number of cycles provided, scrolls the page down and likes the available tweets on the page in each loop pass


"""


class TwitterBot:

    def __init__(self, email, username, password):
        self.email= email
        self.username = username
        self.password = password
        self.bot = driver 
        self.is_logged_in = False

    def login(self):
        bot= self.bot
        bot.get("https://twitter.com/i/flow/login")
        time.sleep(1)
        username = bot.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(self.email)

        bot.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span").click()
        time.sleep(1)

        name = bot.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        name.send_keys(self.username)


        bot.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span").click()
        time.sleep(1)

        password = bot.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.password)

        bot.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span/span').click()
        time.sleep(3)
        self.is_logged_in = True
    
    def logout(self):
        if not self.is_logged_in:
            return
        bot = self.bot
        bot.get('https://twitter.com/home')
        time.sleep(4)

        bot.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div').click()
        time.sleep(1)
        bot.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]').click()
        time.sleep(1)
        bot.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div').click()
        self.is_logged_in = False

    def Post_tweets(self, tweetext):
        if not self.is_logged_in:
            raise Exception("Önce Giriş Yapmalısınız")
        
        bot = self.bot
        # tweet atmak için kod: 
        bot.get("https://twitter.com/home")
        time.sleep(2)
        bot.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div').click()
        tweet = bot.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(tweetext)

        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div["2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div').click()


    def VideoDownloader(url):
        pass
        



