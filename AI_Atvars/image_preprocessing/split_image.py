from PIL import Image

# Load the image
image_path = "C:/Users/Atvar/Desktop/year2/Team Project/images/ghibsky/scaled_pond_in_forest.jpg"  # Replace with your image path
image = Image.open(image_path)

# Original image dimensions
original_width, original_height = image.size

# Ensure the original image is square
# if original_width != original_height:
#     raise ValueError("The input image must have a 1:1 aspect ratio.")

# Target aspect ratio dimensions (16:9 slices)
slice_width = original_width // 4  # Each slice spans 1/4th the width of the image
slice_height = int(slice_width / 16 * 9)  # Calculate height for 16:9 aspect ratio

# Ensure slice height fits the original height; center-crop the height if necessary
if slice_height > original_height:
    raise ValueError("Cannot achieve 16:9 slices with the given image dimensions.")

# Set crop position (choose 'top', 'middle', or 'bottom')
crop_position = "bottom"  # Change to "top", "middle", or "bottom"

if crop_position == "top":
    top = 0
    bottom = slice_height
elif crop_position == "middle":
    top = (original_height - slice_height) // 2
    bottom = top + slice_height
elif crop_position == "bottom":
    bottom = original_height
    top = original_height - slice_height

# Crop and save each slice
for i in range(4):
    left = i * slice_width
    right = (i + 1) * slice_width
    # top = (original_height - slice_height) // 2  # Center the crop vertically
    # bottom = 1024
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(f"C:/Users/Atvar/Desktop/year2/Team Project/image_preprocessing/split_images/scaled_ghibsky_forest/{i + 1}.jpg")

print("Image successfully split into 4 panoramic 16:9 sections.")
