from activity_drawer import ClassActivityDrawer
from chat import Chat
from chat_info_extractor import ChatInfoExtractor
from export import DataExport
from directory_manager import DirectoryManager
from message_categorizer import ChatMesseageCategorizer
from professor import Professor
import constant
from timeline import Timeline
from activity_tracker import ActivityTracker
from chat_collector import collect_data


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

    chat_dates = []
    for chat in chats:
        chat_dates.append(ChatInfoExtractor.class_date(chat))

    act_dict = {}
    for date in chat_dates:
        data = ActivityTracker.all_students_activity(professor, timeline, date)
        act_dict[date] = data

    DataExport.student_chats(constant.Directory.STUDENT_CHAT_DIRECTORY,
                             professor)

    try:
        collect_data()
    except:
        print('No internet connection')
    DataExport.pieplot(professor)
    DataExport.hbarplot(professor)
    ClassActivityDrawer(act_dict, timeline).draw()


if __name__ == '__main__':
    try:
        main()
    except:
        print('script crashed!')
