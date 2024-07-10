class Greet:
    def display(self):
        print("This is instance method")
        
    @classmethod
    def diplay_class(cls):
        print("This is class method")
        
    @staticmethod
    def display_static():
        print("This is static method")
        
_greet = Greet()
_greet.display()
Greet.diplay_class()
_greet.display_static()