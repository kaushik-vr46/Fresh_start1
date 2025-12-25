'''
ENCAPSULATION IN PYTHON:
This example demonstrates data encapsulation using private attributes.
Private attributes are prefixed with double underscore (__) to prevent direct access.
Access and modification is controlled through getter and setter methods.

TASK: Create a Person class with:
- Two private attributes: __name (default "Geeks") and __age (default 10)
- Getter methods: get_name() and get_age()
- Setter methods: set_name(name) and set_age(age)
'''

class Person:
    def __init__(self):
        # Private attributes (prefixed with __) are not directly accessible
        self.__name = "Geeks"  # Default name
        self.__age = 10  # Default age

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        self.__age = age

'''
USAGE EXAMPLES:
p = Person()
print(p.get_name())  # Output: Geeks
print(p.get_age())   # Output: 10

p.set_name("John")
p.set_age(25)
print(p.get_name())  # Output: John
print(p.get_age())   # Output: 25

# Direct access fails:
# print(p.__name)  # ERROR: AttributeError (private attribute)
'''
