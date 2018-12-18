import urllib.request
import urllib.parse
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
        return json

    def send_message(self,chat_id,text):
        url = self.base_url % (self.token,"sendMessage")
        params = urllib.parse.urlencode({"chat_id": chat_id ,"text": text})     #url encoding string == "chat_id=?&text=?"
        url = url + "?" + params
        req = urllib.request.Request(url)
        req.add_header("charset","UTF-8")
        req.add_header("Content-Type","application/json")
        urlopen(req)
