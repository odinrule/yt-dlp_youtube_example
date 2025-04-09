# 這是在終端機輸入url網址的程式版本，故導入sys模組。

import yt_dlp
import sys

url = sys.argv[1]

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',  # 下載 1080p 影片 + 最佳音訊
    'merge_output_format': 'mp4',  # 合併後輸出 MP4 格式
    'outtmpl': 'videos/%(title)s.%(ext)s',  # 指定儲存路徑
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
