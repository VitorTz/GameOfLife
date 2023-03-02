from src.notification import Notification
from src.image import Image as GameImage
from src.constants import Constants
from pathlib import Path
from time import asctime
from PIL import Image


def mkdir_screenshot_folder() -> None:
    """Cria a pasta de capturas de tela caso necessário"""
    if not Constants.screenshot_dir.exists():
        Constants.screenshot_dir.mkdir()
    

def screenshot_name() -> Path:
    """Cria e retorna um nome para a captura de tela"""
    mkdir_screenshot_folder()
    image_name = f"screenshot_{asctime()}.png"
    return Constants.screenshot_dir / image_name


def convert_matrix_to_png_img(image: list[list[int]]) -> Image:
    """Cria e retorna uma imagem para ser salva no formato .png"""
    size = (len(image[0]), len(image))
    img: Image = Image.new(mode="RGB", size=size, color=Constants.window_bg_color)
    for i, line in enumerate(image):
        for j, cell in enumerate(line):
            if cell:
                img.putpixel((j, i), value=Constants.cell_color)
    return img


def show_notification() -> None:
    """Notifica o usuário que a captura de tela foi salva"""
    Notification(
        GameImage(
            Constants.notification_screenshot_saved,
            Constants.notification_screenshot_saved_pos
        )
    ).show()


def take_screenshot(image: list[list[int]]) -> None:
    """Salva uma imagem do estado atual do jogo"""
    img = convert_matrix_to_png_img(image)
    f_name: Path = screenshot_name()
    img.save(f_name, bitmap_format='png')
    show_notification()


