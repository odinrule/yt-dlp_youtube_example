# yt-dlp_youtube_example

本專案python程式必須安裝了ffmpeg才能使用。
在使用此程式時，若系統為macOS，可使用Homebrew來安裝ffmpeg。
在終端機輸入brew install ffmpeg，來安裝ffmpeg。
安裝完成後在終端機輸入 ffmpeg -version 可查看安裝是否成功，以及ffmpeg的版本。

Homebrew的安裝方式：在終端機輸入

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

安裝過程時間較長，安裝完成後可輸入 brew --version 查看版本。

本專案共兩個版本，dlvd.py和download_video.py。可選擇其中一個使用。
（一） dlvd.py是在終端機輸入python3 dlvd.py 需下載的url
（二）download_video.py，須在程式碼url變數的引號內貼上url。

