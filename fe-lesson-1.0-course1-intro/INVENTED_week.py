# INVENTED example: Karim and his week
# Karim, the schedule and the numbers are made up.
hours_per_day = 2
days_per_week = 5
video_hours = 13
practice = 2 * video_hours   # estimate
total_hours = video_hours + practice
weeks = total_hours / (hours_per_day * days_per_week)
print(total_hours)
print(round(weeks, 1))
