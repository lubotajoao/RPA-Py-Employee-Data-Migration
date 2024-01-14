from time import sleep


def getting_legacy_data(employee_id, app = None):
    try:
        # - Clear Employee Search Clear
        clear_btn = app.EmployeeDatabase.child_window(title="Clear", auto_id="btnClear", control_type="Button").wrapper_object()
        clear_btn.click_input()

        # - Inserting the Employee ID into legacy application
        employee_input = app.EmployeeDatabase.child_window(auto_id = "txtEmpId", control_type = "Edit").wrapper_object()
        employee_input.type_keys(employee_id, with_spaces = False)

        # - Searching the Employee Info
        search_btn = app.EmployeeDatabase.child_window(title = "Search", auto_id = "btnSearch", control_type = "Button").wrapper_object()
        search_btn.click_input()

        sleep(1)

        first_name = app.EmployeeDatabase.child_window(auto_id = "txtFirstName", control_type = "Edit").get_value()
        last_name = app.EmployeeDatabase.child_window(auto_id = "txtLastName", control_type = "Edit").get_value()
        email_id = app.EmployeeDatabase.child_window(auto_id = "txtEmailId", control_type = "Edit").get_value()
        city = app.EmployeeDatabase.child_window(auto_id = "txtCity", control_type = "Edit").get_value()
        zip_code = app.EmployeeDatabase.child_window(auto_id = "txtZip", control_type = "Edit").get_value()
        job_title = app.EmployeeDatabase.child_window(auto_id = "txtJobTitle", control_type = "Edit").get_value()
        department = app.EmployeeDatabase.child_window(auto_id = "txtDepartment", control_type = "Edit").get_value()
        manager_name = app.EmployeeDatabase.child_window(auto_id = "txtManager", control_type = "Edit").get_value()
        state = app.EmployeeDatabase.child_window(auto_id = "txtState", control_type = "Edit").get_value()

        return first_name, last_name, email_id, city, zip_code, job_title, department, manager_name, state

    except Exception as e:
        print(f"An error occurred while getting employee data from legacy application:\n{e}")
