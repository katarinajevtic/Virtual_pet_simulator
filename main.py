import random

#  Initializing a VirtualPet object with specified name and default attribute values.
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        self.hunger = max(0, self.hunger - random.randint(5, 15))
        # Increase happiness and health when pet is fed
        print(f"{self.name} has been fed. Hunger level: {self.hunger}, Energy level: {self.energy}")

    def play(self):
        self.energy = max(0, self.energy - random.randint(5, 15))
        self.happiness = min(100, self.happiness + random.randint(10, 20))
        print(f"{self.name} had a great time playing! Energy level: {self.energy}, Happiness level: {self.happiness}")

    def sleep(self):
        self.energy = min(100, self.energy + random.randint(10, 20))
        print(f"{self.name} had good sleep! Energy level: {self.energy}")

    # Printing the current status of the pet
    def status(self):
        print(
            f"Your pet {self.name}'s status is - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")


# Define the  magenta function
def magenta(*args):
    return "\033[35m" + " ".join(map(str, args)) + "\033[0m"


# Getting name of pet
pet_name = input("Name your virtual pet: ").upper()
pet = VirtualPet(pet_name)

# Interact with pet
print(magenta(f"Welcome to the Virtual Pet Game! Meet {pet.name}!"))
print()
while True:
    user_input = input(f"What would you like to do with {pet.name}? (feed/play/sleep/status/quit): ")
    if user_input == 'feed':
        pet.feed()
    elif user_input == 'play':
        pet.play()
    elif user_input == 'sleep':
        pet.sleep()
    elif user_input == 'status':
        pet.status()
    elif user_input == 'quit':
        print(f"Thank you for playing with your virtual pet! {pet.name} says Bye!")
        break
    else:
        print("Invalid input, please try again!")
