from Chat import Chat
from Export import DataExport
from DirectoryManager import DirectoryManager
from MesseageCategorizer import ChatMesseageCategorizer
from Professor import Professor
import Constant


def categorize_all_chat_messages(files: list, professor: Professor):
    for file_name in files:
        chatinfo = Chat(file_name)
        chat = ChatMesseageCategorizer(chatinfo, professor)
        chat.categorize()


def main():

    DirectoryManager.make_directories([Constant.Directory.STUDENT_CHAT_DIRECTORY,
                                       Constant.Directory.STUDENT_CHART_DIRECTORY,
                                       Constant.Directory.OVERALL_RESULT])
    files = DirectoryManager.import_chat_files()

    if not files:
        raise Exception()

    professor = Professor()
    categorize_all_chat_messages(files, professor)
    DataExport.student_chats(Constant.Directory.STUDENT_CHAT_DIRECTORY, 
                                 professor)
    DataExport.overall_result(Constant.Directory.OVERALL_RESULT, files, professor)

 
if __name__ == '__main__':
    
        main()
    
