from django.shortcuts import render
import urllib2
import urllib
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError



def demo(request):
	return render(request,'index.html',{})

def contact_us(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		subject = request.POST.get("subject")
		message = request.POST.get("comments")

		admin_email = 'amol.thinksoft@gmail.com'

		email_template = render_to_string('green/mail_template.html',{'name':name, 'user_email':email})
		try:
			send_mail(
			subject, 
			message, 
			'', 
			[admin_email],
			html_message=email_template,
			#html_message=template,
			fail_silently=False
			)
			print "successfully Send Email"
		except BadHeaderError:
			return HttpResponse('Invalid header format.')

		# sendMail(subject,user_email, message, admin_email)

		# m = Mailin("https://api.sendinblue.com/v2.0","AEZV8NkOQsUWPzIR")
		# data = { "to" : {"amol.shoffex@gmail.com":"to whom!"},
		# "from" : ["@gmail.com","from email!"],
		# "replyto" : [""+email,"reply to!"],
		# "subject" : " "+subject,
		# "text" : "This is the text",
		# "html" : " "+message,
		# }
 
		# result = m.send_email(data)
  #   	print(result)
  #   	print data

	return render(request, "green/query_send.html", {})
