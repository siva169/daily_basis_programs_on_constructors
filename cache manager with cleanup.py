#in this program we will be creating a class called cache and we will be storing temporary values
# on deletion print which values were flushed out



class Cache:
    def __init__(self):
        self.data={"x":1,"b":2,"f":7,"q":21}
        print("cache initiated")


    def __del__(self):
        print(f"cache cleared : {list(self.data.keys())}")


c=Cache()
del c