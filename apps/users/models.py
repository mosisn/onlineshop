from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model that extends the default Django User model.
    This model adds additional fields to the standard Django User model,
    such as email, profile picture, bio, phone number, date of birth,
    address, city, province, postal code, and last purchase date.
    """
    # Email field, unique and required
    email = models.EmailField(
        _("email address"),
        unique=True,
        null=False,
        blank=False
    )
    # Profile picture field, optional
    profile_picture = models.ImageField(
        _("profile picture"),
        upload_to='profile_pictures',
        null=True,
        blank=True
    )
    # Bio field, optional
    bio = models.TextField(
        _("bio"),
        null=True,
        blank=True
    )
    # Phone number field, optional
    phone_number = models.CharField(
        _("phone number"),
        max_length=20,
        null=True,
        blank=True
    )
    # Date of birth field, optional
    date_of_birth = models.DateField(
        _("date of birth"),
        null=True,
        blank=True
    )
    # Address field, optional
    address = models.CharField(
        _("address"),
        max_length=200,
        null=True,
        blank=True
    )
    # City field, optional
    city = models.CharField(
        _("city"),
        max_length=100,
        null=True,
        blank=True
    )
    # Province field, optional
    province = models.CharField(
        _("province"),
        max_length=100,
        null=True,
        blank=True
    )
    # Postal code field, optional
    postal_code = models.CharField(
        _("postal code"),
        max_length=20,
        null=True,
        blank=True
    )
    # Last purchase date field, optional
    last_purchase_date = models.DateField(
        _("last purchase date"),
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the full name of the user as a string.
        """
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
