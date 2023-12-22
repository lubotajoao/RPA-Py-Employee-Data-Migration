from libs import *


def main():
    global first_name, last_name, email_address, city, state, zip_code, job_title, department, manager_name
    try:
        print("The process as started!")

        # Launching web migration application
        options = Options()
        options.add_experimental_option("detach", True)
        edge_driver = webdriver.Edge(options = options)
        edge_driver.maximize_window()
        edge_driver.get(data_migration_portal_url)

        # Launching the legacy application
        app_win = Application(backend = 'uia').start(application_path).connect(title = "Employee Database", timeout = 100)

        for x in range(10):
            # Switching to the web migration application
            window = pygetwindow.getWindowsWithTitle(data_migration_web_window)[0]
            window.activate()

            # Getting the Employee ID from the Migration Web System
            employee_id = getting_id(edge_driver)

            # Getting the Employee Phone Number and Start Date From The Migration API
            phone_number = getting_phone_number(api_url, employee_id)
            start_date = getting_start_date(api_url, employee_id)

            # Switching to the legacy application
            app_win.EmployeeDatabase.set_focus()

            # Getting the Employee Data From Legacy Application
            employee_data = getting_legacy_data(employee_id, app_win)

            for index in range(len(employee_data)):
                if index == 0:
                    first_name = employee_data[index]
                elif index == 1:
                    last_name = employee_data[index]
                elif index == 2:
                    email_address = employee_data[index]
                elif index == 3:
                    city = employee_data[index]
                elif index == 4:
                    zip_code = employee_data[index]
                elif index == 5:
                    job_title = employee_data[index]
                elif index == 6:
                    department = employee_data[index]
                elif index == 7:
                    manager_name = employee_data[index]
                elif index == 8:
                    state = employee_data[index]

            # Switching to the web migration application
            window = pygetwindow.getWindowsWithTitle(data_migration_web_window)[0]
            window.activate()

            # Migrating the Employee Data Into Migration System
            send_migration_data(edge_driver, first_name, last_name, phone_number, email_address, city, state, zip_code, job_title, department, start_date, manager_name)

        sleep(5)

        # Cleaning Up Tasks
        killing_apps(edge_driver, application_path)

    except Exception as e:
        print(f"An error occurred in orchestrator task:\n{e}")
    finally:
        print("The process has finished!")


if __name__ == "__main__":
    main()
