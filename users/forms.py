from django.forms import ModelForm

from users.models import User


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'telephone', 'city', 'zip', 'oranges',
                  'active']
