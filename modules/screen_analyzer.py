import mss
import pytesseract
from PIL import Image
from configuration.configuration_loot_mode1 import good_loot
from configuration.configuration_parameters import screen_size

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def take_screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 50, "left": 0, "width": screen_size["width"], "height": screen_size["height"]}
        output = "screenshots/sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
    return output

def detect_loot(filename):
    img = Image.open(filename)
    return pytesseract.image_to_data(img, output_type='dict')

def find_floor_good_loot(loot_locations):
    found_good_loot = []
    for i in range(len(loot_locations["level"])):
        if loot_locations["text"][i] != "":
            if loot_locations['text'][i] in good_loot:
                found_good_loot.append(
                    {
                        "name": loot_locations['text'][i],
                        "x": loot_locations["left"][i] + loot_locations["width"][i] / 2,
                        "y": loot_locations["top"][i] + loot_locations["height"][i] / 2,
                    }
                )
    return found_good_loot

def find_vendor_good_loot(loot_locations):
    if all([loot in loot_locations["text"] for loot in good_loot]):
        return True
    return False
