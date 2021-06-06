import datetime


class Anniversary(dict):
    key: str
    name: str
    date: datetime.date

    def __init__(self, json: dict):
        super().__init__()
        self.key = json['key']
        self.name = json['name']

        tmp_date = datetime.datetime.strptime(json['date'], '%Y-%m-%d')
        self.date = datetime.date(tmp_date.year, tmp_date.month, tmp_date.day)
