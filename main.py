import time
import random
import os
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='pain.log', encoding='utf-8', level=logging.DEBUG)
#i discovered how to do this so i can make it way easier to rig the results
num = random.randint(0, 100)
#PLEASE git push to 1.0.1 when making changes andrew
#if you don't i swear to god
#i will find you
os.system('clear')
#it took so long to make this stuff appear line by line it's not even funny  -.-
ascii_art_lines = [
  "   ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░  ",
  "  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "  ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "  ░▒▓█▓▒▒▓███▓▒░ ░▒▓████████▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓███████▓▒░  ",
  "  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓███████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ",
  " ", 
  "     ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓███████▓▒░  ",
  "  ░▒▓████▓▒░   ░▒▓████▓▒░             ░▒▓█▓▒░ ",
  "     ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░ ",
  "     ░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓██████▓▒░  ",
  "     ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░       ",
  "     ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░       ",
  "     ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░▒▓██▓▒░▒▓████████▓▒░ ",

]            

for line in ascii_art_lines:
  print(line)
  time.sleep(0.1)
time.sleep(0.5)
print()
print("Welcome to GAYDAR! Let's get things stared for you.")
print()
print("Activating GAYDAR...")
print()
time.sleep(3)
print("GAYDAR Activated!")
print("Scanning for targets...")
print()
time.sleep(3)
print(random.randint(1, 10000), "possible targets found.")
print()
while True:
  print("Who would you like to target?")
  name = input("(name): ")
  print(f"Just to be sure, do you want to target {name}?")
  confirm = input("(y/n): ")
  print()
  if confirm.lower() == "y":
    print("GAYDAR Tip: If you don't want to wait for the scanning process to finish, check the file named 'pain.log'.")
    time.sleep(0.5)
    print("The GAYDAR automatically prints all the names and results of people that have been already scanned.")
    time.sleep(1)
    print("Auto-continuing in 3 seconds...")
    time.sleep(3)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    ascii_art_lines = [ 
      " ░▒▓███████▓▒░  ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░  ░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓███████▓▒░   ░▒▓██████▓▒░                             ",
      "░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                            ",
      "░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                                   ",
      " ░▒▓██████▓▒░  ░▒▓█▓▒░        ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒▒▓███▓▒░                            ",
      "       ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                            ",
      "       ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██▓▒░ ░▒▓██▓▒░ ░▒▓██▓▒░ ",
      "░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░  ░▒▓██▓▒░ ░▒▓██▓▒░ ░▒▓██▓▒░ ",
    ]
    for line in ascii_art_lines:
      print(line)
      time.sleep(0.1)
    break
  else:
    print("Ok then.")
