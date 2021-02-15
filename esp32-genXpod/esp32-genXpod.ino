
int yellowPin = 13;
int powerPin = 33;
int switchPin = 4;
int touchPin = 2;

int changed = 0;


int state = 0;
int play = 1;
int prevTouchVal = 0;
int touchVal = 0;

void setup() {
  Serial.begin(9600);
  pinMode(yellowPin, INPUT_PULLUP);
  pinMode(powerPin, INPUT_PULLUP);
  pinMode(switchPin, INPUT_PULLUP);
  digitalWrite(touchPin, HIGH);
}

void loop() {
  
  delay(500);
  
  touchVal = analogRead(touchPin); 
  if (touchVal < 1000 && touchVal > 0) {
    Serial.write(4);
    Serial.write('\n');
  }
  if (touchVal > 1000 && touchVal < 1300 && touchVal > 0) {
    Serial.write(5);
    Serial.write('\n');
  }
  
  
  
  if (digitalRead(switchPin) == HIGH) {
    
    if (state == 1 || state == 3) {
      state = 0;
      
      Serial.write(state);
      Serial.write('\n');
    }
    //Serial.println(0);

  }
  else {
    if (state == 0 || state == 2){
      state = 1;
      Serial.write(state);
      Serial.write('\n');
    }
    //Serial.println(1);
  }
  
  if (digitalRead(yellowPin) == LOW) {
    //Serial.println(9);
    if (state == 0) state = 2;
    else if (state == 1) state = 3;
    else if (state == 2) state = 0;
    else if (state == 3) state = 1;
    Serial.write(state);
    Serial.write('\n');
  }
 

  if (digitalRead(powerPin) == LOW) {
    Serial.write(8);
    Serial.write('\n');
    //Serial.print(8);
  }
  
}
