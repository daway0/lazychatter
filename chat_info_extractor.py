from chat import Chat


class ChatInfoExtractor:
    @staticmethod
    def class_date(chat: Chat) -> str:
        file_name = chat.file_name
        cursor_start_location = file_name.index(']')+2
        cursor_end_location = file_name[cursor_start_location::].index(
            '_')+cursor_start_location
        return file_name[cursor_start_location: cursor_end_location]

    @staticmethod
    def class_name(chat: Chat) -> str:
        file_name = chat.file_name
        cursor_start_location = file_name.index('-')+1
        curosr_stop_location = file_name.index('[')
        return file_name[cursor_start_location:curosr_stop_location]
