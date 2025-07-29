# YouTube Downloader & Subtitle Translator

This is a simple desktop application built with Python and the Flet framework. It allows users to download video or audio from a given YouTube URL.

Additionally, it includes a feature to automatically download the English transcript of the video, translate it to Portuguese, and save it as a `.srt` subtitle file alongside the media.

## How to Use

1.  **Install Dependencies**: Make sure you have all the necessary libraries installed. You can do this by running:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    ```bash
    python main.py
    ```

3.  **Using the App**:
    *   Paste the YouTube video URL into the "YouTube URL" field.
    *   Click "Choose Directory" to select a folder where the files will be saved.
    *   Click "Download Video" or "Download Audio" to begin the download.
    *   The application will download the selected media and, if available, the translated subtitle file into the chosen directory.

## Dependencies

This project relies on the following Python libraries:

*   `flet`: For the graphical user interface.
*   `yt-dlp`: For downloading video and audio from YouTube.
*   `youtube-transcript-api`: For fetching video transcripts/subtitles.