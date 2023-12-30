from pytube import YouTube
from pytube.exceptions import *
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url, output_path="."):
    try:
        # Validate the URL
        if not url.startswith("https://www.youtube.com/watch?v="):
            raise ValueError("Invalid URL. Make sure it is a valid YouTube video URL.")

        # Create a YouTube object using the video URL
        yt = YouTube(url)

        # Select the highest available resolution
        video = yt.streams.get_highest_resolution()

        # Display information about the video
        print(f"Downloading video: {yt.title}")
        print(f"Resolution: {video.resolution}")
        print(f"Format: {video.mime_type}")

        # Download the video to the specified folder
        video.download(output_path)
        print("Download completed.")

    except RegexMatchError:
        print("Error: Unable to extract video information.")
    except VideoUnavailable:
        print("Error: The video is unavailable.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example of use
if __name__ == "__main__":
    video_url = input("Please enter the YouTube video URL: ")
    download_path = input("Please specify the download path (press Enter to use the current folder): ")

    if not download_path:
        download_path = "."

    download_video(video_url, download_path)