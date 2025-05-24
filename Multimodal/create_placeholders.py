from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(text, filename, size=(800, 450), bg_color=(124, 58, 237), text_color=(255, 255, 255)):
    # Create a new image with the specified background color
    image = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(image)
    
    # Add a gradient effect
    for y in range(size[1]):
        alpha = y / size[1]
        color = (
            int(bg_color[0] * (1 - alpha) + 76 * alpha),
            int(bg_color[1] * (1 - alpha) + 29 * alpha),
            int(bg_color[2] * (1 - alpha) + 149 * alpha)
        )
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position for center alignment
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, font=font, fill=text_color)
    
    # Save the image
    os.makedirs('static/images', exist_ok=True)
    image.save(f'static/images/{filename}')

# Create placeholder images
create_placeholder_image('Gemini Analyzer', 'gemini.png')
create_placeholder_image('Sign Language Translator', 'sign.png') 