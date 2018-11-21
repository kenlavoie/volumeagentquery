from datetime import timedelta
import time, datetime 
import schedule
import first1000out as f1000 
import second1000out as f2000
import third1000out as f3000 
import fourth1000out as f4000
import fifth1000out as f5000


curdates = datetime.datetime.now()
enddates = curdates + datetime.timedelta(days=1000)


def immediatestart():
    while curdates != enddates:
        f1000.superloop() 
        f2000.superloop() 
        f3000.superloop() 
        f4000.superloop() 
        f5000.superloop() 



schedule.every(540).seconds.do(immediatestart())

