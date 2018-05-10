from random import Random
from django.core.mail import send_mail
from users.models import EmailCode
from devious.settings import EMAIL_FROM


# 生成随机字符串
def random_str(randomlength=8):
	str = ''
	chars = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	length = len(chars)-1
	random = Random()
	for i in range(randomlength):
		str += chars[random.randint(0,length)]
	return str


def send_register_email(email,send_type='register'):
	email_record = EmailCode()
	if send_type== "update_email":
		code = random_str(4)
	else:
		code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type =send_type
	email_record.save()


	email_title = ''
	email_body = ''

	if send_type == 'register':
		print('zhuce-----------------------》')
		email_title = '众筹网注册'
		email_body = '请点击下面的链接激活你的账号，http://127.0.0.1:8000/active/{0}'.format(code)

		send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
		print(send_status)
		if send_status:
			pass
	elif send_type == 'forgot':
		email_title = '众筹网修改密码链接'
		email_body = '请点击下面的链接修改你的密码，http://127.0.0.1:8000/reset/{0}'.format(code)

		send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
		if send_status:
			pass

	elif send_type == 'update_email':
		email_title = '众筹网修改邮箱链接'
		email_body = '你的邮箱验证码为{0}'.format(code)

		send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
		if send_status:
			pass