import os, sys, time

try:
    from rich.console import Console
except ModuleNotFoundError: print("Installing modules... (once)"); os.system("pip install rich --no-python-version-warning"); print("Restart termuxflash"); exit(0)

c = Console()


while True:
    os.system("clear")
    c.print("""[blue]
Termux-Flash
++++++++++++""")
    c.print("[red][F]lash\n[E]xit[/red]")
    choice = c.input(">> ").lower()
    if choice == "e": break
    elif choice == "f":
        c.print("""[blue]What folder do you want to flash?
[/blue][red][1] .termux
[2] /usr/bin
[/red]""")
        choice = c.input(">> ").lower()
        archive = c.input("Enter path to .tar.gz archive: ")
        os.system("clear")
        timer_start = time.time()
        if choice == "1":
            c.print(f"Flashing {archive} into .termux ...")

            out = os.popen(f"cd ~/.termux; tar -xvf {archive}; cd ~").read()
        elif choice == "2":
            c.print(f"Flashing {archive} into /usr/bin ...")
            
            out = os.popen(f"cd ~/../usr/bin; tar -xvf {archive}; cd ~").read()

        timer_end = time.time()
        
        if out.count("cannot") < 1: 
            c.print(f"{str(out)}")
            c.print(f"Done ({round(timer_end-timer_start, 3)} ms.)")
        else: 
            c.print(f"{str(out)}")
            print(f"Error ({round(timer_end-timer_start, 3)} ms.)")

        c.input("Hit enter to continue")
os.system("clear")
