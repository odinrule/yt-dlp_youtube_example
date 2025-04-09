import yt_dlp

url = ''  # 在引號內貼上網址

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',  # 下載 1080p 影片 + 最佳音訊
    'merge_output_format': 'mp4',  # 合併後輸出 MP4 格式
    'outtmpl': 'videos/%(title)s.%(ext)s',  # 指定儲存路徑
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
