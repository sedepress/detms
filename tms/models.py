from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True

class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    user = models.ManyToManyField(User, through='UserCompany')

    def __str__(self):
        return self.name

class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_user_company'

class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through='UserProject')

    def __str__(self):
        return self.name

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_user_project'

class Customer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

class Carrier(models.Model):
    name = models.CharField(max_length=128)
    type = models.PositiveSmallIntegerField()
    tax_rate = models.DecimalField(max_digits=10, decimal_places=4)
    contact = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    bank = models.CharField(max_length=50, blank=True)
    bank_num = models.CharField(max_length=50, blank=True)
    bank_person = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Gear(models.Model):
    name = models.CharField(max_length=128)
    type = models.PositiveSmallIntegerField()
    start_range = models.PositiveSmallIntegerField()
    end_range = models.PositiveSmallIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=128)
    type = models.PositiveSmallIntegerField()
    contract_no = models.CharField(max_length=50, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    contact = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Line(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ori_province = models.PositiveIntegerField()
    ori_province_name = models.CharField(max_length=50)
    ori_city = models.PositiveIntegerField()
    ori_city_name = models.CharField(max_length=50)
    ori_area = models.PositiveIntegerField()
    ori_area_name = models.CharField(max_length=50)
    des_province = models.PositiveIntegerField()
    des_province_name = models.CharField(max_length=50)
    des_city = models.PositiveIntegerField()
    des_city_name = models.CharField(max_length=50)
    des_area = models.PositiveIntegerField()
    des_area_name = models.CharField(max_length=50)

class ContractData(Base):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, blank=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.CharField(max_length=256, blank=True)

    class Meta:
        db_table = 'tms_contract_data'

class Area(models.Model):
    part_id = models.PositiveIntegerField()
    pid = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    merger_name = models.CharField(max_length=50)
    code = models.PositiveSmallIntegerField()
    zip_code = models.PositiveIntegerField()
    lel = models.PositiveSmallIntegerField()
    pinyin = models.CharField(max_length=50)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name