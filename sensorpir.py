#Script sensor.py dan sebuah fungsi untuk mengambil data dari sensor tersebut

from gpiozero import MotionSensor   # mengambil package import Motion Sensor

pir = MotionSensor(4)   # PIR Sensor yang terhubung dengan GPIO 4

pir.wait_for_motion()     # Sistem akan menunggu gerakan yang datang
print("Motion Detected!")   #Apabila ada gerakan output Motion Detected

while True:
    print("ada maling")     #Apabila hasil True, keluaran menghasilkan ada Maling
