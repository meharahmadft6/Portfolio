from rembg import remove
from PIL import Image
import io

# Function to remove the background
def remove_background(input_path, output_path):
    try:
        # Open the input image
        with open(input_path, "rb") as file:
            input_image = file.read()

        # Process the image to remove the background
        output_image = remove(input_image)

        # Save the resulting image
        with open(output_path, "wb") as file:
            file.write(output_image)

        print(f"Background removed and saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Paths to the input and output files
input_image_path = "me.jpg"  # Replace with your input image path
output_image_path = "output_image.png"  # Output will be saved as a transparent PNG

# Remove the background
remove_background(input_image_path, output_image_path)
