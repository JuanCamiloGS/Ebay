from django.db import models


class DevilUser(models.Model):
    USER_TYPES = (
        (1, 'normal'),
        (2, 'admin'),
    )

    USER_STATUS = (
        (1, 'nonblocked'),
        (2, 'blocked'),
    )

    username = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    user_mail = models.EmailField(blank=False)
    user_type = models.IntegerField(choices=USER_TYPES)
    user_description = models.TextField()
    user_status = models.IntegerField(choices=USER_STATUS)
    last_online = models.DateTimeField(auto_now=True)


class UserCalification(models.Model):
    target_username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Target User',
        related_name='user_calification_target_user'
    )
    origin_username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Origin User',
        related_name='user_calification_origin_user'
    )
    rating = models.FloatField()
    comment = models.TextField()


class UserAddress(models.Model):
    ACCEPTED_NATIONS = (
        (1, 'Bepluegro'),
        (2, 'Qupraitho'),
        (3, 'Kotrijan'),
        (4, 'Oscya'),
        (5, 'Cheyyae'),
        (6, 'Straunia'),
        (7, 'Aswain'),
        (8, 'Ashain'),
        (9, 'Floal Wharia'),
        (10, 'Broir Smea'),
        (11, 'The Thundering Wall'),
        (12, 'The Sunken Ship Cliff'),
        (13, 'The Tradepost Wall'),
        (14, 'The Ancient Ravine'),
        (15, 'The Silent Cliffs'),
        (16, 'The Raging Canyon'),
    )

    username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='User of Address',
        related_name='user_address_user'
    )
    nation = user_status = models.IntegerField(choices=ACCEPTED_NATIONS)
    direction = models.TextField(blank=False)
    messager = models.IntegerField(blank=False)


class CreditCard(models.Model):
    EVIL_MONEY_COMPANIES = (
        (1, 'The Haunting Bridesmaid'),
        (2, 'The Sniveling Child'),
        (3, 'The Torment Spirit'),
        (4, 'The Depraved Gal'),
        (5, 'The Ringing Soul'),
    )

    username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='User of credit card',
        related_name='credit_card_user'
    )
    number = models.CharField(max_length=15, blank=False)
    company = models.IntegerField(choices=EVIL_MONEY_COMPANIES, blank=False)
    valid_date = models.DateField(blank=False)
    security_code = models.CharField(max_length=3, blank=False)


class Product(models.Model):
    SHIP_METHODS = (
        (1, 'Banshee Carrier'),
        (2, 'Underground Worm'),
        (3, 'Frost Dragon'),
        (4, 'Succubus')
    )
    PAY_METHODS = (
        (1, 'Auction'),
        (2, 'Buy now')
    )

    PRODUCT_STATUS = (
        (1, 'nonblocked'),
        (2, 'blocked'),
    )

    username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='User of product',
        related_name='product_user'
    )
    ship_method = models.IntegerField(choices=SHIP_METHODS, blank=False)
    pay_method = models.IntegerField(choices=PAY_METHODS, blank=False)
    main_picture = models.CharField(max_length=50)
    product_descrition = models.TextField()
    valid_date = models.DateField(blank=False)
    product_status = models.IntegerField(choices=PRODUCT_STATUS)
    current_value = models.IntegerField(blank=False)
    publish_date = models.DateField(blank=False)


class ProductCalification(models.Model):
    target_product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Target User',
        related_name='product_calification_target_user'
    )
    origin_username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Origin User',
        related_name='product_calification_origin_user'
    )
    rating = models.FloatField()
    comment = models.TextField()


class BlockedProduct(models.Model):
    target_product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Target User',
        related_name='blocked_product_target_product'
    )
    origin_username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Origin User',
        related_name='blocked_product_origin_user'
    )
    comment = models.TextField()


class BlockedUser(models.Model):
    target_username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Target User',
        related_name='blocked_user_target_user'
    )
    origin_username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Origin User',
        related_name='blocked_user_origin_user'
    )
    comment = models.TextField()


class Ticket(models.Model):
    date = models.DateField(auto_now=True)
    pay_method = models.IntegerField(choices=Product.PAY_METHODS)
    ship_method = models.IntegerField(choices=Product.SHIP_METHODS)
    customer = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Buyer',
        related_name='ticket_buyer'
    )
    ship_address = models.ForeignKey(
        UserAddress,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Shipping Address',
        related_name='ticket_ship_address'
    )
    bill_address = models.ForeignKey(
        UserAddress,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Billing Address',
        related_name='ticket_bill_address'
    )
    bill_card = models.ForeignKey(
        CreditCard,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Credit Card',
        related_name='ticket_credit_card'
    )


class BoughtProduct(models.Model):
    username = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Buyer',
        related_name='bought_product_buyer'
    )
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Good',
        related_name='bought_product_good'
    )
    date = models.DateField(auto_now=True)
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Buy Ticket',
        related_name='bought_product_ticket'
    )


class Category(models.Model):
    description = models.TextField(blank=False)


class ProductCategory(models.Model):
    category = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Category',
        related_name='product_category_category'
    )
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Good',
        related_name='product_category_good'
    )


class ProductAuctionValueStamp(models.Model):
    value = models.IntegerField(blank=False)
    date = models.DateField(auto_now=True)
    bider = models.ForeignKey(
        DevilUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Buyer',
        related_name='pavs_buyer'
    )
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Good',
        related_name='pavs_good'
    )


class ProductBuyNowValueStamp(models.Model):
    value = models.IntegerField(blank=False)
    date = models.DateField(auto_now=True)
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Good',
        related_name='pbnvs_good'
    )
