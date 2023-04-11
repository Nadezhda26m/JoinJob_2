from datetime import datetime


class Note:
    def __init__(self, title: str, text: str, date_time: datetime,
                 note_id: int, short_text: int = 10):
        self.title = title
        self.text = text
        self.date_time = date_time
        self.NOTE_ID = note_id
        self.short_text = short_text

    def __str__(self) -> str:
        return f'#{self.NOTE_ID:04} <{self.title}> {self.__get_date()}\n\t{self.text}'

    def __repr__(self):
        return f'#{self.NOTE_ID:04} <{self.title}> {self.__get_date()} ' \
               f'>>> {self.text[:self.short_text]}...'

    def __get_date(self):
        return self.date_time.strftime("%d.%m.%Y %H:%M")
