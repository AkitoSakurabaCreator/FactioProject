from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import CustomUser #カスタムユーザー
import os

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "投稿一覧"
        verbose_name_plural = "投稿一覧"
    
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_id = models.SlugField("アイテムID")
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    like = models.IntegerField("評価", validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    created = models.DateTimeField("作成日", default=timezone.now)
    bought = models.BooleanField("購入者", default=False)
    # image = models.ForeignKey(CustomUser(author), )
    
    def __str__(self):
        return f'タイトル: {self.title} | 評価:{self.like} | 投稿者: {self.author.user_screen_id}'
    
    def get_avatar_url(self):
        # return os.path.join(settings.MEDIA_ROOT +  self.author.avatar)
        return self.author.avatar
    
    class Meta:
        verbose_name = "商品レビュー一覧"
        verbose_name_plural = "商品レビュー一覧"
    
class FashionReview(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_id = models.SlugField("アイテムID")
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    like = models.IntegerField("評価", validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    created = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return f'タイトル: {self.title} | 評価:{self.like} | 投稿者: {self.author.user_screen_id}'
    
    def get_avatar_url(self):
        return self.author.avatar
    
    class Meta:
        verbose_name = "カスタマイズコーデレビュー一覧"
        verbose_name_plural = "カスタマイズコーデレビュー一覧"


class Item(models.Model):
    title = models.CharField('タイトル', max_length=100)
    price = models.IntegerField('値段')
    category = models.CharField('カテゴリー', max_length=100)
    brand = models.CharField('ブランド', max_length=100)
    slug = models.SlugField('固有ID')
    description = models.TextField('商品説明')
    sex = models.CharField('性別', max_length=5, default="自由", choices=[('自由', '自由'),('男性', '男性'), ('女性', '女性')])
    color = models.CharField('色', max_length=10, default="None", choices=
    [
    ('白', '白'), ('グレー', 'グレー'), 
    ('黒', '黒'), ('ピンク', 'ピンク'),
    ('赤', '赤'), ('オレンジ', 'オレンジ'),
    ('ベージュ', 'ベージュ'), ('茶', '茶'),
    ('黄', '黄'), ('緑', '緑'),
    ('青', '青'), ('紫', '紫'),
    ('ネイビー', 'ネイビー'), ('カーキ', 'カーキ'),
    ('ゴールド', 'ゴールド'), ('アザー', 'アザー'),
    ('アイボリー', 'アイボリー'), ('オリーブ', 'オリーブ'),
    ]
    )
    # review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField('イメージ画像', upload_to='products_images')
    upload_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name="担当者")
    
    def __str__(self):
        if self.upload_user !=None:
            return self.title + " 担当者: " + self.upload_user.first_name
        else:
            return self.title + " 担当者: 設定してください。"
        
    class Meta:
        verbose_name = "商品一覧"
        verbose_name_plural = "商品一覧"
    

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateTimeField(default=timezone.now)
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f'{self.item.title}:{self.quantity}'
    
    class Meta:
        verbose_name = "注文一覧"
        verbose_name_plural = "注文一覧"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = "注文履歴"
        verbose_name_plural = "注文履歴"

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_change_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = "支払一覧"
        verbose_name_plural = "支払一覧"



from django.urls import reverse

class FashionSaveList(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField("タイトル", max_length=100)
    category = models.CharField("カテゴリー", max_length=100, blank=True, null=True)
    clothing = models.CharField("ジャンル", max_length=100, default='nothing')
    season = models.CharField("季節", max_length=100, default='オールシーズン')
    color = models.CharField("ベースカラー", max_length=10, default='')
    brand = models.CharField("ブランド", max_length=100, blank=True, null=True)
    # using_item = models.CharField(max_length=255, default="none")
    # fashion_item = models.ForeignKey(FashionItemList, on_delete=models.CASCADE)
    # fashion_item = models.OneToOneField(FashionItemList, on_delete=models.CASCADE)
    slug = models.IntegerField("固有ID")
    description = models.TextField("説明")
    author = models.IntegerField("作者アカウントID")
    sex = models.CharField("性別", max_length=2, default="自由")
    publish = models.BooleanField("公開", default=False)
    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "ファッション名: " + self.title + " ユーザ名: " + self.user.user_screen_id
    
    class Meta:
        verbose_name = "ファッション一覧"
        verbose_name_plural = "ファッション一覧"

class FashionItemList(models.Model):
    # FSL = models.OneToOneField(
    #     FashionSaveList, on_delete=models.CASCADE,
    #     )
    FSL = models.ForeignKey(FashionSaveList, on_delete=models.CASCADE)
    # connect_id = models.TextField(FSL.slug)
    using_item = models.CharField("使用アイテム", max_length=20)
    
    # def __str__(self):
    #     return self.FSL.title + self.FSL.slug + self.using_item
    
    def __str__(self):
        return "ファッション名: " + self.FSL.title + " ユーザ名: " + self.FSL.user.user_screen_id + " アイテムID: " + self.using_item
    
    class Meta:
        verbose_name = "ファッション使用アイテム一覧"
        verbose_name_plural = "ファッション使用アイテム一覧"
    

class FavoriteItemList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # connect_id = models.TextField(FSL.slug)
    favorite_item = models.CharField("お気に入りアイテム", max_length=200)
    created = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return " ユーザ名: " + self.user.user_screen_id + " アイテムID: " + self.favorite_item
    
    class Meta:
        verbose_name = "お気に入りアイテム一覧"
        verbose_name_plural = "お気に入りアイテム一覧"

class FavoriteFashionListItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # connect_id = models.TextField(FSL.slug)
    favorite_item = models.IntegerField("お気に入りファッションコーデ")
    created = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return " ユーザ名: " + self.user.user_screen_id + " アイテムID: " + self.favorite_item
    
    class Meta:
        verbose_name = "お気に入りファッションコーデ一覧"
        verbose_name_plural = "お気に入りファッションコーデ一覧"
    

class LikeForPost(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target = models.ForeignKey(FashionSaveList, on_delete=models.CASCADE)

class WebCam(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField('イメージ画像', upload_to='webcam')
    

def CouponWeek():
    return timezone.now() + timezone.timedelta(days=7)

class Coupon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coupon_code = models.CharField('クーポンコード', max_length=20)
    discount = models.IntegerField('割引', default=0, blank=False, null=False)
    end_date = models.DateTimeField(default=CouponWeek)
    timestamp = models.DateTimeField(default=timezone.now)

# class LikeForComment(models.Model):
#     """コメントに対するいいね"""
#     target = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(default=timezone.now)