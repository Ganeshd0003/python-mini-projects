import time
from plyer import notification

while True:
    print("Drink some water!")
    notification.notify(title="Please drink some water", message = "You need to drink some water")
    time.sleep(3)