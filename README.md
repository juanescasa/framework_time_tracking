# framework_time_tracking
I created this project as a help to remember a good practise to track the duration of blocks of code.
The python script shows an example and 
The excel spreadsheet shows some formulas that help building some dictionaries required by the python code. 
The concept:

I have 3 dictionaries:
di_event: it tracks the current time in which each event was executed
di_process_events: it defines the start event and the end event of each process. The excel spreadsheet help to create this dictionary automatically.
di_process_duration: it calculates the duration of each process as a dictionary comprehension.

It is necessary to build manually di_event in each part of the code in which we are interested to track the time.
