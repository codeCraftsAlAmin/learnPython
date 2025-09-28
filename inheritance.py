class Phone: # parent class

    def __init__(self,call,message):
        self.call = call
        self.message = message

    def info(self): 
        print(f"{self.call}, {self.message}")


class Samsung(Phone): # child class

    def __init__(self, call, message, photo):
        super().__init__(call, message)
        self.photo = photo

    def info(self):
        print(f"{self.call}, {self.message}, {self.photo}")


# p = Phone()
s = Samsung("You can call", "You can message", "You can take photo")
s.info()