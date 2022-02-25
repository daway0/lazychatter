

class Student:
    def __init__(self, name) -> None:
        self.__name = name
        self.__data = {}

    def name(self):
        return self.__name

    def add_message(self, text, class_time):

        if not class_time in self.__data.keys():
            self.__data[class_time] = []

        self.__data[class_time].append(text)

    def export_chats(self):
        with open(f'{self.__name}.txt', 'w', encoding='utf-8') as file:
            for key in self.__data.keys():
                for line in self.__data[key]:
                    file.write(f'{key} {line}')
