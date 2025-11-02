# 🥫 PiCan – Touchless Smart Trash Can with Raspberry Pi

> 🇬🇧 **This Description starts in English — Deutsche Version weiter unten 🇩🇪**

---

## 🇬🇧 English Description

**PiCan** turns the trash can into a smart, touchless bin powered by a **Raspberry Pi** OR **ESP32**.  
It uses an **HC-SR04 ultrasonic sensor** and a **SG90 servo motor** to automatically open the lid when your hand approaches — and close it again after a short adjustable delay.

This project is ideal for **IT enthusiasts, students, and teachers** who want to explore **Python programming, GPIO control, and sensor integration** in a real-world project.
Benefit: You can print the complete can with a 3D printer ;-)

---

### 🚀 Features
- Touchless lid opening via ultrasonic distance detection  
- Adjustable trigger distance (default: 9 cm)  
- Smooth servo movement for quiet operation with SG90
- Clean, minimal Python code – perfect for learning GPIO  
- Works on any Raspberry Pi model

- You will also find Arduino Code for ESP32

---

### 🧰 Hardware Requirements
- Raspberry Pi (any model with GPIO) **recommended Raspberry PI 3b or better**
- HC-SR04 ultrasonic distance sensor
- SG90 or MG90S servo motor
- Jumper wires and breadboard
- 5 V power supply
- 1 kΩ + 2 kΩ (or 3x 1kΩ) kresistors for voltage divider for the output signal form HC-SR04 !! (strongly recommended to avoid damage to the Raspberry)

---

### ⚙️ Wiring Overview

|  Component   | Raspberry Pi Pin | BCM     | Note                      |
|--------------|------------------|---------|---------------------------|
| HC-SR04 VCC  | Pin 2 (5 V)      | –       | Power                     |
| HC-SR04 GND  | Pin 6 (GND)      | –       | Ground                    |
| HC-SR04 TRIG | Pin 16           | GPIO 23 | Output                    |
| HC-SR04 ECHO | Pin 18           | GPIO 24 | Input via voltage divider |
| Servo Signal | Pin 12           | GPIO 18 | PWM output                |
| Servo VCC    | Pin 4 (5 V)      | –       | Power                     |
| Servo GND    | Pin 9 (GND)      | –       | Ground                    |

**Voltage divider:**  
Use 1 kΩ (top) + 2 kΩ (bottom) resistors on the ECHO line to safely reduce 5 V to ~3.3 V.
Don´t foget it! The Raspberry Port or SOC will damage - not instead but after a longer time!!!
---

### 💻 Software Setup
```bash
Normally the needed modul python3-rpi.gpio is already pre-installed on every raspberry pi os.

##Author:##
Marco Kister
IT Trainer & Maker
marco-itech.de
TikTok @marco_itech
hallo@marco_itech.de

