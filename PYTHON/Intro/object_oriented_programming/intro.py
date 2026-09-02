"""
Object oriented programming.
<JS, Python, C++, JAVA, etc>

Concept in programming to make
work easy. by using principles.
1. Encapsulation
   - keeping data and methods<functions> inside a class
     while restricting direct access to internal data.
2. Abstraction
   - Hiding uncessary complexity or implrtation of details.
3. Inheritance
   - one class to reuse or extend propertie
     and methods of another class
4. Polymorphisim
   - appering in different forms. Method can
     have different behaviours.
-----------------------------------
JS and python are object oriented.
-> number.toString(), string.toLowerCase()
"""

"""
-> Class ->
  - blueprint for an object.

-> Class could an architectural drawing of a house.
   object -> implentaiton of the drawing.
"""

# is to have the name Capitalized
# fields <properties>
class House:
    bedrooms = 3
    bathrooms = 2
    floors = 1
    area = 120
    owner = ""
    location = ""
    architect = "KIMANI"


    #js constructor
    def __init__(self,owner,location):
        print("Class house created. initializer called")
        self.owner=owner
        self.location=location
      

    def config(self, owner, location):
        self.owner = owner
        self.location = location

    def print_self(self):
        # this <the object itself>: self<object>
        print(self)
        print(self.__dict__) # dictionary <print all properties>


# When access object properties use dot notation
# Bracket notation is for dictionary

#-> method config ->
#-> print self
#Instance class-> create an object from a class
macrine_house=House(owner="Macrine",location="Kikuyu")
# macrine_house.__init__()
# macrine_house.owner="Macrine"
# macrine_house.location="Kikuyu"
# macrine_house.config(owner="Macrine",location="Kikuyu")
print(f"Macrines House Owner {macrine_house.owner}")
print(f"Macrines Location {macrine_house.location}")
print(f"Macrines House Bedrooms {macrine_house.bedrooms}")
print(f"Macrines House Bedrooms {macrine_house.bathrooms}")
print(f"Macrines House Bedrooms {macrine_house.floors}")
print(f"Macrines House Bedrooms {macrine_house.area}")
print(f"Macrines House Designer {macrine_house.architect}")
print("Printing macrines house")
macrine_house.print_self()
print("End of print macrines")


daniel_house=House(owner='Daniel',location="Muranga")# __init__()
# daniel_house.owner='Daniel'
# daniel_house.location="Muranga"
# daniel_house.config(owner="Daniel",location="Muranga")
print(f"Daniels House Owner {daniel_house.owner}")
print(f"Daniels Location {daniel_house.location}")
print(f"Daniels House Bedrooms {daniel_house.bedrooms}")
print(f"Daniels House Bathroom {daniel_house.bathrooms}")
print(f"Daniels House Floors {daniel_house.floors}")
print(f"Daniels House area {daniel_house.area}")
print(f"Daniels House Designer {daniel_house.architect}")
print("Printing daniels house")
daniel_house.print_self()
print("End of print macrines")