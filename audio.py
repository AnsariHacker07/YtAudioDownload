import os
import yt_dlp
from tqdm import tqdm

def download_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def progress_hook(d):
    if d['status'] == 'downloading':
        pbar.update(d['downloaded_bytes'] - pbar.n)
    elif d['status'] == 'finished':
        pbar.close()
        print('Download completed!')

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the download directory: ")

    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Initialize the progress bar
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        total_size = info_dict['filesize']
    
    pbar = tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading audio')

    # Download the audio
    download_audio(url, output_path)
    
