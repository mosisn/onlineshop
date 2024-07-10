from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    Represents a product category in the online shop application.

    Attributes:
        name (models.CharField): The name of the category, with a maximum length of 200 characters.
        slug (models.SlugField): A unique URL-friendly slug for the category, automatically generated from the category name.
            - The `unique` parameter ensures that each slug is unique across all categories.
            - The `blank` parameter allows the slug field to be left blank, as it will be automatically generated.

    Methods:
        save(self, *args, **kwargs): Overrides the default save method to automatically generate the slug from the category name if it has not been set.
            - If the `slug` field is empty, it generates a slug using the `slugify` function from `django.utils.text`.
            - Calls the parent class's `save` method to save the updated object.
    """
    name = models.CharField(
        max_length=200
    )
    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
