import mss
import pytesseract
from PIL import Image
from configuration.configuration_loot_act3 import good_loot

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def take_screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 0, "left": 0, "width": 3180, "height": 1840}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

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
