

class Student:
    def __init__(self, name) -> None:
        self.__name = name
        self.__messages = {}

    def name(self):
        return self.__name

    def add_message(self, text, class_date):

        if not class_date in self.__messages.keys():
            self.__messages[class_date] = []

        self.__messages[class_date].append(text)

    def export_chats(self):
        data_items = self.__messages.items()
        sorted_data = sorted(data_items)

        with open(f'./student_chat/{self.__name}.txt', 'w', encoding='utf-8') as file:
            for key, chat in sorted_data:

                file.write(
                    f'\n[{key}][chats: {len(self.__messages[key])}] \n\n')
                for line in self.__messages[key]:
                    file.write(f'{line}')
