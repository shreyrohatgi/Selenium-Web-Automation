from selenium import webdriver
import csv

csv_links = open('links.csv', 'a')
writer_link = csv.writer(csv_links)

driver = webdriver.Chrome(executable_path='/home/shrey/rera_import/selenium_sample/chromedriver')
driver.get('https://up-rera.in/agents')

for i in range(310, 3268):
    count = (i-2)/10
    while count:
        python_button = driver.find_elements_by_xpath("//a[@data-dt-idx='9']")[0]
        python_button.click()
        count -= 1


    # if ((i - 2)%10 == 0) and (i != 2):
    #     python_button = driver.find_elements_by_xpath("//a[@data-dt-idx='9']")[0]
    #     python_button.click()
    x = str(i)
    if i < 10:
        x = '0' + str(i)

    
    # for i in range(0, count):

    reg_id = driver.find_elements_by_id("ctl00_ContentPlaceHolder1_grdagents_ctl" + x + "_lbluser")[0].text.strip()

    name = 'ctl00$ContentPlaceHolder1$grdagents$ctl' + x + '$imgbtndetail'
    python_button = driver.find_elements_by_xpath("//input[@name='" + name + "' and @type='image']")[0]
    python_button.click()
    driver.switch_to_window(driver.window_handles[1])

        # Write in csv
    csv_row = [driver.current_url, reg_id]
    writer_link.writerow(csv_row)

    print(i)

    driver.close()
    driver.switch_to_window(driver.window_handles[0])

csv_links.close()
driver.close()




