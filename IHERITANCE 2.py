class MobilePhone:
    def make_call(self):
        print("making call....")

def receive_call(self):
    print('receiving call....')

def take_a_picture(self):
    print("taking a picture")

class Apple(MobilePhone):
    def __init__(self,model,color):
        super().__init__()
        self.model = model
        self.color = color

class Samsung(MobilePhone):
    def __init__(self,model,battery_life):
        super().__init__()
        self.model = model
        self.battery_life = battery_life

apple_phone1 = Apple("iphone 12", "Black")
apple_phone2 = Apple("iphone XR", "White")

samsung_phone1 = Samsung("Galaxy S21", "12 hours battery life")
samsung_phone2 = Samsung("Galaxy A27", "16 hours battery life")
