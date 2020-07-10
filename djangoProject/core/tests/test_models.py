from django.test import TestCase

from ..models import Compra
from .factories import CompraFactory

class CompraTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        compra = CompraFactory()
        self.assertEqual(str(compra), compra.product_id)
