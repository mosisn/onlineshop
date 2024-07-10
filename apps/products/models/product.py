from django.db import models
from .category import Category
from django.utils.text import slugify
from users.models import User

STATUS_CHOICES = (
    ('active', 'Active'),
    ('draft', 'Draft'),
    ('archived', 'Archived'),
    ('sold_out', 'Sold out')
)

class Product(models.Model):
    """
    Represents a product in the online shop application.

    Attributes:
        category (models.ManyToManyField): A many-to-many relationship with the `Category` model, allowing a product to belong to multiple categories.
            - The `related_name` parameter sets the name of the reverse relation from the `Category` model to the `Product` model.
        name (models.CharField): The name of the product, with a maximum length of 250 characters.
        image (models.ImageField): The product's main image, uploaded to the 'images' directory.
        description (models.TextField): The detailed description of the product.
        slug (models.SlugField): A unique URL-friendly slug for the product, automatically generated from the product name.
            - The `unique` parameter ensures that each slug is unique across all products.
            - The `blank` parameter allows the slug field to be left blank, as it will be automatically generated.
        status (models.CharField): The current status of the product, which can be 'active', 'draft', 'archived', or 'sold_out'.
            - The `choices` parameter defines the available options for the status.
            - The `default` parameter sets the default status to 'active'.
        price (models.DecimalField): The price of the product, with a maximum of 10 digits and up to 2 decimal places.
        discount (models.DecimalField): The discount applied to the product, with a maximum of 10 digits and up to 2 decimal places.
            - The `null` and `blank` parameters allow the discount field to be left empty.
        stock (models.PositiveIntegerField): The current stock level of the product, with a default value of 0.
        created_at (models.DateTimeField): The date and time when the product was created, automatically set when the product is first saved.
        updated_at (models.DateTimeField): The date and time when the product was last updated, automatically set whenever the product is saved.

    Methods:
        save(self, *args, **kwargs): Overrides the default save method to automatically generate the slug from the product name if it has not been set.
            - If the `slug` field is empty, it generates a slug using the `slugify` function from `django.utils.text`.
            - Calls the parent class's `save` method to save the updated object.
    """
    category = models.ManyToManyField(
        Category,
        related_name='products'
    )
    name = models.CharField(
        max_length=250
    )
    image = models.ImageField(
        upload_to='images'
    )
    description = models.TextField()
    slug = models.SlugField(
        unique=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    stock = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
