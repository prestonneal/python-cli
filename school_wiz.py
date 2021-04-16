import json

def str2Fun():
    return '2133'

# SchoolWiz() utility class calculates and reports a student's final weighted average in a class
class SchoolWiz:
    def __init__(self):
        self.student_name = ""

        self.grades = {
            "exams": {
                "name": "exam" , 
                "scores":  [] , 
                "average": 0 , 
                "weighted_average": 0
            },
            "quizzes": {
                "name": "quiz" , 
                "scores":  [] , 
                "average": 0 , 
                "weighted_average": 0
            },
            "assignments": {
                "name": "assignment" , 
                "scores":  [] , 
                "average": 0 , 
                "weighted_average": 0
            }
        }

        self.final_grade = 0
        self.graded_works_count = 12
        self.no_scores_per_type = 4

    def load_work_types_names_list(self):
        return ["exams", "quizzes", "assignments"]

    def load_work_types_weights_obj(self):
        return {"exams": 20, "quizzes": 40, "assignments": 40}

    def get_student_name(self, prompt=None, strict=True):
        if prompt is None:
            prompt = "What is the student's first name? "
        if strict:
            while True:
                name = input(prompt)
                if name.isalpha():
                    self.student_name = str(name)
                    break
        else:
            self.student_name = str(input(prompt))

    def capture_grade(self, work_type, weight):
        numbers_list = json.loads('{"1":"first","2":"second","3":"third","4":"fourth","5":"fifth"}')
        for i in range(self.no_scores_per_type):
            prompt = ''.join(["What grade did ", str(self.student_name), " score on their ", str(numbers_list[str(i + 1)]), " ", str(self.grades[work_type]["name"]), "? "])
            while True:
                try:
                    score = int(input(prompt))
                    if score < 0 or score > 100:
                        raise ValueError #this will send it to the print message and back to the input option
                    self.grades[work_type]["scores"].append(score)
                    break
                except ValueError:
                    print(''.join(["Invalid input. Your ", str(numbers_list[str(i + 1)]), " ", str(self.grades[work_type]["name"]), " score should be in the range of 0-100."]))
            
        self.grades[work_type]["scores"] = sorted(self.grades[work_type]["scores"])
        self.grades[work_type]["average"] = ((sum(int(i) for i in self.grades[work_type]["scores"])) / self.no_scores_per_type)

        self.grades[work_type]["weighted_average"] = self.grades[work_type]["average"] * weight//100
        self.final_grade += int(self.grades[work_type]["weighted_average"])

    def capture_grades(self):
        weights_list = self.load_work_types_weights_obj() 
        for work_type in self.load_work_types_names_list():
            self.capture_grade(work_type, weights_list[work_type])

    def print_pass_fail_final_grade(self):
        if self.final_grade is not None:
            if (int(self.final_grade) <= 50):
                print(''.join(["\nYou should have studied harder, ", str(self.student_name), "! You're final grade in the class is a  ", str(self.final_grade)]))
                return
            print(''.join(["\nNice Job, ", str(self.student_name), "! You're final grade in the class is a  ", str(self.final_grade)]))

    def print_report(self):
        if self.final_grade is not None:
            print('\nYour Scores: \n', )
            print('Exam scores: ', self.grades["exams"]["scores"])
            print('Quiz scores: ', self.grades["quizzes"]["scores"])
            print('Assignment scores: ', self.grades["assignments"]["scores"])

            print('\nYour Averages: \n', )
            print('Exam average: ', self.grades["exams"]["average"])
            print('Quiz average: ', self.grades["quizzes"]["average"])
            print('Assignment average: ', self.grades["assignments"]["average"])

            self.print_pass_fail_final_grade()

    def run_school_wizard(self):
        self.get_student_name()
        self.capture_grades()
        self.print_report()
