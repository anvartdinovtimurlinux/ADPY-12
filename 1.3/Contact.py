class Contact:
    def __init__(self, name, surname, phone_number, is_favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.is_favorite = is_favorite
        self.extra_info = kwargs

    def __str__(self):
        contact_list = [
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Телефон: {self.phone_number}',
            f'В избранных: {"да" if self.is_favorite else "нет"}',
            'Дополнительная информация:',
        ]
        for key, value in self.extra_info.items():
            contact_list.append(f'\t{key}: {value}')
        return '\n'.join(contact_list)
