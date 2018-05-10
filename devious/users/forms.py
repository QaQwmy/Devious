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
