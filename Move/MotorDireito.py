import RPi.GPIO as GPIO
import time 
import MotorEsquerdo

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

coil_A1 = 26 
coil_B1 = 19
coil_C1 = 13
coil_D1 = 6

GPIO.setup(coil_A1, GPIO.OUT)
GPIO.setup(coil_B1, GPIO.OUT)
GPIO.setup(coil_C1, GPIO.OUT)
GPIO.setup(coil_D1, GPIO.OUT)

bobinas1 = [coil_A1,coil_B1,coil_C1,coil_D1] #direita


passo = ['1001','0101','0110','1010']
passo_inversa = list(passo)
passo_inversa.reverse()


def motor_direita(tempo, voltas):
    for i in range(voltas):
        for j in passo:
            GPIO.output(bobinas1[0],int(j[0]))
            GPIO.output(bobinas1[1],int(j[1]))
            GPIO.output(bobinas1[2],int(j[2]))
            GPIO.output(bobinas1[3],int(j[3]))
            time.sleep(tempo/1000)      
    

# def motor_direita_inversa(direita, voltas):
#     for i in range(voltas):
#         for j in passo_inversa:
            
#             GPIO.output(bobinas1[0],int(j[0]))
#             GPIO.output(bobinas1[1],int(j[1]))
#             GPIO.output(bobinas1[2],int(j[2]))
#             GPIO.output(bobinas1[3],int(j[3]))

#             time.sleep(direita/1000)

