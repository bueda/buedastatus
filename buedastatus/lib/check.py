import bueda

def is_bueda_up():
    '''
    is_up = is_bueda_up()

    Checks whether bueda is active.
    '''
    try:
        result = bueda.enrich(['luispedrocoelho'])
        return True
    except:
        return False

