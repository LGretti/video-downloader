import pytube

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["baixa", "360", "360p"]:
        itag = 18
    elif resolution in ["media", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["alta", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["muito alta", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Insira o link de um vídeo e pressione enter para ir ao próximo (Para seguir digite PARAR):")

    links = []
    link = ""

    while link != "PARAR" and link != "parar":
        link = input()
        links.append(link)

    links.pop()

    return links