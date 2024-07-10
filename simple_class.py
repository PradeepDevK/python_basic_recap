class Laptop:
    def __init__(self, price, processor, ram):
        self.price = price
        self.processor = processor
        self.ram = ram
        
hp = Laptop(100, 'intel5', '2gb')
dell = Laptop(300, 'intel8', '8gb')
lenovo = Laptop(400, 'intel5', '4gb')
print(hp.price)