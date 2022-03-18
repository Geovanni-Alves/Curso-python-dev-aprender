# Logging
''' niveis de logging
debug
info
warning
error
critical
'''
from email import message
import logging
logging.basicConfig(level=logging.DEBUG, filename="app.log",
                    filemode="a", format="%(levelname)s - %(message)s - %(asctime)s")

# logging.debug("Logging nivel debug")
# logging.critical("Logging nivel critical")
# logging.info("Logging nivel info")
# logging.warning("Logging nivel warning")
# logging.error("Logging nivel error")

try:
    email = input("Digite seu e-mail: ")
    senha = int(input("Digite sua senha bancária: "))
    if senha == 1234:
        print("Login feito com sucesso!!")
        logging.info(f"{email} entrou em sua conta bancária")
except ValueError as erro:
    print("Digite apenas números")
    logging.info(erro)
