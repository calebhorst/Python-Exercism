resistor_color_dict = {
"Black": 0,
"Brown": 1,
"Red": 2,
"Orange": 3,
"Yellow": 4,
"Green": 5,
"Blue": 6,
"Violet": 7,
"Grey": 8,
"White": 9
}

def color_code(color):
    return resistor_color_dict[color.capitalize()]


def colors():
     return [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
