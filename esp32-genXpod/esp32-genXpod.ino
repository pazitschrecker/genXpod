int yellowPin = 26;
int bluePin = 35;
int switchPin = 4;
int touchPin = 2;

int changed = 0;


int state = 0;
int play = 1;
int prevTouchVal = 0;
int touchVal = 0;

void setup() {
  Serial.begin(9600);
  pinMode(yellowPin, INPUT);
  pinMode(bluePin, INPUT);
  pinMode(switchPin, INPUT);
  digitalWrite(touchPin, HIGH);
}

void loop() {
  
  delay(200);
  touchVal = analogRead(touchPin);
  //if (touchVal < 1000 && touchVal > 0) Serial.println("BACK \n");
  //if (touchVal > 1000 && touchVal < 1300 && touchVal > 0) Serial.println("NEXT \n");
  if (touchVal < 1000 && touchVal > 0) {
    Serial.write(4);
    Serial.write('\n');
  }
  if (touchVal > 1000 && touchVal < 1300 && touchVal > 0) {
    Serial.write(5);
    Serial.write('\n');
  }
  
  
  if (digitalRead(switchPin) == HIGH) {
    if (state == 0) {
      state = 1;
      Serial.write(state);
      Serial.write('\n');
    }
    else if (state == 2) {
      state = 3;
      Serial.write(state);
      Serial.write('\n');
    }
  }
  else {
    if (state == 1) {
      state = 0;
      Serial.write(state);
      Serial.write('\n');
    }
    else if (state == 3) {
      state = 2;
      Serial.write(state + '\n');
      Serial.write('\n');
    }
  }
  
  if (digitalRead(yellowPin) == LOW) {
    if (state == 0) state = 2;
    else if (state == 1) state = 3;
    else if (state == 2) state = 0;
    else if (state == 3) state = 1;
    Serial.write(state);
    Serial.write('\n');
    delay(200);
  }

  if (digitalRead(bluePin) == LOW) {
    play = (play + 1) % 2;
    if (play == 0) Serial.write("b");
    else Serial.write("n");
    delay(200);
  }

  //Serial.printf("Touch sensor: %d\n", touchVal);
 
  
  //delay(500);
}
