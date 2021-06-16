from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    objects = models.Manager()
    published = PublishedManager()
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateField(auto_now_add=True, editable=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Contact(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('suspended', 'Suspended')
    )

    name = models.ForeignKey(People, max_length=100, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    on_duty = models.CharField(max_length=9, choices=STATUS_CHOICES, default='active')
    phone = models.CharField(max_length=11)
    e_mail = models.CharField(max_length=50)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.name.name}: {self.phone}'


class MembersRightOrder(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('order')


class Member(models.Model):

    ordered = MembersRightOrder()

    order = models.IntegerField(default=0)
    position = models.CharField(max_length=50)
    name = models.ForeignKey(People, max_length=100, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.position}: {self.name.name}'


class EventsRightOrder(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('-date_time')


class Event(models.Model):

    ordered = EventsRightOrder()

    date_time = models.DateTimeField()
    title = models.CharField(max_length=200)
    head = models.ForeignKey(People, max_length=100, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_time', )

    def __str__(self):
        return f'{self.date_time}: {self.title}'


class OrdersRightOrder(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('-date_time')


class Order(models.Model):

    ordered = OrdersRightOrder()

    auto_increment_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        ordering = ('-date_time',)

    def __str__(self):
        return f'{self.date_time}, {self.title}'

    def get_absolute_url(self):
        return reverse('page:order_detail', args=[self.auto_increment_id])


class PhotoView(models.Model):

    id = models.IntegerField(db_index=True, primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.title}'

    def get_absolute_url(self):
        return reverse('page:photo_view', args=[self.id])


class Feedback(models.Model):

    name = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50)
    body = models.TextField()










