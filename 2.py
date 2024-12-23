from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner


class SalaryCalculatorApp(App):
    def build(self):
        self.employees = {
            "Павельев": 3,
            "Тимофеенко": 3,
            "Филин Е.": 4,
            "Филин С.": 4
        }

        self.rates = {
            3: 176,
            4: 196
        }

        # Create the layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Employee Dropdown
        self.employee_label = Label(text="Выберите сотрудника:")
        self.employee_spinner = Spinner(text="Выберите сотрудника", values=list(self.employees.keys()))
        layout.add_widget(self.employee_label)
        layout.add_widget(self.employee_spinner)

        # Total Hours Input
        self.total_hours_label = Label(text="Общее количество часов:")
        self.total_hours_input = TextInput()
        layout.add_widget(self.total_hours_label)
        layout.add_widget(self.total_hours_input)

        # Absent Hours Input
        self.absent_label = Label(text="Часы прогула:")
        self.absent_input = TextInput()
        layout.add_widget(self.absent_label)
        layout.add_widget(self.absent_input)

        # Result Label
        self.result_label = Label(text="Зарплата:")
        self.result_output = TextInput(readonly=True)
        layout.add_widget(self.result_label)
        layout.add_widget(self.result_output)

        # Calculate Button
        self.calculate_button = Button(text="Рассчитать")
        self.calculate_button.bind(on_press=self.calculate_salary)
        layout.add_widget(self.calculate_button)

        return layout

    def calculate_salary(self, instance):
        try:
            selected_employee = self.employee_spinner.text
            grade = self.employees[selected_employee]
            rate = self.rates[grade]

            total_hours = float(self.total_hours_input.text)
            absent_hours = float(self.absent_input.text)
            work_hours = max(0, total_hours - absent_hours)

            salary = work_hours * rate * 2.5
            self.result_output.text = f"{salary:.2f} руб."
        except (ValueError, KeyError):
            self.result_output.text = "Ошибка"


if __name__ == '__main__':
    SalaryCalculatorApp().run()
