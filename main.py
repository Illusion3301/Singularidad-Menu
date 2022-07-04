from colorama import Fore
from colorama import init
import webbrowser
import os
init()

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
    print("╠═" + Fore.WHITE + "        4 - Pratcticar LM" + Fore.RED + "          ═╣")
    print("║                                     ║")
    print("╠═" + Fore.WHITE + "        5 - Singularidad" + Fore.RED + "           ═╣")
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
#****************************************

while True:
    os.system('cls')
    print_header()
    print_menu()
    option = input("Ponga el número correspondiente a su elección >> ")

    if option == "1":
        webbrowser.open("https://www.youtube.com/watch?v=lbUluHiqwoA", new=2, autoraise=True)
    elif option == "2":
        os.system('cls')
        print_header()
        print_menu2()
    
        option = input("Ponga el número correspondiente a su elección >> ")
    
    if option == "1":
        webbrowser.open("https://docs.python.org/3/tutorial/index.html", new=2, autoraise=True)
    elif option == "2":
        webbrowser.open("https://www.youtube.com/watch?v=rfscVS0vtbw", new=2, autoraise=True)

    elif option == "3":
        webbrowser.open("https://www.youtube.com/watch?v=m7kJ_OmM9tM", new=2, autoraise=True)

    elif option == "4":
        webbrowser.open("https://www.youtube.com/watch?v=iX_on3VxZzk&t=34s", new=2, autoraise=True)
        
    elif option == "5":
        print_header()
        print(Fore.WHITE + "La singularidad sería, por expresarlo de alguna forma, el punto máximo que puede alcanzar una Inteligencia Artificial.  Para lograrla, deberíamos conseguir que la propia máquina se enseñe a si misma, haciendo que sea imparable y pueda      aprender lo que un humano tardaría años en tan solo unos segundos e innovar en el mismo tema. Una vez alcanzado este    punto, sería sencillo alcanzar cosas que ahora mismo parecerían inimaginables debido a nuestro limitado tiempo y cuerpo.")
        
    elif option == "0":
        os.system(exit())
        
    else:
        print("Opción inválida. Por favor, elija otra opción.")
    
    input("\nPresione cualquier tecla para continuar...")