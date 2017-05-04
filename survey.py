from guizero import App
from guizero import App
from guizero import App, Combo
from guizero import App, Text
from guizero import App, CheckBox
from guizero import App, ButtonGroup
from guizero import App, PushButton
from guizero import App, info
from guizero import App, Slider
from guizero import App, Picture
from guizero import App, TextBox

app = App(title="Survey", width=900, height=400)

welocome = Text(app, text="Welcome. Please fill out the survey below.")

space = Text(app, text=" ")

questions_1 = Text(app, text="Do you enjoy my projects?", grid=[1,0])

questions = ButtonGroup(app, options=[ ["No", "N"], ["Middle", "M"],["Yes", "Y"] ],
selected="M", horizontal=True, grid=[1,1], align="left")

space1 = Text(app, text=" ")

questions_12 = Text(app, text="Am I improving?", grid=[1,0])

questions_13 = ButtonGroup(app, options=[ ["No", "N"], ["Middle", "M"],["Yes", "Y"] ],
selected="M", horizontal=True, grid=[1,1], align="left")

space_2 = Text(app, text=" ")

questions_14 = Text(app, text="Should I continue on this path?", grid=[1,0])

questions_19 = ButtonGroup(app, options=[ ["No", "N"], ["Middle", "M"],["Yes", "Y"] ],
selected="M", horizontal=True, grid=[1,1], align="left")

space_3 = Text(app, text=" ")

submit = Text(app, text="Please submit the results printed in the Shell to nighthawk136@outlook.com. Thank you!")

app.display()
