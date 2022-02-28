from Professor import Professor


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
        from bidi.algorithm import get_display
        import arabic_reshaper

        name_list = professor.student_name_list()
        reshaped_names_list = []
        for name in name_list:
            reshaped_text = arabic_reshaper.reshape(name)
            artext = get_display(reshaped_text)
            reshaped_names_list.append(artext)

        number_chats_list = []
        all_chats = 0
        for name in professor.student_name_list():
            number_student_chats = professor.get_student(
                name).number_all_chats()
            all_chats += number_student_chats
            number_chats_list.append(number_student_chats)

        plt.xlabel((f'{all_chats} messages '))
        plt.pie(number_chats_list, labels=reshaped_names_list,
                radius=1.4, autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.1)
        plt.show()
