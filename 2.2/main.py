import csv
from Contact import Contact
from PhoneBook import PhoneBook


def get_contacts(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        return list(rows)


def write_contacts(path_to_file, contacts_list):
    with open(path_to_file, 'w', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


def main():
    raw_contacts_list = get_contacts('phonebook_raw.csv')

    my_phone_book = PhoneBook()
    for raw_contact in raw_contacts_list:
        contact = Contact(raw_contact[:7])
        my_phone_book.add_contact(contact)

    contacts_list = my_phone_book.get_contacts_list()
    write_contacts('phonebook.csv', contacts_list)


if __name__ == '__main__':
    main()
