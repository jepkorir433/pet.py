class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")
        
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play right now.")
            
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

# TEST CODE - THIS IS WHAT MAKES THINGS HAPPEN
if __name__ == "__main__":
    my_pet = Pet("Fluffy")
    
    print("Initial status:")
    my_pet.get_status()
    
    print("\nAfter eating:")
    my_pet.eat()
    my_pet.get_status()
    
    print("\nAfter playing:")
    my_pet.play()
    my_pet.get_status()
    
    print("\nAfter sleeping:")
    my_pet.sleep()
    my_pet.get_status()
    
    print("\nTry to play when tired:")
    for _ in range(4):
        my_pet.play()
    my_pet.get_status()