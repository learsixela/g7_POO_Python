from usuario import Usuario
from datetime import datetime
import json

lista_usuarios = []
fecha_hora = datetime.now()

with open("dia12/desafio/usuarios.txt") as usuarios:
    #print(usuarios.readline())
    #print(usuarios.readline())
    linea = usuarios.readline()
    while linea:
        try:
            #print(linea)
            #print(linea)
            #print(json.loads(linea))
            dicc_usuario = json.loads(linea)#
            usuario = Usuario(dicc_usuario["nombre"],dicc_usuario["apellido"],dicc_usuario["email"],dicc_usuario["genero"])
            lista_usuarios.append(usuario)
            #print(lista_usuarios)
        except Exception as e:
            with open(f"dia12/desafio/logs/{fecha_hora.strftime('%Y-%m-%d_%H')}_error.log","a+") as log:
                
                print(fecha_hora.strftime("%Y-%m-%d_%H:%M:%S"))
                log.write(f"[{fecha_hora.strftime('%Y-%m-%d_%H:%M:%S')}] {e}\n")
                print(e)
                log.close()
        finally:
            linea = usuarios.readline()
    usuarios.close()

print(lista_usuarios)