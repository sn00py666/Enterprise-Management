from interface import Interface
import serial


def ard(app: Interface):
    # arduino = serial.Serial('COM3', 9600)
    # data = arduino.readline().decode().strip()

    com = input()

    # Если получен сигнал от Arduino, выполните соответствующее действие
    # if data == 'Button_pressed':
    if com == "1":
        app.change_background()


app = Interface()
ard(app)
