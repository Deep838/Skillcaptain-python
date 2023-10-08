import threading
import time

def my_time(seconds):
    print(f"this will take {seconds} seconds. ")
    time.sleep(seconds)


thread1 = threading.Thread(target=my_time, args=[4])
thread2 = threading.Thread(target=my_time, args=[1])
thread3 = threading.Thread(target=my_time, args=[2])


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("this took 7 seconds to complete")