from django.db import models

# Create your models here.
# 一个类对应一张表
class Book(models.Model):
    # 唯一
    title = models.CharField('书名', max_length=50, default='', unique=True)
    # 非空
    pub=models.CharField('出版社', max_length=100, default='')
    # 总位数7,小数点位数是2
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, default=0.0)
    # 伪删除际记
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s_%s_%s'%(self.title, self.pub, self.price, self.market_price)

class Author(models.Model):
    # 必须要有max_length
    name = models.CharField('姓名', max_length=11)
    age = models.IntegerField('年龄', default=1)
    # 允许为空
    email = models.EmailField('邮箱', null=True)

    class Meta:
        db_table = 'author'
