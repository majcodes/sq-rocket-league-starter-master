# Welcome to the Skillquest Python practice replit. You can use this to get starting points to practice your Python skills along with the lessons that Skillquest publishes.
# This is the main file, where we'll start.
print('running script')

car_speed = 10
car_steering = -1
car_throttle = True

class Car:
  def  __init__ (self, speed, steering, throttle):
    self.speed = speed
    self.steering = steering
    self.throttle = throttle

  def adjust_speed(self,adjustment):
    self.speed = self.speed + adjustment 
  
my_car = Car( 10, -1, True)
your_car = Car(50, 0, False)

print(my_car.speed, my_car.steering, my_car.throttle)
print(your_car.speed, your_car.steering, your_car.throttle)
print('---------------------------------------------------')

my_car.adjust_speed(60)
my_car.adjust_speed(-20)

print(my_car.speed, my_car.steering, my_car.throttle)
print(your_car.speed, your_car.steering, your_car.throttle)