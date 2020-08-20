import panel as pn

text_style = {'font-family': "Optimist"}

#Markdown
markdown_dict = {}
markdown_dict['overall_header'] = pn.pane.Markdown('# Navigation App', style = text_style)
markdown_dict['add_points'] = pn.pane.Markdown('## Add Points of Interest', style = text_style)
markdown_dict['line_separator'] = pn.pane.Markdown('---', style=text_style)


#Markdown status
markdown_dict['mapping_progress'] = pn.pane.Markdown('', style = text_style, name='Map Status Markdown')



#Radio Button

#Buttons
button_dict = {}
button_dict['add_address'] = pn.widgets.Button(name = 'Add Address to Points of Interest', button_type = 'success')
button_dict['map_poi'] = pn.widgets.Button(name = 'Map Points of Interest', button_type = 'primary')

#Text input
text_input_dict = {}
text_input_dict['address_input'] = pn.widgets.TextInput(name = 'Address: ', value = '', sizing_mode = 'stretch_width')

text_input_dict['address_query_display'] = pn.widgets.TextInput(name = 'Address Found: ', value = '', height = 100, sizing_mode = 'stretch_width', disabled=True, aspect_ratio = 'auto')

text_input_dict['all_addresses_display'] = pn.widgets.TextInput(name = 'Current Points of Interest: ', value = '', height = 100, width_policy='max', disabled=True)

#Strings
strings_dict = {}
strings_dict['current_poi'] = pn.pane.Str('Current Points of Interest:', style = text_style)
strings_dict['all_addresses_display'] = pn.pane.Str('', style = text_style, sizing_mode = 'stretch_both')


#Colors
color_dict = {}
color_dict['color_dk_blue'] = "#003A6F"
color_dict['color_red'] = "#A12830"
color_dict['color_gray'] = "#808080"
color_dict['color_yellow'] = "#FFE512"
color_dict['color_green'] = "#00AB39"
color_dict['color_pink'] = "#C41E99"
color_dict['color_orange'] = "#FF5C00"
color_dict['color_lt_blue'] = "#00A7D4"
color_dict['color_purple'] = "#6C1B72"
color_dict['color_dk_green'] = "#0080000"