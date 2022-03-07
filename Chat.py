class Chat:
    def __init__(self, file: str) -> None:
        self.file_name = file
        self.lines = []

        with open(file, 'r', encoding='utf-8') as chat_file:
            for line in chat_file:
                self.lines.append(line)
