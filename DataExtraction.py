from Professor import Professor


class DataExtraction:
    @staticmethod
    def student_chats(directory: str, professor: Professor):
        for student_name in professor.student_name_list():
            student = professor.get_student(student_name)
            with open (f'./{directory}/{student_name}.txt', 'w', encoding='utf-8') as file:
                for line in student.export_chats():
                    file.write(line)

    @staticmethod
    def student_charts(directory):
        pass

    @staticmethod
    def overall_result(directory):
        pass
