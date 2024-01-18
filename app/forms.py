from django import forms

from django.db import models

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='本文', widget=forms.Textarea())

class PostReview(forms.Form):
    title = forms.CharField(label='タイトル', max_length=200)
    content = forms.CharField(label='本文', widget=forms.Textarea())
    # like = forms.IntegerField(label='評価', min_value=1, max_value=5)
    # content_id = forms.SlugField(label='アイテムID')
    # bought = forms.BooleanField(label='購入者', initial=False)


class FashionPostReview(forms.Form):
    title = forms.CharField(label='タイトル', max_length=200)
    content = forms.CharField(label='本文', widget=forms.Textarea())


class SexChoices(models.TextChoices):
    MAN = '男性', '男性'
    WOMAN = '女性', '女性'
    FREE = '自由', '自由'

class SeasonChoices(models.TextChoices):
    ALL_SEASON = 'オールシーズン', 'オールシーズン'
    SUMMER = '夏', '夏'
    SPRING = '春', '春'
    AUTUMN = '秋', '秋'
    WINTER = '冬', '冬'
    
class ClothingChoices(models.TextChoices):
    CASUAL = 'カジュアル', 'カジュアル'
    FORMAL = 'フォーマル', 'フォーマル'
    BASIC = 'ベーシック', 'ベーシック'
    NATURAL = 'ナチュラル', 'ナチュラル'
    SIMPLE  = ' シンプル', 'シンプル'
    MONOTONE = 'モノトーン', 'モノトーン'
    STREET = 'ストリート' , 'ストリート'
    CLASSY = 'きれいめ' , 'きれいめ'
    GIRLY =  'ガーリー', 'ガーリー'
    FEMININ = 'フェミニン' , 'フェミニン'
    BOYISH = 'ボーイッシュ' , 'ボーイッシュ'
    MILITARY = 'ミリタリー' , 'ミリタリー'
    MODE = 'モード' , 'モード'
    TRADITIONAL = 'トラッド' , 'トラッド'
    GAL = 'ギャル' , 'ギャル'
    CONSERVATIVE = 'コンサバ' , 'コンサバ'
    HARAJYUKU_STYLE = '原宿' , '原宿'
    GOTHIC_LOLITA = 'ゴスロリ ' , 'ゴスロリ '
    
class ColoringChoices(models.TextChoices):
    WHITE = '白', '白'
    GRAY = 'グレー', 'グレー'
    BLACK = '黒', '黒'
    PINK = 'ピンク', 'ピンク'
    RED = '赤', '赤'
    ORANGE = 'オレンジ', 'オレンジ'
    BEIGE = 'ベージュ', 'ベージュ'
    BROWN = '茶', '茶'
    YELLOW = '黄', '黄'
    GREEN = '緑', '緑'
    BLUE = '青', '青'
    PURPLE = '紫', '紫'
    NAVY = 'ネイビー', 'ネイビー'
    KHAKI = 'カーキ', 'カーキ'
    GOLD = 'ゴールド', 'ゴールド'
    AZURE = 'アザー', 'アザー'
    IVORY = 'アイボリー', 'アイボリー'
    OLIVE = 'オリーブ', 'オリーブ'

class FashionSaveForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=100)
    # category = forms.CharField(label='カテゴリー', max_length=100)
    clothing = forms.fields.ChoiceField(
        choices=ClothingChoices.choices,
        required=True,
        label='服のジャンル'
    )
    season = forms.fields.ChoiceField(
        choices=SeasonChoices.choices,
        required=True,
        label='季節'
    )
    # brand = forms.CharField(label='ブランド', max_length=255) #True消すの忘れずに！
    
        # publish = forms.BooleanField(initial=False)
    # sex = forms.CharField(label='性別', max_length=5)
    sex = forms.fields.ChoiceField(
        choices=SexChoices.choices,
        required=True,
        label='性別'
    )
    color = forms.ChoiceField(
        choices=ColoringChoices.choices,
        required=True,
        label='カラー'
    )

    description = forms.CharField(label='説明欄', widget=forms.Textarea)
    publish_list = [('False','非公開'),('True','公開')]
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=publish_list, initial='False')

class Coupon(forms.Form):
    couponcode = forms.CharField(label='クーポンコード', max_length=20)