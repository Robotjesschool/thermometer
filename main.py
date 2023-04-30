def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

temp = 0
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
""")

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global temp
    temp = input.temperature()
    if temp >= 22:
        music.play_melody("G F G A G F E D ", 300)
basic.forever(on_forever2)
