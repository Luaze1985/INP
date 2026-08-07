import os
import urllib.request
from PIL import Image, ImageEnhance

# Ensure candidates directory exists
OUTPUT_DIR = os.path.join("site", "mockup", "kandidater")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# List of Unsplash photo IDs and details from the first round
CANDIDATES = [
    {"id": "photo-1541888946425-d81bb19240f5", "name": "kandidat-1.jpg", "description": "Byggeplass med betongskjelett og kran (Ricardo Gomez Angel)"},
    {"id": "photo-1504307651254-35680f356dfd", "name": "kandidat-2.jpg", "description": "Gul tårnkran mot dramatisk himmel (Spencer Davis)"},
    {"id": "photo-1581092921461-eab62e97a780", "name": "kandidat-3.jpg", "description": "Ingeniør i vernehjelm som inspiserer med nettbrett (Science in HD)"},
    {"id": "photo-1486406146926-c627a92ad1ab", "name": "kandidat-4.jpg", "description": "Stålkonstruksjon og glassfasade på høyhus (Sean Pollock)"},
    {"id": "photo-1605647540924-852290f6b0d5", "name": "kandidat-5.jpg", "description": "Massivtre-konstruksjon og treramme (Clay Banks)"},
    {"id": "photo-1503387762-592deb58ef4e", "name": "kandidat-6.jpg", "description": "Arkitekttegning med vernehjelm (rawpixel)"},
    {"id": "photo-1590069261209-f8e9b8642343", "name": "kandidat-7.jpg", "description": "Minimalistisk råbetongvegg og dagslys (Jonas Jacobsson)"},
    {"id": "photo-1513694203232-719a280e022f", "name": "kandidat-8.jpg", "description": "Abstrakt betongtekstur og skyggespill (Unsplash)"},
    {"id": "photo-1497366216548-37526070297c", "name": "kandidat-9.jpg", "description": "Moderne kontorbygning lobby og betongflater (StockSnap)"},
    {"id": "photo-1489516408517-0c0a15662682", "name": "kandidat-10.jpg", "description": "Byggeplass med kraner i solnedgang (Caleb Jones)"}
]

def download_and_process():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for i, item in enumerate(CANDIDATES, 1):
        photo_id = item["id"]
        filename = item["name"]
        dest_path = os.path.join(OUTPUT_DIR, filename)
        
        url = f"https://images.unsplash.com/{photo_id}?q=80&w=1200&auto=format&fit=crop"
        
        print(f"[{i}/{len(CANDIDATES)}] Downloading {filename} ({item['description']})...")
        try:
            req = urllib.request.Request(url, headers=headers)
            temp_path = dest_path + ".tmp"
            with urllib.request.urlopen(req) as response, open(temp_path, 'wb') as out_file:
                out_file.write(response.read())
            
            # Open image using Pillow
            with Image.open(temp_path) as img:
                # 1. Dim the image (reduce brightness to 30%)
                brightness_enhancer = ImageEnhance.Brightness(img)
                img_dimmed = brightness_enhancer.enhance(0.30)
                
                # 2. Desaturate the image (reduce saturation to 45%)
                color_enhancer = ImageEnhance.Color(img_dimmed)
                img_processed = color_enhancer.enhance(0.45)
                
                # Save as JPEG
                img_processed.convert("RGB").save(dest_path, "JPEG", quality=85)
                
            os.remove(temp_path)
            print(f"   Success: processed and saved to {dest_path}")
        except Exception as e:
            print(f"   Error downloading/processing {filename}: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == "__main__":
    download_and_process()
