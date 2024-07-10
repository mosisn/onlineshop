from django.db import models
from users.models import User
from products.models import Product

# Define the choices for the order status
ORDER_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled')
]

class Order(models.Model):
    """
    Represents an order placed by a user in the online shop application.

    Attributes:
        user (models.ForeignKey): The user who placed the order.
        order_date (models.DateTimeField): The date and time when the order was placed.
        cost (models.PositiveIntegerField): The total cost of the order.
        status (models.CharField): The current status of the order, chosen from the `ORDER_STATUS_CHOICES`.
        address (models.TextField): The delivery address for the order.
        created_at (models.DateTimeField): The date and time when the order was created.
        updated_at (models.DateTimeField): The date and time when the order was last updated.

    Methods:
        __str__(): Returns a string representation of the order.
        total_cost: Calculates the total cost of the order.
        total_products: Calculates the total number of products in the order.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    order_date = models.DateTimeField(
        auto_now_add=True
    )
    cost = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='pending'
    )
    address = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    @property
    def total_cost(self):
        return sum(item.quantity * item.price for item in self.items.all())

    @property
    def total_products(self):
        return sum(item.quantity for item in self.items.all())

class OrderItem(models.Model):
    """
    Represents an item in an order placed by a user in the online shop application.

    Attributes:
        order (models.ForeignKey): The order that this item belongs to.
        product (models.ForeignKey): The product that was ordered.
        quantity (models.PositiveIntegerField): The quantity of the product that was ordered.
        price (models.PositiveIntegerField): The price of the product at the time of the order.

    Methods:
        __str__(): Returns a string representation of the order item.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
