import RPi.GPIO as GPIO
import time 
import MotorDireito

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

coil_A2 = 21 
coil_B2 = 20
coil_C2 = 16
coil_D2 = 12

GPIO.setup(coil_A2, GPIO.OUT)
GPIO.setup(coil_B2, GPIO.OUT)
GPIO.setup(coil_C2, GPIO.OUT)
GPIO.setup(coil_D2, GPIO.OUT)

bobinas2 = [coil_A2,coil_B2,coil_C2,coil_D2] #esquerda

passo = ['1001','0101','0110','1010']
passo_inversa = list(passo)
passo_inversa.reverse()


def motor_esquerda(tempo, voltas):
    for i in range(voltas):
        for j in passo:
            GPIO.output(bobinas2[0],int(j[0]))
            GPIO.output(bobinas2[1],int(j[1]))
            GPIO.output(bobinas2[2],int(j[2]))
            GPIO.output(bobinas2[3],int(j[3]))
            time.sleep(tempo/1000)

    
# def motor_esquerda_inversa(esquerda, voltas):
#     for i in range(voltas):
#         for j in passo_inversa:
            
#             GPIO.output(bobinas1[0],int(j[0]))
#             GPIO.output(bobinas1[1],int(j[1]))
#             GPIO.output(bobinas1[2],int(j[2]))
#             GPIO.output(bobinas1[3],int(j[3]))

#             time.sleep(esquerda/1000)