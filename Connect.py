from urllib import request

class Connector:
    def __init__ (self, url):
        try:
            self.page = request.urlopen(url)
        except Exception as e:
            print(e)

    def close(self):
        self.page.close()

def get(url):
    connection = Connector(url)
    content = connection.page.read()
    connection.close()
    return content