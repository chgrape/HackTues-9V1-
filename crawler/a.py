from urllib.parse import urlparse

u = urlparse('//www.cwi.nl:80/%7Eguido/Python.html')

ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',params='', query='', fragment='')

u._replace(scheme='http')

ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',params='', query='', fragment='')