#it took way too long to type this loading text out
#like two days too long
print()
time.sleep(1)
print("Baking a cake.")
time.sleep(0.5)
print("Finding friends...")
time.sleep(2)
print("Error: value can't be zero!")
time.sleep(1)
print("Taking happy pills.")
time.sleep(0.5)
print("Legalizing nuclear bombs.")
time.sleep(0.5)
print("Hacking the mainframe.")
time.sleep(0.5)
print("Fighting third graders.")
time.sleep(0.5)
print("Finding father...")
time.sleep(2)
print("Error: can't find something that doesn't exist!")
time.sleep(1)
print("Having existential crisis.")
time.sleep(0.5)
print("Finishing what Bin Laden started.")
time.sleep(0.5)
print("Checking search history.")
time.sleep(0.5)
print("Bleaching eyes.")
time.sleep(0.5)
print("Preparing for titanfall.")
time.sleep(0.5)
print("Checking for brain wrinkles...")
time.sleep(2)
print("Smooth brain detected! Cutting corners.")
time.sleep(1)
print("Removing human rights.")
time.sleep(0.5)
print("Listening to the chiki's chase soundtrack on loop.")
time.sleep(0.5)
print("Burning down the house.")
time.sleep(0.5)
print("Staying up til midnight.")
time.sleep(0.5)
print("Bringing death to the MPLA.")
time.sleep(0.5)
print("Attempting a manual override on the wall.")
time.sleep(0.5)
print("Getting a divorce.")
time.sleep(0.5)
print("Taking back the creek.")
time.sleep(0.5)
print("Turning it off an back on again.")
time.sleep(0.5)
print("Finding who asked...")
time.sleep(2)
print("Oh my god, we found him!")
time.sleep(1)
print("Checking if a throw is our only option.")
time.sleep(0.5)
print("Spreading democracy across the galaxy.")
time.sleep(0.5)
print("Doing homework...")
time.sleep(2)
print("Error: nevermind I got bored.")
time.sleep(1)
print("Playing Team Fortress Two.")
time.sleep(0.5)
print("Stealing from your local walmart.")
time.sleep(0.5)
print("Eating gas station sushi.")
print(".....")
print()
time.sleep(1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
#line too long? nah, you can never have it too long.
ascii_art_lines = [
  "  ░▒▓███████▓▒░  ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░  ",
  " ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  " ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "  ░▒▓██████▓▒░  ░▒▓█▓▒░        ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "        ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  "        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
  " ░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ",
" ",
" ",
  " ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓██████████████▓▒░  ░▒▓███████▓▒░  ░▒▓█▓▒░        ░▒▓████████▓▒░ ░▒▓████████▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░ ",
  "░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░ ",
  "░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░ ",
  "░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓█▓▒░        ░▒▓██████▓▒░      ░▒▓█▓▒░     ░▒▓██████▓▒░   ░▒▓█▓▒░ ",
  "░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░ ",
  "░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░                ",
  " ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓████████▓▒░ ░▒▓████████▓▒░    ░▒▓█▓▒░     ░▒▓████████▓▒░ ░▒▓█▓▒░ ",

]                                                                                                                                       
for line in ascii_art_lines:
  print(line)
  time.sleep(0.1)

time.sleep(1)
print()
print("Please wait a sec, I need to crunch some numbers.")
time.sleep(3)  
print("Stuff isn't adding up, I need one more thing from you.")
time.sleep(1)
print()
print(f"I should have asked you this in the beginning, but what's {name}'s gender?")
#TO DO: Make it so GAYDAR dumps the name and the result to a log so we can give people
#the same numbers if they enter the same name.

#this could be optimized... but i'm too lazy to mess with the spaghetti that's here now.
while True:
  gender = input("(boy/girl) ")
  if gender.lower() == "Boy":
    logger.info(f'Name = {name}')
    logger.info(f'Result = {num}%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(0.5)
    print()
    #just realized i could have just used else instead of >
    #pretty sure i need to use else because this crap won't work if i use >
    if (num) == 100:
      #it won't work regardless anyway LMAO
      print(f"{name} is {num}% gay! They passed the test with flying colors!")
      break
    else:
      print(f"{name} is {num}% gay!")
      break
  if gender.lower() == "boy":
    logger.info(f'Name = {name}')
    logger.info(f'Result = {num}%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(0.5)
    print()
    if (num) == 100:
      print(f"{name} is {num}% gay! They passed the test with flying colors!")
      break
    else:
      print(f"{name} is {num}% gay!")
      break
  if gender.lower() == "Girl":
    logger.info(f'Name = {name}')
    logger.info(f'Result = {num}%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(0.5)
    print()
    if (num) == 100:
      print(f"{name} is {num}% lesbian! They passed the test with flying colors!")
      break
    else:
      print(f"{name} is {num}% lesbian!")
      break
  if gender.lower() == "girl":
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    if (num) == 100:
      print(f"{name} is {num}% lesbian! They passed the test with flying colors!")
      break
    else:
      print(f"{name} is {num}% lesbian!")
      break
  if gender.lower() == "yes":
    logger.info(f'Name = {name}')
    logger.info(f'Result = {num}%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    if (num) == 100:
      print(f"{name} is {num}% gay and lesbian somehow! They passed the test with flying colors!")
      break
    else:
      print(f"{name} is {num}% gay and lesbian somehow!")
      break
  if gender.lower() == "girl ":
    logger.info(f'Name = {name}')
    logger.info('Result = 100%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    #hi
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    print(f"{name} is 100% lesbian! What, did you expect anything less?")
    break
  if gender.lower() == "boy ":
    logger.info(f'Name = {name}')
    logger.info('Result = 100%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    print(f"{name} is 100% gay! What, did you expect anything less?")
    break
  if gender.lower() == " girl":
    logger.info(f'Name = {name}')
    logger.info('Result = 1000%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    print(f"{name} is 1000% lesbian! They've reached levels of gay not thought possible!")
    break
  if gender.lower() == " boy":
    logger.info(f'Name = {name}')
    logger.info('Result = 1000%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    print(f"{name} is 1000% gay! They've reached levels of gay not thought possible!")
    break
  #i wonder why this part doesn't work...
  if gender.lower() == "no":
    logger.info(f'Name = {name}')
    logger.info('Result = ERROR%')
    logger.info(f'Gender = {gender}')
    logger.info('----------')
    print("Ok, I'll try calculating it again with the correct infomation now.")
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print("Alright, the results are in.")
    time.sleep(1)
    print()
    print(f"{name} is {num}% ga- Uh, les- Wait, what?")
    time.sleep(1)
    print("What do you mean?")
    time.sleep(2)
    print("What do you mean no?")
    time.sleep(3)
    print()
    print("Error: GAYDAR Module 1, 4, and 7 threw a fatal error!")
    time.sleep(0.5)
    print("Fallback order: GAYDAR (Experimental), GAYDAR Helper, GAYDAR Helper (Experimental)")
    print("Preforming fallback procedure...")
    time.sleep(0.5)
    print("Loading GAYDAR (Experimental)...")
    time.sleep(1)
    print("Error: GAYDAR (Experimental) exited with error 17!")
    print("Loading GAYDAR Helper...")
    time.sleep(1)
    print("Error: GAYDAR Helper exited with code 29!")
    print("Loading GAYDAR Helper (Experimental)...")
    time.sleep(1)
    print("Error: GAYDAR Helper (Experimental) exited with code 14!")
    print("Warning: all fallbacks exhausted")
    print("Exit command recieved from GAYDAR Error Handler, Stopping program...")
    time.sleep(1)
    print("GAYDAR exited with code 0. Have a nice day!")
    break
  else:
    print(f"That's not a gender bub. What's {name}'s gender? For real this time.")
    #after break, let's add a continue option, that way you can scan more people without
    #reruning the code.