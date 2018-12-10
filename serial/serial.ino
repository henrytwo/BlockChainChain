#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
Servo servo;

int lockLED = 2;
int ulockLED = 3;
String str = "";
int button = 12;
int buttonState = 0;
boolean overRide = false;
boolean meh = false;

//---------------- help list -----------------------------------------
void printHelp(void){
  Serial.println();
  Serial.println("lock - Lock Device");
  Serial.println("unlock - Unlock Device");
  Serial.println("status - Current Status Of Lock");
  }

//---------------- setup ---------------------------------------------
void setup(){
  Serial.begin(9600);
  pinMode(lockLED, OUTPUT);
  pinMode(ulockLED, OUTPUT);
  servo.attach(13);
  pinMode(button, INPUT);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Hello there!");
  delay(500);
  lcd.clear();
  Serial.flush();
  //printHelp();
}

//--------------- loop ----------------------------------------------- 
void loop(){
  buttonState = digitalRead(button);
  
  if (buttonState == HIGH){
      if (overRide == false && meh == true){
        meh = false;
        digitalWrite(lockLED, HIGH);
        digitalWrite(ulockLED, LOW);
        lcd.setCursor(0,0);
        lcd.print("Device Status:");
        lcd.setCursor(0,1);
        lcd.print("Locked");
        servo.write(30);
        delay(1000);
        lcd.clear();
      } else {
        meh = true;
        digitalWrite(ulockLED, HIGH);
        digitalWrite(lockLED, LOW);
        lcd.setCursor(0,0);
        lcd.print("Device Status:");
        lcd.setCursor(0,1);
        lcd.print("Unlocked");
        servo.write(80);
        delay(1000);
        lcd.clear();
      }
  }
  
  if (Serial.available() > 0){
    str = Serial.readStringUntil('\n');
    Serial.flush();

    if (str == "lock"){
      overRide = false;
      digitalWrite(lockLED, HIGH);
      digitalWrite(ulockLED, LOW);
      lcd.setCursor(0,0);
      lcd.print("Device Status:");
      lcd.setCursor(0,1);
      lcd.print("Locked");
      servo.write(30);
      delay(1000);
      lcd.clear();
    }
    
    else if (str == "unlock"){
      overRide = true;
      digitalWrite(ulockLED, HIGH);
      digitalWrite(lockLED, LOW);
      lcd.setCursor(0,0);
      lcd.print("Device Status:");
      lcd.setCursor(0,1);
      lcd.print("Unlocked");
      servo.write(80);
      delay(1000);
      lcd.clear();
    }
    
    else if (str == "status"){
      if (digitalRead(lockLED) == HIGH){
        Serial.println("true");  
      }
      else {
        Serial.println("false");  
      }
    }
    
    else {
      Serial.println(str);
      lcd.setCursor(0,0);
      lcd.print("Invalid");
      lcd.setCursor(0,1);
      lcd.print("Command!");
      delay(1000);
      lcd.clear();
    }
  }
}

