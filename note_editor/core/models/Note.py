from datetime import datetime


class Note:
    def __init__(self, title, text, date_time=datetime.now()):
        self.title = title
        self.text = text
        self.date_time = date_time

    def __get_date(self):
        return self.date_time.strftime("%d.%m.%Y %H:%M")

    def __str__(self) -> str:
        return f'<{self.title}> {self.__get_date()}\n\t{self.text}\n'


new_note = Note('Note 1', 'Text 1')
print(new_note)
new_note2 = Note('Note 2', 'Text 2')
print(new_note2)
