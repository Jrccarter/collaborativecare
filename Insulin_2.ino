int Xin= A0; // X Input Pin -- usually 510
int Yin = A1; // Y Input Pin -- usually 489
int KEYin = 3; // Push Button
const int buttonPin = 13;     // the number of the pushbutton pin
int buttonState = 0;         // variable for reading the pushbutton status


void setup ()
{
  pinMode (KEYin, INPUT);
  Serial.begin (9600);
  //pinMode(13, OUTPUT); 
//  pinMode(buttonPin, INPUT);
  
}
void loop ()
{
  int xVal, yVal, buttonVal;
//  buttonState = digitalRead(buttonPin);
  xVal = analogRead (Xin);
  yVal = analogRead (Yin);
  buttonVal = digitalRead (KEYin);
//  if (buttonState == HIGH) {
//    Serial.println("FOOD IS ABOUT TO DISRUPT BLOOD SUGAR LEVEL");
//    int ran = random(90, 120); //random average blood sugar level
//    lights(ran);
//    }

  if(xVal > 1000){ //just ate or something so create insulin
    Serial.println("BLOOD SUGAR IS HIGH");
    int ran = random(120, 180); //random high blood sugar level
    Serial.println("INSULIN RELEASED");
    lights(ran);
    Serial.println("INSULIN COMPLETE");
    }
    
    
}
void lights(int levels){
  for(int y = levels; y >= 120; y = y - (y/13)){
    String correct = String(y);
    Serial.println("Your blood sugar level is " + correct);
    for(int i =11; i > 0; i--){
       digitalWrite(i, HIGH); 
       delay(100);
       digitalWrite(i, LOW);  
       delay(100);
      }
  }
  
  }
