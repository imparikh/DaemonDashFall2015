import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage

class email:
	
	fromaddress = 'SmartSpenderCRU@yahoo.com'
	toaddress = 'brandongrinkemeyer@gmail.com'
	text = 'Your child is projected to go over his or her budget. Please review the projection.'

	username = 'SmartSpenderCRU'
	password = 'daemondash'
	
	
	msg = MIMEMultipart()
	msg['From'] = fromaddress
	msg['To'] = toaddress
	msg['Subject'] = 'Spending Limit Warning'

	
# 	def _init_ (self, averagespendingperday, hasoutlier):
# 		self.hasoutlier = hasoutlier
	
# 	itemname = ''
# 	itemprice = ''
# 	purchasedate = ''
# 	averagespendingperday = ''
# 	hasoutlier = ''
	def __init__(self, itemname, itemprice, purchasedate, averagespendingperday, hasoutlier):

		self.itemname = itemname
		self.itemprice = itemprice
		self.purchasedate = purchasedate
		self.averagespendingperday = averagespendingperday
		self.hasoutlier = hasoutlier
		
	def run(self):
		if self.hasoutlier:
			self.text += ' The most outstanding purchase has been %s for %d at %s.' % (self.itemname, self.itemprice, self.purchasedate)
		
		self.text += ' The average spending per day has been %d.' % (self.averagespendingperday)

# for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.


#########the following testing.png file name has to be changed#######

		self.msg.attach(MIMEText(self.text))
		fp = open('testing.png', 'rb')
		img = MIMEImage(fp.read())
		fp.close()
		self.msg.attach(img)

		server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(self.username, self.password)

		server.sendmail(self.fromaddress, self.toaddress, self.msg.as_string())
		server.quit()
