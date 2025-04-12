import yt_dlp

url = 'https://youtu.be/wpyq6ba6W9E?feature=shared'

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': 'videos/%(title)s.%(ext)s',
    'cookiefile': 'cookies.txt',  # ← 加入這一行！
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
