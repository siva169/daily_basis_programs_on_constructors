# in this program we will be writing a program that will simulate opening two connections in a class by ensuring both are closed when object is deleted


class DualConnection:
    def __init__(self):
        self.connection1="DB connection"
        self.connection2="API connection"
        print("both connections are fine")

    def __del__(self):
        print("connections are closed without any interruption")

dc=DualConnection()
del dc