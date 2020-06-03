import re


class Contact:
    def __init__(self, contact_info):
        self.lastname, \
        self.firstname, \
        self.patronymic, \
        self.job, \
        self.position, \
        self.phone, \
        self.email = contact_info

        self.lastname, self.firstname, self.patronymic = self.get_normalize_name()
        self.phone = self.get_normalize_phone()

    def get_normalize_name(self):
        full_name = f'{self.lastname} {self.firstname} {self.patronymic}'
        result = re.findall(r'\w+', full_name)
        if len(result) == 3:
            return result[0], result[1], result[2]
        elif len(result) == 2:
            return result[0], result[1], ''
        else:
            return result[0], '', ''

    def get_normalize_phone(self):
        result = re.sub(
            r'^\s*(8|\+7)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})',
            r'+7(\2)\3-\4-\5',
            self.phone
        )
        result = re.sub(
            r'\s*\(?(доб\.)\s(\d+)\)?',
            r' доб.\2',
            result
        )
        return result

    def update_contact(self, new_contact):
        self.lastname = self.lastname or new_contact.lastname
        self.firstname = self.firstname or new_contact.firstname
        self.patronymic = self.patronymic or new_contact.patronymic
        self.job = self.job or new_contact.job
        self.position = self.position or new_contact.position
        self.phone = self.phone or new_contact.phone
        self.email = self.email or new_contact.email

    def __repr__(self):
        return f'Contact(["{self.lastname}",' \
               f'"{self.firstname}", ' \
               f'"{self.patronymic}", ' \
               f'"{self.job}", ' \
               f'"{self.position}", ' \
               f'"{self.phone}", ' \
               f'"{self.email}"])'

    def __str__(self):
        return f'{self.lastname},' \
               f'{self.firstname},' \
               f'{self.patronymic},' \
               f'{self.job},' \
               f'{self.position},' \
               f'{self.phone},' \
               f'{self.email}'
