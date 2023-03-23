"""File to store all numerical variables. These can be freely changed
without breaking any files."""

background_color = (184, 180, 176)
light, dark, select_color = (237, 199, 190), (115, 88, 81), (245, 188, 88)
width, height = 80, 80
screen_width, screen_height = 750, 800
total_time = 302 * 1000 # milliseconds
x_offset = (screen_width - (width * 8)) / 2
y_offset = (screen_height - (height * 8)) / 2
x_labels = ['a','b','c','d','e','f','g','h']
y_labels = ['8','7','6','5','4','3','2','1']
player_2_location = (x_offset, y_offset - 45)
player_1_location = (x_offset, y_offset + height*8 + 35)
initial_state = [
    ['bR', 'bK', 'bB', 'bQ', 'bG', 'bB', 'bK', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wK', 'wB', 'wQ', 'wG', 'wB', 'wK', 'wR']
]
