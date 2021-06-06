import datetime

from data import Anniversary


def decode_anniversary(data: dict) -> Anniversary:
    key = data['key']
    name = data['name']

    tmp_date = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
    date = datetime.date(tmp_date.year, tmp_date.month, tmp_date.day)
    return Anniversary(key=key, name=name, date=date)
