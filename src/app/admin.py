from django.contrib import admin
from .models import Post

from .models import Item, OrderItem, Order, Payment, FavoriteItemList, FashionSaveList, FashionItemList, Review#EC

admin.site.register(Post)


class QuestionAdmin(admin.ModelAdmin):
    list_filter = [('upload_user__first_name'), 'category', 'brand']
    search_fields = ['upload_user', 'category', 'brand']

admin.site.register(Item, QuestionAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(FavoriteItemList)

admin.site.register(FashionSaveList)
admin.site.register(FashionItemList)
admin.site.register(Review)
