class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} ({self.species})"


class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal} в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee} в зоопарк.")

    def list_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(animal)

    def list_employees(self):
        print("Сотрудники в зоопарке:")
        for employee in self.employees:
            print(employee)


# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавляем животных
    lion = Animal("Лева", "Лев")
    elephant = Animal("Малыш", "Слон")
    zoo.add_animal(lion)
    zoo.add_animal(elephant)

    # Добавляем сотрудников
    keeper = ZooKeeper("Иван")
    vet = Veterinarian("Ветеринар Петр")
    zoo.add_employee(keeper)
    zoo.add_employee(vet)

    # Список животных и сотрудников
    zoo.list_animals()
    zoo.list_employees()

    # Специфические методы
    keeper.feed_animal(lion)
    vet.heal_animal(elephant)