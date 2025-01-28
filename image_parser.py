import json
import os
import re
from PIL import Image

IMAGE_PATH = 'banner'


def sanitize_name(name):
    name = name.replace(' ', '_')
    name = re.sub(r'[^a-zA-Z0-9_\-]', '', name)
    return name

def convert_to_webp(src, dest):
    with Image.open(src) as img:
        img.save(dest, format='webp')

def image_parser():
    os.makedirs(IMAGE_PATH, exist_ok=True)
    with open('songs.json', 'r') as file:
        data = json.load(file)
    
    for pack in data:
        if pack["banner"] and os.path.exists(pack["banner"]):
            pack_banner_path = os.path.join(IMAGE_PATH, f'{pack["title"]}.webp')
            try:
                convert_to_webp(pack["banner"], pack_banner_path)
            except Exception as e:
                print(f'Error processing pack banner: {e}')
                continue
        for song in pack["songs"]:

            if song["banner"] and os.path.exists(song["banner"]):
                song_banner_path = os.path.join(IMAGE_PATH, f'{sanitize_name(pack["title"])}__{sanitize_name(song["title"])}.webp')
                try:
                    convert_to_webp(song["banner"], song_banner_path)
                except Exception as e:
                    print(f'Error processing song banner: {e}')
                    continue
    print(f"Copied banners to {IMAGE_PATH}")
image_parser()