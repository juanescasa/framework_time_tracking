# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:19:35 2021

@author: Juan Calle
"""
"""
This script provides a guide on how to structure the time tracking of an algorithm
"""
import time

#Create 3 dictionaries.
#Captures the time of each moment you want to record in your code
di_event = {}
#captures the start event and end event of each process. 
#This definition is automatized in the excel companion book to this project


#I add integer to the time account to create a duration of the events because 
#the steps are very quick. In a real implementation you do not need to add the integers
di_event['start_initialization'] = time.time() + 1
a=5
b=7
k=17
j=4
di_event['start_ch1'] = time.time() + 2
v=a+b
di_event['start_ch2'] = time.time() + 4
s=j+k
di_event['start_ch3'] = time.time() + 10
ss=s+1
di_event['end_ch3'] = time.time() + 12

di_process_events = {"initialization": ("start_initialization", "start_ch1"),
                    "ch1": ("start_ch1", "start_ch2"),
                    "ch2": ("start_ch2", "start_ch3"),
                    "ch3": ("start_ch3", "end_ch3")}


di_process_duration = {process: di_event[di_process_events[process][1]] - \
                       di_event[di_process_events[process][0]] \
                       for process in di_process_events}


print('Hello world')
print('I am learning to love')
