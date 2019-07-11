#include <Wire.h>

void setup()
{
    Serial.begin(115200);  // Setup serial output to 115.2k
    Wire.begin();  // Initialize I2C communication
    write(0x6B, 0); //Initialize Power Manager Register to 0
    write(0x6A, 0);  // Disable master I2C, enable value is 0x20, so disable it should be just bit 5 = 0, since I don't use other bits and they are all 0.
    write(0x37, 0x02); // Enable bypass mode
    writeMag(0x0A, 0x12); // Setup magnetic sensor to measure contiuously.
}

void loop()
{
    int xh = readMag(0x04); // read x axis, high byte
    int xl = readMag(0x03); // read x axis, lowbyte
    int yh = readMag(0x06);
    int yl = readMag(0x05);
    int zh = readMag(0x08);
    int zl = readMag(0x07);
              readMag(0x09); //This tells the Mag Module to take another measurement. 
    // Combine the values 
    int x = (xh << 8) | (xl & 0xff);
    int y = (yh << 8) | (yl & 0xff);
    int z = (zh << 8) | (zl & 0xff);
    // Print out 
    Serial.print("X,Y,Z=");
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(z);
   // delay(1000); 
}

byte read(int reg)
{
    Wire.beginTransmission(0x68); // starting the transmission to sensor address 0x68
    Wire.write(reg);
    Wire.endTransmission(false);
    Wire.requestFrom(0x68, 1, false); // requestone byte of data
    byte val = Wire.read();
    Wire.endTransmission(true);
    return val;
}

void write(int reg, int data)
{
    Wire.beginTransmission(0x68); // starting the transmission to sensor address 0x68
    Wire.write(reg);
    Wire.write(data);
    Wire.endTransmission(true);
}

byte readMag(int reg)
{
    Wire.beginTransmission(0x0C);
    Wire.write(reg);
    Wire.endTransmission(false);
    Wire.requestFrom(0x0C, 1, false); // requestone byte of data
    byte val = Wire.read();
    Wire.endTransmission(true);
    return val;
}

void writeMag(int reg, int data)
{
    Wire.beginTransmission(0x0C);
    Wire.write(reg);
    Wire.write(data);
    Wire.endTransmission(true);
}
