import requests
import re
import random
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
line_bot_api = LineBotApi('Yyx3Rhdcmm3nMz4FzpingmyAdsw5te+25wwZv4Udq3rHQT1ssPe7Z/iT3n9U3hzOGkwnlnV6J4Gr3ekkWOccW5cqeX+iAtkPr7Cg6gsM/hHR/PzzqkCE4qguXA9P5w12b2VzgaZxBuShhxJIbrVG8wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('df1ee6f8f7b3853bd5a71118bba186b8')

@app.route("/callback", methods=['POST'])
def callback():
    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def bus132(inputMessage):
    payload = {
    '__EVENTTARGET':'DropDownList1',
    '__EVENTARGUMENT':'',
    '__LASTFOCUS':'',
    '__VIEWSTATE':'/wEPDwULLTEyMjA1NzY1NTcPZBYCAgMPZBYIAgEPDxYCHgRUZXh0BSHoq4vpgbjmk4fopoHmn6XoqaLnmoTot6/nt5ogOiDjgIBkZAIDDxAPFgIeC18hRGF0YUJvdW5kZ2QQFYsBOOOAkDEwMeOAkeahg+Wcki3mlofkuK3ot68t5p6c6I+c5biC5aC0ICjljp/moYPlnJIxMDHot68pLOOAkDEwMuOAkeahg+Wcki3mma/pm7LmlrDmnZEgKOWOn+ahg+WckjLot68pLuOAkDEwM+OAkeahg+Wcki3oj6/mmKDlhazlj7ggKOWOn+ahg+WckjEwM+i3rykp44CQMTA144CR5qGD5ZySLeWkp+aciei3ryAo5Y6f5qGD5ZySNei3rykr44CQMTA344CR5qGD5ZySLeS4reW5s+i3ryAo5Y6f5qGD5ZySMTA36LevKS7jgJAxMDnjgJHmoYPlnJIt5paw6IiI6auY5LitICjljp/moYPlnJIxMDnot68pK+OAkDExMOOAkeS4reWjoi3mlofljJbot68gKOWOn+S4reWjojExMOi3ryko44CQMTEx44CR5Lit5aOiLeWNl+WLoiAo5Y6f5Lit5aOiMTEx6LevKTTjgJAxMTLljZfjgJHkuK3lo6It6Zm46LuN5bCI56eR5a245qChICjljp8xMTLljZfot68pLeOAkDExM+OAkeahg+Wcki3lubjnpo/npL7ljYAgKOWOn+ahg+WckjEz6LevKSvjgJAxMTXjgJHkuK3lo6It5bmz5p2x6LevICjljp/kuK3lo6IxMTXot68pLOOAkDExNuOAkeS4reWjoi3oh6rnq4vmlrDmnZEgKOWOn+S4reWjojbot68pKuOAkDExN+OAkeahg+Wcki3lr7bmhbbot68gKOWOn+ahg+WckjE36LevKS7jgJAxMTjjgJHkuK3lo6It5Lit5aOi6auY5LitICjljp/kuK3lo6IxMTjot68pLuOAkDExOeOAkeS4reWjoi3lo6LmlrDphqvpmaIgKOWOn+S4reWjojExOei3rykr44CQMTIw44CR5Lit5aOiLeWkquWtkOmOriAo5Y6f5Lit5aOiMTAy6LevKSnjgJAxMjXjgJHmoYPlnJIt5LiJ6IGW5a6uICjljp/moYPlnJI155SyKSzjgJAxMzLjgJHkuK3lo6It5Lit5aSu5aSn5a24ICjljp/kuK3lo6Iy6LevKS3jgJAxMzXjgJHkuK3lo6It5YWn5aOi6auY5LitICjljp/kuK3lo6IxNei3ryks44CQMTM344CR5qGD5ZySLemKmOWCs+Wkp+WtuCAo5Y6f5qGD5ZySN+i3rykz44CQMTM544CR5qGD5ZySLem+jeWjveihly3mlrDluoTlu58gKOWOn+ahg+Wckjnot68pKuOAkDE1MeOAkeahg+Wcki3lkIzlronooZcgKOWOn+ahg+WckjE16LevKSrjgJAxNTLjgJHmoYPlnJIt5ZCM5a6J6KGXICjljp/moYPlnJIxNei3ryks44CQMTU144CR5Lit5aOiLeWFg+aZuuWkp+WtuCAo5Y6f5Lit5aOiNei3ryks44CQMTU244CR5Lit5aOiLeWFg+aZuuWkp+WtuCAo5Y6f5Lit5aOiNei3ryk144CQMTU344CR5qGD5ZySLeWFq+W+ty3mlrDoiIjpq5jkuK0gKOWOn+ahg+WckjExN+i3ryks44CQMTY544CR5Lit5aOiLeiPr+WLm+ekvuWNgCAo5Y6f5Lit5aOiOei3rykw44CQMTcx44CR5Lit5aOiLemrmOmQteahg+WckuermSAo5Y6f5Lit5aOiMTHot68pKOOAkDE4OOOAkeahg+WckuW+jOermS3kuK3mraPol53mlofnibnljYBA44CQMTg4QeOAkeahg+WckuW+jOermS3kuK3mraPol53mlofnibnljYAo5bu26aeb5qGD5ZyS55uj55CG56uZKSXjgJAxQeOAkeS4reWjoi3moYPlnJIgKOWOn+S4reWjojHnlLIpKeOAkDFC44CR5Lit5aOiLeahg+Wckijlu7bpp5vmpq7msJHphqvpmaIpJ+OAkDHot6/jgJHkuK3lo6It5qGD5ZySICjljp/kuK3lo6Ix6LevKR/jgJAyMDHjgJHomIbnq7kt5YWr5b63ICjljp8yMDEpJeOAkDIwMuOAkemrlOiCsuWkp+WtuC3lt6Xlm5vlt6Xmpa3ljYAx44CQMjA244CR5qGD5ZySLemrmOmQteahg+WckuermSAo5Y6f5qGD5ZySMTA26LevKSvjgJAzMDFB44CR6b6c5bGxLealiuaihSjlu7bpp5vlo73lsbHpq5jkuK0pJeOAkDMwMei3r+OAkem+nOWxsS3mpYrmooUgKOWOnzMwMei3rykd44CQNTAwMOOAkeahg+Wcki3oh7PlloTpq5jkuK0m44CQNTAwMeOAkeahg+Wcki3kuInls73vvIjntpPkuK3muZbvvIkm44CQNTAwNeOAkeahg+Wcki3kuInls73vvIjntpPlsJblsbHvvIka44CQNTAwNuOAkeS4reWjoi3plbflronot68m44CQNTAwOOOAkeahg+Wcki3kuK3lo6LvvIjntpPpvo3lsqHvvIkp44CQNTAwOeOAkeahg+Wcki3mlrDojorvvIjntpPlj7DkuIDnt5rvvIkq44CQNTAx44CR5Y+w54Gj5aW96KGM5pmv6bue5o6l6aeB5oWI5rmW57eaL+OAkDUwMTDjgJHmoYPlnJIt5Lit5aOi77yI57aT5LuB576O44CB5YWr5b6377yJJuOAkDUwMTHjgJHmoYPlnJIt5Lit5aOi77yI57aT56u55be377yJLuOAkDUwMTTjgJHmoYPlnJIt5o236YGL5bGx6by756uZKOe2k+WNl+elpei3rykm44CQNTAxNeOAkeahg+Wcki3lpKflnJLvvIjntpPljZfltIHvvIkm44CQNTAxNuOAkeahg+Wcki3nq7nlnI3vvIjntpPlsbHohbPvvIkm44CQNTAxN+OAkeS4reWjoi3nq7nlnI3vvIjntpPmpYrljp3vvIkm44CQNTAxOOOAkeahg+Wcki3msLTlsL7vvIjntpPomIbnq7nvvIkm44CQNTAxOeOAkeahg+Wcki3mspnltJnvvIjntpPomIbnq7nvvIkt44CQNTAy44CR5Y+w54Gj5aW96KGM5pmv6bue5o6l6aeB5bCP54OP5L6G57eaF+OAkDUwMjDjgJHmoYPlnJIt5LiL56aPGuOAkDUwMjHjgJHmoYPlnJIt5LiL5rW35rmWJuOAkDUwMjLjgJHmoYPlnJIt56u55ZyN77yI57aT5Y2X5bSB77yJKeOAkDUwMjJB44CR5qGD5ZySLeerueWcjSjntpPmjbfpgYvnq5nlj6MpJuOAkDUwMjPjgJHmoYPlnJIt5aSn5ZyS77yI57aT5qWK5Y6d77yJJuOAkDUwMjXjgJHkuK3lo6It5paw5bGL77yI57aT6JeN5Z+U77yJJuOAkDUwMjbjgJHkuK3lo6It5paw5Z2h77yI57aT5a+M5rqQ77yJF+OAkDUwMjfjgJHkuK3lo6It5b6M5rmWGuOAkDUwMjjjgJHmlrDlsYst5LiL5YyX5rmWJOOAkDUwM+OAkeWPsOeBo+WlveihjOimquWtkOaoguWckue3mhrjgJA1MDMw44CR5Lit5aOiLeS4i+WMl+a5linjgJA1MDMx44CR5Lit5aOiLeemj+iIiOWuru+8iOe2k+aWsOWxi++8iSbjgJA1MDMy44CR5Lit5aOiLeingOmfs++8iOe2k+efs+ejiu+8iSbjgJA1MDMz44CR5Lit5aOiLeingOmfs++8iOe2k+S/neeUn++8iSbjgJA1MDM144CR5Lit5aOiLeaWsOWxi++8iOe2k+mBjuW2uu+8iSnjgJA1MDM444CR5Lit5aOiLeadseemj+Wcku+8iOe2k+Wxseadse+8iS/jgJA1MDM544CR5Lit5aOiLeS4reWjou+8iOe2k+awuOWuieOAgeingOmfs++8iSbjgJA1MDQw44CR5qGD5ZySLeingOmfs++8iOe2k+S4reWOne+8iSbjgJA1MDQx44CR5Lit5aOiLeingOmfs++8iOe2k+eZveeOie+8iSbjgJA1MDQy44CR5Lit5aOiLeingOmfs++8iOe2k+aWsOWdoe+8iR3jgJA1MDQz44CR5Lit5aOiLeaoueael+aWsOadkSnjgJA1MDQ044CR5qGD5ZySLem+jea9re+8iOe2k+WNgeS4gOS7ve+8iS/jgJA1MDQ444CR6b6N5r2tLeefs+mWgOawtOW6q++8iOe2k+WNgeS4gOS7ve+8iSnjgJA1MDQ544CR6b6N5r2tLemAuOWcku+8iOe2k+S4ieinkuael++8iRvjgJA1MDXjgJHmv7Hmtbfop4DlhYnlhazou4ov44CQNTA1MOOAkeS4reWjoi3nn7PploDmsLTluqvvvIjntpPlk6HmqLnmnpfvvIkX44CQNTA1MeOAkem+jea9rS3lpKflnaop44CQNTA1M+OAkeahg+Wcki3pvo3mva3vvIjntpPkuZ3pvo3mnZHvvIkv44CQNTA1NeOAkeS4reWjoi3nn7PploDmsLTluqvvvIjntpPlsbHku5TpoILvvIkd44CQNTA1NuOAkeahg+Wcki3nn7PploDmsLTluqtK44CQNTA1N+OAkeahg+Wcki3plbfluprphqvpmaLmoYPlnJLliIbpmaLvvIjntpPlpKfln5TjgIHlt6Xlm5vlt6Xmpa3ljYDvvIks44CQNTA1OeOAkeahg+Wcki3moYPlnJLmqZ/loLTvvIjntpPljZfltIHvvIkv44CQNTA2MOOAkeahg+Wcki3mpq7msJHkuYvlrrbvvIjntpPmm7Tlr67ohbPvvIkv44CQNTA2MeOAkeahg+Wcki3lu7rlnIvljYHkuZ3mnZHvvIjntpPlpKfnq7nvvIkv44CQNTA2M+OAkeahg+Wcki3nq7nmnpflsbHlr7rvvIjntpPlhYnoj6/lnZHvvIk444CQNTA2NOOAkeahg+Wcki3kuInlvrfnhaTnpKbvvIjntpPpvpzlsbHjgIHlnJPlhYnmqYvvvIlB44CQNTA2NeOAkeahg+Wcki3pq5TogrLlrbjpmaLvvIjntpPlpKfln5TjgIHkuK3mraPpgYvli5XlhazlnJLvvIk144CQNTA2OOOAkeahg+Wcki3lkIjlrrbmraHnpL7ljYDvvIjntpPpvpzlsbHlkI7ooZfvvIkv44CQNTA2OeOAkeahg+Wcki3nq7nmnpflsbHlr7rvvIjntpPotaTloZfltI7vvIks44CQNTA3MeOAkeahg+Wcki3nq7nmnpflsbHlr7rvvIjntpPlpJbnpL7vvIkX44CQNTA3M+OAkeahg+Wcki3poILnpL4p44CQNTA3N+OAkeS4reWjoi3lpKflnJLvvIjntpPmn7TmorPltJnvvIkd44CQNTA3OOOAkeS4reWjoi3lu7rlnIvlhavmnZEp44CQNTA4MeOAkeS4reWjoi3lpKflnJLvvIjntpPkuIvmtL3muqrvvIkp44CQNTA4MuOAkeS4reWjoi3lpKflnJLvvIjntpPpm5nmuqrlj6PvvIkg44CQNTA4M+OAkeaNt+mBi+Wkp+WckuermS3mva7pn7Mj44CQNTA4NOOAkeaNt+mBi+Wkp+WckuermS3kuIvlj6Tkuq0g44CQNTA4NeOAkeaNt+mBi+Wkp+WckuermS3mspnltJkp44CQNTA4NuOAkeahg+Wcki3lpKflnJLvvIjntpPkupTloYrljp3vvIkm44CQNTA4N+OAkeS4reWjoi3lpKflnJLvvIjntpPpnZLln5TvvIks44CQNTA4OeOAkeS4reWjoi3moYPlnJLmqZ/loLTvvIjntpPlpKflnJLvvIkk44CQNTA5MOOAkeahg+Wcki3kuIrlt7TpmbUt5p6X54+t5Y+jJOOAkDUwOTHjgJHkuK3lo6It5LiK5be06Zm1Leael+ePreWPox7jgJA1MDkz44CR5aSn5rqqLee+hea1ri3lt7TpmbUt44CQNTA5NOOAkeWkp+a6qi3kuInlhYnvvIjmspnltJnlrZDvvIkt5be06Zm1KeOAkDUwOTXjgJHmoYPlnJIt5YWr5b6377yI57aT5pu05a+u6IWz77yJKeOAkDUwOTbjgJHmoYPlnJIt5aSn5rqq77yI57aT5pu05a+u6IWz77yJKeOAkDUwOTfjgJHlpKfmuqot56u556+Z5Y6d77yI57aT576O6I+v77yJKeOAkDUwOTjjgJHkuK3lo6It5aSn5rqq77yI57aT5a6Y6Lev57y677yJLOOAkDUwOTnjgJHlpKfmuqot6Zi/5aeG5Z2q77yI57aT5oe35b635qmL77yJJuOAkDUxMDHjgJHlpKfmuqot6bav5q2M77yI57aT5Lit5paw77yJF+OAkDUxMDTjgJHlpKfmuqot5b6p6IiIKeOAkDUxMDXjgJHlpKfmuqot5bCP54OP5L6G77yI57aT5LiJ5rCR77yJKuOAkDUxMDbjgJHlpKfmuqot6Zye6Zuy5p2R77yI57aTIOW+qeiIiO+8iSnjgJA1MTA344CR5aSn5rqqLeidmeidoOa0nu+8iOe2k+S4ieawke+8iSbjgJA1MTA544CR5aSn5rqqLemrmOmBtu+8iOe2k+e+hea1ru+8iRjjgJA1MTEw44CRIOWkp+a6qi3lnarmnpcm44CQNTExMuOAkeWkp+a6qi3kuK3lo6LvvIjntpPlhavlvrfvvIk444CQNTExNuOAkeahg+Wcki3lj7DljJfplbfluprphqvpmaLvvIjntpPmnb7lsbHmqZ/loLTvvIks44CQNTExOOOAkeS4reWjoi3kuIvlhaflrprvvIjntpPkupTloYrljp3vvIkf44CQNjAx44CR5YWn5aOiLeaNt+mBi+i/tOm+jeermSXjgJA3MDHjgJHpvo3mva0t6ZW35bqa6Yar6ZmiICjljp83MDEpJeOAkDcwMuOAkeWkp+a6qi3plbfluprphqvpmaIgKOWOnzcwMikl44CQNzA344CR5qGD5ZyS6auY5LitLeah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',
    '__EVENTVALIDATION':'/wEWjQECssDKiAMCneSP5QoCwOT21A4C5Y2pogQC1MGP4gcC0oDRuAQCusrK4goC1MH/4wcC1MH74wcC0oDBuAQC1MH34wcC0oDVuAQCwOT61A4C96n7lwICusqy4goC+eqd+Q0C0oDduAQCs9jZlAgC96nzlwICwOSO1w4Cs9jdlAgC3/PoeQLA5IrXDgL3qevyCgL3qd/ZDQLSgNm4BALSgM3nDAKOt7u5AgK6ys7iCgLljZWiBAL3qeeXAgL3qdvyCgLA5IbXDgLf89ikCwLf8+R5Avvq8aUEArrKuuIKAtTB8+MHArPYqd4LArPYwZQIArTKqskNApOL5YgGApaL5YgGArnKot8BAqzK/twBApLwk5IMApLw89gIApSL5YgGAoWL5YgGAuWNgYkPArXK+twBAueNyaIEAr7Kot8BAvvqnfkNArTK/twBAsbkxoEFArTKwuIKArrKht8BArXK9twBAt7zmKoPArXK/twBAq/Kit8BAr7K8twBAq/Kht8BAqPzyKoPAvGp95cCAr7Kpt8BAvXkxoEFAq/K8twBAq/K9twBAtDzpKoPAr7Kit8BAvvqgfkNArXKjt8BAq/K/twBAq/K+twBAtDzgKoPArjKgt8BArjK9twBArjK+twBArHYrcEEArnKht8BAt3zmKoPArvKpt8BAsfkxoEFAt3zpKoPArrK9twBApKL5YgGArTKht8BArTK+twBArrKit8BArrK+twBAqzKit8BAoi3s7kCAqzKgt8BAtnz5HkC2fPMgwICucr23AECvsr+3AEC542togQCucry3AECtMqm3wECtcqC3wECtcqG3wECtMqi3wECucqO3wECucr63AEC5ty0qQMC5tyolAoCzIDduAQC8an/lwICtMqC3wECusqm3wECu8r63AECu8qi3wECrMqG3wEC8anjlwICtMq24goCu8qO3wECu8ry3AECu8r23AECzICVqQ4Cu8r+3AECtMrG4goCkvC7lgoCvsr63AECovOkqg8Co/PkeQLE5IbXDgL96pH5DQL96oWkBAK3mbbpCwK2mbbpCwLC5PrUDgLnjZ2iBAKqrsqsBQLP18DmCwL65LqBBQLQgLV1ArnKgt8BAvWp18AO8rnZezMmXYfKZ2Prv9qqBtYPKJewGY3TCSnKuzvaVgg=',
    'DropDownList1':'3220'
    }

    timeNow = (datetime.now()) + timedelta(hours = 8)
    dateNow = timeNow.strftime('%Y/%m/%d')
    hourNow = timeNow.strftime('%H:%M')
    hourNowFormat = datetime.strptime(hourNow, '%H:%M')
    TIME_FORMAT = "%H:%M"

    res = requests.post("http://www.tybus.com.tw/aspx/BusTime.aspx", data = payload)
    soup = BeautifulSoup(res.text,'html.parser')
    content = '公車時刻表:自中壢火車站發車\n自' + dateNow + ' ' + hourNow +'起\n\n'

    for train in soup.select('#GridView1'):
        data = train.findAll('td')

    count = 0
    for i in data:
        if count%4 == 0:
            bus = i.text.strip()
            busFormat = datetime.strptime(bus, TIME_FORMAT)
            if busFormat > hourNowFormat:
                content += bus + '\n'
        count = count + 1
    return content


def HSR_timetable(inputMessage):

    timeNow = (datetime.now()) + timedelta(hours = 8)
    dateNow = timeNow.strftime('%Y/%m/%d')
    hourNow = timeNow.strftime('%H:%M')
    
    if inputMessage == "北車到中大":
        startStation = '977abb69-413a-4ccf-a109-0272c24fd490'
        endStation = 'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
        content = '高鐵時刻表:從台北到桃園\n'
    else:
        startStation = 'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
        endStation = '977abb69-413a-4ccf-a109-0272c24fd490'
        content = '高鐵時刻表:從桃園到台北\n'
    
    
    payload = {
        'StartStation':startStation,
        'EndStation':endStation,
        'SearchDate':dateNow,
        'SearchTime':hourNow,
        'SearchWay':'DepartureInMandarin'
    }

    res = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = payload)
    Timetable_str = res.text
    soup = BeautifulSoup(Timetable_str,'html.parser')

    content += '自' + dateNow + ' ' + hourNow + '起\n\n'
    for train in soup.select('.touch_table'):
        data = "車號:" + train.select('.column1')[0].text
        data += "\n發車時間:" + train.select('.column3')[0].text
        data += "\n抵達時間:" + train.select('.column4')[0].text
        data += "\n\n"
        content += data
    return content


def default_factory():
    return 'not command'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    inputMessage = event.message.text
    
    if inputMessage == "中壢132":
        content = bus132(inputMessage)
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=content))
        return 0
    
    if inputMessage == "北車到中大" or inputMessage == "中大到北車":
        content = HSR_timetable(inputMessage)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if event.message.text == "交通時刻表":
        buttons_template = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='交通時刻表',
                text='要去哪裡呢？',
                thumbnail_image_url='https://i.imgur.com/Rukskow.png',
                actions=[
                    MessageTemplateAction(
                         label='北車到中大',
                         text='北車到中大'
                    ),
                    MessageTemplateAction(
                         label='中大到北車',
                         text='中大到北車'
                    ),
                    MessageTemplateAction(
                         label='中壢132',
                         text='中壢132'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    

    buttons_template = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='哈囉！',
            text='想做什麼呢？',
            thumbnail_image_url='https://i.imgur.com/e0uxvBB.png',
            actions=[
                MessageTemplateAction(
                    label='交通時刻表',
                    text='交通時刻表'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


if __name__ == '__main__':
    app.run()
