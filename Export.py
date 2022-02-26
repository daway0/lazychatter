from ChatDataExtractor import ChatDataExtractor
from Professor import Professor
import xlsxwriter


class DataExport:
    @staticmethod
    def student_chats(directory: str, professor: Professor):
        for student_name in professor.student_name_list():
            student = professor.get_student(student_name)
            with open(f'./{directory}/{student_name}.txt', 'w', encoding='utf-8') as file:
                for line in student.export_chats():
                    file.write(line)

    @staticmethod
    def student_charts(directory):
        pass

    @staticmethod
    def overall_result(directory, files, professor: Professor):
        workbook = xlsxwriter.Workbook('overall_result.xlsx')
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
