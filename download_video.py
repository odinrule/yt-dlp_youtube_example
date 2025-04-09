import yt_dlp

url = ''  # 在引號內貼上網址

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',  # 下載 1080p 影片 + 最佳音訊
    'merge_output_format': 'mp4',  # 合併後輸出 MP4 格式
    'outtmpl': 'videos/%(title)s.%(ext)s',  # 指定儲存路徑
}

# 稍後加入函式subtitle可以下載隨附影片的字幕檔

# 另一個函式sound或類別，測試可否只下載聲音檔

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
