from collections import UserDict
import datetime
import requests

class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone

    def __str__(self):
        output = f"Name: {self.name.value}\n"
        for phone in self.phones:
            output += f"Phone: {phone.value}\n"
        output += "---------\n"
        return output


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name.value]

    def edit_record(self, name, new_record):
        self.data[name.value] = new_record

    def search_records(self, query):
        search_results = AddressBook()
        for record in self.data.values():
            if query.lower() in record.name.value.lower():
                search_results.add_record(record)
        return search_results


API_KEY = "653c3ccd328356a16a58c6dbd440c093"


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter both name and phone"
        
    return inner


contacts = AddressBook()


@input_error
def add_contact(name, phone):
    if name.value in contacts:
        record = contacts[name.value]
    else:
        record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added successfully"


@input_error
def change_contact(name, old_phone, new_phone):
    if name.value in contacts:
        record = contacts[name.value]
        record.edit_phone(old_phone, new_phone)
        return "Contact updated successfully"
    else:
        return "Contact not found"


@input_error
def get_phone(name):
    if name.value in contacts:
        record = contacts[name.value]
        return record.phones
    else:
        return "Contact not found"


def show_all_contacts():
    if contacts:
        output = ""
        for record in contacts.values():
            output += str(record)
        return output
    else:
        return "No contacts found"


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"The current weather in {city} is {weather_description}. Temperature: {temperature}°C"
    else:
        return "Failed to retrieve weather information"


def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return f"The current time is {current_time}"


def help_commands():
    return """
    Available commands:
    - hello: Greet the assistant
    - add <name> <phone>: Add a contact with the given name and phone number
    - change <name> <old_phone> <new_phone>: Change the phone number of an existing contact
    - phone <name>: Get the phone number(s) of a contact
    - show all: Show all saved contacts
    - weather <city>: Get the current weather in the specified city
    - time: Get the current time
    - help: Show available commands
    - goodbye, close, exit: Close the assistant
    """


def main():
    print("Welcome to the Assistant! How can I help you?")
    while True:
        user_input = input("Enter a command: ").lower().split(" ")
        command = user_input[0]
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            name = Name(user_input[1])
            phone = Phone(user_input[2])
            print(add_contact(name, phone))
        elif command == "change":
            name = Name(user_input[1])
            old_phone = Phone(user_input[2])
            new_phone = Phone(user_input[3])
            print(change_contact(name, old_phone, new_phone))
        elif command == "phone":
            name = Name(user_input[1])
            print(get_phone(name))
        elif command == "show" and user_input[1] == "all":
            print(show_all_contacts())
        elif command == "weather":
            city = " ".join(user_input[1:])
            print(get_weather(city))
        elif command == "time":
            print(get_current_time())
        elif command == "help":
            print(help_commands())
        elif command in ["goodbye", "close", "exit", "bye"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Type 'help' to see the available commands.")


if __name__ == "__main__":
    main()
