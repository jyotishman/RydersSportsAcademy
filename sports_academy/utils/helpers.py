import json
from decimal import Decimal
from urllib.parse import urljoin, urlparse

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context


class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, Decimal):
			return float(o)
		return super(DecimalEncoder, self).default(o)


class CreateXMLContext(object):
	"""
	context = {
		'items': [
			{
				'type': "urls",
				'data': [
					{
						'loc': "url1",
						'lastmod': "date1",
						'changefreq': "monthly",
						'images': [
							{
								'loc': "image_url1"
							}
						]
					}
				]
			},
			{
				'type': "sitemaps",
				'sitemaps': [
					{
						'loc': "url2",
						'lastmod': "date2",
						'changefreq': "monthly",
						'images': [
							{
								'loc': "image_url2"
							}
						]
					}
				]
			},
			{
				'type': "images",
				'images': [
					{
					   'loc': "image_url3"
					}
				]
			}
		]
	}
	return context
	"""

	def __init__(self, host, media_url):
		self.items = []
		self.host = host
		self.media_url = urljoin(host, media_url)

	def is_valid_url(self, url):
		try:
			result = urlparse(url)
		except:
			return False
		else:
			return all([result.scheme, result.netloc, result.path])

	@property
	def generate_xml_context(self):
		return {
			'items': self.items
		}

	def __create_xml_images_context(self, images):
		if isinstance(images, str):
			return {
				'loc': images if self.is_valid_url(images) else urljoin(self.media_url, str(images))
			}
		data = []
		for image in images:
			data.append({
				'loc': image if self.is_valid_url(image) else urljoin(self.media_url, str(image))
			})
		return data

	def __create_unit_xml_context(self, loc, mode=None, lastmod=None, changefreq=None, images=[]):
		if mode == 'images':
			data = self.__create_xml_images_context(loc)
			return data
		if isinstance(loc, list) and len(loc) > 1: images = loc[0]
		data = {
			'loc': urljoin(self.host, loc)
		}
		if lastmod:
			data.update(lastmod=lastmod.strftime('%Y-%m-%dT%H:%M:%SZ'))
		if changefreq:
			data.update(changefreq=changefreq)
		if images:
			data.update(images=self.__create_xml_images_context(images))
		return data

	def __create_xml_context(self, mode, loc, lastmod=None, changefreq=None, images=[]):
		for item in self.items:
			if 'type' in item.keys() and item.get('type', None) == mode:
				if mode not in item.keys():
					return item.update({
						mode: [self.__create_unit_xml_context(loc, mode, lastmod, changefreq, images)]
					})
				else:
					return item.get(mode).append(
						self.__create_unit_xml_context(loc, mode, lastmod, changefreq, images))
		return self.items.append({
			'type': mode,
			mode: [self.__create_unit_xml_context(loc, mode, lastmod, changefreq, images)]
		})

	def create_xml_url_context(self, loc, lastmod=None, changefreq=None, images=[]):
		self.__create_xml_context("urls", loc, lastmod, changefreq, images)

	def create_xml_sitemap_context(self, loc, lastmod=None, changefreq=None, images=[]):
		self.__create_xml_context("sitemaps", loc, lastmod, changefreq, images)

	def create_xml_image_context(self, loc, lastmod=None, changefreq=None):
		self.__create_xml_context("images", loc, lastmod=lastmod, changefreq=changefreq)


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
