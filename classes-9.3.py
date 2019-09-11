## Exercise 9.3 Users

## Making a class called User

class User():
    """Making the attruibutes"""
    def __init__(self,
                 first_name,
                 last_name,
                 age,
                 eid
                 ,):
        self.first = first_name
        self.last = last_name
        self.id = eid
        self.age = age

    def describe_user(self):
        """Printing the summary of the user"""
        print("==========User Profile: " + str(self.id) + "==========")
        print("First name : " + self.first.title())
        print("Last name : " + self.last.title())
        print("Employee age: " + str(self.age))
        print("Employee ID: " + str(self.id))

    def greet_user(self):
        """Printing the greeting for the user"""
        print("\n=============Welcome Mr./Ms. " + self.first.title() + "===================")
        print("Welcome to this simulation")
        print("You are player" + str(self.id))


user_1 = User('Darryl','Prabhu',23,1096362)


user_1.describe_user()

user_1.greet_user()
