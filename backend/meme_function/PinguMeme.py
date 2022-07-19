from MemeGenerator import MemeGenerator

class PinguMeme:
    def __init__(self, static_content_path):
        self._FIRST_LINE_Y = 90
        self._SECOND_LINE_Y = 430

        template_path = f'{static_content_path}/angry_pingu.png'
        font_path = f'{static_content_path}/impact.ttf'
        self._generator = MemeGenerator(template_path, font_path)
        
    def set_text(self, first_line, second_line):
        self._generator.put_meme_text(first_line, self._FIRST_LINE_Y)
        self._generator.put_meme_text(second_line, self._SECOND_LINE_Y)

    def save(self, output_path):
        self._generator.save_meme(output_path)


if __name__ == '__main__':
    pingu_meme = PinguMeme('static')

    first_line_text = input('First text line: ')
    second_line_text = input('Second text line: ')


    pingu_meme.set_text(first_line_text, second_line_text)
    pingu_meme.save('meme.png')
