import sys
# import argparse
# print( "type: ",type(sys.argv))
# print("length: ",len(sys.argv))
# print("value: ",sys.argv[1], sys.argv[2])
# print("modules: ",sys.modules)
# print("before import length of modules: ",len(sys.modules))
# import math
# print("after import length of modules: ",len(sys.modules))

# print ("max size: ", sys.maxsize)

# my_list=list(range(sys.maxsize))
# print(my_list)

# print(sys.version)
# print(sys.version_info)
# print(sys.platform)


# for word in sys.stdin:
#     if "q"== word.strip():
#         sys.exit("program terminated...")
#     else:
#         sys.stdout= open('output.txt', 'w')
#         print(f'Input: {word}')

# print('exit')        


# a= 5
# if sys.argv[1] == "size":
#      print(sys.getsizeof(a))

class CLI_command:
     def __init__(self):
        pass
        self.task =[]

     def task_handle(self):
          print('now enter your commant')
          while True:
             try:
                 command = input(">> ").strip().lower()

                 if command == 'q':
                      print("exit to the task terminal...")
                      break
                 elif command == 'add':
                      input_task= input("enter your task here :")
                      if input_task:
                          self.task.append(input_task)
                          print(f'your task is been added to the list \n and your task is: {input_task}')
                      else:
                          print("task is not found...")    
                 elif command == 'show':
                       if self.task:                          
                           print(f'your task length is {len(self.task)}')
                           for task in self.task:
                              print(f'your task is:\n {task}')
                       else:
                         print('there is no task to show...') 
             except EOFError:
                   print("\nEnd of input. Exiting...")
                   break
               
                    
def main():
     if len(sys.argv)<2 :
          sys.exit("you have not writtern any commant so program has been terminated...") 

     if sys.argv[1]=='task':
          my_task= CLI_command()
          my_task.task_handle()
     else:
           exit("Invalid argument. Use 'task' to start the task manager.")

if __name__ == "__main__":
    main()           