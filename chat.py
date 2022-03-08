from chat_repairman import ChatRepairman


class Chat:
    def __init__(self, file: str) -> None:
        self.__lines = []
        self.file_name = file
        self.messages = []

        with open(file, 'r', encoding='utf-8') as chat_file:
            for line in chat_file:
                self.__lines.append(line)

        self.messages = ChatRepairman(self.__lines).repair()
