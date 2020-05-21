class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts_list = []
        print(f'Телефонная книга "{self.name}" создана')

    def show_all(self):
        if self.contacts_list:
            print(f'Телефонная книга {self.name}:')
            for i, contact in enumerate(self.contacts_list, 1):
                print(f'{i}) {contact}\n')
        else:
            print(f'Телефонная книга "{self.name}" пуста')

    def show_favorite(self):
        favorite_list = [contact for contact in self.contacts_list if contact.is_favorite]
        if favorite_list:
            print(f'Список избранных контактов в телефонной книге {self.name}:')
            for i, contact in enumerate(favorite_list, 1):
                print(f'{i}) {contact}\n')
        else:
            print(f'В телефонной книге "{self.name}" нет избранных контактов')

    def add(self, contact):
        if contact in self.contacts_list:
            print('Этот контакт уже есть в телефонной книге')
        else:
            self.contacts_list.append(contact)
            print(f'{contact.name} {contact.surname} успешно добавлен')

    def delete(self, phone_number):
        for contact in self.contacts_list:
            if contact.phone_number == phone_number:
                print(f'{contact.name} {contact.surname} успешно удален')
                self.contacts_list.remove(contact)
        else:
            print(f'{phone_number} отсутствует в телефонной книге')

    def get_contact(self, name, surname):
        if self.contacts_list:
            for contact in self.contacts_list:
                if contact.name == name and contact.surname == surname:
                    return contact
            else:
                print(f'{name} {surname} отсутствует в телефонной книге')
        else:
            print(f'Телефонная книга "{self.name}" пуста')
