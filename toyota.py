class Toyota:
    
    brand = 'toyota'

    def __init__(self, color):
        self.color = color

rav4 = Toyota('black')
altis = Toyota('silver')

print(rav4.brand)
print(rav4.color)
Toyota.brand = 'Ford'
print(altis.brand)
rav4.brand = 'benz'
print(altis.brand)
