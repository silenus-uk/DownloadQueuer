import webbrowser
import time

# opens text file containing urls, opens them in firefox then deletes the line ofthe read file


with open('DownloadQueue.txt', 'r') as fin:
    data = fin.read().splitlines(True)
if(len(data)>0):
    itemsLeft = True

while(itemsLeft):
    with open('DownloadQueue.txt', 'r') as fin:
        data = fin.read().splitlines(True)
        print(data[0])
        webbrowser.open_new(data[0])
    with open('downloadLog.txt','a') as fout:
        fout.writelines(data[0])
        fout.writelines("Download Started at %s\n" % time.ctime())
        
    if(len(data)>1):
       with open('DownloadQueue.txt', 'w') as fout:
            fout.writelines(data[1:])
    else:
        with open('DownloadQueue.txt', 'w') as fout:
            fout.writelines('FINISHED')
        itemsLeft = False
    time.sleep(1200)

