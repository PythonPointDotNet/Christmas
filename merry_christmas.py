from pyfiglet import Figlet
f = Figlet(font='slant')
from time import sleep
import sys

for x in ["1","2",'3',"PythonPoint.net", "Wishes", "You"] :
    print(f.renderText(x), end='')
    sys.stdout.flush()
    sleep(0.7)
print(f.renderText(';-:----------'))
sleep(0.7)
print(f.renderText("Merry"))
sleep(0.8)
print(f.renderText("Christmas"))
sleep(0.8)
print(f.renderText("-----------:;"))
sleep(0.8)
print(f.renderText(";-:-- Like"))
sleep(0.8)
print(f.renderText(";-:-- Share"))
# sleep(0.8)
# print(f.renderText(";-:-- Subscribe"))
