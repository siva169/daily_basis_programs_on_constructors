#in this program we will be writing a code that simulates a class model session where a constructor loads a dataset and the destructor logs that the training session is over


class ModelSession:
    def __init__(self,model_name):
        self.model_name=model_name
        print(f"{self.model_name} model training started...")



    def __del__(self):
        print(f"{self.model_name} model training session is completed")

m=ModelSession("vision net")
m1=ModelSession("claude4.0")
m2=ModelSession("chatgpt4.0")
del m
del m1
del m2