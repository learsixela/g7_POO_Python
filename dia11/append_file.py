from datetime import datetime

try:
    now = datetime.now()
    print(now.strftime('%Y-%m-%d'))
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("dia11/logs/error.log", "a+") as log:
        log.seek(0)#posicionate al principio
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(73)#en byte
        print(log.read(25))#cant byte a imprimir 