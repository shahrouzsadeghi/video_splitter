# Video Splitter for Instagram Stories

A user-friendly Python tool that splits long videos into Instagram-ready segments, preserving the optimal aspect ratio.

## Description

This tool helps you split long videos into shorter segments, specifically optimized for Instagram stories. It maintains the proper aspect ratio and automatically handles both portrait and landscape videos. Perfect for content creators who want to share longer videos as Instagram stories.

## Features

- **Instagram Story Optimization:** Creates segments ideally formatted for Instagram stories.
- **Automatic Aspect Ratio Handling:** Properly resizes videos while preserving their quality.
- **User-Friendly Interface:** Simple interactive prompts for non-technical users.
- **Flexible Configuration:** Customize segment length and output folder.
- **Progress Tracking:** Shows clear progress as your video is processed.

## Requirements

- Python 3.x
- [MoviePy](https://zulko.github.io/moviepy/) library

## Installation

### For Windows Users

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org).
   - During installation, make sure to check "Add Python to PATH".

2. **Install the Required Library:**
   - Open Command Prompt (search for "cmd" in the Start menu).
   - Run the following command:
     ```bash
     pip install moviepy
     ```

3. **Download the Video Splitter:**
   - Download `video_splitter.py` from this repository.

### For Mac Users

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org).

2. **Install the Required Library:**
   - Open Terminal (from Applications > Utilities).
   - Run the following command:
     ```bash
     pip install moviepy
     ```

3. **Download the Video Splitter:**
   - Download `video_splitter.py` from this repository.

## How to Use

### Method 1: Interactive Mode (Easiest for Beginners)

1. **Start the Program:**
   - Double-click on `video_splitter.py`, or
   - Open Command Prompt/Terminal, navigate to the folder containing the script, and run:
     ```bash
     python video_splitter.py
     ```

2. **Follow the Prompts:**
   - Enter the path to your video file when asked.
   - Optionally specify an output folder (or press Enter for default).
   - Optionally specify a segment length in seconds (or press Enter for the default 59 seconds).

3. **Wait for Processing:**
   - The program will show progress as it splits your video.
   - When complete, it will inform you where your video segments are saved.

### Method 2: Command Line (Advanced)

For those comfortable with the command line, you can run:

```bash
python video_splitter.py path/to/your/video.mp4 -o output_folder -l 59
```

Where:
- `path/to/your/video.mp4` is the path to your video file.
- `-o output_folder` (optional) specifies the output folder.
- `-l 59` (optional) sets the segment length in seconds.

## Tips for Instagram Stories

- The default segment length of 59 seconds is ideal for Instagram stories.
- Both portrait (9:16) and landscape videos are automatically handled.
- Portrait videos work best for Instagram stories.
- Segments are created in MP4 format, which works well with Instagram.

## Troubleshooting

### Error Loading Video
- Ensure the video file path is correct.
- Verify that the video file is not corrupted.
- Try moving the video to a path without special characters.

### Installation Issues
- If `pip install moviepy` fails, try:
  ```bash
  python -m pip install moviepy
  ```

### Video Quality Issues
- The original video quality is preserved, but note that Instagram uploads might reduce quality.
- For best results, use high-quality source videos.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes. For major changes, please open an issue first to discuss your ideas.

