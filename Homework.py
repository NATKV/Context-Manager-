import datetime
    
class Division:

    def __init__(self):
        self.code_launch_time = datetime.datetime.now()
        print("The code was launched on: ", self.code_launch_time)
        print("Write two positive numbers")
        

    
    def __enter__(self):
        return self
    
    def __exit__(self, type_err, val, tb):
        self.code_completion_time = datetime.datetime.now()
        print("Date and time of code completion: ", self.code_completion_time)
        if type_err != None:
            print(type_err)
            print(val)
            print(tb)

    def calculation(self):
        code_execution_time = self.code_completion_time - self.code_launch_time
        print(code_execution_time, "were spent on code execution")
        
        
                  
division_game = Division()


    
with division_game:
    number_1 = int(input())
    number_2 = int(input())
    result = number_1 / number_2
    print(result)
    
division_game.calculation()
