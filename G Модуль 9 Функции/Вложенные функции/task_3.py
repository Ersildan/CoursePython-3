def sourcetemplate(url):
    def func(**kwargs):
        if len(kwargs) != 0:
            return f'{url}?'+ "&".join([f"{k}={v}" for k,v in sorted(kwargs.items())])
        else:
            return url
    return func
