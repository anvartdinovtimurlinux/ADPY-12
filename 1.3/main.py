from Contact import Contact
from PhoneBook import PhoneBook


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    glen = Contact('Glen', 'Mayer', '+73454364644', address='Не дом и не улица')
    bill = Contact('Bill', 'Murrey', '+73216547809', is_favorite=True, telegram='@billyyyy', skype='billy@krasavcheg.com')

    my_book = PhoneBook('Черный список людей, которым я не собираюсь звонить')
    my_book.show_all()

    my_book.add(jhon)
    my_book.add(glen)
    my_book.show_all()

    my_book.show_favorite()
    my_book.add(bill)
    my_book.show_favorite()

    my_buddy = my_book.get_contact('Мой старый приятель', 'Забыл, блин, как его там')
    print(my_buddy)  # None
    my_enemy = my_book.get_contact('Bill', 'Murrey')
    print(my_enemy)
