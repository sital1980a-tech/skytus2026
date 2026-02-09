import time

def traffic_light():
    while True:
        print("Red - Stop")
        time.sleep(3)  
        print("Yellow - Wait")
        time.sleep(1)  
        print("Green - Go")
        time.sleep(3)  

traffic_light()
