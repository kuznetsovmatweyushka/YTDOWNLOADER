from aiogram import *
import pytube
import os



def yt_downloader_bot():
    TOKEN = "5642956556:AAFAk_A2IRoTM43qEaQ4s_6wgstgFtSG51g"

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def begin(message: types.Message):
        await bot.send_message(message.chat.id, "Привет,привет, я загрузчик видео с ютуб. \
    Я маленький, но я стараюсь, к сожалению ТГ не даёт возможности отправить тебе файл больше 50Мб, \
    но скоро я обязательно стану круче \
    !!! Для загрузки видео с ютуб напиши \
    /download <ССЫЛКА НА ВИДЕО>', после чего появится возможность скачать файл \
    по команде /tag <НОМЕР ТЭГА>.")
    @dp.message_handler(commands=["download"])
    async def available_files(msg: types.Message):
        global link
        link = str(msg.text)
        link = link.split()
        link = str(link[1])
        yt = pytube.YouTube(link)
        lst_streams = [str(i) for i in yt.streams]
        lst_streams = [i[9:-1].split() for i in lst_streams]
        for i in range(len(lst_streams)):
            if "abr="  in lst_streams[i][2]:
                lst_streams[i][2] = lst_streams[i][2].strip('abr=""')
            elif "res=" in lst_streams[i][2]:
                lst_streams[i][2] = lst_streams[i][2].strip('res=""')
            if 'mime_type=' in lst_streams[i][1]:
                lst_streams[i][1] = lst_streams[i][1].strip('mime_type=')

        dict_streams = {"/tag " + lst_streams[i][0].strip('itag=""'): "Формат" + " " \
            + lst_streams[i][1] + " " +  "Качество: " + lst_streams[i][2] for i in range(len(lst_streams))}
        await msg.answer("Доступны для скачивания следующие файлы:")
        for key, value in dict_streams.items():
            await msg.answer(value + f" .Чтобы скачать введите {key}")


    @dp.message_handler(commands=["tag"])
    async def get_video_tag(msg: types.Message):
        tag = str(msg.text)
        tag = tag.split()
        tag = int(tag[1])
        download(tag)
        file = open(f"C:\\Users\\ukeuk\\Desktop\\Учеба\\YouTube_downloader\\Tg_bot_version\\Tranzit\\{path_downloaded_file}", 'rb')
        await bot.send_document(msg.chat.id, file)
        os.remove(f"C:\\Users\\ukeuk\\Desktop\\Учеба\\YouTube_downloader\\Tg_bot_version\\Tranzit\\{path_downloaded_file}")


    def download(tag):
        yt = pytube.YouTube(link)
        ys = yt.streams.get_by_itag(tag)
        p = "C:\\Users\\ukeuk\\Desktop\\Учеба\\YouTube_downloader\\Tg_bot_version\\Tranzit\\"
        ys.download(p)
        global path_downloaded_file
        path_downloaded_file = str(os.listdir(p)[0])

    executor.start_polling(dp)
