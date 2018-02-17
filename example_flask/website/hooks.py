from website import app

_domain_name = app.config['SERVER_NAME'].split(':')[0]


def domain_name():
    return _domain_name

# test 
@app.context_processor
def context_processor():
    return dict(domain_name=domain_name)
