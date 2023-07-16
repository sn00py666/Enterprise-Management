import serial
from tkinter import Tk, Canvas, Button, PhotoImage
import threading


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1024x600")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.button_image_Settings = \
            PhotoImage(file="./Assets/Images/button_1.png")
        self.buttonSettings = Button(
            image=self.button_image_Settings,
            borderwidth=0,
            highlightthickness=0,
            command=self.change_background,
            relief="flat"
        )
        self.buttonSettings.place(
            x=8.999999999999972,
            y=416.0,
            width=66.0,
            height=66.0)

        self.button_image_Charts = \
            PhotoImage(file="./Assets/Images/button_2.png")
        self.buttonCharts = Button(
            image=self.button_image_Charts,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_charts,
            relief="groove"
        )
        self.buttonCharts.place(
            x=8.999999999999972,
            y=311.0,
            width=64.0,
            height=72.0)

        self.button_imageInfo = PhotoImage(file="./Assets/Images/button_3.png")
        self.buttonInfo = Button(
            image=self.button_imageInfo,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_info,
            relief="flat"
        )
        self.buttonInfo.place(
            x=8.999999999999972,
            y=107.0,
            width=66.0,
            height=66.0)

        self.button_imagepParametrs = \
            PhotoImage(file="./Assets/Images/button_4.png")
        self.buttonParametrs = Button(
            image=self.button_imagepParametrs,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_parametrs,
            relief="flat"
        )
        self.buttonParametrs.place(
            x=9.999999999999972,
            y=209.0,
            width=62.0,
            height=68.0)

        self.button_imageOff = PhotoImage(file="./Assets/Images/button_5.png")
        self.buttonOff = Button(
            image=self.button_imageOff,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_off,
            relief="flat"
        )
        self.buttonOff.place(
            x=7.999999999999972,
            y=519.0,
            width=66.0,
            height=66.0)

        self.canvas.create_text(
            375.0,
            471.0,
            anchor="nw",
            text="15%",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            409.0,
            522.0,
            anchor="nw",
            text="50",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            893.0,
            518.0,
            anchor="nw",
            text="150",
            fill="#000000",
            font=("Inter Medium", 30 * -1)
        )

        self.canvas.create_text(
            824.0,
            284.0,
            anchor="nw",
            text="50",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            847.0,
            316.0,
            anchor="nw",
            text="51",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            801.0,
            349.0,
            anchor="nw",
            text="52",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            538.0,
            284.0,
            anchor="nw",
            text="8",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            561.0,
            316.0,
            anchor="nw",
            text="9",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            515.0,
            349.0,
            anchor="nw",
            text="10",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            241.99999999999997,
            284.0,
            anchor="nw",
            text="5",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            265.0,
            316.0,
            anchor="nw",
            text="6",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            218.99999999999997,
            349.0,
            anchor="nw",
            text="7",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        # Создаем задний фон и интерфейс, подгружаем фото
        self.image_Background_Turbo = \
            PhotoImage(file="./Assets/Images/Background_Turbo.png")
        self.image_image_1 = PhotoImage(file="./Assets/Images/image_1.png")
        self.background = self.image_image_1
        self.image_1 = self.canvas.create_image(
            508.0, 292.0,
            image=self.background)

        self.image_Interface_Turbo = \
            PhotoImage(file="./Assets/Images/Interface_Turbo.png")
        self.image_image_2 = PhotoImage(file="./Assets/Images/image_2.png")
        self.ColorInterface = self.image_image_2
        self.image_2 = self.canvas.create_image(
            512.0, 307.0,
            image=self.ColorInterface)

        self.window.resizable(False, False)

        self.arduino = serial.Serial('COM3', 9600)
        # self.listen_for_arduino()

        # Запускаем прослушивание Arduino в отдельном потоке
        thread = threading.Thread(target=self.listen_for_arduino)
        thread.daemon = True
        thread.start()

        self.window.mainloop()

    def listen_for_arduino(self):
        # Запустите цикл прослушивания сигналов от Arduino

        data = self.arduino.readline().decode().strip()

        # Если получен сигнал от Arduino, выполните соответствующее действие
        if data == 'Button_pressed':
            self.change_background()

    def button_off(self):
        print("button_off")

    def change_background(self):
        if self.background == self.image_image_1:
            self.canvas.delete(self.image_1)
            self.background = self.image_Background_Turbo
            self.image_1 = self.canvas.create_image(
                508.0, 292.0,
                image=self.background)

            self.canvas.delete(self.image_2)
            self.ColorInterface = self.image_Interface_Turbo
            self.image_2 = self.canvas.create_image(
                512.0, 307.0,
                image=self.ColorInterface)
        else:
            self.canvas.delete(self.image_1)
            self.background = self.image_image_1
            self.image_1 = self.canvas.create_image(
                508.0, 292.0,
                image=self.background)

            self.canvas.delete(self.image_2)
            self.ColorInterface = self.image_image_2
            self.image_2 = self.canvas.create_image(
                512.0, 307.0,
                image=self.ColorInterface)

    def button_charts(self):
        print("button_charts")

    def button_parametrs(self):
        print("button_parametrs")

    def button_info(self):
        print("button_info")
