from PIL import Image
import os

gif_folder = 'gif'
output_folder = 'pngs'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

gif_files = [f for f in os.listdir(gif_folder) if f.endswith('.gif')]
gif_files.sort(key=lambda x: int(x.split('.')[0]))  # Sort by numeric prefix

for idx, gif_file in enumerate(gif_files):
    gif_path = os.path.join(gif_folder, gif_file)
    output_path = os.path.join(output_folder, f'Hobo{idx}.png')
    
    with Image.open(gif_path) as gif_image:
        first_frame = gif_image.convert("RGBA").convert("RGB")
        first_frame.save(output_path, format="PNG")
    
    print(f'Converted {gif_file} to {output_path}')