def add_time(start, duration, day=None):

  if duration == "0:00":
    return start

  am_pm = start.split()[1] 

  start_time = start.split()[0].split(":")

  start_hour = int(start_time[0])
  start_minutes = int(start_time[1])

  duration_hour = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1])

  end_hour = int(start_hour + duration_hour)
  end_minute = int(start_minutes + duration_minutes)

  if int(end_minute) > 60:
     hours = int(str(end_minute/60).split(".")[0])
     end_hour = str(int(end_hour) + hours)
     end_minute = int(end_minute%60)
     if len(str(end_minute)) == 1:
       end_minute = "0" + str(end_minute)

  # calculate amount of days
  days = int(str(int(end_hour)/24).split(".")[0])
  end_hour = int(end_hour) - days*24

  eve = {
    "AM": "PM",
    "PM" : "AM"
  }

  if int(end_hour) % 12 != end_hour:
    am_pm = eve[am_pm]

  if end_hour > 12:
    end_hour %= 12
  if am_pm not in start and am_pm != "PM":
    days += 1
  
  days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  chosen_day = None
  if day:
    input_day = days_of_the_week.index(day.capitalize())
    next_day = input_day + days
    if next_day > len(days_of_the_week):
      next_day = next_day%len(days_of_the_week)
    chosen_day = days_of_the_week[next_day]

  if days == 0 and chosen_day:
    new_time = str(end_hour) + ":"+str(end_minute)+" "+am_pm+", "+chosen_day
  elif days == 0:
    new_time = str(end_hour) + ":"+ str(end_minute) + " " + am_pm
  elif days == 1 and  chosen_day:
    new_time = str(end_hour) + ":"+str(end_minute)+" "+am_pm+", "+chosen_day+" (next day)"
  elif days == 1:
    new_time = str(end_hour) + ":"+str(end_minute)+" "+am_pm+" (next day)"
  elif chosen_day:
    new_time = str(end_hour) + ":"+str(end_minute)+" "+ am_pm +", "+chosen_day+ f" ({days} days later)"
  else:
    new_time = str(end_hour) + ":"+str(end_minute)+" "+ am_pm + f" ({days} days later)"


  return new_time