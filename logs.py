#%%
import random
import backoff
import logging

#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging. Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

#%%
@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError,TimeoutError), max_tries= 10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f"RND: {rnd} ")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")

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
