from PIL import Image

# Function to get and save the center of the image
def save_image_center(image_path, crop_width=200):
    # Open the image
    image = Image.open(image_path)
    
    # Get image dimensions
    width, height = image.size
    center_x, center_y = width // 2, height // 2

    # Calculate the aspect ratio of the original image
    aspect_ratio = height / width

    # Calculate the corresponding crop height while maintaining the aspect ratio
    crop_height = int(crop_width * aspect_ratio)

    # Calculate the crop box (center crop area)
    left = center_x - crop_width // 2
    top = center_y - crop_height // 2
    right = center_x + crop_width // 2
    bottom = center_y + crop_height // 2

    # Crop the image to the center area with respect to aspect ratio
    center_image = image.crop((left, top, right, bottom))

    # Save the center crop to a new file
    output_path = image_path.replace(".jpg", "_center.jpg")
    center_image.save(output_path)

    print(f"Center of the image saved as {output_path} with aspect ratio preserved.")
    return output_path

# Example usage
# image_path = "mntn.jpg"
# output_file = save_image_center(image_path, crop_width=800)