Address Book Assistant
This is a simple command-line address book assistant implemented in Python. It allows users to manage contacts, get weather information, and check the current time.

Features
Add a contact with a name and phone number.
Update the phone number of an existing contact.
Retrieve the phone number(s) of a contact.
Show all saved contacts.
Get the current weather in a specified city.
Get the current time.
Installation
Clone the repository:

git clone <repository-url>
Change to the project directory:

cd address-book-assistant
Create a virtual environment:

python3 -m venv venv
Activate the virtual environment:

For Linux and macOS:

source venv/bin/activate
For Windows:

venv\Scripts\activate
Install the required packages:

pip install -r requirements.txt
Usage
To start the address book assistant, run the following command:

python main.py
The assistant will greet you and prompt you to enter a command. You can use the following commands:

hello: Greet the assistant.
add <name> <phone>: Add a contact with the given name and phone number.
change <name> <old_phone> <new_phone>: Change the phone number of an existing contact.
phone <name>: Get the phone number(s) of a contact.
show all: Show all saved contacts.
weather <city>: Get the current weather in the specified city.
time: Get the current time.
help: Show available commands.
goodbye, close, exit, bye: Close the assistant.
API Key
The assistant uses the OpenWeatherMap API to retrieve weather information. To use the weather feature, you need to provide an API key in the main.py file. Replace <YOUR_API_KEY> with your actual API key:

API_KEY = "<YOUR_API_KEY>"
You can obtain an API key by signing up at OpenWeatherMap and generating an API key.