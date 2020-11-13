import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

headers = {
    'authority': 'www.goal.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 OPR/72.0.3815.186',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.goal.com/en/premier-league/fixtures-results/2020-11-27/2kwbbcootiqqgmrzs6o5inle5',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.2.1933335234.1605214226; _gid=GA1.2.804160976.1605214226; _hjTLDTest=1; _hjid=cdf349ed-41a2-49c1-998d-489ebadbfd54; _hjFirstSeen=1; ___ws-sr=https://www.google.com/; _fbp=fb.1.1605214227809.696060815; __browsiSessionID=12e41449-08d8-4785-a24f-b0558694197e&false&false&SEARCH&us&desktop-2.7.uc.2&false; __browsiUID=4ad2fe86-fe30-4a09-bba0-3d5ff2015fb8; ___ws_d_st={}; _hjAbsoluteSessionInProgress=0; __qca=P0-210120168-1605214227988; gig_bootstrap_3_wCLJT75ffirrzBqqAJaHe1zYGgdpb9XFkjxEQfrxraM-xO_if-uM1uVBZZ5r4naE=_gigya_ver3; ortcsession-w5tlOg-s=2ec054f048fca2c7; ortcsession-w5tlOg=2ec054f048fca2c7; _cb_ls=1; _cb=ZVFu2BOJZgpCmwAzF; _cb_svref=https%3A%2F%2Fwww.goal.com%2Fen%2Fpremier-league%2Ffixtures-results%2F2kwbbcootiqqgmrzs6o5inle5; OptanonConsent=isIABGlobal=false&datestamp=Thu+Nov+12+2020+16%3A04%3A20+GMT-0500+(Eastern+Standard+Time)&version=6.4.0&hosts=&consentId=ad3adf22-f828-4028-84ed-6ca50acfd863&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=US%3BNY&AwaitingReconsent=false; OptanonAlertBoxClosed=2020-11-12T21:04:20.725Z; ___ws_ses=92D243747FDC59A3.5; ___ws_vis=92D243747FDC59A3.1605215067016; ___ws_ses_sec=1344:1605215067016; ___ws_vis_sec=1344:1605215067016; ws-refr=https://www.goal.com/en/premier-league/fixtures-results/2020-11-28/2kwbbcootiqqgmrzs6o5inle5; _chartbeat2=.1605215055013.1605215068349.1.BA0VMuB--pbjDQaIUACL9UQBBPZNWi.2; _gat_UA-62411523-1=1',
}

currentDate = str(date.today()) + " " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(" ")[1])

params = (
    ('date', currentDate),
    ('calendarId', '8g80ydy1enmztpyanmadpofoq'),
    ('timezone', '-0500'),
)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.goal.com/en/ajax/competition/matches/2kwbbcootiqqgmrzs6o5inle5?date=2020-11-22%2014%3A00%3A00&calendarId=8g80ydy1enmztpyanmadpofoq&timezone=-0500', headers=headers)

def main():
    r = requests.get(
        'https://www.goal.com/en/ajax/competition/matches/2kwbbcootiqqgmrzs6o5inle5', headers=headers, params=params)

    # print(r.json()['html'])
    content = r.json()['html']

    soup = BeautifulSoup(content, 'html.parser')

    print(date.today())

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(" ")[1])

    # print(soup.prettify())

    # print(soup.time.text)

    prev = soup.find(class_='nav-switch__prev')

    # print("prev ", prev)

    next = soup.find(class_='nav-switch__next')

    # print("next ", next)

    for game in soup.find_all(class_='match-main-data'):
        print(game.get_text())


if __name__ == "__main__":
    main()
