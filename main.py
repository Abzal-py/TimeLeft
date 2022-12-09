from datetime import datetime
 
 
now = [int(datetime.now().strftime("%H")),int(datetime.now().strftime("%M"))]
message = "it's just {time} left to end {event}"
schedule = {"lesson1": [[8,20],[9,0]]}
 
 
def interval(time_now, events):
   pass
 
 
 
def time_left(time_now, events):
   interval(time_now=time_now, events=events)
   pass
 
 
def main():
   print(now)
 
 
if __name__ == "__main__":
   main()