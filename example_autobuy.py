from lolzapi import LolzteamApi
from time import sleep

api = LolzteamApi('TOKEN')
while 1:
    items = api.market_list('steam', pmax=150, optional={'game[]': '730'})
    for i in items['items']:
        api.market_buy(i['item_id'])
    sleep(10)
