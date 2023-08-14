def add_time(start, duration, day=None):
  # Parse the start time
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  start_hour = start_hour % 12  # Convert to 12-hour format

  # Parse the duration
  duration_hour, duration_minute = map(int, duration.split(':'))

  # Calculate the end time
  end_minute = (start_minute + duration_minute) % 60
  carry_hour = (start_minute + duration_minute) // 60
  end_hour = (start_hour + duration_hour + carry_hour) % 12

  # Determine the period (AM/PM)
  end_period = period
  if (start_hour + duration_hour + carry_hour) // 12 == 1:
    if period == 'AM':
      end_period = 'PM'
    else:
      end_period = 'AM'

  # Calculate the number of days later
  num_days_later = (start_hour + duration_hour + carry_hour) // 12

  # Get the day of the week if provided
  if day:
    day = day.lower()
    days_of_week = [
      'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
      'saturday'
    ]
    start_day_index = days_of_week.index(day)
    end_day_index = (start_day_index + num_days_later) % 7
    end_day = days_of_week[end_day_index].capitalize()
  else:
    end_day = None

  # Format the end time string
  end_time = f"{end_hour or 12}:{str(end_minute).zfill(2)} {end_period}"

  # Format the output based on the number of days later
  if num_days_later == 0:
    if end_day:
      return f"{end_time}, {end_day}"
    else:
      return end_time
  elif num_days_later == 1:
    if end_day:
      return f"{end_time} (next day), {end_day}"
    else:
      return f"{end_time} (next day)"
  else:
    if end_day:
      return f"{end_time}, {num_days_later} days later, {end_day}"
    else:
      return f"{end_time}, {num_days_later} days later"


print(add_time("3:00 PM", "3:10"))

print(add_time("11:30 AM", "2:32", "Monday"))

print(add_time("11:43 AM", "00:20"))

print(add_time("10:10 PM", "3:30"))

print(add_time("11:43 PM", "24:20", "tueSday"))

print(add_time("6:30 PM", "205:12"))