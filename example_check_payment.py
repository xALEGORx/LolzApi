from lolzapi import LolzteamApi
from random import randint

api = LolzteamApi('TOKEN', 11111)
comment = randint(100000, 1000000)
amount = 100
print('Send money to https://lolz.guru/alegor')
print('- Amount:', amount)
print('- Comment:', comment)
while 1:
    input('I paid, check payment...')
    if api.market_payments(type_='income', pmin=amount, pmax=amount, comment=comment)['payments']:
        print('Payment was found!')
        break
    else:
        print('Payment not found!')