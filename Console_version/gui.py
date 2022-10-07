def get_link():
    link = input('Вставьте ссылку на видео: ')
    return link


def get_resolutinon():
    res = input('Введите качество ("720p", "480p", "360p", "240p", "144p"): ')
    return res

def get_path_for_download():
    path = input('Введите путь куда сохранить видео: ')
    return path

def get_tag():
    tag = int(input('Введите тэг: '))
    return tag