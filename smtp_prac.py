##import smtplib
##message = """From: From Person <minatoryan7@gmail.com> 
##To: To Person <marvinryan@ymail.com>
##Subject: This is an Email from python
##
##This is a test e-mail message.
##Foobar*1000000000!!!! Yeeeyankdaakdadp[ofafaaar]
##"""
##mail = smtplib.SMTP('smtp.gmail.com',465)
##
##mail.ehlo() # identify self to server, ehlo is for extendedsmtp server helo is for normal
##mail.starttls() #Transport Layer Security, any commands after this will be encrypted
##mail.login('minatoryan7@gmail.com','password')
##sender = 'minatoryan7@gmail.com'
##receivers =['marvinryan@ymail.com']
##mail.sendmail(sender, receivers, message)
##mail.close() #close connection



import smtplib
message = """From: From Ryan Marvin <marvinryan@ymail.com>
To: To Person <minatoryan7@gmail.com> 
Subject: This is an Email from python
This is a test e-mail message via python.

Foobar*1000000000!!!! Yeeeyankdaakdadp[ofafaaar]
"""
mail = smtplib.SMTP('smtp.mail.yahoo.com',25)

mail.ehlo() # identify self to server, ehlo is for extendedsmtp server helo is for normal
mail.starttls() #Transport Layer Security, any commands after this will be encrypted
mail.login('marvinryan@ymail.com','')
sender = 'marvinryan@ymail.com'
receivers =['minatoryan7@gmail.com','cirujoy@yahoo.com','georgekiainjenga@gmail.com','evalyna.nganga@gmail.com']
mail.sendmail(sender, receivers, message)
mail.close() #close connection

