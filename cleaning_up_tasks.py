import pywinauto

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep
from pywinauto.application import Application


def killing_apps(edge_driver, application_path):
    try:
        # Closing the legacy application
        edge_driver.quit()

        sleep(1)

        # Closing the legacy application
        app = pywinauto.application.Application(backend = "uia")
        app.connect(path = application_path, title = "Employee Database", timeout = 100)
        app.kill()
    except Exception as e:
        print(f"An error occurred while cleaning up tasks:\n{e}")
        exit()
    else:
        print("Apps closed!")

