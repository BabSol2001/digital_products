from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE) #
    title = models.CharField(_('title'),max_length=100)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categories/')
    is_enabled = models.BooleanField(_('is enabled'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    update_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    category = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    update_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

class File(models.Model):
    product = models.ForeignKey('product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=100)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    update_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')