#!/usr/bin/python

class JustCounter:
   __secret_count = 0
  
   def count(self):
      self.__secret_count += 1
      print(self.__secret_count)

counter = JustCounter()
counter.count()
counter.count()
# can't access
print(counter.__secret_count)