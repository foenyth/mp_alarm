# Alarm clock
# Loop and print the time
# Activate a youtube video if the time is equal

# Import libraries
import time
import webbrowser
import random

# The use can set the time they want to be alarm. The String the user puts in must be the same as the example to work.
print "When do you want to be alarmed?\nUse this format.\nExample: 08:06:00"

Alarm = raw_input("> ")

# State the Time variable to be usable in the while-loop
Time = time.strftime("%H:%M:%S")

# Open the text file with the provided youtube links
with open("links.txt") as f:
    content = f.readlines()

# When the time does not equal the Alarm string given above, print the time
while Time != Alarm:
    print "The time is " + Time
    # Restating the Time variable allows the time to refresh
    Time = time.strftime("%H:%M:%S")
    # Updating the time
    time.sleep(1)

# When the Time variable is equal to the Alarm string, activate the code
if Time == Alarm:
    print "This is the time!"
     # from the variable content, a random link is chosen and then that link is stored in random_video varibale
    random_video = random.choice(content)
    # Using webbrowser library, it opens youtube link
    webbrowser.open(random_video)
