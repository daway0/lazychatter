from professor import Professor


class ActivityTracker():
    @staticmethod
    def all_students_activity(professor: Professor, timeline: list[str], class_date) -> dict:
        timeline_msg_dict = {}
        # {'16:20': 5,
        #  '16:21': 1,
        #  '16:30': 0, ...}

        for time in timeline:
            number_msgs = 0
            for std_name in professor.student_name_list():
                student = professor.get_student(std_name)
                number_msgs += student.msgs_in_time(time, class_date)
            timeline_msg_dict[time] = number_msgs

        return timeline_msg_dict