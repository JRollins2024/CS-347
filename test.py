from proximity import *
from ADAS import *
from CruiseControl import *

######################################
# Proximity tests

# Test 1
car_bounds = (3, 5, 2, 3)
obstacles = [(6, 6, 2, 2)]
vectorProx = [car_bounds,obstacles]
obstr_data = get_car_obstructions(car_bounds, obstacles)
print(obstructions_to_str(obstr_data))

######################################
# Parking tests

# Test 1
speed = 5
car_bounds = (4, 2, 3, 2)
goal_bounds = (4, 7, 3, 2)
obstacles = [(1, 7, 3, 2), (7, 7, 3, 2)]
vectorPark1 = [speed,car_bounds,goal_bounds,obstacles]
path_data = is_parking_path_clear(vectorPark1)
print(f'Parking path is clear: {path_data}')

# Test 2
speed = 9
car_bounds = (4, 2, 3, 2)
goal_bounds = (4, 7, 3, 2)
obstacles = [(1, 7, 3, 2), (6, 7, 3, 2)]
vectorPark2 = [speed,car_bounds,goal_bounds,obstacles]
path_data = is_parking_path_clear(vectorPark2)
print(f'Parking path is clear: {path_data}')

# Test 3
speed = 5
car_bounds = (4, 2, 3, 2)
goal_bounds = (4, 7, 3, 2)
obstacles = [(1, 7, 3, 2), (1, 4, 3, 2)]
vectorPark3 = [speed,car_bounds,goal_bounds,obstacles]
path_data = is_parking_path_clear(vectorPark3)
print(f'Parking path is clear: {path_data}')

#Test 4
speed = 15
car_bounds = (4, 2, 3, 2)
goal_bounds = (4, 7, 3, 2)
obstacles = [(1, 7, 3, 2), (1, 4, 3, 2)]
vectorPark4 = [speed,car_bounds,goal_bounds,obstacles]
path_data = is_parking_path_clear(vectorPark4)
print(f'Parking path is clear: {path_data}')


############################################
#ADAS tests

#Test 1
car_on = True
car_bounds = (3, 5, 2, 3)
speed = 40
obstacles = [(6, 6, 2, 2)]
obstr_dataADAS1 = get_car_obstructions(car_bounds, obstacles)
vectorADAS1 = [car_on,speed,car_bounds,obstacles,obstr_data]
spd_dir_data = ADAS(vectorADAS1)
print(f'New speed and position are : {spd_dir_data}')

#Test 2
car_on = True
car_bounds = (3, 5, 2, 3)
speed = 40
obstacles = [(4, 7, 3, 2)]
obstr_data = get_car_obstructions(car_bounds, obstacles)
vectorADAS2 = [car_on,speed,car_bounds,obstacles,obstr_data]
spd_dir_data = ADAS(vectorADAS2)
print(f'New speed and position are : {spd_dir_data}')

############################################
# Network Test
network_list = ['PizzaPlex_Wifi', 'Exotic_Butters', 'FBI_Surveilance_Van', 'Peepaw_Aftons_WheelChair']
isConnected = True

############################################
#Cruise Control Tests
car_on = True
car_bounds = (4,2,3,2)
speed = 35
vectorCC1 = [car_on, car_bounds, speed]
cruise = CC(vectorCC1)
print(f'Set speed is {cruise}')
######################################
#Security test
car_bounds = (3, 5, 2, 3)
minutes = 6

if minutes == 5:
 SusFigure = [(6, 6, 2, 2)]
else:
 SusFigure = [(4, 7, 3, 2)]


rightCam=("https://forum-files-playcanvas-com.s3-eu-west-1."
        "amazonaws.com/original/1X/ba9948556abceac3646ef346bfb31750ea0ed604.png")

backCam = ("https://cdn.vox-cdn.com/thumbor/0Tc0bb6heYL9w8FHyv2h558uH2Q=/0x0:1280x720/1200x675/filters:focal"
           "(503x158:707x362)/cdn.vox-cdn.com/uploads/chorus_image/image/70677405/five_nights_movie.0.0.jpg")

sus_data = get_car_obstructions(car_bounds, SusFigure)


