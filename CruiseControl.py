


#keeps car at constant speed, does no accelerate or deccerlate over time
def CC(v):
    car_on = v[0] #is the car on
    car_bounds = v[1] #where is the car
    speed = v[2] #Car's speed
    if(car_on == False):
        logfile.write("["+datetime.now().strftime("%H:%M:%S")+ "] Cruise Control Failed to turn on. \n")
        logfile.close()
        return "Car must be on"
    else:
        return speed
