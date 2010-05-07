import bueda
bueda.init('IxJLXW5wdoy4l8vUJCaoljkxHbFzaNmldk6Fzw')

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

