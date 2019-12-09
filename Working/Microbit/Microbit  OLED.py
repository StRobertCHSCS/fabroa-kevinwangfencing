from microbit import*

#include <SPI.h>
#include <wire.h>
#include <Adafruit_GFX.h>
#include Adafruit_SSD1306
#define OLED_RESET 4

Adafruit_SSD1306.display(OLED_RESET);

void OLED_setup():
(pin 1: G)
(pin 2: VC)
(pin 3: TX)
(pin 4: NC)
{
    Serials.begins (9600);
    display.begins(SSD1306_SWITCHCAPVCC, 0x3c);
    display.clearDisplay();// text display tests
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0,0);
    display.println("HELLO,world!");
    display.setTextColor(BLACK,WhITE);//&#039;inverted&#039;text
    display.println(3.141592);
    display.setTextSize(2);
    display.setTextColor(WHITE);
    display.print("0x");
    display.println(0xDEADBEEF,HEX);
    display.display();
    display.clearDisplay();
}
void loop()
{
}