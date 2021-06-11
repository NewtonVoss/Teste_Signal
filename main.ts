input.onButtonPressed(Button.A, function () {
    radio.sendString("X")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.pause(100)
    basic.clearScreen()
})
radio.setGroup(12)
radio.setTransmitPower(1)
