from PIL import Image

def change_color(image_path, original_color, new_color, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Load image data
        img = img.convert("RGBA")  # Ensure image is in RGBA format
        data = img.getdata()

        # Create a list to hold the new image data
        new_data = []

        # Replace the original color with the new color
        for item in data:
            # Check if pixel matches the original color
            if item[0] == original_color[0] and item[1] == original_color[1] and item[2] == original_color[2]:
                # Change it to the new color
                new_data.append((new_color[0], new_color[1], new_color[2], item[3]))
            else:
                # Keep the original pixel color
                new_data.append(item)

        # Update the image with the new data
        img.putdata(new_data)
        
        # Save the modified image to the output path
        img.save(output_path)
        print(f"Image saved to {output_path}")

def change_color_if_not_match(image_path, match_color, new_color, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Load image data
        img = img.convert("RGBA")  # Ensure image is in RGBA format
        data = img.getdata()

        # Create a list to hold the new image data
        new_data = []

        # Change the color of pixels that do not match the specified match_color
        for item in data:
            # Check if pixel does not match the match_color
            if item[0] != match_color[0] or item[1] != match_color[1] or item[2] != match_color[2]:
                # Change it to the new color
                new_data.append((new_color[0], new_color[1], new_color[2], item[3]))
            else:
                # Keep the original pixel color
                new_data.append(item)

        # Update the image with the new data
        img.putdata(new_data)
        
        # Save the modified image to the output path
        img.save(output_path)
        print(f"Image saved to {output_path}")

def change_color_within_interval(image_path, min_color, max_color, new_color, output_path):
    """
    Changes the color of pixels in an image if they fall within the specified color interval.

    Parameters:
    - image_path: Path to the input image.
    - min_color: A tuple representing the minimum RGB color in the interval (inclusive).
    - max_color: A tuple representing the maximum RGB color in the interval (inclusive).
    - new_color: A tuple representing the new RGB color to apply.
    - output_path: Path to save the modified image.
    """
    # Open an image file
    with Image.open(image_path) as img:
        # Load image data
        img = img.convert("RGBA")  # Ensure image is in RGBA format
        data = img.getdata()

        # Create a list to hold the new image data
        new_data = []

        # Replace colors within the specified interval with the new color
        for item in data:
            r, g, b, a = item
            if (min_color[0] <= r <= max_color[0] and
                min_color[1] <= g <= max_color[1] and
                min_color[2] <= b <= max_color[2]):
                # Change pixel color to new_color
                new_data.append((new_color[0], new_color[1], new_color[2], a))
            else:
                # Keep the original pixel color
                new_data.append(item)

        # Update the image with the new data
        img.putdata(new_data)
        
        # Save the modified image to the output path
        img.save(output_path)
        print(f"Image saved to {output_path}")

#Usage
image_path = 'C:/Users/ololi/StudioProjects/AI-generatedCAH/public/images/logo.png'  # Path to the input image
min_color = (200, 200, 200)  # Minimum color in the interval (light gray)
max_color = (255, 255, 255)  # Maximum color in the interval (white)
new_color = (173, 168, 168)  # New color to apply
output_path = 'C:/Users/ololi/StudioProjects/AI-generatedCAH/public/images/logo_output.png'  # Path to save the modified image

change_color_within_interval(image_path, min_color, max_color, new_color, output_path)
