# Написать программу для управления списком контактов.
# В качестве примера добавьте в программу два обьекта Contact в список контактов
# Так же необходимо выполнять операции по удалению контакта и поиску контакте в списке
# (удаление и посик осуществляется пользователем)
# Результаты операий должны выводиться на экран.


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | Телефон: {self.phone} | Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Контакт '{contact.name}' добавлен")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Контакт '{name}' удалён")
                return
        print(f"Контакт с именем '{name}' не найден")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Контакт найден:")
                print(contact)
                return
        print(f"Контакт с именем '{name}' не найден")

    def show_contacts(self):
        print("\nВаш список контактов:")
        for contact in self.contacts:
            print(contact)
        if not self.contacts:
            print("Список контактов пуст. Добавьте первого контакта")


def main():
    manager = ContactManager()
    while True:
        print("\n-- Меню --")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Показать все контакты")
        print("5. Выйти из программы")

        choice = input("Выберите пункт меню (1-5): ")

        if choice == "1":
            name = input("Имя: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            manager.add_contact(Contact(name, phone, email))

        elif choice == "2":
            name = input("Введите имя для удаления: ")
            manager.remove_contact(name)

        elif choice == "3":
            name = input("Введите имя для поиска: ")
            manager.find_contact(name)

        elif choice == "4":
            manager.show_contacts()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор в меню. Введите число от 1 до 5")

main()