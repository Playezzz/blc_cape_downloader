import os
import wget
import shutil

id = input('Введите ID: ')
frames = input('Введите количество кадров: ')
downloadType = input('Введите тип: ')
frame = 0

shutil.rmtree('./temp')
os.mkdir('temp')

if(int(frames) == 1):
    wget.download(f'https://cosmetics.badlion.net/{downloadType}/{downloadType}_{id}.png', out='./temp/0.png')
else:
    while(frame <= int(frames) - 1):
        print('\nСкачиваю кадр #' + str(frame + 1))
        wget.download(f'https://cosmetics.badlion.net/{downloadType}/{id}/{downloadType}_{id}-{frame}.png', out='./temp/'+str(frame)+'.png')
        frame += 1