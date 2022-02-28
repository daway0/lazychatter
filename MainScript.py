from Chat import Chat
from Export import DataExport
from DirectoryManager import DirectoryManager
from MesseageCategorizer import ChatMesseageCategorizer
from Professor import Professor
import Constant


def categorize_all_chat_messages(files: list, professor: Professor) -> None:
    for file_name in files:
        chat = Chat(file_name)
        ChatMesseageCategorizer(chat, professor).categorize()
        


def main() -> None:
    DirectoryManager.make_directories([Constant.Directory.STUDENT_CHAT_DIRECTORY,
                                       Constant.Directory.STUDENT_CHART_DIRECTORY,
                                       Constant.Directory.OVERALL_RESULT])
    files = DirectoryManager.import_chat_files()

    if files == []:
        raise Exception('Chat files not found!')

    professor = Professor()
    categorize_all_chat_messages(files, professor)
    DataExport.student_chats(Constant.Directory.STUDENT_CHAT_DIRECTORY, 
                                 professor)
    DataExport.pieplot(professor)

 
if __name__ == '__main__':
    try:
        main()
    except:
        print ('script crashed')
    
