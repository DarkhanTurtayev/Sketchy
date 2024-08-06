import os
import ssl
import certifi
from pytube import YouTube

ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()

import yt_dlp as youtube_dl

def download_youtube_video(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestvideo[height<=2160][vcodec!=vp9.2][ext=mp4]',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        video_title = info_dict.get('title', None)
        return os.path.join(output_path, f"{video_title}.mp4")
    
youtube_url = "https://www.youtube.com/watch?v=vlDzYIIOYmM"
output_path = '/Users/macstudiod/Desktop/Upscaler/videos'

download_youtube_video(youtube_url, output_path)