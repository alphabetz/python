import urllib.request as ur


reqs = ['/register', '/search-ajax', '/search/', '/fuck']

for resources in reqs:
    url = ur.urlopen("http://127.0.0.1:8084" +resources)
    print(resources, url.getcode())
