import os, psutil, time, subprocess, multiprocessing, sys
import threading
import tempfile
file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

def code(name,lock):
       time.sleep(10)
       with lock:  

        with open(file_name, 'w') as f:
                print("guardando en "+file_name)
                f.write("codigo limpio fue escrito por "+str(name)) 
                
        time.sleep(5)
        subprocess.run(["ping", "google.com"])


# llama  a mi metodo usando hilos
lock = threading.Lock()
h = threading.Thread(target=code, args=("alexander fuela",lock,))
h.start()

h1 = threading.Thread(target=code, args=("alexander fuela",lock,))
h1.start()

h2 = threading.Thread(target=code, args=("alexander fuela",lock,))
h2.start()

h3 = threading.Thread(target=code, args=("alexander fuela",lock,))
h3.start()

h4 = threading.Thread(target=code, args=("alexander fuela",lock,))
h4.start()

h.join()
h1.join()
h2.join()
h3.join()
h4.join()
