# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import smtplib
import pandas as pd
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
password= config["smtp_creds"]["password"]
user=config["smtp_creds"]["username"]

def send_bd_mails(recipient, subj,msg ):
    # creating server from smtp library
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # starting server
    server.starttls()
    # logging to the account
    server.login(user, password)


    Body = "\r\n".join((
        "From: %s" % user,
        "To: %s" % recipient,
        "Subject: %s" % subj,
        "",
        msg,
    ) )
    print(Body)
    # sending mail
    server.sendmail(user, [recipient], Body)
    print("mail sent")

def check_todays_bd(filename):
    file = pd.read_csv(filename, usecols = ["name", "birthday", "email"])
    #print(file)
    today = time.strftime("%d-%b")
    print(today,type(today))
    for bd in file.index:
        # print(bd)
        # print(file["birthday"][bd],type(file["birthday"][bd]))
        if today == file["birthday"][bd]:
            recipient = file["email"][bd]
            subj = "birthday wishes"
            msg = "happy birthday"
            print("Sending mail ......")
            send_bd_mails(recipient,subj,msg)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #send_bd_mails("pratima.singh1104@gmail.com", "birthday wishes", "are u happy" )
    check_todays_bd("Birthday.csv")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
