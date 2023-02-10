import logging

from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


logger = logging.getLogger('auth')


@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    """Log when user logs in."""
    logger.info('User %s login successful.', user)


@receiver(user_logged_out)
def log_user_logout(sender, user, **kwargs):
    """Log when user logs out."""
    logger.info('User %s logout successful.', user)


@receiver(user_login_failed)
def log_user_login_failed(sender, request, **kwargs):
    """Log when user login fails."""
    user = request.POST.get("username")
    logger.info('User login failed for: %s', user)
