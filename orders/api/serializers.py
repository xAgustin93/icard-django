from rest_framework.serializers import ModelSerializer

from orders.models import Order
from products.api.serializers import ProductSerializer
from tables.api.serializers import TableSerializer


class OrderSerializer(ModelSerializer):
    product_data = ProductSerializer(source='product', read_only=True)
    table_data = TableSerializer(source='table', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'table', 'table_data', 'product',
                  'product_data', 'payment', 'close', 'created_at']
