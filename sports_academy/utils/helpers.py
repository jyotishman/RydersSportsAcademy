import json
from decimal import Decimal

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context


class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, Decimal):
			return float(o)
		return super(DecimalEncoder, self).default(o)


def send_mail(subject, recipient_list, message, from_email=settings.DEFAULT_FROM_EMAIL, silence=False, context={}):
	context = Context(context)
	if not from_email:
		print("DEFAULT_FROM_EMAIL is not configured. Check conf.ini")
		# log_on_sentry(
		#     "DEFAULT_FROM_EMAIL is not configured. Check conf.ini",
		#     None,
		#     'ERROR',
		# )
		from_email = 'showtopten@gmail.com'

	mail = EmailMultiAlternatives(
		subject,
		message,
		from_email,
		recipient_list,
		bcc=[],
		cc=[],
	)
	mail_response = mail.send(fail_silently=silence)
	if not mail_response:
		print("Mail was not sent")
		# log_on_sentry(
		#     "Mail was not sent",
		#     None,
		#     "WARNING",
		#     extra={
		#         'subject': subject,
		#         'message': message,
		#         'mail_context': str(context),
		#     }
		# )
		return False
	return True


def convert_to_dict(data):
	return json.loads(json.dumps(data))
