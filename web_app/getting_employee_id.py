def getting_id(edge_driver):
    try:
        text = edge_driver.find_element('xpath', "//*[@id='employeeID']")
        employee_id = text.get_attribute("value")

        return employee_id

    except Exception as e:
        print(f"An error occurred while getting the employee ID: {e}")
        exit()
