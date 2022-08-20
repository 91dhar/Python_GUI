import PySimpleGUI as sg

layout = [
	[
		sg.Input(key = '-INPUT-'),
		sg.Spin(['KM to Mile','KG to Pound','Seconds to Minutes'], key = '-UNITS-'), 
		sg.Button('Convert', key = '-CONVERT-')
	],
	[sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window('Converter',layout)

while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-CONVERT-':
		input_value = values['-INPUT-']
		if input_value.isnumeric():
			match values['-UNITS-']:
				case 'KM to Mile':
					output = round(float(input_value) * 0.6214,2)
					output_string = f'{input_value} KM are {output} Miles.'
				case 'KG to Pound':
					output = round(float(input_value) * 2.20462,2)
					output_string = f'{input_value} KG are {output} Pounds.'
				case 'Seconds to Minutes':
					output = round(float(input_value) / 60,2)
					output_string = f'{input_value} Seconds are {output} Minutes.'

			window['-OUTPUT-'].update(output_string, text_color='yellow')
		else:
			window['-OUTPUT-'].update('Please enter a number', text_color='yellow')

window.close()