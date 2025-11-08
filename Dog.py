class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name, "was Born")

    def speak(self):
        print("YELP!", self.name)

    def wag(self):
        print("Dog's wag tail")

    def __del__(self):
        print("destroy!!")

# puddle = Dog("puddle")
# sheperd = Dog("sheperd")

# puddle.speak()
# sheperd.speak()

# 다음은 상속(inheritance)
class Puppy(Dog):
    def __init__(self):
        self.name = "Puppy"
        print("QQQQ> Puppy was Born")

    def speak(self):
        print("Bow wow!", self.name)

    def wag(self):
        print("Puppy's wag tail")

d = Dog("puddle")
p = Puppy()
d.speak()
p.speak()
