from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class MemeGenerator:
    def __init__(self, image_path, font_path='impact.ttf'):
        self._image_path = image_path
        self._image = Image.open(image_path)
        self._draw = ImageDraw.Draw(self._image)
        self._font = ImageFont.truetype(font_path, 42)

    def _put_text(self, text, x, y, with_outline, outline_thickness):
        if with_outline:
            self._draw.text((x-outline_thickness, y-outline_thickness), text,(0,0,0),font=self._font)
            self._draw.text((x+outline_thickness, y-outline_thickness), text,(0,0,0),font=self._font)
            self._draw.text((x+outline_thickness, y+outline_thickness), text,(0,0,0),font=self._font)
            self._draw.text((x-outline_thickness, y+outline_thickness), text,(0,0,0),font=self._font)

        self._draw.text((x, y), text, (255,255,255), font=self._font)

    def put_meme_text(self, text, y, with_outline=True, outline_thickness=2):
        text_width, _ = self._draw.textsize(text, self._font)
        self._put_text(text, self._image.width/2 - text_width/2, y, with_outline, outline_thickness)

    def save_meme(self, file_path):
        self._image.save(file_path)

    def show_meme(self):
        self._image.show()

