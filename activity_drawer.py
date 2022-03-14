from textwrap import indent
from PIL import ImageDraw, Image
import math
from professor import Professor
from student import Student
from timeline import Timeline


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


class StudentActivityDrawer:
    def __init__(self, professor: Professor, timeline: list) -> None:
        self.__professor = professor
        self.__timeline = timeline

    def draw(self, detail: bool = False):
        indent = 50
        line_number_x = int(indent/2)
        width = 1920
        width_indent = width+indent*2
        length = width / len(self.__timeline)
        height = int(length * (len(self.__professor.student_name_list())+1))
        board = Board(width_indent, height, color_fill='black').build()
        db = ImageDraw.Draw(board)

        y = 0
        line_number = 0
        for (_, student), msgs in self.__professor.sorted_name_list()[::-1]:

            line_number += 1
            x = 0
            db.text((x, y), str(msgs))
            opacity_ratio = self.__cal_opacity(student)
            x = indent
            for time in self.__timeline:
                std_msgs = student.msgs_in_time(time)
                if not std_msgs == 0:

                    opacity = std_msgs * opacity_ratio
                    sq = Square(length, (0, opacity, 0))
                    sq.draw(x, y, db)
                    if detail:
                        db.text(
                            (x, y), f'{std_msgs}', fill='white')
                x += length
            db.text((line_number_x, y), f'>{line_number}', fill='yellow')
            db.text((width+indent, y), f'{line_number}<', fill='yellow')
            db.text((int((width_indent)/2), y),
                    f'<{line_number}>', fill=(100, 100, 100))
            db.rectangle((indent, y, width, y), fill=(40, 40, 40))
            y += length
        x = indent
        db.rectangle((indent, y, width+indent, y), fill='white')
        # wihte line
        y += int(length/3)
        for time in self.__timeline:
            if self.__timeline.index(time) % 10 == 0:
                db.text((x, y), f"{time}'")
            if self.__timeline.index(time) == len(self.__timeline)-1:
                db.text((x-length, y), f"{time[3:]}'")
            x += length
        if detail:
            board.save('students-activity-detail.png')
        else:
            board.save('students-activity.png')
        board.show()

    def __cal_opacity(self, student: Student):
        max = student.max_msgs_in_min()
        return math.ceil(150/max)
