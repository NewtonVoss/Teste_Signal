input.onButtonPressed(Button.A, function () {
    radio.sendString("X")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.pause(1000)
    basic.clearScreen()
    basic.showNumber(radio.receivedPacket(RadioPacketProperty.SignalStrength) + 128)
    basic.pause(1000)
    basic.clearScreen()
})
radio.setGroup(2)
radio.setTransmitPower(2)
