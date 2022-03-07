from chat import Chat
from export import DataExport
from directory_manager import DirectoryManager
from message_categorizer import ChatMesseageCategorizer
from professor import Professor
import constant
from chat_repairman import ChatRepairman


def categorize_all_chat_messages(files: list, professor: Professor) -> None:
    for file_name in files:
        chat = Chat(file_name)
        repaired_chat = ChatRepairman(chat).repair()
        ChatMesseageCategorizer(repaired_chat, professor).categorize()


def main() -> None:
    DirectoryManager.make_directories(
        [constant.Directory.STUDENT_CHAT_DIRECTORY])
    files = DirectoryManager.import_chat_files()

    if not files:
        raise Exception('Chat files not found!')

    professor = Professor()
    categorize_all_chat_messages(files, professor)
    DataExport.student_chats(constant.Directory.STUDENT_CHAT_DIRECTORY,
                             professor)
    DataExport.pieplot(professor)
    DataExport.hbarplot(professor)


if __name__ == '__main__':
    try:
        main()
    except:
        print('script crashed!')
