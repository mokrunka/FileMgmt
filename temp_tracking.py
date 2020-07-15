import time

# a little function to grab the pi's temperature from the file where it's tracked
filename = r'/sys/class/thermal/thermal_zone0/temp'

with open(filename, 'r') as f:
        for line in f:
                temperature = line

# the temperature is listed in degrees C * 1000, so we'll make it human readable
temperature = int(temperature)
temperature = temperature / 1000

log_filename = r'/home/mokrunka/Documents/temperature_log'

# generate a timestamp to add to each line
time_stamp = time.localtime()
current_time = time.strftime('%x %X', time_stamp)

# open/create the logfile and append the current temp and time
# note that this is going to run on a cronjob every 4 hours
with open(log_filename, 'a') as l:
        l.write(f'{temperature}, {current_time}\n')