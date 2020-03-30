import time
from time import time as tm
import random
import datetime
import pytz

print(time.gmtime(0))

print(time.localtime())

print(time.time())

timex = time.localtime()

print("year: ",timex.tm_year)

print("month: ",timex.tm_mon)

print("date: ",timex.tm_mday)
print('-' * 50)
input("press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = tm()

input("press enter to stop")
end_time = tm()

print("Started at " + time.strftime("%x",time.localtime(start_time)))
print("Ended at " + time.strftime("%x",time.localtime(end_time)))
print("Reaction time is: {} " .format(end_time - start_time))
print('-'*50)

print("time:   ", time.get_clock_info('time'))
print("monotonic:   ", time.get_clock_info('monotonic'))
print("perf_counter:   ", time.get_clock_info('perf_counter'))
print("process_time:   ", time.get_clock_info('process_time'))

print('-'*50)

print("The time on this system starts at: " + time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0} with an offset of {1} " .format(time.tzname[0], time.timezone))

if time.daylight ==0: # you can change it not equal to zero according to your timezone
    print("The DST timezone is: "+ time.tzname[1])

print("Local time is "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is "+ time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print('-'*50)

print(datetime.datetime.now())
print(datetime.datetime.today())
print(datetime.datetime.utcnow())

print('-'*50)

country = 'Asia/Kolkata'
t_z = pytz.timezone(country)
local_time = datetime.datetime.now(tz = t_z)
print("time at {} is {} " .format(country,local_time))
print("UTC is {} " .format(datetime.datetime.utcnow()))

for i in pytz.all_timezones:
    print(i)

for i in sorted(pytz.country_names):
    print("{}   ,    {}".format(pytz.country_names[i],pytz.country_timezones.get(i)))

print("-"*50)
# using localize function
print(datetime.datetime.now())
print(pytz.utc.localize(datetime.datetime.now()))






