import yt_dlp

url = input("請輸入 YouTube 影片網址：")

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': 'videos/%(title)s.%(ext)s',
    'cookiesfrombrowser': ('chrome',),
    'geo_bypass': True,
    'force_ipv4': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
