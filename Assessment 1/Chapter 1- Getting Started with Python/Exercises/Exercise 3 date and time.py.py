#Import the datetime module for date and time operations.
import datetime
#Get the current date and time.
current_date_time=datetime.datetime.now()
#Format the current date and time as a string in the format "YYYY-MM-DD HH:MM:SS"
formatted_date_time=current_date_time.strftime("%Y-%m-%d %H:%M:%S")
# Print the formatted date and time.
print("current date and time:",formatted_date_time)