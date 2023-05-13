import os
import pytube
from pytube import YouTube


# Define a function to download a YouTube video
def download_video(url):
    try:
        # Get the video object
        video = YouTube(url)

        # Check if the video has subtitles in English
        if "en" in video.captions:
            # Download the video with the highest available quality and audio
            video_stream = (
                video.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            video_stream.download(output_path=f"./{video.title}/")
            subtitle = video.captions.get_by_language_code("en")
            subtitle_str = subtitle.generate_srt_captions()
            with open(f"./{video.title}/{video.title}.srt", "w") as srt_file:
                srt_file.write(subtitle_str)
        else:
            # Download the video with the highest available quality and audio
            video_stream = (
                video.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            video_stream.download(output_path=f"./{video.title}/")

        print(f"Video downloaded successfully: {video.title}")

    except pytube.exceptions.PytubeError as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"Unexpected error occurred while downloading {url}: {e}")


# Read the text file containing the URLs
with open("urls.txt", "r") as f:
    urls = f.readlines()

# Download each video
for url in urls:
    download_video(url.strip())
