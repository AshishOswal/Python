import smtplib                            #library for SMTP(simple mail transfer protocol) 

gmail_user=("useremail@gmail.com")        #User Credentials for Authentication  
gmail_passwd=("password")

sent_from=gmail_user                      
to='ashishoswal94@gmail.com'              #Email-ID of receiver
Subject='Workstatus'  
body='WorkDone'
Cc=['ashutosh.porwal3@gmail.com ','probal.das@hotmail.com ']  #CC if any else []
Bcc=[]
email_text = "From: %s \r\n" % sent_from + "To: %s \r\n" % to + "CC: %s \r\n" % ",".join(Cc) + "Subject: %s \r\n" % Subject + body          #Fills in the strings at respective Positions
toaddr=[to]+Cc+Bcc                        # Adds Cc and Bcc along with receivers Address       


try:
	server=smtplib.SMTP('smtp.gmail.com',587)   #Establish Connection with SMTP server
	server.ehlo()                               #Clause for the SMTP server to introduce itself with the client with Authorized Certificates 
	server.starttls()                           #Used for Secure Email Communication
	server.login(gmail_user,gmail_passwd)       #Autenticate User Provided Credentials
	server.sendmail(sent_from,toaddr,email_text)  #Sends mail 
	server.close()
	print("Email sent")
	
except:
	print("Something went wrong!")
