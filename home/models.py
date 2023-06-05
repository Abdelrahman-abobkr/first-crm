from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    age = models.CharField(max_length = 2, blank=True, null=True)
    img = models.ImageField(upload_to='Customer_Photo', default='2.png')
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

    def img_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.img))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Customer, self).save(*args, **kwargs)



@receiver(post_save, sender=User)
def CreateUserProfile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(user=instance)



class Product(models.Model):
    name = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Out Of Order', 'Out Of Order'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name