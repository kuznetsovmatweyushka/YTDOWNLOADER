import gui
import pytube 


def download_video():
    yt = pytube.YouTube(gui.get_link())
    lst_streams = [str(i) for i in yt.streams]
    lst_streams = [i[9:-1].split() for i in lst_streams]
    for i in range(len(lst_streams)):
        if "abr="  in lst_streams[i][2]:
            lst_streams[i][2] = lst_streams[i][2].strip('abr=""')
        elif "res=" in lst_streams[i][2]:
            lst_streams[i][2] = lst_streams[i][2].strip('res=""')
        if 'mime_type=' in lst_streams[i][1]:
            lst_streams[i][1] = lst_streams[i][1].strip('mime_type=')

    dict_streams= {"Тэг: " + lst_streams[i][0].strip('itag=""'): "Формат" + " " \
         + lst_streams[i][1] + " " +  "Качество: " + lst_streams[i][2] for i in range(len(lst_streams))}
    print("Доступны для скачивания следующие файлы:")
    for key, value in dict_streams.items():
        print(value + f" .Чтобы скачать введите {key}")

    ys = yt.streams.get_by_itag(gui.get_tag())
    p = gui.get_path_for_download()
    print('Загрузка...')
    ys.download(p)
    print("Загрузка завершена!!!")