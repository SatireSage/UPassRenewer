from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os
import sys
from os import path
import time
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
mainframe = Frame(window)


def UPass(uni, cas_user_id, cas_user_pass, user_compass_num, user_cvn_num):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=r"C:\Users\Sahaj\PycharmProjects\UPAss\chromedriver.exe", options=options)
    driver.get("https://upassbc.translink.ca/")
    time.sleep(2)
    uni = int(uni)
    if uni == 1:
        BCIT_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[2]')
        BCIT_Element.click()
    elif uni == 2:
        Cap_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[3]')
        Cap_Element.click()
    elif uni == 3:
        Douglas_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[4]')
        Douglas_Element.click()
    elif uni == 4:
        ECARR_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[5]')
        ECARR_Element.click()
    elif uni == 5:
        KPU_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[6]')
        KPU_Element.click()
    elif uni == 6:
        Langara_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[7]')
        Langara_Element.click()
    elif uni == 7:
        NVIT_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[8]')
        NVIT_Element.click()
    elif uni == 8:
        SFU_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[9]')
        SFU_Element.click()
    elif uni == 9:
        UBC_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[10]')
        UBC_Element.click()
    elif uni == 10:
        VCC_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[11]')
        VCC_Element.click()
    else:
        Empty_Element = driver.find_element_by_xpath('//*[@id="PsiId"]/option[1]')
        Empty_Element.click()
    Go_Button = driver.find_element_by_xpath('//*[@id="goButton"]')
    Go_Button.click()
    time.sleep(2)
    CAS_Username = driver.find_element_by_xpath('//*[@id="username"]')
    CAS_Username.send_keys(cas_user_id)
    CAS_Password = driver.find_element_by_xpath('//*[@id="password"]')
    CAS_Password.send_keys(cas_user_pass)
    if driver.current_url == 'https://upassbc.translink.ca/fs/CompassCard/Link':
        print("Linking Compass Card")
        time.sleep(2)
        Compass_Num = driver.find_element_by_xpath('//*[@id="link-CompassNumber"]')
        Compass_Num.send_keys(user_compass_num)
        CVN_Num = driver.find_element_by_xpath('//*[@id="link-CVN"]')
        CVN_Num.send_keys(user_cvn_num)
        Compass_Link_Card = driver.find_element_by_xpath('//*[@id="btnLink"]')
        Compass_Link_Card.click()
    if driver.current_url == 'https://upassbc.translink.ca/fs/':
        time.sleep(2)
        print("Opening Compass")
        try:
            Compass_Status = driver.find_element_by_xpath('//*[@id="form-request"]/table/tbody/tr[2]/td[3]/div')
            print(Compass_Status.text)
            messagebox.showinfo(title='Status', message=Compass_Status.text)
            print("Thanks!\n")
        except NoSuchElementException:
            print("No Status yet")
            pass

        try:
            Compass_Check_Present = driver.find_element_by_xpath('//*[@id="chk_0"]')
            Compass_Check_Present.click()
        except NoSuchElementException:
            print("Checked")
            pass

        try:
            Compass_Check_Present2 = driver.find_element_by_xpath('//*[@id="chk_1"]')
            Compass_Check_Present2.click()
        except NoSuchElementException:
            print("Checked\n")
            pass

        try:
            time.sleep(2)
            Compass_Check_Request = driver.find_element_by_xpath('//*[@id="requestButton"]')
            Compass_Check_Request.click()
        except NoSuchElementException:
            print("Requested")
            pass
    time.sleep(2)


def credential_writer(new_file):
    # UNIVERSITIES = [
    #     '-',
    #     'British Columbia Institute of Technology',
    #     'Capilano University',
    #     'Douglas College',
    #     'Emily Carr University of Art and Design',
    #     'Kwantlen Polytechnic University',
    #     'Langara College',
    #     'Nicola Valley Institute of Technology',
    #     'Simon Fraser University',
    #     'University of British Columbia',
    #     'Vancouver Community College'
    # ]
    # university_writer = StringVar(window)
    # university_writer.set(UNIVERSITIES[0])
    #
    # Credentials_Counter = False
    # while not Credentials_Counter:
    #     w = OptionMenu(mainframe, university_writer, *UNIVERSITIES)
    #     w.pack()
    #     window.mainloop()
    #     print(university_writer.get())
    #
    #     uid_writer = simpledialog.askstring("Credentials", "Please enter your username")
    #     password_writer = simpledialog.askstring("Credentials", "Please enter your password")
    #     compass_card_writer = simpledialog.askstring("Credentials", "Please enter your Compass Card Number")
    #     cvn_writer = simpledialog.askstring("Credentials", "Please enter your CVN")
    #
    #     Credentials_Counter = messagebox.askyesno('Credentials?',
    #                                               "Is this information correct? Press No to re-enter info.\nUsername: " + uid_writer
    #                                               + "\nPassword: " + password_writer + "\nCompass Card Number: " + compass_card_writer
    #                                               + "\nCVN: " + cvn_writer)

    Username_Counter = False
    while not Username_Counter:
        cas_uid_writer = input('Please enter your CAS Username: ')
        id_check = input("Please re-enter your username: ")
        if cas_uid_writer != id_check:
            print("You entered the wrong username! Please try again")
        else:
            new_file.write(cas_uid_writer)
            break
    print("\n")
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
    print("\n")
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
    print("\n")
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
    print("\n")
    print("Thank You! Please re-run the file to renew you UPass!")


def runner():

    File = open(r"C:\Users\Sahaj\PycharmProjects\UPAss\pass_writer.txt", "r")
    uni_name = File.readline()
    cas_id = File.readline()
    cas_pass = File.readline()
    compass_num = File.readline()
    cvn_num = File.readline()
    if messagebox.askyesno('Proceed?', 'Would you like to proceed now?'):
        UPass(uni_name, cas_id, cas_pass, compass_num, cvn_num)
    else:
        messagebox.showinfo('Exit', 'No worries! Next time just run the file to renew you UPass bc!')
        sys.exit()


def runner2():
    File_Created = open(r'C:\Users\Sahaj\PycharmProjects\UPAss\pass_writer.txt', "a+")
    if messagebox.askyesno('Proceed?', 'Would you like to proceed now?'):
        credential_writer(File_Created)
    else:
        messagebox.showinfo('Exit', 'No worries! Next time just run the file to renew you UPass bc!')
        sys.exit()


def main():
    if path.exists(r'C:\Users\Sahaj\PycharmProjects\UPAss\pass_writer.txt'):
        empty_check = os.stat(r'C:\Users\Sahaj\PycharmProjects\UPAss\pass_writer.txt').st_size
        if empty_check != 0:
            runner()
        else:
            runner2()
    else:
        runner2()


main()