import datetime

from note_editor.core.mvp.View import View

class ViewConsole(View):

    def get_note_title(self) -> str:
        new_title = input("Введите заголовок: ")
        if len(new_title) > 2:
            return new_title
        else:
            print("Заголовок должен содержать не менее 3 символов")
            return self.get_note_title()

    def get_note_text(self) -> str:
        new_text = input("Введите текст заметки: ")
        if len(new_text) > 0:
            return new_text
        else:
            print("Текст должен содержать минимум 1 символ")
            return self.get_note_text()

    def get_len_preview_text(self) -> int:
        len_short_text = input("Введите минимальное количество символов для отображения "
                               "текста заметки \nв свернутой форме: ")
        if len_short_text.isdigit() and 0 < int(len_short_text) < 16:
            return int(len_short_text)
        else:
            print("Введите число от 1 до 15")
            return self.get_len_preview_text()

    def print_str(self, format_note: str):
        print(format_note)

    def show_notepad(self, format_note: str, index: int):
        print(f'{index}. {format_note}')

    def get_index_note(self, max_index: int) -> int:
        index = input("Введите номер заметки: ")
        if index.isdigit() and 0 < int(index) <= max_index:
            return int(index) - 1
        else:
            print(f"Введите число от 1 до {max_index} включительно")
            return self.get_index_note(max_index)

    def show_commands(self, commands: list[str]):
        print("\nСписок доступных команд: ", end="")
        print(', '.join(commands))

    def show_parameters(self, parameters: list[str]):
        for i in range(len(parameters)):
            print(f'{i + 1}. {parameters[i]}')

    def get_index_command(self, commands: list[str]) -> int:
        command = input("Введите команду: ")
        if command in commands:
            return commands.index(command)
        else:
            print("Неверная команда")
            return self.get_index_command(commands)

    def get_parameter_to_change(self, parameters: list[str], flag=True) -> int:
        if flag:
            print("Выберите параметр для изменения: ")
            self.show_parameters(parameters)
        number = input("Введите число: ")
        if number.isdigit() and 0 < int(number) <= len(parameters):
            return int(number)
        else:
            print(f"Введите число от 1 до {len(parameters)} включительно")
            return self.get_parameter_to_change(parameters, False)

    def show_old_title(self, old_value: str, name_value="заголовок"):
        print(f"Текущий {name_value}: {old_value}")

    def show_old_text(self, old_value: str, name_value="текст"):
        self.show_old_title(old_value, name_value)

    def get_date(self, format_date="%d.%m.%Y") -> datetime:
        date_now = datetime.datetime.now()
        date = input("Введите дату в формате дд.мм.гггг: ")
        flag = True
        if len(date.split('.')) == 3:
            try:
                datetime.datetime.strptime(date, format_date)
            except Exception:
                flag = False
        else:
            flag = False
        if flag:
            input_date = datetime.datetime.strptime(date, format_date)
            if input_date <= date_now and input_date.year >= 2000:
                return input_date
            else:
                print(f"Введите корректную дату (01.01.2000 - "
                      f"{date_now.strftime(format_date)})")
                return self.get_date()
        print('Неверный формат даты')
        return self.get_date()

    def confirm_action(self) -> bool:
        action = input("Подтвердите действие (yes/no): ")
        if action == "yes":
            return True
        elif action == "no":
            return False
        print("Неверная команда")
        return self.confirm_action()
