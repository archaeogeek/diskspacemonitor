import os,sys
import platform
import ctypes
import smtplib


config = {
    "email": {
        "from": "jocook@astuntechnology.com",
        "to": ["jocook@astuntechnology.com"],
        "subject": "Disk Space Monitor: %(folder)s",
        "message": "The drive %(folder)s is reaching its space limit. \n\nThe Monitoring Pixie.",
        "username": "jocook@astuntechnology.com",
        "password": "jwh30Astun",
        "smtp_server": "smtp.gmail.com:587"
    },
    
    "disk":{
		"folder": "C:",
		"limit" : "4"
		}
}


def get_free_space():
		
	""" Return folder/drive free space (in bytes)"""
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

	#should allow people to enter folder/drive as an option, and do conversion to unicode automatically. Should email results if gets below a defined value
	# should check more than one drive as well, eg C, D, E

