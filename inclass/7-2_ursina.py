from ursina import *

app = Ursina()

for i in range(30):
    a= Entity(model='sphere', color=color.red, texture='brick', x= i)

EditorCamera()

app.run()