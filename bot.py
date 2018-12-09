from urllib.request import urlopen

class Bot:
    base_url = "https://api.telegram.org/bot%s/%s"

    def __init__(self, token):
        self.token = token

    def get_me(self):
        url = self.base_url % (self.token, "getMe")
        res = urlopen(url)
        json = res.read()
        res.close()
