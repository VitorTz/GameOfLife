from src.notification import ImageNotification
from src.image import Image as GameImage
from src.constants import Constants
from time import asctime
from PIL import Image


def take_screenshot(image: list[list[int]]) -> None:
    """Salva uma imagem do estado atual do jogo"""
    size = (len(image[0]), len(image))
    img = Image.new(mode="RGB", size=size, color=Constants.window_bg_color)
    for i, line in enumerate(image):
        for j, cell in enumerate(line):
            if cell:
                img.putpixel((j, i), value=Constants.cell_color)
    
    image_name = f"screenshot_{asctime()}.png"
    if not Constants.screenshot_dir.exists():
        Constants.screenshot_dir.mkdir()
    f_name = Constants.screenshot_dir / image_name
    img.save(f_name, bitmap_format='png')

    ImageNotification(
        GameImage(
            Constants.screenshot_saved_warning,
            Constants.screenshot_saved_warning_pos
        )
    ).show()
    

