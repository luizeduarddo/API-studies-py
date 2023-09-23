#%%
import random
import backoff

#%%
@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError,TimeoutError), max_tries= 10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
        RND: {rnd}
        args: {args if args else 'sem args'}
        kargs: {kargs if kargs else 'sem kargs'}
""")
    if rnd < .2:
        raise ConnectionAbortedError('Conexao foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexao foi recusada')
    elif rnd < .6:
        raise TimeoutError ('Tempo de espera excedido')
    else: 
        return "Ok!"

#%%
test_func()
