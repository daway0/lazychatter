from chat import Chat
from chat_info_extractor import ChatInfoExtractor


class Timeline:
    def __init__(self, chats: list[Chat]) -> None:
        self.__start = None
        self.__end = None

        start_times = []
        end_times = []

        for chat in chats:
            start, end = ChatInfoExtractor.start_end(chat)
            start_times.append(start)
            end_times.append(end)

        self.__start = sorted(start_times)[0]
        self.__end = sorted(end_times)[-1]

    def create(self) -> list:
        timeline = []
        hour, min = self.__hour_min_tuple(self.__start)
        end_hour, end_min = self.__hour_min_tuple(self.__end)

        while not (hour == end_hour and min == end_min):
            if min == 60:
                min = 0
                hour += 1
            timeline.append(self.__t_str_maker(hour, min))
            min += 1
        return timeline

    def __hour_min_tuple(self, time: str) -> tuple:
        hour = int(time[0:2])
        min = int(time[3:])
        return (hour, min)

    def __t_str_maker(self, hour: int, min: int) -> str:
        str_time = f'{str(hour).zfill(2)}:{str(min).zfill(2)}'
        return str_time
