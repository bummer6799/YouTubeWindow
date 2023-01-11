import webview

YouTubeVideo = input('Enter YouTube video link: \n')
webview.create_window("YouTube", YouTubeVideo, width=320, height=240)
webview.start()
