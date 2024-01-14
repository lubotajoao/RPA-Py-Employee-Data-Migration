from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep
from pywinauto.application import Application


# This module is not being used. It's kept for study purpose

def running_apps(application_path, data_migration_portal_url):
    try:
        # Launching the web application
        options = Options()
        options.add_experimental_option("detach", True)
        edge_driver = webdriver.Edge(options=options)
        edge_driver.maximize_window()
        edge_driver.get(data_migration_portal_url)

        sleep(1)

        # Launching the legacy application
        app_win = Application(backend='uia').start(application_path).connect(title="Employee Database", timeout=100)

        return edge_driver

    except Exception as e:
        print(f"An error occurred in launching apps: {e}")
        exit()
    finally:
        print("Apps launched!")
