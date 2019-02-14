import urllib.request
import urllib.response
import os
import random

i = int(input('Start: '))
j = int(input('End: '))
while True:

    url = 'https://traffic.libsyn.com/syntax/Syntax00'+str(i)+'.mp3'
    if (i > 9):
        url = 'https://traffic.libsyn.com/syntax/Syntax0'+str(i)+'.mp3'
    if(i > 99):
        url = 'https://traffic.libsyn.com/syntax/Syntax'+str(i)+'.mp3'
    if(i == j + 1):
        break
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    file_size = int(u.info()['Content-Length'])
    print("Downloading: %s MBytes: %s" %
          (file_name, str(int(file_size/1048576))))
    # print(len(u.read(8192)))
    file_size_dl = 0
    block_sz = 1048576

    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (
            file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status,)
    os.system('clear')
    print("Downloaded: %s " % (file_name))
    i = i + 1
    f.close()
# print(html.read())
# print(soup)
