import psutil
import sys
import os
import subprocess
import signal

from tabulate import tabulate

def list_processes():
    headers = ["PID", "Nume", "Path", "Memorie Procesor (bytes)", "Memorie RAM Utilizată (bytes)"]
    rows = []

    for process in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            process_info = process.info
            process_id = process_info['pid']
            process_name = process_info['name']
            process_path = process_info['exe']
            process_obj = psutil.Process(process_id)
            memory_info = process_obj.memory_info()
            cpu_memory = memory_info.rss
            ram_memory = psutil.virtual_memory().used

            rows.append([process_id, process_name, process_path, cpu_memory, ram_memory])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print(tabulate(rows, headers=headers, tablefmt="grid"))

def run_process(path, *params):
    try:
        subprocess.Popen([path] + list(params), creationflags=subprocess.CREATE_NEW_CONSOLE)
        print(f"Procesul a fost pornit.")
    except FileNotFoundError as e:
        print(f"Fisierul {path} nu a fost gasit.")
    except Exception as e:
        print(f"A intervenit o eroare: {e}")

def suspend_process(pid):
    try:
        process = psutil.Process(pid)
        process.suspend()
        print(f"Procesul cu PID-ul {pid} a fost suspendat.")
    except psutil.NoSuchProcess as e:
        print(f"Nu există niciun proces cu PID-ul {pid}.")

def resume_process(pid):
    try:
        process = psutil.Process(pid)
        process.resume()
        print(f"Procesul cu PID-ul {pid} a fost repornit.")
    except psutil.NoSuchProcess as e:
        print(f"Nu există niciun proces cu PID-ul {pid}.")
    except psutil.AccessDenied as e:
        print(f"Nu ai permisiunea de a reporni procesul cu PID-ul {pid}.")

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Procesul cu PID-ul {pid} a fost oprit.")
    except psutil.NoSuchProcess as e:
        print(f"Nu există niciun proces cu PID-ul {pid}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilizare: process.py <comanda> [parametri]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "view":
        list_processes()
    elif command == "run":
        if len(sys.argv) < 4:
            print("Utilizare: process.py run <path> <parametri>")
            sys.exit(1)
        path_to_run = sys.argv[2]
        params_to_run = sys.argv[3:]
        run_process(path_to_run, *params_to_run)
    elif command == "suspend":
        if len(sys.argv) != 3:
            print("Utilizare: process.py suspend <PID>")
            sys.exit(1)
        pid_to_suspend = int(sys.argv[2])
        suspend_process(pid_to_suspend)
    elif command == "resume":
        if len(sys.argv) != 3:
            print("Utilizare: process.py resume <PID>")
            sys.exit(1)
        pid_to_resume = int(sys.argv[2])
        resume_process(pid_to_resume)    
    elif command == "kill":
        if len(sys.argv) != 3:
            print("Utilizare: process.py kill <PID>")
            sys.exit(1)
        pid_to_kill = int(sys.argv[2])
        kill_process(pid_to_kill)
    else:
        print(f"Comanda necunoscută: {command}")
        sys.exit(1)
