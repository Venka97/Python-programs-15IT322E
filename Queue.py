# from queue import Queue
#
# def print_q(q):
#     while not q.empty():
#         print(q.get())
#         q.task_done()
#
# q = Queue(maxsize=0)
#
# for z in range(20):
#     q.put("item -"+ str(z))
#
# print_q(q)
#
from threading import Thread
import time
from threading import Thread

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
   Thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   Thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")
while 1:
    pass