from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date, datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

BC_number = 'BCO10330243'                                           #<--- input
# Building consent number
# Kumeu `BCO10327748`
# Orewa BCO10324422
# Roxborough BCO10331153
# William Ave BCO10330243
# Pukemarino BCO10338403
# Otara BCO10350139

year = 2023                                                         #<--- input
month = 6                                                           #<--- input
day = 30                                                            #<--- input
# inspection date


inspection_type = '11'                                               #<--- input each project the number may varies
# Inspection type number
# Check the list number from council website


inspectiondate = date(year, month, day)
currentdate = date.today()

n = ((inspectiondate.month)-(currentdate.month))

success = 0

while success == 0:

    driver = webdriver.Chrome()
    url = 'https://signin.aucklandcouncil.govt.nz/ofis/pages/public/'
    driver.get(url)

    driver.implicitly_wait(10)

    driver.find_element_by_css_selector('#navSignIn').click()

    driver.find_element_by_xpath('//*[@id="txtEMAIL"]').send_keys('joe.y@ploceusbuilding.com')
 
    driver.find_element_by_css_selector('#btnUpdateProfile').click()

    driver.find_element_by_css_selector('#txtPassword').send_keys('58Kanoway!')

    driver.find_element_by_css_selector('.bigger-110').click()

    url = 'https://onlineservices.aucklandcouncil.govt.nz/councilonline/inspection/consent-search?bookingType=single#'
    driver.get(url)

    driver.find_element_by_css_selector('#bcoReference').send_keys(BC_number)

    driver.find_element_by_css_selector('#bcoReference').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('.inspection-book-button.bookSearchResultInspectionBtn').click()

    driver.find_element_by_css_selector('#inspectionType').click()

    from selenium.webdriver.support.select import Select

    select_type = Select(driver.find_element_by_id('inspectionType'))

    select_type.select_by_index(inspection_type)

    driver.find_element_by_css_selector('.inspection-next-btn.inspection-nav-button.pull-right').click()

    #apply only if the booking is in next month to change the clender to next month
    if n==1:
       driver.find_element_by_css_selector('.fa.fa-chevron-circle-right').click()

    time.sleep(5)

    driver.find_element_by_xpath('//*[contains(@id,"{}")]'.format(inspectiondate)).click()
    yn = driver.find_element_by_xpath('//*[contains(@id,"{}")]'.format(inspectiondate)).get_attribute('class')
    if yn == 'dow-clickable event-styled':
        print(inspectiondate,'available for booking')
    
        success = 1
    else:
        driver.close()
        time.sleep(300)

select_ampm = Select(driver.find_element_by_id('inspectionTimeSlot'))

pm = driver.find_element_by_xpath('//*[contains(@value,"12:00:00-16:00:00")]').get_attribute('value')

if pm == '12:00:00-16:00:00':
    print('Afternoon slot available')
    ampm = '12:00:00-16:00:00'

else:
    ampm = '08:00:00-12:00:00'
    print('only monring slot available')

select_ampm.select_by_value(ampm)

time.sleep(5)

driver.find_element_by_xpath('//*[@id="readyNowNo"]').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="onSiteContactOff"]').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="siteContactName"]').send_keys('Kevin Liu')               #<--- input name receving email

time.sleep(1)

driver.find_element_by_xpath('//*[@id="siteContactNo"]').send_keys('0224578318')                    #<--- input number receiving text 0224578318

time.sleep(1)

driver.find_element_by_xpath('//*[@id="siteContactEmail"]').send_keys('kevin.l@ploceusbuilding.com')   #<--- input email receiving

time.sleep(1)


driver.find_element_by_xpath('//*[@id="simpleBookingForm"]/div[4]/button[2]').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="acceptTermsAndConditions"]').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="simpleBookingForm"]/div[4]/button[2]').click()

time.sleep(5)

driver.close()


#address = driver.find_element_by_xpath('//*[@id="simpleBookingForm"]/div[4]/button[2]').text

#ins_type = driver.find_element_by_xpath('//*[@id="simpleBookingForm"]/div[3]/div[1]/fieldset[1]/span').text

#time.sleep(1)

#timebooked = driver.find_element_by_xpath('//*[@id="simpleBookingForm"]/div[3]/div[1]/fieldset[3]/span').text

#time.sleep(1)

#driver.find_element_by_xpath('//*[@id="simpleBookingForm"]/div[4]/button[2]').click()

#time.sleep(1)

#driver.close()



# driver = webdriver.Chrome()
# outlook = 'https://outlook.live.com/owa/'
# driver.get(outlook)
# driver.find_element_by_xpath()