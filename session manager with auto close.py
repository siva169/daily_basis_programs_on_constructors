#in this program we will be writing a code that designs a class called session that simulates a user session on deletion


class Session:
    def __init__(self,user):
        self.user=user
        print(f"session is started for {self.user} successfully")


    def __del__(self):
        print(f"session ended for {self.user}")


s1=Session("siva phanindra")
del s1