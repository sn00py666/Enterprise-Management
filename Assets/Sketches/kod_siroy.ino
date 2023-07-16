#include <UTFT.h>

#define dispMISO    8
#define dispSCK     7
#define dispCS      6
#define dispRST     5
#define dispDC      4

#define disp2MISO    30
#define disp2SCK     37
#define disp2CS      35
#define disp2RST     33
#define disp2DC      31

extern uint8_t SmallFont[];
extern uint8_t BigFont[];
extern uint8_t SevenSegNumFont[];
extern uint8_t BigFontRus[];

UTFT myGLCD(TFT01_24SP, dispMISO, dispSCK, dispCS, dispRST, dispDC);


UTFT my2GLCD(TFT01_24SP, disp2MISO, disp2SCK, disp2CS, disp2RST, disp2DC);
                       
                          
int counter = 0;
int y = 0;
int sueta_state = 0;
int anti_state = 0;

const uint8_t EN    = 11;       
const uint8_t L_PWM = 12;        
const uint8_t R_PWM = 13;  

int val = 0;      // val will be used to store the state
                  // of the input pin
int old_val = 0;  // this variable stores the previous
                  // value of "val"
int state = 0;    // 0 = LED off and 1 = LED on

void setup() {
  Serial.begin(9600);
  digitalWrite(L_PWM, LOW ); 
  digitalWrite(R_PWM, HIGH);  
  pinMode(22, INPUT_PULLUP);
  pinMode(24, INPUT_PULLUP);
  pinMode(EN,    OUTPUT);    
  pinMode(L_PWM, OUTPUT);    
  pinMode(R_PWM, OUTPUT);  
  
  myGLCD.InitLCD();
  myGLCD.setBackColor (VGA_WHITE);                     // устанавливаем цвет заливки фона шрифта
  myGLCD.fillScr      (VGA_WHITE);                     // указываем цвет заливки экрана
   
  my2GLCD.InitLCD();
  my2GLCD.setBackColor (VGA_WHITE);                     // устанавливаем цвет заливки фона шрифта
  my2GLCD.fillScr      (VGA_WHITE);                     // указываем цвет заливки экрана

    myGLCD.setFont(BigFontRus);
    myGLCD.setColor(VGA_BLACK);

    my2GLCD.setFont(BigFontRus);
    my2GLCD.setColor(VGA_BLACK);

    
  myGLCD.textRus("РЫНОК НА СУТКИ ВПЕРЕД",  10, 10);                         // выводим текст в указанных координатах
  myGLCD.fillRect(0,30,320,35);                     

  
  my2GLCD.textRus("БАЛАНСИРУЮЩИЙ РЫНОК",  1, 10);                         // выводим текст в указанных координатах
  my2GLCD.fillRect(0,30,320,35);                     // рисуем закрашенный прямоугольник (с противоположными углами в координатах 10x170 - 150x230)
 
  myGLCD.textRus("Генерация =", 10, 70);                        
  my2GLCD.textRus("ЗАКУПКА =", 10, 70);                         // выводим текст в указанных координатах

 myGLCD.textRus("Прогноз =", 10, 140);                         // выводим текст в указанных координатах
 my2GLCD.textRus("ПРОГНОЗ =", 10, 140);                         // выводим текст в указанных координатах

 myGLCD.textRus("СТАТУС = ", 10, 200);                         // выводим текст в указанных координатах
 my2GLCD.textRus("СТАТУС = ", 10, 200);                         // выводим текст в указанных координатах

  myGLCD.textRus("мвт/ч", 200, 140);                         // выводим текст в указанных координатах


 
pinMode(39, OUTPUT);
pinMode(41, OUTPUT);
pinMode(43, OUTPUT);
pinMode(45, OUTPUT);
pinMode(47, OUTPUT);
pinMode(49, OUTPUT);
pinMode(51, OUTPUT);
pinMode(53, OUTPUT);

}

