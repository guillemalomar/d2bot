import mss
import pytesseract
from PIL import Image
from loot import good_loot

pytesseract.pytesseract.tesseract_cmd = r'C:\<path-to-your-tesseract>\Tesseract-OCR\tesseract.exe'

def take_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(output='screenshots/travincal_loot.png')
    return filename

def detect_loot(filename):
    img = Image.open(filename)
    data = pytesseract.image_to_data(img, output_type='dict')
    return data['text']

def find_good_loot(loot_locations):
    found_good_loot = []
    for i in range(len(loot_locations["level"])):
        if loot_locations["text"][i] != "":
            if loot_locations['text'][i] in good_loot:
                found_good_loot.append(
                    {
                        "name": loot_locations['text'][i],
                        "x": loot_locations["data"][i] + loot_locations["width"][i] / 2,
                        "y": loot_locations["top"][i] + loot_locations["height"][i] / 2,
                    }
                )
    return found_good_loot
