import os
from bot_class import TwitterBot

email= "cihatdayi5@gmail.com"
username =  "LFCSZC"
password = "Antalya.7"
if __name__ == "__main__":
    try:
        pj = TwitterBot(email=email,username=username,password=password)
        pj.login()
        pj.Post_tweets("")
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)