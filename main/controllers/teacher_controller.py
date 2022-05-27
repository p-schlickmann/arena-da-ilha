from main.views.teacher_view import TeacherView


class TeacherController:

    def __int__(self, teacher_controller):
        self.__teacher_controller = teacher_controller
        self.__view = TeacherView()

    def open_view(self):
        options = {
            1: self.register_lesson,
            2: self.add_credits,
            3: self.see_billing,
        }
        selected_option = self.__view.open()
        options[selected_option]()

    def register_lesson(self):
        print('Register Lesson')

    def add_credits(self):
        print('Add Credits')

    def see_billing(self):
        print('See Billing')
