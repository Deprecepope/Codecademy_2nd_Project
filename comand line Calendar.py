"""This is a program to make a command line calendar"""
from time import sleep, strftime
sylus = "Deprece"
calendar = {}
def welcome():
  print "Welcome" + sylus + "."
  print "Calendar is opening"
  sleep(1)
  strftime("%A %B %d, %y")
  strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Please press A to Add,U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Calendar is empty."
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("What date?")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Updated succesfully"
      print calendar
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "The date entered was invalid!"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue 
        else:
          start = False    
      else:
        calendar[date] = event
        print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "The calendar is already empty"
      else:
        event = raw_input("What event?")
        foundEvent = False
        for date in calendar.keys():
          if event == calendar[date]:
            foundEvent = True
            del calendar[date]
            print "The event was succesfully deleted!"
            print calendar
        if not foundEvent:
          print "An incorrect event was entered"
    elif user_choice == 'X':
      start = False
    else:
      print "An invalid command was entered!"
      start = False
start_calendar()
          
    
