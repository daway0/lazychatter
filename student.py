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

    def export_chats(self) -> None:
        data_items = self.__messages.items()
        sorted_data = sorted(data_items)
        all_messages = []

        for key, _ in sorted_data:
            all_messages.append(
                f'\n[{key}][chats: {len(self.__messages[key])}] \n\n')
            for line in self.__messages[key]:
                all_messages.append(f'{line}')
        return all_messages

    def chats_in_date(self, date: str) -> int:
        if date in self.__messages.keys():
            return len(self.__messages[date])
        return 0

    def number_all_chats(self) -> int:
        number = 0
        for key in self.__messages:
            number += len(self.__messages[key])
        return number

    def number_all_classes(self) -> int:
        return len(self.__messages)