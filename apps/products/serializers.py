from rest_framework import serializers
from models.product import Product
from models.category import Category
from models.order import Order, OrderItem
from models.review import Review
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'image',
            'description',
            'slug',
            'status',
            'price',
            'discount',
            'stock',
            'low_stock_threshold',
            'created_at',
            'updated_at',
        ]
        read_only_fiels = [
            'id',
            'created_at',
            'updated_at'
        ]
        
        def get_is_low_stock(self, object):
            return object.is_low_stock
        
        def validate_price(self, price):
            if price <= 0:
                raise serializers.ValidationError('Price must be greater than 0.')
            return price
        
        def validate_discount(self, price):
            if price < 0:
                raise serializers.ValidationError("Discount must be a non-negative number.")
            return price
        
        def create(self, validated_data):
            # Perform any custom logic before creating the product instance
            product = Product.objects.create(**validated_data)
            # Perform additional actions after creating the product instance
            return product

        def update(self, instance, validated_data):
            # Perform any custom logic before updating the product instance
            product = super().update(instance, validated_data)
            # Perform additional actions after updating the product instance
            return product 


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'quantity',
            'price'
            ]

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_cost = serializers.ReadOnlyField()
    total_products = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'order_date',
            'cost',
            'status',
            'address',
            'created_at',
            'updated_at',
            'items',
            'total_cost',
            'total_products'
            ]


class ReviewSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    Product = ProductSerializer(read_only=True)
    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'product',
            'rating',
            'text',
            'created_at',
            'updated_at'
            ]