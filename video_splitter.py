import moviepy.editor as mp
import os
import math
import argparse
import sys
from pathlib import Path

def split_video(video_path, output_folder=None, segment_length=59):
    """
    Splits the input video into segments of specified length, optimized for Instagram stories.
    
    Parameters:
        video_path (str): Path to the input video file.
        output_folder (str): Directory where the segments will be saved.
        segment_length (int or float): Desired length of each segment in seconds.
    """
    # If no output folder specified, create one based on input filename
    if output_folder is None:
        video_name = Path(video_path).stem
        output_folder = f"{video_name}_segments"
    
    # Load the video file
    print(f"Loading video: {video_path}")
    try:
        video = mp.VideoFileClip(video_path)
    except Exception as e:
        print(f"Error loading video: {e}")
        return False
    
    # Calculate the duration of the video
    video_duration = video.duration
    
    # Calculate the number of segments using ceiling division
    num_segments = math.ceil(video_duration / segment_length)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"Video Duration: {video_duration:.2f} seconds")
    print(f"Number of Segments: {num_segments}")
    print(f"Segments will be saved to: {os.path.abspath(output_folder)}")
    
    try:
        # Split the video into segments
        for i in range(num_segments):
            start_time = i * segment_length
            end_time = min((i + 1) * segment_length, video_duration)
            
            print(f"\nProcessing segment {i + 1}/{num_segments} ({start_time:.2f}s to {end_time:.2f}s)...")
            
            # Extract the segment (includes both video and audio)
            segment = video.subclip(start_time, end_time)
            
            # Preserve the Instagram-friendly resize logic from old.py
            # For portrait videos, set height; for landscape, set width
            segment = segment.resize(
                height=video.h if video.h > video.w else None,
                width=video.w if video.w > video.h else None
            )
            
            # Define the output file path
            output_file = os.path.join(output_folder, f"segment_{i + 1}.mp4")
            
            # Write the segment to the output file
            print(f"Saving segment {i + 1}... (this may take a while)")
            segment.write_videofile(
                output_file,
                codec="libx264",
                audio_codec="aac",
                verbose=False,
                logger=None
            )
            
            print(f"✓ Segment {i + 1} saved successfully.")
    
        print("\n✓ Video splitting completed!")
        print(f"Your video segments are ready in the folder: {os.path.abspath(output_folder)}")
    
    except Exception as e:
        print(f"\nError during video processing: {e}")
        return False
    finally:
        # Always close the video to free resources
        video.close()
    
    return True

def main():
    # Set up argument parser for command line usage
    parser = argparse.ArgumentParser(description="Split videos into segments for Instagram stories")
    
    parser.add_argument("video_path", nargs="?", help="Path to the video file you want to split")
    parser.add_argument("-o", "--output", help="Folder to save the segments (optional)")
    parser.add_argument("-l", "--length", type=float, default=59,
                        help="Length of each segment in seconds (default: 59)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Interactive mode if no video path provided
    if args.video_path is None:
        print("=== Instagram Story Video Splitter ===")
        print("This tool helps you split a long video into segments for Instagram stories.")
        
        video_path = input("\nEnter the path to your video file: ").strip()
        if not video_path:
            print("No video file specified. Exiting.")
            return
        
        output_choice = input("Enter output folder name (or press Enter for default): ").strip()
        output_folder = output_choice if output_choice else None
        
        length_input = input("Enter segment length in seconds (or press Enter for 59 seconds): ").strip()
        segment_length = float(length_input) if length_input else 59
    else:
        video_path = args.video_path
        output_folder = args.output
        segment_length = args.length
    
    # Check if file exists
    if not os.path.isfile(video_path):
        print(f"Error: The video file '{video_path}' does not exist.")
        return
    
    # Process the video
    split_video(video_path, output_folder, segment_length)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting.")
        sys.exit(0)