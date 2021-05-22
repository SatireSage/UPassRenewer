from selenium import webdriver
import os
from os import path

yes_and_no_array = ["yes", "no", "Yes", "No", "y", "n", "Y", "N"]


def UPass(cas_user_id, cas_user_pass, user_compass_num, user_cvn_num):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Sahaj\Downloads\chromedriver_win32 (1)\chromedriver")
    driver.get("https://upassbc.translink.ca/")
    SFU_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[9]')
    SFU_Element.click()
    Button = driver.find_element_by_xpath('//*[@id="goButton"]')
    Button.click()
    CAS_Username = driver.find_element_by_xpath('//*[@id="username"]')
    CAS_Username.send_keys(cas_user_id)
    CAS_Password = driver.find_element_by_xpath('//*[@id="password"]')
    CAS_Password.send_keys(cas_user_pass)
    # CAS_Login = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    # CAS_Login.click()
    if driver.current_url == 'https://upassbc.translink.ca/fs/CompassCard/Link':
        Compass_Num = driver.find_element_by_xpath('//*[@id="link-CompassNumber"]')
        Compass_Num.send_keys(user_compass_num)
        CVN_Num = driver.find_element_by_xpath('//*[@id="link-CVN"]')
        CVN_Num.send_keys(user_cvn_num)
        Compass_Link_Card = driver.find_element_by_xpath('//*[@id="btnLink"]')
        #Compass_Link_Card.click()
        input("Please press a key")
    elif driver.current_url == 'https://upassbc.translink.ca/fs/':
        Compass_Data = driver.find_element_by_xpath('//*[@id="form-request"]/table/tbody/tr[1]/td[3]')
        Compass_Body = driver.find_element_by_xpath('//*[@id="form-request"]/table/tbody')


def credential_writer(new_file):
    Username_Counter = False
    while not Username_Counter:
        cas_uid_writer = input('Please enter your CAS Username: ')
        id_check = input("Please re-enter your username: ")
        if cas_uid_writer != id_check:
            print("You entered the wrong username! Please try again")
        else:
            new_file.write(cas_uid_writer)
            break
    Password_Counter = False
    while not Password_Counter:
        cas_pass_writer = input('Please enter your CAS Password: ')
        pass_check = input("Please re-enter your Password: ")
        if cas_pass_writer != pass_check:
            print("You entered the wrong Password! Please try again")
        else:
            new_file.write("\n")
            new_file.write(cas_pass_writer)
            break
    Compass_Counter = False
    while not Compass_Counter:
        compassID_writer = input('Please enter your Compass Card Number: ')
        compass_check = input("Please re-enter your Compass Card Number: ")
        if compassID_writer != compass_check:
            print("You entered the wrong Password! Please try again")
        else:
            new_file.write("\n")
            new_file.write(compassID_writer)
            break
    CVN_Counter = False
    while not CVN_Counter:
        CVN_writer = input('Please enter your CVN Number: ')
        CVN_check = input("Please re-enter your CVN Number: ")
        if CVN_writer != CVN_check:
            print("You entered the wrong Password! Please try again")
        else:
            new_file.write("\n")
            new_file.write(CVN_writer)
            break
    print("Thank You! Please re-run the file to renew you UPass!")


if path.exists(r'C:\Users\Sahaj\PycharmProjects\UPAss\venv\pass_writer.txt'):
    empty_check = os.stat(r'C:\Users\Sahaj\PycharmProjects\UPAss\venv\pass_writer.txt').st_size
    if empty_check != 0:
        File = open(r"C:\Users\Sahaj\PycharmProjects\UPAss\venv\pass_writer.txt", "r")
        cas_id = File.readline()
        cas_pass = File.readline()
        compass_num = File.readline()
        cvn_num = File.readline()
        choice = input("Would you like to proceed now: ")
        try:
            if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
                UPass(cas_id, cas_pass, compass_num, cvn_num)
            elif choice == "no" or choice == "No" or choice == "n" or choice == "N":
                print('No worries! Next time just run the file to renew you UPass bc!')
                quit()
        except str(choice) not in yes_and_no_array:
            print("Im sorry please say yes or no!")
    else:
        File_Created = open(r'C:\Users\Sahaj\PycharmProjects\UPAss\venv\pass_writer.txt', "a+")
        choice = input("Would you like to proceed now: ")
        try:
            if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
                credential_writer(File_Created)
            elif choice == "no" or choice == "No" or choice == "n" or choice == "N":
                print('No worries! Next time just run the file to renew you UPass bc!')
                quit()
        except str(choice) not in yes_and_no_array:
            print("Im sorry please say yes or no!")
else:
    File_Created = open(r'C:\Users\Sahaj\PycharmProjects\UPAss\venv\pass_writer.txt', "a+")
    choice = input("Would you like to proceed now: ")
    try:
        if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
            credential_writer(File_Created)
        elif choice == "no" or choice == "No" or choice == "n" or choice == "N":
            print('No worries! Next time just run the file to renew you UPass bc!')
            quit()
    except str(choice) not in yes_and_no_array:
        print("Im sorry please say yes or no!")

# Currently doesn't do anything past login and when user says something other than no it doesn't make sure to retry
# Need to make it work for different systems and browsers
