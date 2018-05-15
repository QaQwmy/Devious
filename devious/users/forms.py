from django import forms


# 用户登录表单验证
class UserLoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)


# 用户注册表单验证
class UserRegisterForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
	email = forms.EmailField(required=True)


# 添加收货地址的表单验证
class AddressForm(forms.Form):
	name = forms.CharField(required=True)
	phone = forms.CharField(required=True,error_messages={'required':  "密码不能为空"})
	address = forms.CharField(required=True)


# 上传图片验证
class Upload(forms.Form):
	image_title = forms.FileField(required=False)
	image_detail = forms.FileField(required=False)


class Upload1(forms.Form):
	image = forms.FileField(required=False)