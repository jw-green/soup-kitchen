# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def MakeSoup(url):
    '''
    Makes a BeautifulSoup object from a url.
    '''

    try:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'} 
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

def DownloadFile(url, filename):
    '''
    Download a file from a URL with a progress meter.
    '''

    href = urlopen(url)
    f = open(filename, 'wb')
    meta = href.info()
    file_size = int(meta.get_all("Content-Length")[0])

    print("Downloading: %s Bytes: %s" % (filename, file_size))

    file_size_dl = 0
    block_sz = 8192
    status_len = 0

    while True:
        buffer = href.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)

        status = "%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)

        print(status, end='')

        backspace(status_len)
        status_len = len(status)

    f.close()

    print('\n', end='')
