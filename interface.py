import serial
import time
from tkinter import Tk, Canvas, Button, PhotoImage
import threading


class Interface:
    def __init__(self):
        
        self.sueta_status = "off"
        self.window = Tk()
        self.window.geometry("800x480")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.button_image_Settings_black = PhotoImage(file="./Assets/Images/button_settings_black.png")
        self.button_image_Settings_white = PhotoImage(file="./Assets/Images/button_settings_white.png")
        self.buttonSettings = Button(
            image=self.button_image_Settings_white,
            borderwidth=0,
            highlightthickness=0,
            command=self.change_background,
            relief="flat"
        )
        self.buttonSettings.place(
            x=5.0,
            y=324.0,
            width=50.0,
            height=50.0)
        
        self.image_sueta = PhotoImage(file="./Assets/Images/sueta_white.png")

        self.button_image_Charts_black = PhotoImage(file="./Assets/Images/button_charts_black.png")
        self.button_image_Charts_white = PhotoImage(file="./Assets/Images/button_charts_white.png")
        self.buttonCharts = Button(
            image=self.button_image_Charts_white,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_charts,
            relief="groove"
        )
        self.buttonCharts.place(
            x=5.0,
            y=236.0,
            width=50.0,
            height=50.0)

        self.button_image_Info_black = PhotoImage(file="./Assets/Images/button_info_black.png")
        self.button_image_Info_white = PhotoImage(file="./Assets/Images/button_info_white.png")
        self.buttonInfo = Button(
            image=self.button_image_Info_white,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_info,
            relief="flat"
        )
        self.buttonInfo.place(
            x=5.0,
            y=62.0,
            width=50.0,
            height=50.0)

        self.button_imagep_Parametrs_black = PhotoImage(file="./Assets/Images/button_parametrs_black.png")
        self.button_imagep_Parametrs_white = PhotoImage(file="./Assets/Images/button_parametrs_white.png")
        self.buttonParametrs = Button(
            image=self.button_imagep_Parametrs_white,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_parametrs,
            relief="flat"
        )
        self.buttonParametrs.place(
            x=5.0,
            y=150.0,
            width=50.0,
            height=50.0)

        self.button_imageOff_black = PhotoImage(file="./Assets/Images/button_off_black.png")
        self.button_imageOff_white = PhotoImage(file="./Assets/Images/button_off_white.png")
        self.buttonOff = Button(
            image=self.button_imageOff_white,
            borderwidth=0,
            highlightthickness=0,
            command=self.change_text,
            relief="flat"
        )
        self.buttonOff.place(
            x=5.0,
            y=412.0,
            width=50.0,
            height=50.0)
        #
        #ТЕСТ ЗАМЕНЫ ТЕКСТА ПЕЕРЕМЕННЫМИ
        #
        
        # Создаем задний фон и интерфейс, подгружаем фото
        self.image_Background_Black = \
            PhotoImage(file="./Assets/Images/BG_BLACK.png")
        self.image_background_White = PhotoImage(file="./Assets/Images/BG_WHITE.png")
        self.background = self.image_background_White
        self.BG = self.canvas.create_image(
            400.0, 240.0,
            image=self.background)
        
        

        self.window.resizable(False, False)

        # self.arduino = serial.Serial('COM3', 9600)
        # self.listen_for_arduino()

        # Запускаем прослушивание Arduino в отдельном потоке

        # thread = threading.Thread(target=self.listen_for_arduino)
        # thread.daemon = True
        # thread.start()
        self.paint_text("#000000")
        self.window.mainloop()

    # def listen_for_arduino(self):
    #     # Запустите цикл прослушивания сигналов от Arduino
    #     while True:
    #         data = self.arduino.readline().decode().strip()

    #         # Если получен сигнал от Arduino, выполните соответствующее действие
    #         if data == 'Button_pressed':
    #             self.change_background()
    def paint_text(self, Fill_text):

        self.text1 = self.canvas.create_text(
            327.0,
            351.0,
            anchor="nw",
            text="15%",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            402.0,
            425.0,
            anchor="nw",
            text="150",
            fill=Fill_text,
            font=("Inter Medium", 30 * -1)
        )

        self.canvas.create_text(
            197.0,
            191.0,
            anchor="nw",
            text="1",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            215.0,
            224.0,
            anchor="nw",
            text="2",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            172.0,
            256.0,
            anchor="nw",
            text="3",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            681.0,
            191.0,
            anchor="nw",
            text="7",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            699.0,
            224.0,
            anchor="nw",
            text="8",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            656.0,
            256.0,
            anchor="nw",
            text="9",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            439.0,
            191.0,
            anchor="nw",
            text="4",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            457.0,
            224.0,
            anchor="nw",
            text="5",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            414.0,
            256.0,
            anchor="nw",
            text="6",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            353.0,
            386.0,
            anchor="nw",
            text="99",
            fill=Fill_text,
            font=("Inter Medium", 20 * -1)
        )

    def change_text(self):
        for i in range(100):
            self.text1_value = str(i)
            # Update the canvas text
            self.canvas.itemconfig(text=self.text1_value)
        self.text1_value = "15%"
        self.canvas.itemconfig(text=self.text1_value)

    def change_background(self):
        if self.background == self.image_background_White:
            # меняем цвет заднего фона
            self.canvas.delete(self.BG)
            self.background = self.image_Background_Black
            self.BG = self.canvas.create_image(
                400.0, 240.0,
                image=self.background)
            # меняем цвета кнопок

            self.buttonSettings.configure(image=self.button_image_Settings_black)
            self.buttonCharts.configure(image=self.button_image_Charts_black)
            self.buttonInfo.configure(image=self.button_image_Info_black)
            self.buttonParametrs.configure(image=self.button_imagep_Parametrs_black)
            self.buttonOff.configure(image=self.button_imageOff_black)
            self.paint_text("#ffffff")
            self.Change_sueta_color("./Assets/Images/sueta_black.png")

        else:
            self.canvas.delete(self.BG)
            self.background = self.image_background_White
            self.BG = self.canvas.create_image(
                400.0, 240.0,
                image=self.background)
            
            self.buttonSettings.configure(image=self.button_image_Settings_white)
            self.buttonCharts.configure(image=self.button_image_Charts_white)
            self.buttonInfo.configure(image=self.button_image_Info_white)
            self.buttonParametrs.configure(image=self.button_imagep_Parametrs_white)
            self.buttonOff.configure(image=self.button_imageOff_white)
            self.paint_text("#000000")
            self.Change_sueta_color("./Assets/Images/sueta_white.png")

    def button_charts(self):
        print("button_charts")

    def button_parametrs(self):
        if self.sueta_status == "off":
            self.sueta = self.canvas.create_image(
                485.0 + 90, 306 + 90,
                image=self.image_sueta,
            )

            self.sueta_status = "on"
            
        else:
            self.canvas.delete(self.sueta)
            self.sueta_status = "off"



    def button_info(self):
        print("button_info")

    def Change_sueta_color(self, image):
        if self.sueta_status == "on":
            self.image_sueta = PhotoImage(file=image)
            self
            self.sueta = self.canvas.create_image(
                    485.0 + 90, 306 + 90,
                    image=self.image_sueta
                )
            self.button_parametrs()
            self.button_parametrs()
        else:
            self.image_sueta = PhotoImage(file=image)