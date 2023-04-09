from JoinJob2NoteEditor.note_editor.core.mvp.View import View


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

    def show_full_note(self, full_note: str):
        print(full_note)

    def show_short_note(self, short_note: str):
        self.show_full_note(short_note)

    def get_index_note(self, max_index: int) -> int:
        index = input("Введите номер заметки: ")
        if index.isdigit() and 0 < int(index) <= max_index:
            return int(index) - 1
        else:
            print(f"Введите число от 1 до {max_index} включительно")
            return self.get_index_note(max_index)

    def show_commands(self, commands: list[str]):
        print("Список доступных команд: ", end="")
        print(', '.join(commands))

    def show_parameters(self, parameters: list[str]):
        for i in range(len(parameters)):
            print(f'{i + 1}. {parameters[i]}')

    def get_index_command(self, commands: list[str]) -> int:
        command = input("Введите команду: ")
        if command in commands:
            return commands.index(command)
        else:
            print(f"Неверная команда")
            return self.get_index_command(commands)

    def get_parameter_to_change(self, parameters: list[str]) -> int:
        index = input("Выберите параметр для изменения. Введите число: ")
        if index.isdigit() and 0 < int(index) <= len(parameters):
            return int(index) - 1
        else:
            print(f"Введите число от 1 до {len(parameters)} включительно")
            return self.get_parameter_to_change(parameters)
