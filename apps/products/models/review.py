from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .product import Product
from users.models import User

class Review(models.Model):
    """
    Represents a review for a product in the online shop application.

    Attributes:
        product (models.ForeignKey): A foreign key to the `Product` model, representing the product being reviewed.
        user (models.ForeignKey): A foreign key to the `User` model, representing the user who left the review.
        rating (models.PositiveIntegerField): The rating given by the user, ranging from 1 to 5 (inclusive).
            - The `verbose_name` parameter sets the human-readable name for this field in the admin interface.
            - The `default` parameter sets the default rating to 5.
            - The `validators` parameter ensures that the rating is between 1 and 5 (inclusive) using the `MinValueValidator` and `MaxValueValidator` classes.
            text (models.TextField): The text of the review written by the user.
            - The `verbose_name` parameter sets the human-readable name for this field in the admin interface.
        created_at (models.DateTimeField): The date and time when the review was created, automatically set when the review is first saved.
        updated_at (models.DateTimeField): The date and time when the review was last updated, automatically set whenever the review is saved.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        verbose_name='Rating',
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField(
        verbose_name='Review Text'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
