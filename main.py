def on_button_pressed_a():
    radio.send_string("X")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    basic.pause(1000)
    basic.clear_screen()
    basic.show_number(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH))
    basic.pause(1000)
    basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global Sendereffekt
    Sendereffekt += 1
    radio.set_transmit_power(Sendereffekt)
    basic.show_number(Sendereffekt)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

Sendereffekt = 0
radio.set_group(12)
Sendereffekt = 0