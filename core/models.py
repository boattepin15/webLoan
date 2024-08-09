from django.db import models
from django.contrib.auth.models import User
import uuid
import os

def profile_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('uploads', 'profile', filename)

def slip_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('uploads', 'slip', filename)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile.png", upload_to=profile_image_path)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "โปรไฟล์"


    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="เบอร์โทรติดต่อ")
    address_line = models.CharField(max_length=255, blank=True, verbose_name="ที่อยู่")
    province = models.CharField(max_length=100, blank=True, verbose_name="จังหวัด")
    district = models.CharField(max_length=100, blank=True, verbose_name="อำเภอ")
    postal_code = models.CharField(max_length=10, blank=True, verbose_name="รหัสไปรษณีย์")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ที่อยู่ลูกค้า"


    def __str__(self):
        return f'{self.user.username} - {self.address_line}, {self.district}, {self.province}, {self.postal_code}'

class Slip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slip')
    slip_image = models.ImageField(upload_to=slip_image_path, verbose_name="สลีป")
    cost = models.FloatField(verbose_name="จำนวนเงิน")
    approve = models.BooleanField(default=False, verbose_name="อนุมัติ")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="เวลาบันทึก")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "หลักฐานการโอนเงิน"
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.user.username} - Slip'

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='location')
    lat = models.CharField(max_length=255, verbose_name="ละติจูด")
    lng = models.CharField(max_length=255, verbose_name="ลองจิจูด")
    map_link = models.URLField(max_length=255, verbose_name="google map")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="เวลาบันทึก")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ตำแหน่งของลูกค้า"

    def __str__(self):
        return self.user.username

class Checkin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkins')
    checkin = models.BooleanField(default=False, verbose_name="เปิดให้เช็คอิน")
    checkin_time = models.DateTimeField(auto_now_add=True)
    des = models.CharField(max_length=255, verbose_name="คำอธิบาย")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "เครดิต"


    def __str__(self):
        return f'{self.user.username} checked in at {self.checkin_time} - {self.des}'
