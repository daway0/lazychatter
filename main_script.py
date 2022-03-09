from chat import Chat
from export import DataExport
from directory_manager import DirectoryManager
from message_categorizer import ChatMesseageCategorizer
from professor import Professor
import constant
from timeline import Timeline
from activity_tracker import ActivityTracker


def categorize_all_chat_messages(files: list, professor: Professor) -> None:
    for file_name in files:
        chat = Chat(file_name)
        ChatMesseageCategorizer(chat, professor).categorize()


def main() -> None:
    DirectoryManager.make_directories(
        [constant.Directory.STUDENT_CHAT_DIRECTORY])
    files = DirectoryManager.import_chat_files()

    if not files:
        raise Exception('Chat files not found!')

    chats = []
    for file_name in files:
        chats.append(Chat(file_name))

    professor = Professor()
    timeline = Timeline(chats).create()
    categorize_all_chat_messages(files, professor)
    all_act_dict = ActivityTracker.all_students_activity(professor, timeline)
    print(all_act_dict)
    DataExport.student_chats(constant.Directory.STUDENT_CHAT_DIRECTORY,
                             professor)
    DataExport.pieplot(professor)
    DataExport.hbarplot(professor)


if __name__ == '__main__':
    main()
