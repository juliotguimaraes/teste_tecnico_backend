from django.test import TestCase

from ..serializers import CompraSerializer
from .factories import CompraFactory


class CompraSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Compra object for each field."""
        compra = CompraFactory()
        for field_name in [
            'date', 'discount', 'manufacturer_id', 'product', 'product_id', 'quantity', 'store_id', 'total_value', 'value'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(compra, field_name)
            )
