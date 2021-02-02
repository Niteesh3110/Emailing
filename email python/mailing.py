import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'NIteesh Panchal'
email['to'] = 'niteeshpanchal31@gmail.com' 
email['subject'] = 'Wassup!'

email.set_content('You suck :)')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smpt:
	smpt.ehlo()
	smpt.starttls()
	smpt.login('niteeshpanchal2000@gmail.com', 'Niteesh31')
	smpt.send_message('email')
	print("ALL DONE!")
