#define LED 13

void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  digitalWrite (LED_BUILTIN, LOW);
  Serial.println("Hi!, I am Arduino");
}

void loop() {
  if(Serial.available()){
    
     
    
    char data = Serial.read();
    

    if (data == '1')
      digitalWrite (LED_BUILTIN, HIGH);

    if (data == '0')
      digitalWrite (LED_BUILTIN, LOW);
  }
} 
