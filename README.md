# settings.py
add the settings.py these

- CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
- CRISPY_TEMPLATE_PACK = "bootstrap5"
- AUTH_USER_MODEL = 'accounts.User'
- LOGIN_URL = '/accounts/login/' 
- LOGIN_REDIRECT_URL = '/' 
- Add to middleware
    - ...
    - 'accounts.middlewares.auth_mware.AdminLoginRestrictionMiddleware'
