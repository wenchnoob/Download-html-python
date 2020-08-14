from Connect import get

def download(url, saveTo):
    file = open(saveTo, "w")
    file.write(get(url).decode("utf-8"))
    file.close()
    