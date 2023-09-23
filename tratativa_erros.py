#%%
import requests
import json

#%%
def multi_moeda(valor, moeda): 
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]}  hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

#%%
multi_moeda(10, "USD-BRL")

#%%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check
def multi_moeda(valor, moeda): 
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]}  hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

#%%
multi_moeda(25, 'USD-BRL')
multi_moeda(25, 'EUR-BRL')
multi_moeda(25, 'BTC-BRL')
multi_moeda(25, 'GBP-BRL')
multi_moeda(25, 'LUI-BRL')
multi_moeda(25, 'ARS-BRL')