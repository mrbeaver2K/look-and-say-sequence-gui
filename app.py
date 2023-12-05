import PySimpleGUI as sg
from sys import exit
layout = [[sg.Text("Input a Number to be sequenced from and a maximum Sequence length.")],
          [sg.Input(key="Number", default_text="1"), sg.Input(key="Max")],
          [sg.ProgressBar(1, key="Progress")],
          [sg.Button("Sequence"), sg.Button("Close")]]
window = sg.Window("Window", layout)
progress = 0
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Close"):
        window.close()
        exit()
    if event == "Sequence":
        window["Progress"].Update(max=int(values["Max"]))
        sequence = [values["Number"]]
        for i in range(1, int(values["Max"])):
            step = [int(d) for d in sequence[-1]]
            nextstep = []
            currentn = step[0]	
            currents = 0
            for j in step:
                if j == currentn:
                    currents += 1
                else:
                    nextstep.append(str(currents))
                    nextstep.append(str(currentn))
                    currents = 1
                currentn = j
            nextstep.append(str(currents))
            nextstep.append(str(currentn))
            sequence.append("".join(nextstep))
            progress += 1
            window["Progress"].UpdateBar(progress)
        sg.popup("\n".join(sequence))
