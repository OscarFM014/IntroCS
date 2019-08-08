# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(size, units, bandwidth, bunits):
    if units == "kb":
        size = (size * 2 ** 10 )
    elif units == "kB":
        size = (size * 2 ** 10 * 8)
    elif units == "Mb":
        size = (size * 2 ** 20)
    elif units == "MB":
        size = (size * 2 ** 20 * 8)
    elif units == "Gb":
        size = (size * 2 ** 30)
    elif units == "GB":
        size = (size * 2 ** 30 * 8)
    elif units == "Tb":
        size = (size * 2 ** 40)
    elif units == "TB":
        size = (size * 2 ** 40 * 8)

    if bunits == "kb":
        bandwidth = (bandwidth * 2 ** 10 )
    elif bunits == "kB":
        bandwidth = (bandwidth * 2 ** 10 * 8)
    elif bunits == "Mb":
        bandwidth = (bandwidth * 2 ** 20)
    elif bunits == "MB":
        bandwidth = (bandwidth * 2 ** 20 * 8)
    elif bunits == "Gb":
        bandwidth = (bandwidth * 2 ** 30)
    elif bunits == "GB":
        bandwidth = (bandwidth * 2 ** 30 * 8)
    elif bunits == "Tb":
        bandwidth = (bandwidth * 2 ** 40)
    elif bunits == "TB":
        bandwidth = (bandwidth * 2 ** 40 * 8)


    seconds = size / bandwidth

    



    segundos = seconds % 60
    minutes = int(seconds - segundos) / 60 % 60
    hour = int(seconds / 60 / 60)

    if hour == 1:
        if minutes == 1: 
            if segundos == 1:
                return str(hour) + " hour, " + str(minutes) + " minute, " + str(segundos) +" second"
            else:
                return str(hour) + " hour, " + str(minutes) + " minute, " + str(segundos) +" seconds"
        elif seconds == 1:
            return str(hour) + " hour, " + str(minutes) + " minutes, " + str(segundos) +" second"
        else:
            return str(hour) + " hour, " + str(minutes) + " minutes, " + str(segundos) +" seconds"
    elif minutes == 1: 
        if segundos == 1:
            return str(hour) + " hours, " + str(minutes) + " minute, " + str(segundos) +" second"
        else:
            return str(hour) + " hours, " + str(minutes) + " minute, " + str(segundos) +" seconds"
    elif segundos == 1:
        return str(hour) + " hours, " + str(minutes) + " minutes, " + str(segundos) +" second"
    else:
        return str(hour) + " hours, " + str(minutes) + " minutes, " + str(segundos) +" seconds"



    






print (download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print (download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print (download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print (download_time(11,'GB', 5, 'MB'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print (download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print (download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


