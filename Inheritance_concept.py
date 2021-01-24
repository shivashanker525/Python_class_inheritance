"""
About Evolution of Tesla car company from petrol engines to
electric and adoption of newer technologies.

In this firstly the parent company is stick to some
basic principles and concepts whichever defines company's
unique motto.
"""


class Tesla():
    '''
    Tesla is a parent company,this follows some basic principles
    That are designed here in this class Tesla.
    So whenver we design new/child cars we have
    to inherit all this basic principles.
    '''

    def __init__(self):
        print("I'm a Tesla the innovation")

    def Design(self):
        print("Tesla follows unique design of a car " +
              "when compared to all other companies")

    def Raw_Material(self):
        print("Tesla uses variety of metals to build a car")

    def Security(self):
        print("Tesla gives higher priority for security in all the products")

    def Safety(self):
        print("Tesla always introduces newest ways" +
              " to make their cars more safe")


class New_Telsa_Electric(Tesla):
    '''
    Here we can add-on some new features or innovations in parent features
    It will give you the updated version of the parent.
    '''

    Price_In_Lakhs = 85

    def __init__(self, model_name, model_number):
        self.model_name = model_name
        self.model_number = model_number
        print("I'm a child/new class/car")
        super().__init__()

    def Airbag_Technology(self):
        print("In this model introduced modern Air_bag Technology")

    def Electric_battery_technology(self):
        print("There is a new innovation in " +
              "engine system,electric batteries are introduced")

    def Disc_Fluid_Braking_System(self):
        print("A new innovation in brake system technology")

    '''
    we added some new features to our new model New_Telsa_Electric class/car
    '''


class New_Tesla_Automatic(Tesla):
    '''
    Here we can add-on some new features or innovations in parent features
    It will give you the updated version of the parent.
    '''

    Price_In_Lakhs = 85

    def __init__(self, model_name, model_number):
        self.model_name = model_name
        self.model_number = model_number
        print("I'm a child/new Tesla_Automatic class/car")
        super().__init__()

    def Self_Driving_Technology(self):
        print("Advanced technology is added to this model " +
              "self-driving technology is drastical change")

    def Airbag_Technology(self):
        print("In this model introduced modern Air_bag Technology")

    def Disc_Fluid_Braking_System(self):
        print("A new innovation in brake system technology")

    def Horse_Power(self):
        print("We updated the horse power of an engine in this model")

    '''
    we added some new features to our new model New_Tesla_Automatic class/car
    '''


class New_Tesla_Sel_Driving_Cum_Electric(New_Telsa_Electric, New_Tesla_Automatic):
    '''
    This model/class inherits properties from both the parent classes/models
    '''

    Price_In_Lakhs = 123

    def __init__(self, model_name, model_number):
        self.model_name = model_name
        self.model_number = model_number
        print("I'm a hybrid model of Tesla_Automatic and Telsa_Electric")

    def Sensor_Technology(self):
        print("A new innovation in car technology")

    '''
    This model/class also consists of some add-on features.
    ****
    In this class MRO concept is covered as both parent classes
    consists of some similar featues/methods
    '''


'''
Declaring classes and defining new objects from the classes
Checking the inheritance and MRO in defined classes.
'''

# above we called all methods and attributes related to
# parent/Tesla class we canot access child classes
# We created an object of a parent class
parent = Tesla()
parent.Design()
parent.Raw_Material()
parent.Security()
parent.Safety()

# Here inheritance comes into picture
# Here we called all methods from parent and it's own class
# we defined an object of a New_Telsa_Electric class
child_1 = New_Telsa_Electric('Tesla_Bizord', 5269)
print(child_1.model_name)
print(child_1.model_number)
print(child_1.Price_In_Lakhs)
child_1.Airbag_Technology()
child_1.Design()
child_1.Disc_Fluid_Braking_System()
child_1.Electric_battery_technology()
child_1.Raw_Material()
child_1.Safety()
child_1.Security()

# Here we called all methods from parent and it's own class
# we defined an object of a New_Tesla_Automatic class
child_2 = New_Tesla_Automatic('Tesla_Radar', 5285)
print(child_2.model_name)
print(child_2.model_number)
print(child_2.Price_In_Lakhs)
child_2.Self_Driving_Technology()
child_2.Airbag_Technology()
child_2.Design()
child_2.Disc_Fluid_Braking_System()
child_2.Raw_Material()
child_2.Safety()
child_2.Security()

'''
 Here we are getting into multiple inheritance
 we will also see MRO concept here
'''

Grand_child = New_Tesla_Sel_Driving_Cum_Electric('Tesla_Fizor', 8569)

# We can access all methods and attributes from both parent classes

print(Grand_child.model_name, Grand_child.model_number)
# Here we are calling the method which is present in both parent classes
# So MRO concept was implemented here.
Grand_child.Airbag_Technology()
Grand_child.Disc_Fluid_Braking_System()
Grand_child.Design()
Grand_child.Self_Driving_Technology()
Grand_child.Electric_battery_technology()