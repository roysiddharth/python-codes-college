#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python code making use of in-built library such as time and keyboard to make a stopwatch 
# and countdown timer

# control statements such as if-else, if-elif-else, if-if-if are used.
# user defined functions countdown_timer() and stopwatch() used.
# in-built functions such as divmod(), time(), input(), lower() used.

# 2021_08_25_PL1_2148026 Python Lab assignment

# Note: if 'keyboard' library is not installed use "pip install keyboard" from 
# Anaconda command prompt.


# In[ ]:


# importing the time and keyboard in-built libraries
import time
import keyboard


# In[ ]:


print('Enter choice: ')
choice = input() # input choice for stopwatch or timer

# lower() function used to convert the input string into lowercase
if choice.lower() == "countdown": 
    t = int(input("Enter the time (in secs): "))
    countdown_timer(t) # countdown function call
elif choice.lower() == "stopwatch":
    print("Press Spacebar on the keyboard to stop...")
    stopwatch() # stopwatch function call
else:
    # if no condition of if-elif satisfies, prints "invalid input"
    print("Invalid input!") 


# In[ ]:


# defining the countdown timer function
def countdown_timer(t):
    
    while t > 0:
        # divmod() is a predefined function that returns the quotient and remainder 
        # of two arguments as tuple
        mins, secs = divmod(t, 60)
        
        # string formatting the timer
        timer = "{:02d}:{:02d} left".format(mins, secs)
        
        # \r is a carriage return that is used to refresh the timer every tick
        print(timer, end = '\r')
        
        # used to elapse one second every iteration of the loop (part of the 'time' library)
        time.sleep(1) 
        t -= 1
    print("Time out! ")


# In[ ]:


# defining stopwatch function
def stopwatch():
    
    # initialize the hours, mins and secs to 0
    secs = 0
    mins = 0
    hours = 0
    
    while True:
        # string formatting the stopwatch
        timer = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        print(timer, end = '\r')
        time.sleep(1)
        secs += 1
        if secs == 60:
            secs = 0
            mins += 1
        if mins == 60:
            mins = 0
            hours += 1
        # part of the 'keyboard' library, breaks loop when space is pressed
        if keyboard.is_pressed('space'): 
            break
    print("Time elapsed: " + timer)

