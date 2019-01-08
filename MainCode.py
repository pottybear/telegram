#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
import sqlite3
from bot import A
import re
import requests

conn = sqlite3.connect("/home/ubuntu/epl/epl.db")
cur = conn.cursor()

goaltext = "[%s]  (vs. %s)  <b>%s</b> ⚽️ ⚽️ ⚽️ ⚽️ ⚽️ ⚽️ \n%s scored a goal in today's game !\n<b>Check the links below for more details!!!</b>"

assisttext = "[%s]  (vs. %s)  <b>%s</b> ⚽️ ⚽️ ⚽️ ⚽️ ⚽️ ⚽️ \n%s assisted in scoring in today's game !\n<b>Check the links below for more details!!!</b>"

link = "http://www.spotvnews.co.kr/?mod=news&act=articleView&idxno=%s&sc_code=&page=&total="

def son():
    cur.execute("select date from telson order by id desc limit 1")
    trigger = cur.fetchone()[0]

    if trigger != "None" :  # It checks for signals that send telegram text messages.
        cur.execute("select goal,assist,date,vs,result from son order by id desc limit 1")
        stats = cur.fetchone()
        goal,assist,vs,result = stats[0],stats[1],stats[3],stats[4]
        date = str("20" + stats[2]).replace(".", "-")

        html = requests.get("http://www.spotvnews.co.kr/?mod=news&act=articleList&sc_area=A&sc_sdate={0}&sc_edate={0}&sc_word=pl+review".format(date))
        content = bs(html.content.decode("utf-8"), "html.parser")
        contentlist = content.find("div", {"class" : "article_list"}).find_all("a", {"class" : "list_title_a"})
        linkNum = ""
        for Y in range(len(contentlist)):
            ok = re.compile("손흥민").search(str(contentlist[Y]))
            if ok != None:
                linkNum = re.compile(r"idxno=(?P<obj>\d+)",re.I).findall(str(contentlist[Y]))[0]

        if len(linkNum) <= 2 :
            print("not find")


        elif int(goal) >= 1 :
            A.send_photo("-1001473413632", "AgADBQADS6gxGxEK2VTGX2aIBaQNlRhs3jIABOWsiCpr_uLKSXwBAAEC", goaltext % (date, vs, result, "Son Heung-Min"))
            A.send_message("-1001473413632", link % (linkNum))

            A.send_photo("607901207", "AgADBQADS6gxGxEK2VTGX2aIBaQNlRhs3jIABOWsiCpr_uLKSXwBAAEC", goaltext % (date, vs, result, "Son Heung-Min"))
            A.send_message("607901207", link % (linkNum))

            cur.execute("insert into telson values(null,'None')")
            conn.commit()
            cur.close()

        elif int(assist) >= 1 :
            A.send_photo("-1001473413632", "AgADBQADS6gxGxEK2VTGX2aIBaQNlRhs3jIABOWsiCpr_uLKSXwBAAEC", assisttext % (date, vs, result, "Son Heung-Min"))
            A.send_message("-1001473413632", link % (linkNum))

            A.send_photo("607901207", "AgADBQADS6gxGxEK2VTGX2aIBaQNlRhs3jIABOWsiCpr_uLKSXwBAAEC", assisttext % (date, vs, result, "Son Heung-Min"))
            A.send_message("607901207", link % (linkNum))

            cur.execute("insert into telson values(null,'None')")
            conn.commit()
            cur.close()

        else :
            cur.execute("insert into telson values(null,'None')")
            conn.commit()
            cur.close()

