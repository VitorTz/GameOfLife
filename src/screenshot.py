from src.constants import Constants
from PIL import Image
from time import asctime




def take_screenshot(image: list[list[int]]) -> None:
    size = (len(image[0]), len(image))
    img = Image.new(mode="RGB", size=size, color=Constants.window_bg_color)
    for i, line in enumerate(image):
        for j, cell in enumerate(line):
            if cell:
                img.putpixel((j, i), value=Constants.cell_color)
    
    image_name = f"screenshot_{asctime()}.png"
    f_name = Constants.screenshot_dir / image_name
    img.save(f_name, bitmap_format='png')
    print(f"Image {f_name} saved")


