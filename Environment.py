import os

class Environment:
    domain = os.environ.get("DOMAIN")
    if domain[-1] == '/':
        domain = domain[:-1]
    
    _scheme = f"{domain}/scheme"
    # _predicate = f'{domain}/math#predicate'
    # _entity = f'{domain}/math#entity'