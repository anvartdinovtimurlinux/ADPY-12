import csv
import re
import pymongo
import datetime


def read_data(csv_file, db):
    with open(csv_file, encoding='utf8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            day, month = map(int, line['Дата'].split('.'))
            event = {'artist': line['Исполнитель'],
                     'price': int(line['Цена']),
                     'place': line['Место'],
                     'date': datetime.datetime(year=2020, month=month, day=day),
                     }
            db.event.insert_one(event)


def find_cheapest(db):
    events_sorted_price = db.event.find().sort('price')
    return [(event['artist'], f"{event['price']}\u20BD", event['place'], str(event['date']))
            for event in events_sorted_price]


def find_by_name(name, db):
    regex = re.compile(f'.*{name}.*', re.IGNORECASE)
    events_search_name = db.event.find({'artist': regex}).sort('price')
    return [(event['artist'], f"{event['price']}\u20BD", event['place'], str(event['date']))
            for event in events_search_name]


def find_earlist(db):
    events_sorted_date = db['event'].find().sort('date')
    return [(event['artist'], f"{event['price']}\u20BD", event['place'], str(event['date']))
            for event in events_sorted_date]


if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client['netology']

    read_data('artists.csv', db)

    print('Сортировка по возрастанию цены:')
    print(*find_cheapest(db), sep='\n')

    print('\nПоиск по части имени:')
    part_name = 'th'
    print(f'поиск по {part_name}:')
    print(*find_by_name(part_name, db), sep='\n')

    print('\nСортировка по дате')
    print(*find_earlist(db), sep='\n')
    client.close()
