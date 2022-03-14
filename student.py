class Student:
    def __init__(self, name) -> None:
        self.__name = name
        self.__messages = {}
        self.__messages_in_time = {}

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

    def msgpp_in_time(self, time: str, date: str):
        if not date in self.__messages_in_time.keys():
            self.__messages_in_time[date] = {}

        if not time in self.__messages_in_time[date].keys():
            self.__messages_in_time[date][time] = 0
        self.__messages_in_time[date][time] += 1

    def msgs_in_time_date(self, time: str, class_date: str) -> int:
        msgs = 0
        if class_date in self.__messages_in_time.keys():
            if time in self.__messages_in_time[class_date].keys():
                msgs += self.__messages_in_time[class_date][time]

        return msgs

    def msgs_in_time(self, time: str) -> int:
        msgs = 0
        for date in self.__messages_in_time.keys():
            if time in self.__messages_in_time[date].keys():
                msgs += self.__messages_in_time[date][time]

        return msgs

    def max_msgs_in_min(self) -> int:
        max = 0
        merged_dict = {}
        for date in self.__messages_in_time:
            for time in self.__messages_in_time[date]:
                if not time in merged_dict.keys():
                    merged_dict[time] = self.__messages_in_time[date][time]
                else:
                    merged_dict[time] += self.__messages_in_time[date][time]

        for time in merged_dict:
            if merged_dict[time] > max:
                max = merged_dict[time]
        return max
