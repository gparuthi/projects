import redis
from datetime import datetime
import smtplib
import argparse
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


def send(user, pwd, to, subject, text):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, pwd)
    mailServer.sendmail(user, to, msg.as_string())
    mailServer.close()

DM_OBSERVER_CH = 'dm_observer'

class DataMiningListener(object):
	def __init__(self):
		self.rc = redis.Redis(host='gauravparuthi.com', port=6379, db=1)
		self.ps = self.rc.pubsub()
		self.ps.subscribe([DM_OBSERVER_CH,'All'])

	def run(self):
		for item in self.ps.listen():
			if item['type'] == 'message':
				# send email to me
				msg = str(item['data'])
				print 'Sending email with subject: '+ msg
				send('kinggp@gmail.com', 'gpisgreat', 'gparuthi@gmail.com', 'DM_UPDATE', msg)	

print 'Listening to Redis now'
dml = DataMiningListener()
dml.run()