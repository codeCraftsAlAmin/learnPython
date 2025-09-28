# # Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing.

'''
Syntax and usages
------------------
try:
      # Code 
except SomeException:
      # Code 
else:
     # Code 
finally:
    # Code 

,,,,,,,,,,,,,,
- try: Runs the risky code that might cause an error.
- except: Catches and handles the error if one occurs.
- else: Executes only if no exception occurs in try.
- finally: Runs regardless of what happens useful for cleanup tasks like closing files.

'''
n = 5

try:
    res = 12/n
    # print(res)
except ZeroDivisionError:
    print("You can't divide by zero!")
except TypeError:
    print("Input must be an integer number")
else:
        print(res)
finally:
    print("Process complete")