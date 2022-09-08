
def add_time(start, duration, day = None):
  days = {"Monday": 1 ,"Tuesday": 2 , "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday":6,"Sunday": 7}
  
  if day != None:
    current_day = day.capitalize()

  # numbers of the duration
  split_duration = [x for x in duration.split(":")]
  duration_hours = int(split_duration[0])
  duration_minutes = int(split_duration[1])
  
  

  # numbers of the start time
  split_start = [x for x in start[:len(start) - 2].split(":")]
  start_hour = split_start[0]
  start_minutes = split_start[1]

  am_pm = start[len(start) - 2:]

  if duration_hours > 23:
    remaining_time = duration_hours % 24
    days_gone = duration_hours // 24
    
    current_hour = int(start_hour) + int(remaining_time)
    current_minutes = int(start_minutes) + int(duration_minutes)

    if current_minutes > 60:
      current_minutes = current_minutes - 60
      current_hour += 1

    if len(str(current_minutes)) == 1:
      current_minutes = "0" + str(current_minutes)

    if current_hour >= 12:
      if am_pm == "PM":
         # this does indicate a new day
        am_pm = "AM"
        days_gone += 1
      elif am_pm == "AM":
        am_pm = "PM"
      
      if current_hour > 12:
        current_hour = current_hour % 12
    

    # logic missing to determine the day

    if days_gone == 1:
      
      if day != None:
        start_ = days[current_day]
        for i in range(days_gone):
          start_ += 1
          if start_ == 8:
            start_ = 1

        current_day = list(days.keys())[list(days.values()).index(start_)]
        return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + ", " + current_day + " (next day)")
      else:
        return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + " (next day)")

    if day != None:
      start_ = days[current_day]
      for i in range(days_gone):
        start_ += 1
        if start_ == 8:
          start_ = 1

      current_day = list(days.keys())[list(days.values()).index(start_)]
      return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + ", " + current_day + f" ({days_gone} days later)")
    else:
      return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + f" ({days_gone} days later)")
    
  else:
    current_hour = int(start_hour) + int(duration_hours)
    current_minutes = int(start_minutes) + int(duration_minutes)
    print(current_minutes)
    next_day = False
    # differentioation of the case that the previous was either AM or PM

    if current_minutes > 60:
      current_minutes = current_minutes - 60
      current_hour += 1

    if len(str(current_minutes)) == 1:
      current_minutes = "0" + str(current_minutes)


    if current_hour >= 12:
      if am_pm == "PM":
         # this does indicate a new day
        am_pm = "AM"
        next_day = True
      elif am_pm == "AM":
        am_pm = "PM"
        
      if current_hour > 12:
        current_hour = current_hour % 12

    if next_day:
      
      if day != None:
        return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + ", " + current_day + " (next day)")
      else:
        return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + " (next day)")

    if day != None:
      
      return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm + ", " + current_day)
    else:
      return(str(current_hour) + ":" + str(current_minutes) + " " + am_pm)

print(add_time("2:59 AM", "24:00", "saturDay"))