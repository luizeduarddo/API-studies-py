#%%
# imports
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

#%%
if ret:
    print(ret)
else:
    print('Failed')

#%%
dolar = json.loads(ret.text)['USDBRL']
#%%
print(f"30 Dolares hoje custam {float(dolar['bid']) * 30} reais")

#%%
def cotacao(valor, moeda):
    url =f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]}  hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

#%%
cotacao(26, 'USD-BRL')

#%%
cotacao(26, 'JPY-BRL')