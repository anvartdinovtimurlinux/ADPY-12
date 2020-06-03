class PhoneBook:
    def __init__(self):
        self.contacts = dict()

    def add_contact(self, contact):
        lastname = contact.lastname
        if lastname in self.contacts:
            self.contacts[lastname].update_contact(contact)
        else:
            self.contacts[lastname] = contact

    def get_contacts_list(self):
        return [str(contact).split(',') for contact in self.contacts.values()]
