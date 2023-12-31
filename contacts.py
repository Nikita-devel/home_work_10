class Name:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value).capitalize()


class Phone:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(str(name).capitalize())
        self.phones = []
        if phone is not None:
            self.phones.append(Phone(phone))

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Phone number not found")

    def __str__(self):
        output = f"Name: {self.name.value}\n"
        for phone in self.phones:
            output += f"Phone: {phone.value}\n"
        output += "---------\n"
        return output


class AddressBook(dict):
    def add_record(self, record):
        self[record.name.value] = record

    def delete_record(self, name):
        del self[name.value]

    def edit_record(self, name, new_record):
        self[name.value] = new_record

    def search_records(self, query):
        search_results = AddressBook()
        for record in self.values():
            if query.lower() in record.name.value.lower():
                search_results.add_record(record)
        return search_results
