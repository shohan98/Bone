from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='boneuser:index'):
    """
    Decorator for views that checks that the logged in user is a normal user,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_user,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def active_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='boneuser:index'):
    """
    Decorator for views that checks that the logged in user is an active account,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


#def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
#    """
#    Decorator for views that checks that the logged in user is a teacher,
#    redirects to the log-in page if necessary.
#    """
#    actual_decorator = user_passes_test(
#        lambda u: u.is_active and u.is_admin,
#        login_url=login_url,
#        redirect_field_name=redirect_field_name
#    )
#    if function:
#        return actual_decorator(function)
#    return actual_decorator
