class Dog:
    approved_breeds = ["Corgi", "Poodle", "Pug"]

    def __init__(self, name, breed):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            raise ValueError("Name must be a string between 1 and 25 characters.")
        if not isinstance(breed, str) or breed not in self.approved_breeds:
            raise ValueError("Breed must be in list of approved breeds.")
        
        self.name = name
        self.breed = breed

# Example usage:
try:
    my_dog = Dog("Fido", "Corgi")
    print(my_dog)
except ValueError as e:
    print(e)
