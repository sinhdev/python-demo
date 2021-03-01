class Employee:
   'Common base class for all employees'
   emp_count = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.emp_count += 1
   
   def display_count(self):
     print("Total Employee %d" % Employee.emp_count)

   def display_employee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.display_employee()
emp2.display_employee()
print("Total Employee %d" % Employee.emp_count)

# Returns true if 'age' attribute exists
print("has age attribute:", hasattr(emp1, 'age'))
# Set attribute 'age' at 8
setattr(emp1, 'age', 8)
# Returns value of 'age' attribute
print("age: ", getattr(emp1, 'age'))
# Delete attribute 'age'
delattr(emp1, 'age')

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)