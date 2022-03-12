from PIL import ImageDraw, Image


class Board:
    def __init__(self, width, height, title, color_fill='black') -> None:
        self.__width = width
        self.__height = height
        self.__color_fill = color_fill
        self.__title = title

    def build(self):
        board = Image.new('RGBA', (self.__width, self.__height),
                          color=self.__color_fill)

        return board


class Square():
    def __init__(self, length, color_fill) -> None:
        self.__length = length
        self.__color_fill = color_fill

    def draw(self, x, y, board):
        drawble_board = ImageDraw.Draw(board)
        rect_coor = (x, y, x+self.__length, y+self.__length)
        drawble_board.rectangle(rect_coor,
                                outline=None,
                                fill=self.__color_fill,)
