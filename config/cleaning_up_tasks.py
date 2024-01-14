import pywinauto

from time import sleep


def killing_apps(edge_driver, application_path):
    try:
        # Implementar a validação caso exista a instância da drive aberta
        # Closing the legacy application
        edge_driver.quit()

        sleep(1)

        # Implementar a validação de verificação da aplicação aberta ou em execução
        # Closing the legacy application
        app = pywinauto.application.Application(backend = "uia")
        app.connect(path = application_path, title = "Employee Database", timeout = 100)
        app.kill()
    except Exception as e:
        print(f"An error occurred while cleaning up tasks:\n{e}")
        exit()
    else:
        print("Apps closed!")
