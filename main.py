import time
import random
import os
import sys
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='pain.log', encoding='utf-8', level=logging.DEBUG)
#i can make the loading text pull randomly from a file now! horray!
def random_line(fname):
  lines = open(fname).read().splitlines()
  return random.choice(lines)
print(random_line('load.txt'))
t = time.localtime(time.time())
localtime = time.asctime(t)
#i wanna print the current time cuz y'know, why not?
#i discovered how to do this so i can make it way easier to rig the results
num = random.randint(0, 100)
stdin_backup = sys.stdin        
devnull = open(os.devnull, 'w')  
#i stole this code from stackoverflow lol
sys.stdin = devnull
#PLEASE git push to 1.0.2 when making changes andrew
#if you don't i swear to god
#i will find you
os.system('clear')
#it took so long to make this stuff appear line by line it's not even funny
ascii_art_lines = [
  "  /$$$$$$   /$$$$$$  /$$     /$$ /$$$$$$$   /$$$$$$  /$$$$$$$    /$$$$$$$ /$$   /$$",
  " /$$__  $$ /$$__  $$|  $$   /$$/| $$__  $$ /$$__  $$| $$__  $   |__ $$__/ |$$$$$$$$",
  "| $$  \__/| $$  \ $$ \  $$ /$$/ | $$  \ $$| $$  \ $$| $$  \ $$     |$$    |$$/$$|$$",
  "| $$ /$$$$| $$$$$$$$  \  $$$$/  | $$  | $$| $$$$$$$$| $$$$$$$/     |_/    |_/   |_/",
  "| $$|_  $$| $$__  $$   \  $$/   | $$  | $$| $$__  $$| $$__  $$",
  "| $$  \ $$| $$  | $$    | $$    | $$  | $$| $$  | $$| $$  \ $$",
  "|  $$$$$$/| $$  | $$    | $$    | $$$$$$$/| $$  | $$| $$  | $$",
  " \______/ |__/  |__/    |__/    |_______/ |__/  |__/|__/  |__/",
  " ", 
  "   /$$          /$$$$$$        /$$$$$$ ",
  " /$$$$         /$$$_  $$      /$$__  $$",
  "|_  $$        | $$$$\ $$     |__/  \ $$",
  "  | $$        | $$ $$ $$       /$$$$$$/",
  "  | $$        | $$\ $$$$      /$$____/ ",
  "  | $$        | $$ \ $$$     | $$      ",
  " /$$$$$$  /$$ |  $$$$$$/ /$$ | $$$$$$$$",
  "|______/ |__/  \______/ |__/ |________/",

]            

for line in ascii_art_lines:
  print(line)
  time.sleep(0.1)
time.sleep(0.5)
print()
print("Welcome to GAYDAR!")
print(f"The current time and date is {localtime}")
print("Let's get things stared for you.")
print()
print("Activating GAYDAR...")
text = "░▒▒▓██████████████████████▓▒▒░"
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print()
print("GAYDAR Activated!")
print("Scanning for targets...")
text = "░▒▒▓██████████████████████▓▒▒░"
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print()
print(random.randint(1, 10000), "possible targets found.")
print()
while True:
  sys.stdin = stdin_backup
  print("Who would you like to target?")
  name = input("(name): ")
  print(f"Just to be sure, do you want to target {name}?")
  confirm = input("(y/n): ")
  print()
  if confirm.lower() == "y":
    break
  else:
    print("Ok then.")
sys.stdin = devnull
os.system('clear')
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
  "  /$$$$$$                                          /$$                               ", 
  " /$$__  $$                                        |__/                                ",
  "| $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$  /$$ /$$$$$$$   /$$$$$$            " ,
  "|  $$$$$$  /$$_____/ |____  $$| $$__  $$| $$__  $$| $$| $$__  $$ /$$__  $$            ",
  " \____  $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$  \ $$| $$  \ $$            ",
  " /$$  \ $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$            ",
  "|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$| $$| $$  | $$|  $$$$$$$ /$$ /$$ /$$",
  " \______/  \_______/ \_______/|__/  |__/|__/  |__/|__/|__/  |__/ \____  $$|__/|__/|__/",
  "                                                                 /$$  \ $$            ",
  "                                                                |  $$$$$$/            ",
  "                                                                 \______/             ",
]
for line in ascii_art_lines:
  print(line)
  time.sleep(0.1)
print()
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.5)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.7)
print(random_line('load.txt'))
time.sleep(0.5)
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
ascii_art_lines = [

  "  /$$$$$$                                                                         ",
  " /$$__  $$                                                                        ",
  "| $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$                                           ",
  "|  $$$$$$  /$$_____/ |____  $$| $$__  $$                                          ",
  " \____  $$| $$        /$$$$$$$| $$  \ $$                                          ",
  " /$$  \ $$| $$       /$$__  $$| $$  | $$                                          ",
  "|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$                                         " ,
  " \______/  \_______/ \_______/|__/  |__/                                          ",
  "",
  "  /$$$$$$                                    /$$             /$$               /$$",
  " /$$__  $$                                  | $$            | $$              | $$",
  "| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ | $$  /$$$$$$  /$$$$$$    /$$$$$$ | $$",
  "| $$       /$$__  $$| $$_  $$_  $$ /$$__  $$| $$ /$$__  $$|_  $$_/   /$$__  $$| $$",
  "| $$      | $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$| $$$$$$$$  | $$    | $$$$$$$$|__/",
  "| $$    $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$_____/  | $$ /$$| $$_____/    ",
  "|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$$ /$$",
  " \______/  \______/ |__/ |__/ |__/| $$____/ |__/ \_______/   \___/   \_______/|__/",
  "                                  | $$                                            ",
  "                                  | $$                                            ",
  "                                  |__/                                            ",

]                                                                                                                                       
for line in ascii_art_lines:
  print(line)
  time.sleep(0.1)

time.sleep(1)
print()
print("Please wait a sec, I need to crunch some numbers.")
print()
text = "░▒▒▓██████████████████████▓▒▒░"
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print()
print()
print("Stuff isn't adding up, I need one more thing from you.")
time.sleep(1)
print(f"I should have asked you this in the beginning, but what's {name}'s gender?")
#this could be optimized... but i'm too lazy to mess with the spaghetti that's here now.
while True:
  sys.stdin = stdin_backup
  gender = input("(boy/girl) ")
  sys.stdin = devnull
  if gender.lower() == "Boy" or "boy":
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
    if (num) >= 80:
      print(f"{name} is {num}% gay! They passed the test with flying colors!")
      break
    if (num) >= 50:
      print(f"{name} is {num}% gay! They're shooting to the top!")
      break
    else:
      print(f"{name} is {num}% gay!")
      break
  if gender.lower() == "Girl" or "girl":
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
    if (num) >= 80:
      print(f"{name} is {num}% lesbian! They passed the test with flying colors!")
      break
    if (num) >= 50:
      print(f"{name} is {num}% lesbian! They're shooting to the top!")
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
    if (num) >= 50:
      print(f"{name} is {num}% gay and lesbian somehow! They're shooting to the top!")
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
    print("Exit command recieved from GAYDAR Error Handler, stopping program...")
    time.sleep(1)
    print("GAYDAR exited with code 0. Have a nice day!")
    break
  else:
    print(f"That's not a gender bub. What's {name}'s gender? For real this time.")
    #after break, let's add a continue option, that way you can scan more people without
    #reruning the code.