import urllib.request


def ConectInternet():
    objurl = urllib.request.urlopen("https://www.google.com")

    if objurl.getcode() == 200:
        data = objurl.read()
        print(data)


ConectInternet()
