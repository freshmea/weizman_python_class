from pyo import *

s=Server().boot()
s.start()
sf=SfPlayer('Roly-Poly.mp3', speed=1, loop=True).out()
a=Sine().out()
#  while True:
#      pass

