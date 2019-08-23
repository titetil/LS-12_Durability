
import smtplib
import sys

gmail_user = "ctctesttank@gmail.com"
gmail_pwd = "carotestcenter"
FROM = "ctctesttank@gmail.com"
TO = sys.argv[1]
SUBJECT = sys.argv[2]
TEXT = sys.argv[3]

# Prepare actual message
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, [TO], SUBJECT, TEXT)

# SMTP_SSL Example
server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo() # optional, called by login()
server_ssl.login(gmail_user, gmail_pwd)  
# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
server_ssl.sendmail(FROM, TO, message)
#server_ssl.quit()
server_ssl.close()
print('successfully sent the mail')
