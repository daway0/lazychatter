from message import Message


class ChatRepairman:
    def __init__(self, lines: list[str]):
        self.__lines = lines

    def repair(self) -> list[Message]:
        msg_list = []
        for line in self.__lines:
            line = ChatRepairman.__remove_break(line)
            line = ChatRepairman.__remove_listenonly(line)

            if ChatRepairman.__is_empty_message(line):
                continue
            if ChatRepairman.__is_structured(line):

                msg = Message(line)
                msg_list.append(msg)
                current_author = msg.author()
                current_time = msg.time()
                continue

            structured_message = f'{current_time} {current_author}: {line}'
            strd_msg = Message(structured_message)
            msg_list.append(strd_msg)

        return msg_list

    @classmethod
    def __is_structured(cls, line: str):
        msg = Message(line)

        if msg.time() == None:
            return False
        return True
    # valid chatline starts with:[00:00] bla bla bla

    @classmethod
    def __is_empty_message(cls, line: str):
        if line.strip() == '':
            return True
        msg = Message(line)
        if msg.time() != None and msg.author() == None and msg.message() == None:
            return True
        return False
    # empty msg:[00:00] [empty]

    @classmethod
    def __remove_break(cls, line: str):
        return line.replace('\n', '')

    @classmethod
    def __remove_listenonly(cls, line: str):
        if 'LISTENONLY-' in line:
            return line.replace('LISTENONLY-', '')
        return line
