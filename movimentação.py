import RPi.GPIO as GPIO
import time
from MotorDireito import *
from MotorEsquerdo import *
from multiprocessing import Process


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 




def frente(tempo, voltas):
    for i in range(voltas):
        for j in passo:
            GPIO.output(bobinas1[0],int(j[0]))
            GPIO.output(bobinas1[1],int(j[1]))
            GPIO.output(bobinas1[2],int(j[2]))
            GPIO.output(bobinas1[3],int(j[3]))

            GPIO.output(bobinas2[0],int(j[0]))
            GPIO.output(bobinas2[1],int(j[1]))
            GPIO.output(bobinas2[2],int(j[2]))
            GPIO.output(bobinas2[3],int(j[3]))

            time.sleep(tempo/1000)

   
def re(tempo, voltas):
    for i in range(voltas):
        for j in passo_inversa:
            GPIO.output(bobinas1[0],int(j[0]))
            GPIO.output(bobinas1[1],int(j[1]))
            GPIO.output(bobinas1[2],int(j[2]))
            GPIO.output(bobinas1[3],int(j[3]))

            GPIO.output(bobinas2[0],int(j[0]))
            GPIO.output(bobinas2[1],int(j[1]))
            GPIO.output(bobinas2[2],int(j[2]))
            GPIO.output(bobinas2[3],int(j[3]))

            time.sleep(tempo/1000)
    

while True:
    try:
        direcao = str(input("f -> Frente ou r -> Ré e c -> Curva:  "))

        if direcao == 'f':
            tempo = int(input("Intervalo de passo (2 ms recomendado): "))
            voltas = 50* int(input("Quantas voltas? "))
            frente(tempo, voltas)
    
        if direcao == 'r':
            tempo = int(input("Intervalo de passo (2 ms recomendado): "))
            voltas = 50* int(input("Quantas voltas? "))
            re(tempo, voltas)      

        if direcao == 'c':
            direita = int(input("Intervalo de passo do motor DIREITO (2 ms recomendado): "))
            esquerda = int(input("Intervalo de passo do motor ESQUERDO (2 ms recomendado): "))
            voltas= 50* int(input("Quantas voltas motor? "))
            processo_d = Process(target=motor_direita, args=(direita,voltas))
            processo_e = Process(target=motor_esquerda, args=(esquerda,voltas))
            
            processo_d.start()
            processo_e.start()


            # processo_d.join() #espera o termino do programa
            # processo_e.join()
            
    except KeyboardInterrupt:
        GPIO.cleanup()
 