def ki():
    cur.execute("select date from telki order by id desc limit 1")
    trigger = cur.fetchone()[0]

    if trigger != "None" :  # It checks for signals that send telegram text messages.
        cur.execute("select goal,assist,date,vs,result from ki order by id desc limit 1")
        stats = cur.fetchone()
        goal, assist, vs, result = stats[0], stats[1], stats[3], stats[4]
        date = str("20" + stats[2]).replace(".", "-")

        html = requests.get("http://www.spotvnews.co.kr/?mod=news&act=articleList&sc_area=A&sc_sdate={0}&sc_edate={0}&sc_word=pl+review".format(date))
        content = bs(html.content.decode("utf-8"), "html.parser")
        contentlist = content.find("div", {"class" : "article_list"}).find_all("a", {"class" : "list_title_a"})
        linkNum = ""
        for Y in range(len(contentlist)):
            ok = re.compile("기성용").search(str(contentlist[Y]))
            if ok != None:
                linkNum = re.compile(r"idxno=(?P<obj>\d+)",re.I).findall(str(contentlist[Y]))[0]

        if len(linkNum) <= 2 :
            print("not find")


        elif int(goal) >= 1 :
            A.send_photo("-1001473413632", "AgADBQADT6kxG_dQ4VRNBrtB9iShOHl03zIABPpz_d91vMf6HPgAAgI", goaltext % (date, vs, result, "Ki Sung-Yueng"))
            A.send_message("-1001473413632", link % (linkNum))

            A.send_photo("607901207", "AgADBQADT6kxG_dQ4VRNBrtB9iShOHl03zIABPpz_d91vMf6HPgAAgI", goaltext % (date, vs, result, "Ki Sung-Yueng"))
            A.send_message("607901207", link % (linkNum))

            cur.execute("insert into telki values(null,'None')")
            conn.commit()
            cur.close()

        elif int(assist) >= 1 :
            A.send_photo("-1001473413632", "AgADBQADT6kxG_dQ4VRNBrtB9iShOHl03zIABPpz_d91vMf6HPgAAgI", assisttext % (date, vs, result, "Ki Sung-Yueng"))
            A.send_message("-1001473413632", link % (linkNum))

            A.send_photo("607901207", "AgADBQADT6kxG_dQ4VRNBrtB9iShOHl03zIABPpz_d91vMf6HPgAAgI", assisttext % (date, vs, result, "Ki Sung-Yueng"))
            A.send_message("607901207", link % (linkNum))

            cur.execute("insert into telki values(null,'None')")
            conn.commit()
            cur.close()


        else :
            cur.execute("insert into telki values(null,'None')")
            conn.commit()
            cur.close()


def hhc():

    hhcurl = '''https://search.naver.com/search.naver?where=news&query="황희찬""분데스2"&ds={0}&de={0}&docid=&nso=so%3Ar%2Cp%3Afrom{1}to{1}'''
    cur.execute("select date from telhhc order by id desc limit 1")
    trigger = cur.fetchone()[0]

    if trigger != "None" :  # It checks for signals that send telegram text messages.
        cur.execute("select goal,assist,date,vs,result from hhc order by id desc limit 1")
        stats = cur.fetchone()
        goal, assist, vs, result = stats[0], stats[1], stats[3], stats[4]
        date = str("20" + stats[2])

        html = requests.get(hhcurl.format(date,date.replace(".","")))
        content = bs(html.content.decode("utf-8"), "html.parser")

        try :
            linkNum = content.find("div", {"class" : "thumb"}).find("a", href = True)["href"]


            if int(goal) >= 1 :
                A.send_photo("-1001473413632", "AgADBQADTqkxG_dQ4VT3pZj7EZ6sbLJU2zIABDceEjl1znArro4CAAEC", goaltext % (date, vs, result, "Hwang Hee-Chan"))
                A.send_message("-1001473413632", linkNum)

                A.send_photo("607901207", "AgADBQADTqkxG_dQ4VT3pZj7EZ6sbLJU2zIABDceEjl1znArro4CAAEC", goaltext % (date, vs, result, "Hwang Hee-Chan"))
                A.send_message("607901207", linkNum)

                cur.execute("insert into telhhc values(null,'None')")
                conn.commit()
                cur.close()

            elif int(assist) >= 1 :
                A.send_photo("-1001473413632", "AgADBQADTqkxG_dQ4VT3pZj7EZ6sbLJU2zIABDceEjl1znArro4CAAEC", assisttext % (date, vs, result, "Hwang Hee-Chan"))
                A.send_message("-1001473413632", linkNum)

                A.send_photo("607901207", "AgADBQADTqkxG_dQ4VT3pZj7EZ6sbLJU2zIABDceEjl1znArro4CAAEC", assisttext % (date, vs, result, "Hwang Hee-Chan"))
                A.send_message("607901207", linkNum)

                cur.execute("insert into telhhc values(null,'None')")
                conn.commit()
                cur.close()


            else :
                cur.execute("insert into telhhc values(null,'None')")
                conn.commit()
                cur.close()

        except :
            print("Not found")


son()
ki()
hhc()
