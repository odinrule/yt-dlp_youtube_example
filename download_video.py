import yt_dlp

url = input("請輸入影片網址：")

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': 'videos/%(title)s.%(ext)s',
    'cookiesfrombrowser': ('chrome',),  # 自動從chrome瀏覽器讀取cookies
    'geo_bypass': True,
    'force_ipv4': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
