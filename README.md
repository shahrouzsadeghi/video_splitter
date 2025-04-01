

```markdown
# Video Splitter

A simple Python tool to split videos into segments using MoviePy.

## Description

This repository contains a Python script that splits an input video into multiple segments of a specified duration. It leverages the [MoviePy](https://zulko.github.io/moviepy/) library to process video files, ensuring that each segment retains the original video's aspect ratio.

## Features

- **Video Splitting:** Divide a video into segments based on a specified segment length.
- **Aspect Ratio Preservation:** Automatically resizes segments to maintain the original video's aspect ratio.
- **Easy to Use:** Minimal configuration required to get started.

## Requirements

- Python 3.x
- [MoviePy](https://zulko.github.io/moviepy/) (install via `pip install moviepy`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   ```

2. **Change to the Repository Directory:**

   ```bash
   cd video-splitter
   ```

3. **Install Dependencies:**

   ```bash
   pip install moviepy
   ```

## Usage

1. **Configure the Script:**
   - Open `video_splitter.py`.
   - Update the following variables as needed:
     - `video_path`: Path to your input video file.
     - `output_folder`: Directory where the segments will be saved.
     - `segment_length`: Duration (in seconds) for each segment.

2. **Run the Script:**

   ```bash
   python video_splitter.py
   ```

3. **Check Output:**
   - The segments will be saved in the specified output folder, named as `segment_1.MOV`, `segment_2.MOV`, etc.

## Repository Structure

```plaintext
.
├── video_splitter.py   # Main script to split video
├── README.md           # Project documentation
├── .gitignore          # Specifies files to ignore in Git
└── LICENSE             # Project license (MIT License)
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.
```


