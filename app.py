import os
from bot_class import TwitterBot

# private user keys

"""
userkeys.txt format
"email"
"username"
"password"

"""
with open("userkeys.txt", "r") as file:
    satirlar = file.readlines()
    if len(satirlar) >= 3:
        email = satirlar[0].strip()
        username = satirlar[1].strip()
        password = satirlar[2].strip()

# Post tweet
if __name__ == "__main__":
    try:
        pj = TwitterBot(email,username,password)
        pj.login()
        pj.Post_tweets("merhaba")
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)