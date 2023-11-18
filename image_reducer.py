from PIL import Image, UnidentifiedImageError
import os


def reduce_image_size(directory, quality):
    saved_space = 0

    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            input_file_path = os.path.join(root, file)

            try:
                # Open the image
                with Image.open(input_file_path) as img:
                    # Get the original size
                    original_size = os.path.getsize(input_file_path)

                    # Save the image with reduced quality, overwriting the original file
                    img.save(input_file_path, quality=quality, optimize=True)

                    # Get the new size
                    new_size = os.path.getsize(input_file_path)

                    # Calculate and accumulate saved space
                    saved_space += original_size - new_size

                    print(f"Reduced size of {input_file_path}")

            except (UnidentifiedImageError, OSError):
                print(f"Skipping non-image file: {input_file_path}")

    # Print the total saved space
    print(f"\nTotal space saved: {saved_space / (1024 * 1024):.2f} MB")


# Get the current working directory
current_directory = os.getcwd()

# Set the quality for image compression (0-100, higher is better quality)
compression_quality = 85  # set your desired compression quality

# Apply the image size reduction in the current directory and its subdirectories
reduce_image_size(current_directory, compression_quality)
