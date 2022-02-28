from ChatDataExtractor import ChatDataExtractor
from Professor import Professor
import xlsxwriter


class DataExport:
    @staticmethod
    def student_chats(directory: str, professor: Professor) -> None:
        for student_name in professor.student_name_list():
            student = professor.get_student(student_name)
            with open(f'./{directory}/{student_name}.txt', 'w', encoding='utf-8') as file:
                for line in student.export_chats():
                    file.write(line)

    @staticmethod
    def student_charts(directory: str, professor: Professor):
        pass

    @staticmethod
    def pieplot(professor: Professor):
        import matplotlib.pyplot as plt
        import matplotlib
        from bidi.algorithm import get_display
        import arabic_reshaper

        name_list = professor.student_name_list()
        reshaped_names_list = []
        for name in name_list:
            reshaped_text = arabic_reshaper.reshape(name)
            artext = get_display(reshaped_text)
            reshaped_names_list.append(artext)

        number_chats_list = []
        for name in professor.student_name_list():
            number_student_chats = professor.get_student(
                name).number_all_chats()
            number_chats_list.append(number_student_chats)

        plt.pie(number_chats_list, labels=reshaped_names_list,
                radius=1.4, autopct='%1.1f%%', pctdistance=0.8)
        plt.show()

    @staticmethod
    def overall_result(directory, files, professor: Professor) -> None:
        workbook = xlsxwriter.Workbook(f'./{directory}/overall_result.xlsx')
        worksheet = workbook.add_worksheet()
        # column
        dates_dict = ChatDataExtractor.class_dates(files)
        for col in dates_dict:
            worksheet.write(0, col, dates_dict[col])

            # row
            row = 1
            for student_name in professor.student_name_list():
                student = professor.get_student(student_name)
                worksheet.write(row,0, student_name)
                worksheet.write(
                    row, col, student.chats_in_date(dates_dict[col]))
                row += 1

        workbook.close()
