"""Usando procesos, abre tres procesos,cada uno de los cuales debe….
	P1: debe abrir el bloc de notas/editor de texto del sistema que uses
	P2: debes esperar 5 segundos para cambiar la prioridad de P1
	P3: se lanza 2 segundos después de P2 haya arrancado y mata a P1 al instante
	¿Qué es lo que ocurre durante la ejecución?¿Termina el programa correctamente?¿Cómo podrías solucionarlo?
OPCIONAL +0,5: ¿Qué mecanismo de los estudiados te permitiría sincronizar la muerte de P1?Describe  todo lo que se te ocurra al respecto 	"""
import os
import time
import psutil
import multiprocessing
import subprocess
import sys
import psutil

def abrir_notepad():
    print("Abriendo block de notas")
    subprocess.Popen(['notepad.exe'])  # Abre el Bloc de notas

def esWindows():
  try:
    sys.getwindowsversion()
  except AttributeError:
    return (False)
  else:
    return (True)

def cambiar_prioridad():
    time.sleep(5)  # Espera 5 segundos antes de cambiar la prioridad
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == "notepad.exe":
            p = psutil.Process(proceso.info['pid'])

            print("PID del proceso:", proceso.info['pid'])
            print("Prioridad del proceso antes de cambio:", p.nice())

            p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)

            print("PID del proceso:", proceso.info['pid'])
            print("Nueva prioridad del proceso:", p.nice())

def eliminar_proceso():
        time.sleep(7)
        for proc in psutil.process_iter():
            try:
                # Obtener el nombre del proceso
                nombreProceso = proc.name()    
                if proc.name() == "notepad.exe":
                    PID = proc.pid
                    print(proc.username())
                    print("Eliminando el proceso: ", nombreProceso , ' ::: ', PID)
                    proc.kill()    
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print ("error")


if __name__ == "__main__":
    proceso_1 = multiprocessing.Process(target=abrir_notepad, name="proceso_1")
    proceso_2 = multiprocessing.Process(target=cambiar_prioridad, name="proceso_2")
    proceso_3 = multiprocessing.Process(target=eliminar_proceso, name="proceso_3")

    proceso_1.start()
    proceso_2.start()
    proceso_3.start()

    proceso_1.join()
    proceso_2.join()
    proceso_3.join()

    print("Procesos completados")
