import moviepy.editor as mp
import os
import math

def split_video(video_path, output_folder, segment_length):
    """
    Splits the input video into segments of specified length.
    
    Parameters:
        video_path (str): Path to the input video file.
        output_folder (str): Directory where the segments will be saved.
        segment_length (int or float): Desired length of each segment in seconds.
    """
    # Load the video file
    video = mp.VideoFileClip(video_path)
    
    # Calculate the duration of the video
    video_duration = video.duration
    
    # Calculate the number of segments using ceiling division
    num_segments = math.ceil(video_duration / segment_length)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"Video Duration: {video_duration} seconds")
    print(f"Number of Segments: {num_segments}")
    
    # Split the video into segments
    for i in range(num_segments):
        start_time = i * segment_length
        end_time = min((i + 1) * segment_length, video_duration)
        
        # Extract the segment (includes both video and audio)
        segment = video.subclip(start_time, end_time)
        
        # Resize the segment to maintain the original aspect ratio.
        # For portrait videos, it sets the height; for landscape videos, it sets the width.
        segment = segment.resize(
            height=video.h if video.h > video.w else None,
            width=video.w if video.w > video.h else None
        )
        
        # Define the output file path
        output_file = os.path.join(output_folder, f"segment_{i + 1}.MOV")
        
        # Write the segment to the output file
        segment.write_videofile(output_file, codec="libx264", audio_codec="aac")
        
        print(f"Segment {i + 1} saved successfully.")
    
    print("Video splitting completed.")
    video.close()

if __name__ == "__main__":
    # Specify the input video file path
    video_path = "video1.MOV"
    
    # Specify the output folder path
    output_folder = "output"
    
    # Specify the segment length in seconds
    segment_length = 59
    
    # Call the function to split the video
    split_video(video_path, output_folder, segment_length)

