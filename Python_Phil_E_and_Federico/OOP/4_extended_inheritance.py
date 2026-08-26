'''If the Daughter class has inherited her way of laughing from her father, and her vocation 
from her mother, and today they have the same job at the Prosecutor's Office, create multiple 
inheritance that allows this class to inherit correctly from Father and Mother.'''

class Mother:
    def vocation():
        print("Be a doctor!")

class Father:
    def laughing():
        print("hahaha")

class Daughter(Mother, Father):
    pass