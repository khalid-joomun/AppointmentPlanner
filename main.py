# Khalid Joomun
#
# 28th July 2020
#   First attempt at Appointment planner program
#   Attempting daily view using PySimpleGui
#   Using linear approach, not using OOP for Window
#
# 30th July
#   GUI working, fully designed
#   TO-DO: Make names persistent
#
# 31st July
#   Persistent names DONE.
#   Fully functional
#   TO-DO: Store names in text file

import PySimpleGUI as sg
sg.theme('DefaultNoMoreNagging')

namesdict = {
    'Lundi': ["1", "", "a", "", "", "", "", "", ""],
    'Mardi': ["2", "", "b", "", "", "", "", "", ""],
    'Mercredi': ["", "", "c", "", "", "", "", "", ""],
    'Jeudi': ["", "", "d", "", "", "", "", "", ""],
    'Vendredi': ["", "", "e", "", "", "", "", "", ""]
}
list1 = ['_NAME0_', '_NAME1_', '_NAME2_', '_NAME3_',
         '_NAME4_', '_NAME5_', '_NAME6_', '_NAME7_', '_NAME8_']
days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
head = 'Calibri 40'
reg = 'Calibri 35'


class EditWindow:
    def __init__(self):
        self.index = 0
        self.timecolumn = [
            [sg.Text(
                'Horraire',
                font=(reg),
                justification='center',
                background_color='dark grey',
                size=(10, 1),
                pad=(0, 7))],
            [sg.Text(
                ' 8:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                ' 8:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                ' 9:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                ' 9:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '10:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '10:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '11:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '11:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '12:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))]
        ]
        # namesdict['Monday'][2]
        self.namecolumn = [
            [sg.Text('Patient', font=(head), justification='center',
                     background_color='dark grey', size=(25, 1), pad=(0, 7))],
            [sg.Input(namesdict[days[self.index]][0], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME0_')],
            [sg.Input(namesdict[days[self.index]][1], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME1_')],
            [sg.Input(namesdict[days[self.index]][2], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME2_')],
            [sg.Input(namesdict[days[self.index]][3], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME3_')],
            [sg.Input(namesdict[days[self.index]][4], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME4_')],
            [sg.Input(namesdict[days[self.index]][5], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME5_')],
            [sg.Input(namesdict[days[self.index]][6], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME6_')],
            [sg.Input(namesdict[days[self.index]][7], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME7_')],
            [sg.Input(namesdict[days[self.index]][8], font=(reg),
                      size=(25, 1), pad=(0, 5), key='_NAME8_')],
        ]
        self.layout = [
            [sg.Button(
                'Previous',
                font=('Helvetica 15'),
                pad=(20, 0),
                key='_PREVIOUS_'),

                sg.Text(
                    text=days[self.index],
                    font=(head),
                    justification='center',
                    size=(10, 1),
                    pad=(60, 5),
                    key='_DAY_'),

                sg.Button(
                    'Next',
                    font=('Helvetica 15'),
                    pad=(20, 0),
                    key='_NEXT_')],

            [sg.Column(self.timecolumn), sg.Column(self.namecolumn)],
            [sg.Radio('AM', "RADIO1", font=('Calibri 24'), pad=(10, 0),
                      default=True),
             sg.Radio('PM', "RADIO1", font=('Calibri 24'), pad=(10, 0)),
             sg.Text("spacer", pad=(25, 0), text_color=('white')),
             sg.Button('Save', font=('Helvetica 20'), size=(20, 1),
                       pad=(0, 25), key='_SAVE_'),
             sg.Ok('Done', font=('Helvetica 20'), size=(20, 1),
                   pad=(5, 25), key='_DONE_')],
        ]
        self.window = sg.Window('Appointments', self.layout, size=(900, 775),
                                element_justification='c', keep_on_top=True)

    def getDay(self):
        return days[self.index]

    def NextDay(self):
        self.index = self.index + 1
        self.window.Element('_DAY_').Update(days[self.index])
        self.window.Element('_NAME0_').Update(namesdict[days[self.index]][0])
        self.window.Element('_NAME1_').Update(namesdict[days[self.index]][1])
        self.window.Element('_NAME2_').Update(namesdict[days[self.index]][2])
        self.window.Element('_NAME3_').Update(namesdict[days[self.index]][3])
        self.window.Element('_NAME4_').Update(namesdict[days[self.index]][4])
        self.window.Element('_NAME5_').Update(namesdict[days[self.index]][5])
        self.window.Element('_NAME6_').Update(namesdict[days[self.index]][6])
        self.window.Element('_NAME7_').Update(namesdict[days[self.index]][7])
        self.window.Element('_NAME8_').Update(namesdict[days[self.index]][8])

    def PreviousDay(self):
        self.index = self.index - 1
        self.window.Element('_DAY_').Update(days[self.index])
        self.window.Element('_NAME0_').Update(namesdict[days[self.index]][0])
        self.window.Element('_NAME1_').Update(namesdict[days[self.index]][1])
        self.window.Element('_NAME2_').Update(namesdict[days[self.index]][2])
        self.window.Element('_NAME3_').Update(namesdict[days[self.index]][3])
        self.window.Element('_NAME4_').Update(namesdict[days[self.index]][4])
        self.window.Element('_NAME5_').Update(namesdict[days[self.index]][5])
        self.window.Element('_NAME6_').Update(namesdict[days[self.index]][6])
        self.window.Element('_NAME7_').Update(namesdict[days[self.index]][7])
        self.window.Element('_NAME8_').Update(namesdict[days[self.index]][8])


class DisplayWindow:
    def __init__(self):
        self.index = 0
        self.timecolumn = [
            [sg.Text(
                'Horraire',
                font=(head),
                justification='center',
                background_color='dark grey',
                size=(10, 1),
                pad=(0, 7))],
            [sg.Text(
                ' 8:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                ' 8:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                ' 9:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                ' 9:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '10:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '10:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '11:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '11:30',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))],
            [sg.Text(
                '12:00',
                font=(reg),
                justification='center',
                size=(10, 1),
                pad=(0, 5))]
        ]
        self.namecolumn = [
            [sg.Text('Patient', font=(head), justification='center',
                     background_color='dark grey', size=(25, 1), pad=(0, 7))],
            [sg.Text(namesdict[days[self.index]][0], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME0_')],
            [sg.Text(namesdict[days[self.index]][1], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME1_')],
            [sg.Text(namesdict[days[self.index]][2], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME2_')],
            [sg.Text(namesdict[days[self.index]][3], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME3_')],
            [sg.Text(namesdict[days[self.index]][4], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME4_')],
            [sg.Text(namesdict[days[self.index]][5], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME5_')],
            [sg.Text(namesdict[days[self.index]][6], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME6_')],
            [sg.Text(namesdict[days[self.index]][7], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME7_')],
            [sg.Text(namesdict[days[self.index]][8], font=(reg),
                     size=(25, 1), pad=(0, 5), key='_NAME8_')],
        ]
        self.layout = [
            [sg.Button(
                'Previous',
                font=('Helvetica 15'),
                pad=(20, 0),
                key='_PREVIOUS_'),

                sg.Text(
                    text=days[self.index],
                    font=(head),
                    justification='center',
                    size=(10, 1),
                    pad=(60, 5),
                    key='_DAY_'),

                sg.Button(
                    'Next',
                    font=('Helvetica 15'),
                    pad=(20, 0),
                    key='_NEXT_')],

            [sg.Column(self.timecolumn), sg.Column(self.namecolumn)],
            [sg.Radio('AM', "RADIO1", font=('Calibri 24'), default=True),
             sg.Radio('PM', "RADIO1", font=('Calibri 24'), pad=(10, 0)),
             sg.Button('Edit', font=('Helvetica 20'), size=(20, 1),
                       pad=(180, 10), key='_EDIT_')],
            [sg.Text("spacer", pad=(57, 0), text_color=('white')),
             sg.Button('Weekly view', font=('Helvetica 20'), size=(20, 1),
                       pad=(200, 0), key='_WEEKLY_')]
        ]
        self.window = sg.Window('Appointments', self.layout, size=(900, 775),
                                element_justification='c', keep_on_top=True,
                                location=(300, 0))

    def NextDay(self):
        self.index = self.index + 1
        self.window.Element('_DAY_').Update(days[self.index])
        self.window.Element('_NAME0_').Update(namesdict[days[self.index]][0])
        self.window.Element('_NAME1_').Update(namesdict[days[self.index]][1])
        self.window.Element('_NAME2_').Update(namesdict[days[self.index]][2])
        self.window.Element('_NAME3_').Update(namesdict[days[self.index]][3])
        self.window.Element('_NAME4_').Update(namesdict[days[self.index]][4])
        self.window.Element('_NAME5_').Update(namesdict[days[self.index]][5])
        self.window.Element('_NAME6_').Update(namesdict[days[self.index]][6])
        self.window.Element('_NAME7_').Update(namesdict[days[self.index]][7])
        self.window.Element('_NAME8_').Update(namesdict[days[self.index]][8])

    def PreviousDay(self):
        self.index = self.index - 1
        self.window.Element('_DAY_').Update(days[self.index])
        self.window.Element('_NAME0_').Update(namesdict[days[self.index]][0])
        self.window.Element('_NAME1_').Update(namesdict[days[self.index]][1])
        self.window.Element('_NAME2_').Update(namesdict[days[self.index]][2])
        self.window.Element('_NAME3_').Update(namesdict[days[self.index]][3])
        self.window.Element('_NAME4_').Update(namesdict[days[self.index]][4])
        self.window.Element('_NAME5_').Update(namesdict[days[self.index]][5])
        self.window.Element('_NAME6_').Update(namesdict[days[self.index]][6])
        self.window.Element('_NAME7_').Update(namesdict[days[self.index]][7])
        self.window.Element('_NAME8_').Update(namesdict[days[self.index]][8])


class WeekView:
    def __init__(self):
        self.index = 0
        self.timecolumn = [
            [sg.Text(
                ' 8:00',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(5, 10))],
            [sg.Text(
                ' 8:30',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                ' 9:00',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                ' 9:30',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                '10:00',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                '10:30',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                '11:00',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                '11:30',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))],
            [sg.Text(
                '12:00',
                font=(reg),
                justification='center',
                size=(4, 1),
                pad=(0, 10))]
        ]
        self.spacer = [
            [sg.Text(
                ' 8:00',
                font=(reg),
                justification='center',
                size=(3, 1),
                text_color='white',
                pad=(10, 10))]]
        self.line2 = [[sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0),
                               text_color='white')]]
        self.line = [[sg.Text('|', font=(reg), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))],
                     [sg.Text('|', font=(reg), size=(1, 1), pad=(0, 0))]
                     ]
        self.namecolumn = [
            [sg.Text(namesdict[j][i], font=(reg),
                     justification='center',
                     size=(11, 1), pad=(5, 10), background_color='light grey')
             for j in days]
            for i in range(9)]
        self.layout = [
            [sg.Column(self.spacer), sg.Column(self.line2, pad=(0, 0)),
                sg.Button(
                    'Lundi',
                    font=(reg),
                    size=(10, 1),
                    pad=(15, 1),
                    button_color=('black', 'light blue'),
                    key='_MONDAY_'),
                sg.Button(
                    'Mardi',
                    font=(reg),
                    size=(10, 1),
                    pad=(10, 1),
                    button_color=('black', 'light blue'),
                    key='_TUESDAY_'),
                sg.Button(
                    'Merc.',
                    font=(reg),
                    size=(10, 1),
                    pad=(15, 1),
                    button_color=('black', 'light blue'),
                    key='_WEDNESDAY_'),
                sg.Button(
                    'Jeudi',
                    font=(reg),
                    size=(10, 1),
                    pad=(10, 1),
                    button_color=('black', 'light blue'),
                    key='_THURSDAY_'),
                sg.Button(
                    'Vend.',
                    font=(reg),
                    size=(10, 1),
                    pad=(13, 1),
                    button_color=('black', 'light blue'),
                    key='_FRIDAY_')
             ],
            [sg.Column(self.timecolumn, pad=(0, 0)),
             sg.Column(self.line, pad=(0, 0)),
             sg.Column(self.namecolumn, pad=(0, 0))
             ],
            [sg.Radio('AM', "RADIO1", font=(reg), default=True, pad=(20, 25)),
             sg.Radio('PM', "RADIO1", font=(reg), pad=(0, 25))]
            # size(width, height)
        ]
        self.window = sg.Window('Appointments', self.layout, size=(1440, 775),
                                element_justification='l')


def Daily():
    index = 0
    edit = EditWindow()
    display = DisplayWindow()
    while True:
        event, values = display.window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '_NEXT_':
            try:
                display.NextDay()
            except IndexError:
                pass
        if event == '_PREVIOUS_':
            try:
                display.PreviousDay()
            except IndexError:
                pass
        if event == '_WEEKLY_':
            display.window.close()
            Weekly()
        if event == '_EDIT_':
            display.window.close()
            while True:
                event, values = edit.window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == '_NEXT_':
                    try:
                        when = edit.getDay()
                        for x in list1:
                            namesdict[when][index] = values[x]
                            index = index + 1
                        index = 0
                        edit.NextDay()
                    except IndexError:
                        pass
                if event == '_PREVIOUS_':
                    index = index - 1
                    try:
                        when = edit.getDay()
                        for x in list1:
                            namesdict[when][index] = values[x]
                            index = index + 1
                        index = 0
                        edit.PreviousDay()
                    except IndexError:
                        pass
                if event == '_SAVE_':
                    # print(values)
                    when = edit.getDay()
                    for x in list1:
                        namesdict[when][index] = values[x]
                        index = index + 1
                        # print(x)
                        # print(index)
                        # print(values[x])
                    index = 0
                if event == '_DONE_':
                    edit.window.close()
                    del display
                    del edit
                    try:
                        Daily()
                    except UnboundLocalError:
                        pass


def Weekly():
    week = WeekView()
    while True:
        event, values = week.window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in ('_MONDAY_', '_TUESDAY_', '_WEDNESDAY_', '_THURSDAY_',
                     '_FRIDAY_'):
            week.window.close()
            Daily()


try:
    Daily()
except UnboundLocalError:
    pass
