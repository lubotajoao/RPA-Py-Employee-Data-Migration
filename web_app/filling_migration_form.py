from selenium.webdriver.support.select import Select


def send_migration_data(edge_driver, first_name, last_name, phone_number, email_address, city, state, zip_code, job_title, department, start_date, manager_name):
    set_first_name = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[2]/div[1]/input')
    set_first_name.send_keys(first_name)

    set_last_name = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[2]/div[2]/input')
    set_last_name.send_keys(last_name)

    set_phone_number = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[3]/div[1]/input')
    set_phone_number.send_keys(phone_number)

    set_email_address = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[3]/div[2]/input')
    set_email_address.send_keys(email_address)

    set_city = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[4]/div[1]/input')
    set_city.send_keys(city)

    select_state = Select(edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[4]/div[2]/select'))
    select_state.select_by_value(state)

    set_zip = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[4]/div[3]/input')
    set_zip.send_keys(zip_code)

    set_job_title = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[5]/div[1]/input')
    set_job_title.send_keys(job_title)

    select_department = Select(edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[5]/div[2]/select'))
    select_department.select_by_value(department)

    set_start_date = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[6]/div[1]/input')
    set_start_date.send_keys(start_date)

    set_manager_name = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[6]/div[2]/input')
    set_manager_name.send_keys(manager_name)

    submit_btn = edge_driver.find_element('xpath', '/html/body/div[2]/div/form/div[7]/div[1]/button')
    submit_btn.click()
