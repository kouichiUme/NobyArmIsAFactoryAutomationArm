const Gpio = require('pigpio').Gpio;
 
const led = new Gpio(17, {mode: Gpio.OUTPUT});
//17
//18
//22
//23
//24
//27
let dutyCycle = 0;
console.log(led.getFrequency());
 
setInterval(() => {
  led.pwmWrite(dutyCycle);
 
  dutyCycle += 5;
  if (dutyCycle > 255) {
    dutyCycle = 0;
  }
}, 20);
