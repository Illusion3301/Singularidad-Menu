from enum import auto
from colorama import Fore
from colorama import init
import webbrowser
import urllib3
import os
import subprocess
init()

invalida = "Opción inválida. Por favor, elija otro número"
escoja = "Ponga el número correspondiente a su elección >> "
clear = os.system('cls')

def print_header():
    print(Fore.RED + "\n.▄▄ · ▪   ▐ ▄  ▄▄ • ▄• ▄▌▄▄▌   ▄▄▄· ▄▄▄  ▪  ·▄▄▄▄   ▄▄▄· ·▄▄▄▄ ")
    print(Fore.RED + "▐█ ▀. ██ •█▌▐█▐█ ▀ ▪█▪██▌██•  ▐█ ▀█ ▀▄ █·██ ██▪ ██ ▐█ ▀█ ██▪ ██ ")
    print(Fore.RED + "▄▀▀▀█▄▐█·▐█▐▐▌▄█ ▀█▄█▌▐█▌██▪  ▄█▀▀█ ▐▀▀▄ ▐█·▐█· ▐█▌▄█▀▀█ ▐█· ▐█▌")
    print(Fore.RED + "▐█▄▪▐█▐█▌██▐█▌▐█▄▪▐█▐█▄█▌▐█▌▐▌▐█ ▪▐▌▐█•█▌▐█▌██. ██ ▐█ ▪▐▌██. ██")
    print(Fore.RED + " ▀▀▀▀ ▀▀▀▀▀ █▪·▀▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀ .▀  ▀▀▀▀▀▀▀▀▀•  ▀  ▀ ▀▀▀▀▀•\n")

def print_menu():
    print("╔═════════════════════════════════════╗")
    print("║                                     ║")
    print("║" + Fore.WHITE + "     Por favor, elige una opción:" + Fore.RED +"    ║")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        1 - ¿Qué es una IA?" + Fore.RED + "        ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        2 - ¿Qué es Python?" + Fore.RED + "        ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        3 - Bioinformática" + Fore.RED + "         ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        4 - Pratcticar Ml" + Fore.RED + "          ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        5 - Singularidad" + Fore.RED + "           ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        6 - Primer RN" + Fore.RED + "              ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        7 - Preparar entorno" + Fore.RED + "       ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        0 - Salir" + Fore.RED + "                  ═╣")
    print("║                                     ║")
    print("╚═════════════════════════════════════╝\n")

def print_menu2():
    
    print("╔═════════════════════════════════════╗")
    print("║                                     ║")
    print("║" + Fore.WHITE + "     Por favor, elige una opción:" + Fore.RED +"    ║")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "      1 - Python Documentation" + Fore.RED + "     ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "      2 - Videotutorial" + Fore.RED + "            ═╣")
    print("║                                     ║")
    print("╚═════════════════════════════════════╝\n")

def print_menu3():
    print("╔═════════════════════════════════════╗")
    print("║                                     ║")
    print("║" + Fore.WHITE + "     Por favor, elige una opción:" + Fore.RED +"    ║")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "     1 - Bioinformática básica" + Fore.RED + "     ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "     2 - Bioinformática avanzada" + Fore.RED + "   ═╣")
    print("║                                     ║")
    print("╚═════════════════════════════════════╝\n")

while True:
    clear
    print_header()
    print_menu()
    option = input(escoja)

    if option == "1":
        webbrowser.open("https://www.youtube.com/watch?v=lbUluHiqwoA", new=2, autoraise=True)
    elif option == "2":
        clear
        print_header()
        print_menu2()
    
        option = input(escoja)
    
    if option == "1":
        webbrowser.open("https://docs.python.org/3/tutorial/index.html", new=2, autoraise=True)
    elif option == "2":
        webbrowser.open("https://www.youtube.com/watch?v=rfscVS0vtbw", new=2, autoraise=True)

    elif option == "3":
        clear
        print_menu3()
        
        option = input(escoja)
        
        if option == "1":
            webbrowser.open("https://www.youtube.com/watch?v=m7kJ_OmM9tM", new=2, autoraise=True)
            
        elif option == "2":
            webbrowser.open("https://youtu.be/fKI06-R0hKQ", new=2, autoraise=True)
            
        else:
            print(invalida)

    elif option == "4":
        webbrowser.open("https://www.youtube.com/watch?v=iX_on3VxZzk&t=34s", new=2, autoraise=True)
        
    elif option == "5":
        print_header()
        print(Fore.WHITE + "La singularidad sería, por expresarlo de alguna forma, el punto máximo que puede alcanzar una Inteligencia Artificial.  Para lograrla, deberíamos conseguir que la propia máquina se enseñe a si misma, haciendo que sea imparable y pueda      aprender lo que un humano tardaría años en tan solo unos segundos e innovar en el mismo tema. Una vez alcanzado este    punto, sería sencillo alcanzar cosas que ahora mismo parecerían inimaginables debido a nuestro limitado tiempo y cuerpo.")
        
    elif option == "6":
        webbrowser.open("https://www.youtube.com/watch?v=iX_on3VxZzk&t=34s", new=2, autoraise=True)
        
    elif option == "7":
        os.system('pip install tensorflow')
        f = open("FirstAI.py","w+")
        os.system('python -m idlelib FirstAI.py')
        
    elif option == "0":
        os.system(exit())
        
    else:
        print(invalida)
    
    input("\nPresione cualquier tecla para continuar...")
