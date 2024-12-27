from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('blog/post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('blog/post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('blog/post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    path('product/<slug>', views.ItemDetailView.as_view(), name='product'),

    path('additem/<slug>', views.addItem, name='additem'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('removeitem<slug>', views.removeItem, name='removeitem'),
    path('removesingleitem<slug>', views.removeSingleItem, name='removesingleitem'),
    path('payment/', views.PaymentView.as_view(), name='payment'),

    path('favorite_menu/', views.FavoriteMenuView.as_view(), name='favorite_menu'),

    path('review_menu/', views.ReviewMenuView.as_view(), name='review_menu'),


    path('favorite_view/', views.FavoriteView.as_view(), name='favorite_view'),
    path('favorite_item/<slug>', views.FavoriteItemView.as_view(), name='favorite_item'),
    path('favorite_delete/<slug>', views.FavoriteItemDeleteView.as_view(), name='favorite_delete'),


    path('favorite_add/', views.FavoriteItemAdd, name='favorite_add'),

    path('favorite_fashion/', views.FavoriteFashionView.as_view(), 
    name='favorite_fashion'),
    path('favorite_list_add/<slug>', views.FavoriteItemListAdd.as_view(), name='favorite_list_add'),
    path('favorite_list_delete/<slug>', views.FavoriteItemListDelete.as_view(), name='favorite_list_delete'),
    
    path('thanks/', views.ThanksView.as_view(), name='thanks'),

    path('fashion_customize/', views.FashionCustomize.as_view(), name='fashion_customize'),
    path('fashion_check/', views.FashionCheck.as_view(), name='fashion_check'),
    path('fashion_view/<slug>', views.FashionView.as_view(), name='fashion_view'),
    
    path('fashion_view_review/<slug>', views.FashionReviewPost.as_view(), name='fashion_view_review'),
    path('fashion_view_review/success', views.FashionReviewSuccess.as_view(), name='fashion_view_review_success'),
    
    path('fashion_view_review_list/', views.FashionReviewList.as_view(), name='fashion_view_review_list'),


    path('fashion_customize_edit/<slug>', views.FashionCustomizeEdit.as_view(), name='fashion_customize_edit'),
    path('fashion_field_edit/<slug>', views.FashionFieldEdit.as_view(), name='fashion_field_edit'),
    path('fashion_customize_delete/<slug>', views.FashionCustomizeDelete.as_view(), name='fashion_customize_delete'),
    path('fashion_customize_review_edit/<int>/<slug>', views.FashionReviewEdit.as_view(), name='fashion_customize_review_edit'),
    path('fashion_customize_review_delete/<int>/<slug>', views.FashionReviewDelete.as_view(), name='fashion_customize_review_delete'),


    path('fashion_my_list/', views.FashionMyList.as_view(), name='fashion_my_list'),
    path('fashion_list/', views.FashionList.as_view(), name='fashion_list'),

    path('review/post/<slug>', views.ReviewPost.as_view(), name='review_post'),
    path('review/success', views.ReviewSuccess.as_view(), name='review_success'),
    path('review_list/', views.ReviewList.as_view(), name='review_list'),
    path('review_edit/<int>/<slug>', views.ReviewEdit.as_view(), name='review_edit'),
    path('review_delete/<int>/<slug>', views.ReviewDelete.as_view(), name='review_delete'),

    path('like_for_post/', views.like_for_post, name='like_for_post'),  # 追加
    path('like/', views.like, name='like'),  # 追加
]