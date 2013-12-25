django-simple-signup
====================

Simple django signup

# Description
This is using the user creation form from Django, however the native form doesn't allow you to set the user model.
Therefore, I copied it and added a few views around this.


# Setup steps

*  pip install -e git://github.com/jonashagstedt/django-simple-signup.git#egg=simple-signup
*  (if you don't use your own template) pip install -e git://github.com/jonashagstedt/django-form-mangler.git#egg=form_mangler
*  add ```simple_signup``` to ```INSTALLED_APPS```
*  set ```AUTH_USER_MODEL``` in settings (if you have one, else it will use Django default user)
*  add ```url(r'^accounts/', include('simple_signup.urls')),``` to your urls.py


# Additional notes

You don't have to use the exact url as proposed.
```url(r'^accounts/', include('simple_signup.urls')),``` could just as well be
```url(r'^someplaceelse/', include('simple_signup.urls')),```
