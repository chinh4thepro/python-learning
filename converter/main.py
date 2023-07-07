import PySimpleGUI as sg

layout = [ 
    [sg.Text('Text', enable_events = True, key = '-TEXT-'), sg.Spin(['item 1', 'item 2'])], 
    [sg.Button('Button', key = 'Button1')], 
    [sg.Input()],
    [sg.Text('hello'), sg.Button('Test button', key = 'Button2')]
]

window = sg.Window('Converter',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Button1':
        print('Button pressed')
    
    if event == 'Button2':
        print('Test button pressed')

    if event == '-TEXT-':
        print('TEXt  pressedo')

window.close()