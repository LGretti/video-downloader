print("Carregando...")

import pytube
import youtube_downloader
import file_converter

print('''
O que você deseja?

(1) Baixar vídeos do youtube manualmente
(2) Baixar uma playlist do youtube
(3) Baiar vídeos do youtube e converter para mp3


''')

choice = input("Escolha: ")

if choice == "1" or choice == "2":
    quality = input("Favor selecionar a qualidade (baixa, media, alta, muito alta):")
    if choice == "2":
        link = input("Insira o link da playlist: ")
        print("Baixando playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("Download concluído!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Baixando...")
        filename = youtube_downloader.download_video(link, 'baixa')
        print("Convertendo...")
        file_converter.convert_to_mp3(filename)
else:
    print("Entrada inválida! Abortando...")
