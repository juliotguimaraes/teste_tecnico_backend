from django.db import models
from django.conf import settings
from decimal import Decimal
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import datetime
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

class Compra(models.Model):
    date = models.DateField(_('Data'),null=True, blank=True)
    discount = models.DecimalField(_('Desconto(R$)'), null=True, blank=True, max_digits=20, decimal_places=2, default=Decimal('0.00'))
    manufacturer_id = models.IntegerField(_('Manufatura ID'), validators=[MinValueValidator(0000000000), MaxValueValidator(9999999999)])
    product = models.CharField(_('Produto'), max_length=50, default='')
    product_id = models.IntegerField(_('Produto ID'), validators=[MinValueValidator(0000000000), MaxValueValidator(9999999999)])
    quantity = models.DecimalField(_('Quantidade'), null=True, blank=True, max_digits=20, decimal_places=2, default=Decimal('0.00'))
    store_id = models.CharField(_('Produto'), max_length=20, default='')
    total_value = models.DecimalField(_('Valor Total (R$)'), null=True, blank=True, max_digits=20, decimal_places=2, default=Decimal('0.00'))
    value = models.DecimalField(_('Valor (R$)'), null=True, blank=True, max_digits=20, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return  '%s %s' % (self.product_id, self.product)
    # class Meta:
    #     verbose_name = 'Compra'
    #     verbose_name_plural = 'Compras'
    #     ordering = ['product']
