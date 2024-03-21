import datetime
import time

go = True 

while(go):
    timeRightNow = datetime.datetime.now()
    specific = timeRightNow.second
    if (specific > 10):
        print (specific)

    time.sleep(2)