void loop() {
    
val = digitalRead(24);
val = !val;
if ((val == HIGH) && (old_val == LOW)){
    state = 1 - state;
  }
   if (val != old_val){

    myGLCD.setColor(VGA_WHITE);
    myGLCD.fillRect(150,200,320,240);                     // рисуем закрашенный прямоугольник (с противоположными углами в координатах 10x170 - 150x230)
   
   my2GLCD.setColor(VGA_WHITE);
     my2GLCD.fillRect(150,200,320,240);                     // рисуем закрашенный прямоугольник (с противоположными углами в координатах 10x170 - 150
   }
   // - МЕСТО КОТОРОЕ ТРЕБУЕТ ПОЯСНЕНИЙ -

  old_val = val; 

   // В переменную old_val записываем значение val, которое при нажатии кнопки получило значение HIGH  
   // Все ли верно до этого места в рассуждениях?

   // Если после инверсии state будет иметь состояние логической истинны, то включаем либо выключаем LED

  if (state == 1) {
   my2GLCD.setFont(BigFontRus);
 myGLCD.setFont(BigFontRus);
     myGLCD.setFont(BigFontRus);
    myGLCD.setColor(VGA_RED);
    my2GLCD.setColor(VGA_RED);
      myGLCD.textRus("ГЕНЕРАЦИЯ", 150, 200);                         // выводим текст в указанных координатах
 my2GLCD.textRus("ЗАКУПКА ", 150, 200);                         // выводим текст в указанных координата
 Serial.println(1);
  } 
  else {
   my2GLCD.setFont(BigFontRus);
     myGLCD.setFont(BigFontRus);
    myGLCD.setColor(VGA_GREEN);
    my2GLCD.setColor(VGA_GREEN);
      myGLCD.textRus("ЗАКУПКА ", 150, 200);                         // выводим текст в указанных координатах
 my2GLCD.textRus("не работает", 150, 200);                         // выводим текст в указа
 Serial.println(2);

 my2GLCD.setFont(BigFontRus);
myGLCD.setFont(BigFont);
 myGLCD.printNumI(533, 170, 140,  1,  '0');     
 my2GLCD.printNumI(0, 180, 120,  1,  '0');     
     
  }
//anti_state = digitalRead(22);

//if (sueta_state == 0){ 
 //my2GLCD.setFont(BigFontRus);
   // my2GLCD.setColor(VGA_BLACK);
     //myGLCD.setFont(BigFontRus);
    //myGLCD.setColor(VGA_BLACK);
 // myGLCD.textRus("Суета", 10, 200);                         // выводим текст в указанных координатах
 //my2GLCD.textRus("Суета", 10, 200);                         // выводим текст в указанных координатах
//}


//if (anti_state == 0){
  
 //my2GLCD.setFont(BigFontRus);
   // my2GLCD.setColor(VGA_BLACK);
    //my2GLCD.drawRect(10,20,150,80);
     //myGLCD.setFont(BigFontRus);
    //myGLCD.setColor(VGA_BLACK);
     // myGLCD.textRus("СТАТУС = ВЫРОБОТКА", 10, 200);                         // выводим текст в указанных координатах
// my2GLCD.textRus("СТАТУС = неиспользуется", 10, 200);                         // выводим текст в указанных координатах
//}


 analogWrite(EN, counter);

//y = map(counter, 0, 255, 0, 50);


     if (y >= 10 ){
counter = 0;
my2GLCD.setFont(SevenSegNumFont);
myGLCD.setFont(SevenSegNumFont);
 myGLCD.printNumI(y, 200, 50,  2,  '0');     
 my2GLCD.printNumI(y, 250, 50,  2,  '0');     
     
  }
     else{
      my2GLCD.setFont(SevenSegNumFont);
      myGLCD.setFont(SevenSegNumFont);
myGLCD.printNumI(y, 200, 50,  1,  '0');
my2GLCD.printNumI(y, 200, 50,  1,  '0');
    

      counter = counter + 1;
      if (counter >= 250){
counter = 0;
      }
      }


   }
