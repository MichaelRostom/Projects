from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeyG_kubBRnvRFDxB6oUotAU4NSsXTRxZCOkT7vc7hI1HGMeQ/viewform')
sleep(3)
for i in range(1000) :
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[1]/span').click()  # clicks the first dropdown menue
    sleep(0.49)
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div[2]/div[4]/span').click()  # clicks the first option

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/span').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div[2]/div[4]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div[2]/div[6]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div[2]/div[6]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div[2]/div[6]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[2]/div[6]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[4]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[14]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[14]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[15]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[15]/div/div[2]/div[2]/div[4]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[16]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[16]/div/div[2]/div[2]/div[6]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[17]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[17]/div/div[2]/div[2]/div[4]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[18]/div/div[2]/div[1]/div[1]/div[1]/span').click()

    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[18]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[19]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[19]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[20]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[20]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[21]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[21]/div/div[2]/div[2]/div[4]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[22]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[22]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[23]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[23]/div/div[2]/div[2]/div[3]').click()

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[2]/div[24]/div/div[2]/div[1]/div[1]/div[1]/span').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[24]/div/div[2]/div[2]/div[6]').click()

    sleep(0.45)
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div/div/div[3]/div/div/div/span/span').click()  # clicks the submit button
    sleep(0.3)
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    driver.back()
    sleep(1.1)
    print(i + 1)
