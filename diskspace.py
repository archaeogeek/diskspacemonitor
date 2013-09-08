import os
import platform
import ctypes
import smtplib


config = {
    "email": {
        "from": "add sender email here",
        "to": "add recipient email here",
        "subject": "Disk Space Monitor: %(folder)s",
        "message": "The drive %(folder)s is reaching its space limit. \n\nFrom the DiskSpace Pixie.",
        "username": "your email address",
        "password": "your email password",
        "smtp_server": "your smtp server"
    },
    
    "disk":{
        "folder": '/', #use windows convention eg C: or linux /
        "limit" : "4" #size in GB at which you'd like alert to be fired
        }
}


def get_free_space():
    """ Return folder/drive free space (in bytes) and email if less than a defined limit"""
    folder = config["disk"]["folder"]
    limit = config["disk"]["limit"]
        
    print "Folder is %s" % folder
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        freegb = free_bytes.value/(1024*1024*1024)
        #return free_bytes.value
        print "free space is %s GB" % freegb
    else:
        #return os.statvfs(folder).f_bfree
        freegb = os.statvfs(folder).f_bfree/(1024*1024)
        print "free space is %s GB" % freegb
            
    if int(freegb) <= int(limit):
        send_alert(folder)
        
def send_alert(folder):
    """send an email"""
    
    local_vars = locals()
    email_subject = config["email"]["subject"] % local_vars
    email_message = config["email"]["message"] % local_vars

    email_body = "\r\n".join(["From: %s" % config["email"]["from"], "To: %s" % ";".join(config["email"]["to"]), "Subject: %s" % email_subject, "", email_message])

    server = smtplib.SMTP(config["email"]["smtp_server"])
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config["email"]["username"], config["email"]["password"])
    server.sendmail(config["email"]["from"], config["email"]["to"], email_body)
    server.quit()

get_free_space()


