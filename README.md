django-simple-signup
====================

Simple django signup

# Setup steps

*  pip install -e git://github.com/jonashagstedt/django-simple-signup.git#egg=simple-signup
*  add ```simple_signup``` to ```INSTALLED_APPS```
*  set ```AUTH_USER_MODEL``` in settings (if you have one, else it will use Django default user)
*  add ```url(r'^accounts/', include('simple_signup.urls')),``` to your urls.py


# Additional notes

You don't have to use the exact url as proposed.
```url(r'^accounts/', include('simple_signup.urls')),``` could just as well be
```url(r'^someplaceelse/', include('simple_signup.urls')),```
