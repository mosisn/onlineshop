from rest_framework import serializers
from models.product import Product
from models.category import Category


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