input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
let temp = 0
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
basic.forever(function () {
	
})
basic.forever(function () {
    temp = input.temperature()
    if (temp >= 22) {
        music.playMelody("G F G A G F E D ", 300)
    }
})
