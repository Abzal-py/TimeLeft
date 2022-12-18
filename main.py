from datetime import datetime
 
 
now = [int(datetime.now().strftime("%H")),int(datetime.now().strftime("%M"))]
message = "it's just {} left to end {}"
schedule = {"lesson1": [[8,20], [9,0]], 
            "break 1-2": [[9,0], [9,5]], 
            "lesson2" : [[9,5], [9,45]],
            "break 2-3": [[9,45], [9,55]],
            "lesson3": [[9,55], [10,35]],
            "break 3-4": [[10,35], [10,40]],
            "lesson4": [[10,40], [11,20]],
            "lunch1": [[11,20], [11,50]],
            "lesson5": [[11,50], [12,30]],
            "lunch2": [[12,30], [13,0]],
            "lesson6": [[13,0], [13,40]],
            "break 6-7": [[13,40], [13,45]],
            "lesson7" : [[13,45], [14,25]],
            "poldnik1": [[14,25], [14,40]],
            "lesson8" : [[14,40], [15,20]],
            "poldnik2": [[15,20], [15,35]],
            "lesson9" : [[15,35], [16,15]],
            "break 9-10": [[16,15], [16,20]],
            "lesson10" : [[16,20], [17,0]],
            "break 10-11": [[17,0], [17,10]],
            "lesson11" : [[17,10], [17,50]]}


def time_left(time1: list, time2: list) -> list:
   hours_left = time2[0] - time1[0]
   minutes_left = time2[1] - time1[1]
   return [hours_left, minutes_left]


def current_event(cur_time: list, timetable: dict):
   cur_hour = cur_time[0]
   cur_minute = cur_time[1]
   print(cur_hour, cur_minute)
   for index, item in timetable.items():
      time1_hour = item[0][0]
      time1_minute = item[0][1]
      time2_hour = item[1][0]
      time2_minute = item[1][1]  
      if True:
         print(cur_hour, time1_hour, time2_hour)
         print(index)
   return True


def main(): 
   print(current_event(now, schedule))


if __name__ == "__main__":
   main()