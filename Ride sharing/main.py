from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Rider,Driver
from vehicle import Car,Bike

niye_jao = RideSharing("Niye Jao")

rahim = Rider("Rahim","rahim@gmail.com",1234,"Banasree", 1200)
niye_jao.add_rider(rahim)
karim = Driver("Karim","karim@gmail.com",5678,"Gulshan")
niye_jao.add_driver(karim)
rahim.request_ride(niye_jao,"Uttara","car")
karim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
#print(niye_jao)