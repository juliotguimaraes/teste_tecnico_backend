from factory import DjangoModelFactory, Faker
from ..models import Compra

class CompraFactory(DjangoModelFactory):
    date = Faker('2020-06-03')
    discount = Faker('0.0')
    manufacturer_id = Faker('59852')
    product = Faker('COMEDOURO VIDA PET PCAES 236ML UN')
    product_id = Faker('251865')
    quantity = Faker('2.0')
    store_id = Faker('3_8')
    total_value = Faker('17.98')
    value = Faker('8.99')

    class Meta:
        model = Compra
