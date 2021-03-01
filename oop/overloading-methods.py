# define parent class
class Parent:
   def __init__(self):
       print('no param')
   def __init__(self, att1):
       print('1 param')
   def my_method(self):
      print('Calling parent method')

# define child class
class Child(Parent):
   def my_method(self):
      print('Calling child method')

c = Child("Child")    # instance of child
c.my_method()         # child calls overridden method

p1 = Parent("attribute")