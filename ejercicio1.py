#variable X = numsEnCola
import time
import threading
import random
import queue

class Producer(threading.Thread):
    def __init__(self, cola, pt):
        threading.Thread.__init__(self)
        self.cola = cola
        self.pt = pt
    
    def run(self):
        while True:
            self.cola.put(random.randint(100, 500))
            time.sleep(self.pt)

class Consumer(threading.Thread):
    def __init__(self, cola, ct, numsEnCola):
        threading.Thread.__init__(self)
        self.cola = cola
        self.ct = ct
        self.numsEnCola = numsEnCola
    
    def run(self):
        while True:
            lista = []
            for i in range(self.numsEnCola):
                lista.append(self.cola.get())
            
            self.calculateMultiplication(lista)
            time.sleep(self.ct)
    
    def calculateMultiplication(self, lista):
        result = 1
        for num in lista:
            result *= num
        print("Multiplicación de los números:", lista, "= ", result)

def mainEj2(nP, nC, PT, CT, numsEnCola):
    cola = queue.Queue()
    listProducer = []
    for i in range(nP):
        t1 = Producer(cola, PT)
        listProducer.append(t1)
    
    listConsumer = []
    for i in range(nC):
        t2 = Consumer(cola, CT, numsEnCola)
        listConsumer.append(t2)
    
    for producer in listProducer:
        producer.start()
    for consumer in listConsumer:
        consumer.start()
    for producer in listProducer:
        producer.join()
    for consumer in listConsumer:
        consumer.join()

if __name__ == '__main__':
    #mainEj2(1, 1, 1, 4, 3)
    mainEj2(4, 2, 2, 2, 2)
    #mainEj2(2, 6, 1, 10, 4)
