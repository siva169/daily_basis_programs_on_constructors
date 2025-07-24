#in this program we will be tracking how many times constructor  and destructor are called using a class variable

class Tracker:
    count=0


    def __init__(self):
        Tracker.count+=1
        print(f"constructor summoned .Total:{Tracker.count}")


    def __del__(self):
        Tracker.count-=1
        print(f"summoning of destructor being done.remaining: {Tracker.count}")


q=Tracker()
b=Tracker()
del q
del b