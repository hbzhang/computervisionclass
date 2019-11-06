#import datetime
from datetime import datetime
import time
time1 = datetime.now()
time2 = datetime.now()
timed = time2- time1

print(timed.microseconds)

'''

start = time.time()
end = time.time()

print(start-end)

'''
