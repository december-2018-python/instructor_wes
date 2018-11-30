class Animal:
  def __init__(self, name, num_legs):
    self.name = name
    self.num_legs = num_legs
    self.health = 100
  
  def say_hello(self):
    print(f'Hello, my name is {self.name}')

  def exist(self):
    # self.health = self.health - 1
    self.health -= 1
    return self
  
  def display_health(self):
    print(self.health)
    return self
  
  def sleep(self):
    self.health += 1
    return self

class Dog(Animal):
  def __init__(self, name, num_legs):
    super().__init__(name, num_legs)
    self.health = 200
    self.is_goodboy = True

  def bark(self):
    super().say_hello()
    print(f"woof woof")
    return self
  
  def sleep(self):
    self.health += 3
    return self

fuzzy = Dog("Fuzzy", 4)
spike = Animal("Spike", 3)
spike.sleep().display_health()
fuzzy.sleep().display_health().bark()

# my_list = [1, 2, 3, 4]
# print(my_list.pop())
# print(my_list)