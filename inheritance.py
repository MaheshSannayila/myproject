#single inheritance
# class Bike():
#     def __init__(self,wheels,gears,mileage,speed):
#         self.wheels=wheels
#         self.gears=gears
#         self.mileage=mileage
#         self.speed=speed
#     def display_properties(self):
#         print(self.wheels)
#         print(self.gears)
#         print(self.mileage)
#         print(self.speed)
# class Car(Bike):
#     def car_products(self,seats):
#         self.seats=seats
#         self.tyres=tyres
#     def display_car_properties(self):
#         self.display_properties()
#         print(self.tyres)
#         print(self.seats)

# c=Car("4wheels","4gears","60/L","120/h")
# c.car_products("4seats")
# c.display_car_properties()


# #multilevel inheritance
# class Bike():
#     def __init__(self,wheels,gears,mileage,speed):
#         self.wheels=wheels
#         self.gears=gears
#         self.mileage=mileage
#         self.speed=speed
#     def display_properties(self):
#         print(self.wheels)
#         print(self.gears)
#         print(self.mileage)
#         print(self.speed)
# class truck(Bike):
#     def truck_products(self,truck_size):
#         self.truck_size=truck_size
#     def display_truck_properties(self):
#         self.display_properties()
#         print(self.truck_size)
# class lorry(truck):
#     def display_lorry_properties(self):
#         self.display_truck_properties()
#         self.display_properties()
# l=lorry("4 wheels","4 gears","30km/L","60km/h")
# l.truck_products("largesize")
# l.display_lorry_properties()

# #multiple inheritance
# class Bike():
#     def __init__(self,wheels,gears,mileage,speed):
#         self.wheels=wheels
#         self.gears=gears
#         self.mileage=mileage
#         self.speed=speed
#     def display_properties(self):
#         print(self.wheels)
#         print(self.gears)
#         print(self.mileage)
#         print(self.speed)
# class truck():
#     def truck_products(self,truck_size):
#         self.truck_size=truck_size
#     def display_truck_properties(self):
#         print(self.truck_size)
# class lorry(Bike,truck):
#     def display_lorry_properties(self):
#         self.display_properties()
#         self.display_truck_properties()
# l=lorry("4 wheels","4 gears","30km/L","60km/h")
# l.truck_products("largesize")
# l.display_lorry_properties()



# #hyrarchical inheritance
# class Bike():
#     def __init__(self,wheels,gears,mileage,speed):
#         self.wheels=wheels
#         self.gears=gears
#         self.mileage=mileage
#         self.speed=speed
#     def display_properties(self):
#         print(self.wheels)
#         print(self.gears)
#         print(self.mileage)
#         print(self.speed)
# class truck(Bike):
#     def truck_products(self,truck_size):
#         self.truck_size=truck_size
#     def display_truck_properties(self):
#         self.display_properties()
#         print(self.truck_size)
# class lorry(Bike):
#     def display_lorry_properties(self,size):
#         self.size=size
#         print(size)
#         self.display_properties()
    
# l=lorry("4 wheels","4 gears","30km/L","60km/h")
# l.display_lorry_properties("laurge size")

# print(" ")
# t=truck("4 wheels","4 gears","30km/L","60km/h")
# t.truck_products("minisize")
# t.display_truck_properties()