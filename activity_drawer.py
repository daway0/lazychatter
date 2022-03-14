from PIL import ImageDraw, Image
import math


class Board:
    def __init__(self, width, height, title='act_tracker', color_fill='black') -> None:
        self.__width = width
        self.__height = height
        self.__color_fill = color_fill
        self.__title = title

    def build(self):
        board = Image.new('RGBA', (self.__width, self.__height),
                          color=self.__color_fill,)

        return board


class Square:
    def __init__(self, length, color_fill) -> None:
        self.__length = length
        self.__color_fill = color_fill

    def draw(self, x, y, board):

        rect_coor = (x, y, x+self.__length, y+self.__length)
        board.rectangle(rect_coor,
                        outline=None,
                        fill=self.__color_fill,)


class ClassActivityDrawer:
    def __init__(self, activty_dict, timeline: list) -> None:
        self.__data = activty_dict
        self.__opacity_ratio = None
        self.__timeline = timeline

    def draw(self, detail: bool = False):
        width = 1920
        length = width / len(self.__timeline)
        height = int(length * (len(self.__data.keys())+1))
        board = Board(width, height, color_fill='black').build()
        db = ImageDraw.Draw(board)

        y = 0

        for date in self.__data:
            self.__cal_opacity(date)
            x = 0

            for time in self.__data[date]:

                # drawble_board

                if not self.__data[date][time] == 0:

                    opacity = self.__data[date][time] * self.__opacity_ratio
                    sq = Square(length, (opacity, 0, 0))
                    sq.draw(x, y, db)
                    if detail:
                        db.text(
                            (x, y), f'{self.__data[date][time]}', fill='white')
                x += length
                opacity = 0
            y += length
        x = 0
        db.rectangle((0, y, width, y), fill='white')
        y += int(length/3)
        for time in self.__timeline:
            if self.__timeline.index(time) % 10 == 0:
                db.text((x, y), f"{time}'")
            if self.__timeline.index(time) == len(self.__timeline)-1:
                db.text((x-length, y), f"{time[3:]}'")
            x += length
        if detail:
            board.save('activity-detail.png')
        else:
            board.save('activity.png')
        board.show()

    def __cal_opacity(self, date):
        max = 0

        for time in self.__data[date]:
            if self.__data[date][time] > max:
                max = self.__data[date][time]

        self.__opacity_ratio = math.ceil(255/max)
