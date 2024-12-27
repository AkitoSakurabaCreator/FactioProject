from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm, PostReview, FashionSaveForm, Coupon, FashionPostReview
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item, OrderItem, Order, Payment, Review, FashionSaveList, FashionItemList, LikeForPost, Like, FavoriteItemList, FavoriteFashionListItem,FashionReview #EC
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser

from django.db.models import Q

from django.core.paginator import Paginator

from django.http import JsonResponse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        search_data = ''
        sex_data = ''
        item_data = Item.objects.all()


        
        # paginator = Paginator(item_data, 10) # 1ページに10件表示
        paginator = Paginator(item_data, 52) # 1ページに10件表示
        p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
        item_data = paginator.get_page(p) # 指定のページのArticleを取得


        return render(request, 'app/store/index.html', {
            'item_data': item_data,
            'search_data': search_data,
            # 'articles': articles
        })

    def post(self, request, *args, **kwargs):
        item_data = Item.objects.all()
        search_data = request.POST['search']
        search_id_data = request.POST['search_id']
        sex_data = request.POST['sex']
        
        print(Item.objects.filter(Q(sex=sex_data)).all())

        if search_id_data == 'title':
            result = Item.objects.filter(Q(title__contains=search_data)).all()
        elif search_id_data == 'category':
            result = Item.objects.filter(Q(category=search_data)).all()
            
        elif search_id_data == 'brand':
            result = Item.objects.filter(Q(brand__contains=search_data)).all()
        else:
            result = Item.objects.filter(Q(title__contains=search_data) | Q(category=search_data) | Q(brand__contains=search_data)).all()

        return render(request, 'app/store/index.html', {
            'item_data': item_data,
            'search_data': result
        })
        
        
class BlogView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/blog/blog.html', {
            'post_data': post_data
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/blog/post_detail.html', {
            'post_data': post_data
        })

class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        return render(request, 'app/blog/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', post_data.id)

        return render(request, 'app/blog/post_form.html', {
            'form': form
        })

class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'content': post_data.content
            }
        )

        return render(request, 'app/blog/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/blog/post_form.html', {
            'form' : form
        })

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/blog/post_delete.html', {
            'post_data' : post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('Index')


class ItemDetailView(View):
    def get(self, request, *args, **kwargs):
        slug=self.kwargs['slug']
        item_data = Item.objects.get(slug=slug)
        review_data = Review.objects.filter(content_id=slug)
        Favorite_Item_List = FavoriteItemList.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()
        Favorite_data = False
        if Favorite_Item_List.count() == 0:
            Favorite_data = True
            

        paginator = Paginator(review_data, 3)
        p = request.GET.get('p')
        review_data = paginator.get_page(p)
        request.session['TempPage'] = request.build_absolute_uri()

        return render(request, "app/store/product.html", {
            'item_data': item_data,
            "review_data": review_data,
            'slug': slug,
            'favorite': Favorite_data
        })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_item_count = self.object.like_for_item_set.count()
        # ポストに対するイイね数
        context['like_for_item_count'] = like_for_item_count
        # ログイン中のユーザーがイイねしているかどうか
        if self.object.like_for_item_set.filter(user=self.request.user).exists():
            context['is_user_liked_for_item'] = True
        else:
            context['is_user_liked_for_item'] = False

        return context


# まだ
class ItemReviewView(View):
    
    
    def get(self, request, *args, **kwargs):
        slug=self.kwargs['slug']
        item_data = Item.objects.get(slug=slug)
        review_data = Item.objects.filter(content_id=slug)
        return render(request, "app/store/product.html", {
            'item_data': item_data,
            'slug': slug
        })
    


class ReviewPost(View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.get(slug=self.kwargs['slug'])
        form = PostReview(request.POST or None)
        print (item_data)
        # review_data = Review.objects.filter(content_id=self.kwargs['slug'])
        context={
            'form': form,
            'item_data': item_data
        }
        return render(request, "app/review/review_post.html", context)
    
    def post(self, request, *args, **kwargs):
        content_id=self.kwargs['slug']
        order = OrderItem.objects.filter(user_id=request.user.id, item__slug=content_id)
        rate = request.POST['rate']
        
        bought = False
        if order:
            bought = True

        if not(1 <= int(rate) <=5):
            raise ValueError('評価基準がおかしい。')
        form = PostReview(request.POST or None)
        if form.is_valid():
            obj = Review(
                title=form.cleaned_data['title'], 
                content=form.cleaned_data['content'],
                like=rate, bought=bought, content_id=content_id,
                author=request.user
                )

            obj.save()
            return redirect('review_success')
        else:
            print('error')
            if form.is_valid() == False:
                for ele in form :
                    print(ele)

        context={
            'form': form
        }
        return render(request, "app/review/review_post.html", context)

class ReviewSuccess(View):
    def get(self, request, *args, **kwargs):
        UserName = CustomUser.objects.get(id=request.user.id)
        context = {
            'User': UserName.first_name
        }
        return render(request, "app/review/review_success.html", context)

class ReviewList(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            item_data = Item.objects.all()
            Review_Data = Review.objects.filter(Q(author_id=request.user.id))
            paginator = Paginator(Review_Data, 10)
            p = request.GET.get('p')
            Review_Data = paginator.get_page(p)
            request.session['TempPage'] = request.build_absolute_uri()

            context={
                'item_data': item_data,
                'Review_Data': Review_Data
            }
            return render(request, 'app/review/review_list.html', context)
        else:
                response = redirect('Index')
                return response



class ReviewEdit(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            context = {}
            user_id = request.user.id
            Review_ID = self.kwargs['int']
            slug = self.kwargs['slug']
            
            request.session['TempPage'] = request.build_absolute_uri()

            Review_Data = Review.objects.filter(Q(author_id=user_id) & Q(content_id=slug) & Q(id=Review_ID))

            if Review_Data.count() > 0:
                form = PostReview(
                request.GET or None,
                initial = {
                    'title': Review_Data.last().title,
                    'content': Review_Data.last().content,
                }
            )
        
                context={
                    'form': form
                }
                return render(request, 'app/review/review_edit.html', context)
            else:
                return redirect(request.session['TempPage'])
        else:
                response = redirect('Index')
                return response
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            user_id = request.user.id
            Review_ID = self.kwargs['int']
            slug = self.kwargs['slug']
            Review_Data = Review.objects.filter(Q(author_id=user_id) & Q(content_id=slug) & Q(id=Review_ID)).last()
            
            request.session['TempPage'] = request.build_absolute_uri()
            
            rate = request.POST['rate']
            
            form = PostReview(request.POST or None)

            if form.is_valid():
                Review_Data.title = form.cleaned_data['title']
                Review_Data.content = form.cleaned_data['content']
                Review_Data.like = rate
                Review_Data.save()

            return redirect('review_list')
        else:
                response = redirect('Index')
                return response

class ReviewDelete(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            user_id = request.user.id
            Review_ID = self.kwargs['int']
            slug = self.kwargs['slug']
            Review_Data = Review.objects.filter(Q(author_id=user_id) & Q(content_id=slug) & Q(id=Review_ID))

            if Review_Data.count() > 0:
                Review_Data.last().delete()
            else:
                return redirect(request.session['TempPage'])
            return redirect(request.session['TempPage'])
        else:
                return redirect(request.session['TempPage'])


class FashionReviewEdit(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            context = {}
            user_id = request.user.id
            Review_ID = self.kwargs['int']
            slug = self.kwargs['slug']
            
            request.session['TempPage'] = request.build_absolute_uri()

            Review_Data = Review.objects.filter(Q(author_id=user_id) & Q(content_id=slug) & Q(id=Review_ID))

            if Review_Data.count() > 0:
                form = PostReview(
                request.GET or None,
                initial = {
                    'title': Review_Data.last().title,
                    'content': Review_Data.last().content,
                }
            )
        
                context={
                    'form': form
                }
                return render(request, 'app/review/review_edit.html', context)
            else:
                return redirect(request.session['TempPage'])
        else:
                response = redirect('Index')
                return response
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            user_id = request.user.id
            Review_ID = self.kwargs['int']
            slug = self.kwargs['slug']
            Review_Data = Review.objects.filter(Q(author_id=user_id) & Q(content_id=slug) & Q(id=Review_ID)).last()
            
            request.session['TempPage'] = request.build_absolute_uri()
            
            rate = request.POST['rate']
            
            form = PostReview(request.POST or None)

            if form.is_valid():
                Review_Data.title = form.cleaned_data['title']
                Review_Data.content = form.cleaned_data['content']
                Review_Data.like = rate
                Review_Data.save()

            return redirect('review_list')
        else:
                response = redirect('Index')
                return response

class FashionReviewDelete(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            user_id = request.user.id
            Review_ID = self.kwargs['int']
            slug = self.kwargs['slug']
            Review_Data = Review.objects.filter(Q(author_id=user_id) & Q(content_id=slug) & Q(id=Review_ID))

            if Review_Data.count() > 0:
                Review_Data.last().delete()
            else:
                return redirect(request.session['TempPage'])
            return redirect(request.session['TempPage'])
        else:
                return redirect(request.session['TempPage'])



class FashionReviewPost(View):
    def get(self, request, *args, **kwargs):
        form = FashionPostReview(request.POST or None)
        
        slug = self.kwargs['slug']
        item_data = Item.objects.all()
        fashion_item_data = FashionSaveList.objects.filter(Q(publish=True) & Q(slug=slug))
        if fashion_item_data.exists():
            fashion_list_data = FashionItemList.objects.filter(FSL__slug=slug).all()
        else:
            return redirect('Index')

        # print (fashion_item_data)
        context={
            'item_data': item_data,
            'fashion_item_data': fashion_item_data,
            'fashion_list_data': fashion_list_data,
            'form': form,
            'article': slug
        }
        return render(request, "app/fashion/review/review_fashion.html", context)
    
    def post(self, request, *args, **kwargs):
        content_id=self.kwargs['slug']
        order = OrderItem.objects.filter(user_id=request.user.id, item__slug=content_id)
        rate = request.POST['rate']
        
        bought = False
        if order:
            bought = True

        if not(1 <= int(rate) <=5):
            raise ValueError('評価基準がおかしい。')
        form = FashionPostReview(request.POST or None)
        if form.is_valid():
            obj = FashionReview(
                title=form.cleaned_data['title'], 
                content=form.cleaned_data['content'],
                like=rate, content_id=content_id,
                author=request.user
                )
            obj.save()
            return redirect('review_success')
        else:
            print('error')
            if form.is_valid() == False:
                for ele in form :
                    print(ele)

        context={
            'form': form
        }
        return render(request, "app/review/review_post.html", context)


# レビュー一覧
class FashionReviewList(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            item_data = Item.objects.all()
            
            FashionReview_Data = FashionReview.objects.filter(Q(author_id=request.user.id))
            
            paginator = Paginator(FashionReview_Data, 10)
            p = request.GET.get('p')
            FashionReview_Data = paginator.get_page(p)

            request.session['TempPage'] = request.build_absolute_uri()
            
            fashion_list_data = FashionItemList.objects.filter(Q(FSL__publish=True))
        
            context={
                'item_data': item_data,
                'fashion_list_data': fashion_list_data,
                'FashionReview_Data': FashionReview_Data
            }
            return render(request, 'app/fashion/review/review_fashion_list.html', context)
        else:
                response = redirect('Index')
                return response

class FashionReviewSuccess(View):
    def get(self, request, *args, **kwargs):
        UserName = CustomUser.objects.get(id=request.user.id)
        context = {
            'User': UserName.first_name
        }
        return render(request, "app/review/review_success.html", context)


@login_required
def addItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order = Order.objects.filter(user=request.user, ordered=False)

    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)

    return redirect('order')


class OrderView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            form = Coupon(request.POST or None)
            order = Order.objects.get(user=request.user, ordered=False)
            context = {
                'order': order,
                'form': form
            }
            return render(request, 'app/store/order.html', context)
        except ObjectDoesNotExist:
            return render(request, 'app/store/order.html')
        
    def post(self, request, *args, **kwargs):
        try:
            form = Coupon(request.POST or None)
            order = Order.objects.get(user=request.user, ordered=False)
            
            context = {
                'order': order,
                'form': form,
            }
            return render(request, 'app/store/order.html', context)
        except ObjectDoesNotExist:
            return render(request, 'app/store/order.html')

@login_required
def removeItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect('order')

    return redirect('product', slug=slug)


@login_required
def removeSingleItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
            return redirect('order')
    return redirect('product', slug=slug)


class PaymentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(user=request.user, ordered=False)
        user_data = CustomUser.objects.get(id=request.user.id)
        context = {
            'order': order,
            'user_data': user_data
        }
        return render(request, 'app/store/payment.html', context)

    def post(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        # print(user_data)
        if not(user_data.first_name == '' or user_data.last_name == '' or user_data.zipcode == '' or user_data.address == '' or user_data.tel == ''):
        
            order = Order.objects.get(user=request.user, ordered=False)
            order_items = order.items.all()
            amount = order.get_total()

            payment = Payment(user=request.user)
            payment.stripe_change_id = 'test_stripe_charge_id'
            payment.amount = amount
            payment.save()

            order_items.update(ordered=True)
            for item in order_items:
                item.save()

            order.ordered = True
            order.payment = payment
            order.save()
            
            send_email(order_items, user_data)

            return redirect('thanks')
        else:
            Switch = True
            user_data = CustomUser.objects.get(id=request.user.id)
            return render(request, 'accounts/profile/profile.html', {
                'user_data': user_data,
                'Switch': Switch
            })
        
from django.core.mail import EmailMultiAlternatives

def send_email(order_items, user_data):
    items = ''
    for item in order_items:
        items += item.item.title
        
    mail_title="ご注文していただきありがとうございます。"
    text_content="""
    　　　　　　　　　　　　{user_data.first_name}様、この度は{items}をご注文していただき誠にありがとうございます。
            """
    html_content=f"""
            <p>{user_data.first_name}様、この度は{items}をご注文していただき誠にありがとうございます。</p>
            <p><strong>※このメールに返信はできません</strong></p>
            <p>お問い合わせしたい内容がございましたら<a href="{{ request.scheme }}://{{ request.get_host }}inquiry/">こちらから</a>お願い致します。</p>
            """

    msg=EmailMultiAlternatives(
            subject=mail_title, 
            body=text_content, 
            from_email='任意のメールアドレス', 
            to=[user_data.email],
            )
    msg.attach_alternative(html_content,"text/html")
    msg.send()

class FavoriteMenuView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            request.session['TempPage'] = request.build_absolute_uri()
            return render(request, 'app/store/favoritemenu.html')
        else:
                response = redirect('Index')
                return response

class ReviewMenuView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            request.session['TempPage'] = request.build_absolute_uri()
            return render(request, 'app/review/review_menu.html')
        else:
                response = redirect('Index')
                return response


# お気に入りファッションコーデ一覧
class FavoriteFashionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            request.session['TempPage'] = request.build_absolute_uri()

            item_data = Item.objects.all()

            Favorite_Item_List = FavoriteFashionListItem.objects.filter(user_id=request.user.id).all()
            
            paginator = Paginator(Favorite_Item_List, 20)
            p = request.GET.get('p')
            Favorite_Item_List = paginator.get_page(p)
            

            fashion_item_data = FashionSaveList.objects.filter(publish=True).all()

            fashion_list_data = FashionItemList.objects.filter().all()
            #↑要素があるものだけを取り出すという機能にできるならばするべき。
            
            context={
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data,
                'Favorite_Item_List': Favorite_Item_List
            }
            
            return render(request, 'app/store/favorite_fashion.html', context)
        else:
                response = redirect('Index')
                return response
        
        
# お気に入りファッションコーデ一覧 ADD
class FavoriteItemListAdd(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            slug = self.kwargs['slug']
            Favorite_Item_List = FavoriteFashionListItem.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()
            if Favorite_Item_List.count() == 0:
                obj = FavoriteFashionListItem(
                    user_id=request.user.id,
                    favorite_item=slug
                )
                obj.save()
            
                return redirect(request.session['TempPage'])
            else:
                return redirect(request.session['TempPage'])
        else:
                response = redirect('Index')
                return response

# お気に入りファッションコーデ一覧 Delete
class FavoriteItemListDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            slug = self.kwargs['slug']
            Favorite_Item_List = FavoriteFashionListItem.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()

            if Favorite_Item_List.count() != 0:
                Favorite_Item_List.delete()
                return redirect(request.session['TempPage'])
            else:
                return redirect(request.session['TempPage'])
        else:
                response = redirect(request.session['TempPage'])
                return response


# お気に入りアイテム一覧
class FavoriteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            item_data = Item.objects.all()
            Favorite_Item_List = FavoriteItemList.objects.filter(user_id=request.user.id).all()
            
            paginator = Paginator(Favorite_Item_List, 20)
            p = request.GET.get('p')
            Favorite_Item_List = paginator.get_page(p)

            request.session['TempPage'] = request.build_absolute_uri()
            context={
                'item_data': item_data,
                'Favorite_Item_List': Favorite_Item_List
            }
            return render(request, 'app/store/favorite.html', context)
        else:
                response = redirect('Index')
                return response
        
# お気に入りアイテム一覧 ADD
class FavoriteItemView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            slug = self.kwargs['slug']
            Favorite_Item_List = FavoriteItemList.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()
            if Favorite_Item_List.count() == 0:
                obj = FavoriteItemList(
                    user_id=request.user.id,
                    favorite_item=slug
                )
                obj.save()
                return redirect(request.session['TempPage'])
            else:
                return redirect(request.session['TempPage'])
        else:
                response = redirect('Index')
                return response

# お気に入りアイテム一覧 DELETE
class FavoriteItemDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            slug = self.kwargs['slug']
            Favorite_Item_List = FavoriteItemList.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()
            if Favorite_Item_List.count() != 0:
                Favorite_Item_List.delete()
                # return redirect('product', slug)
                return redirect(request.session['TempPage'])
            else:
                return redirect(request.session['TempPage'])
        else:
                response = redirect(request.session['TempPage'])
                return response

def FavoriteItemAdd(request):
    slug = request.POST.get('slug')
    # number2 = int(request.POST.get('number2'))
    Favorite_Item_List = FavoriteItemList.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()
    if Favorite_Item_List.count() == 0:
        obj = FavoriteItemList(
            user_id=request.user.id,
            favorite_item=slug
        )
        obj.save()
    return JsonResponse("Success")

class FavoriteItemView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            slug = self.kwargs['slug']
            Favorite_Item_List = FavoriteItemList.objects.filter(Q(user_id=request.user.id) & Q(favorite_item=slug)).all()
            if Favorite_Item_List.count() == 0:
                obj = FavoriteItemList(
                    user_id=request.user.id,
                    favorite_item=slug
                )
                obj.save()
                return redirect('product', slug)
            else:
                return redirect('product', slug)
        else:
                response = redirect('Index')
                return response
        

class ThanksView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/store/thanks.html')
    

class FashionCustomize(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            item_data = Item.objects.all()
            return render(request, 'app/fashion/fashion.html', {
                'item_data': item_data
            })
        else:
            item_data = Item.objects.all()
            return render(request, 'app/fashion/fashion.html', {
                'item_data': item_data
            })  

class FashionCheck(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            if request.GET['FashionItemData'] != '':

                form = FashionSaveForm(request.POST or None)

                split = request.GET['FashionItemData'].split(',')
                request.session['FashionTempItem'] = split
                item_data = Item.objects.all()
                
                brand_tag = ''
                for split_value in split:
                    for search in item_data:
                        if search.slug == split_value:
                            if brand_tag.upper().find(search.brand):
                                brand_tag += search.brand + ','
                            
                            
                if brand_tag[len(brand_tag) - 1] == ',':
                    brand_tag = brand_tag[:-1]
                
                request.session['FashionTempBrandTag'] = brand_tag
                price = 0
                for item in item_data:
                    for value in split:
                        if item.slug == value:
                            price += item.price
                context={
                    'data': item_data,
                    'tests': split,
                    'price': price,
                    'form': form
                }
                return render(request, 'app/fashion/fashion_preview.html', context)
            else:
                response = redirect('fashion_customize')
                return response
            
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            # slug_list = ''
            print ("post")
            if request.session['FashionTempItem'] and request.session['FashionTempBrandTag']:
                FashionTempItem = request.session['FashionTempItem']
                form = FashionSaveForm(request.POST)
                
                if form.is_valid():
                    title = form.cleaned_data["title"]
                    clothing = form.cleaned_data["clothing"]
                    category = "カスタマイズ"
                    season = form.cleaned_data["season"]
                    brand = request.session['FashionTempBrandTag']
                    description = form.cleaned_data["description"]
                    publish = form.cleaned_data["publish"]
                    sex = form.cleaned_data["sex"]
                    color = form.cleaned_data["color"]
                    slug = ''

                    
                    if (FashionSaveList.objects.order_by("id").last()) != None:
                        slug = str(FashionSaveList.objects.order_by("id").last().id + 1)
                    else:
                        slug = '1'
                    author = request.user.id
                    
                    obj = FashionSaveList(
                    title=title, clothing=clothing, season=season, category=category,
                    brand=brand, color=color, description=description, publish=publish,
                    sex=sex, slug=slug, author=author,
                    user_id=request.user.id
                    )

                    obj.save()

                    for save_value in FashionTempItem:
                        if save_value != '':
                            item_save = FashionItemList(
                                FSL_id=slug,
                                using_item = save_value
                            )
                            item_save.save()

                    response = redirect('fashion_view', slug)
                    return response
                response = redirect('fashion_customize')
                return response


class FashionList(View):

    def get(self, request, *args, **kwargs):
        context = {}
        if request.method == 'GET':
            item_data = Item.objects.all()
            fashion_item_data = FashionSaveList.objects.filter(publish=True).all()
            fashion_list_data = FashionItemList.objects.filter().all()
            paginator = Paginator(fashion_item_data, 4)
            p = request.GET.get('p')
            fashion_item_data = paginator.get_page(p)
            
            request.session['TempPage'] = request.build_absolute_uri()
            context={
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data
            }
            return render(request, 'app/fashion/fashion_list.html', context)
        else:
                response = redirect('Index')
                return response


    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':

            item_data = Item.objects.all()
            search_data = request.POST['search']
            search_id_data = request.POST['search_id']
            sex_data = request.POST['sex']
            
            request.session['TempPage'] = request.build_absolute_uri()
            
            FashionListPublish = FashionSaveList.objects.filter(Q(publish=True)).all()
            if search_data != '':
                if search_id_data == 'title':
                    fashion_item_data = FashionListPublish.filter(Q(title__contains=search_data)).all()
                elif search_id_data == 'category':
                    fashion_item_data = FashionListPublish.filter(Q(category=search_data)).all()
                    
                elif search_id_data == 'brand':
                    fashion_item_data = FashionListPublish.filter(Q(brand__contains=search_data)).all()
                elif search_id_data == 'user':
                    fashion_item_data = FashionListPublish.filter(Q(user__user_screen_id__contains=search_data)).all()
                else:
                    fashion_item_data = FashionListPublish.filter(Q(title__contains=search_data) | Q(category=search_data) | Q(brand__contains=search_data) | Q(user__user_screen_id__contains=search_data)).all()
            else:
                return redirect('fashion_list')

            fashion_list_data = FashionItemList.objects.filter().all()
            context={
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data
            }
            return render(request, 'app/fashion/fashion_list.html', context)
        else:
                response = redirect('Index')
                return response


class FashionSave(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        context = {}
        if request.method == 'GET':
                print(request.GET)
                slug = self.kwargs['slug']
                
                item_data = Item.objects.all()
                fashion_item_data = FashionSaveList.objects.get(slug=slug)
                split = fashion_item_data.using_item.split(',')
                brand_tag = fashion_item_data.brand.split(',')
                # using_item_data = 
                user = CustomUser.objects.get(id=fashion_item_data.author)
                context={
                    'data': item_data,
                    'fashion_data': fashion_item_data,
                    'tests': split,
                    'user': user,
                    'brand' : brand_tag
                }
                return render(request, 'app/fashion/fashion_view.html', context)
        else:
                response = redirect('Index')
                return response

class FashionView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 投稿に対するいいねの数
        like_count = self.object.like_set.count()
        context['like_count'] = like_count

        if self.object.like_set.filter(user_id=self.request.user).exists():
            context['is_user_liked'] = True
        else:
            context['is_user_liked'] = False

        return context
    
    def get(self, request, *args, **kwargs):

        context = {}
        if request.method == 'GET':
            slug = self.kwargs['slug']
            item_data = Item.objects.all()
            fashion_item_data = FashionSaveList.objects.filter(Q(publish=True) & Q(slug=slug))
            if fashion_item_data.exists():
                fashion_list_data = FashionItemList.objects.filter(FSL__slug=slug).all()
                
                review_data = FashionReview.objects.filter(content_id=slug)
                paginator = Paginator(review_data, 3)
                p = request.GET.get('p')
                review_data = paginator.get_page(p)

                request.session['TempPage'] = request.build_absolute_uri()

            else:
                return redirect('Index')
        
            context={
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data,
                'article': slug,
                'review_data': review_data
            }
            return render(request, 'app/fashion/fashion_view.html', context)
        else:
                response = redirect('Index')
                return response

def like(request):
    article_pk = request.POST.get('article_pk')
    context = {
        'user_id': f'{ request.user }',
    }
    article = get_object_or_404(FashionSaveList, slug=article_pk)
    like = Like.objects.filter(target=article, user_id=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=article, user_id=request.user)
        context['method'] = 'create'

    context['like_count'] = article.like_set.count()

    return JsonResponse(context)

class FashionCustomizeEdit(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            user = request.user.id
            slug = self.kwargs['slug']

            item_data = Item.objects.all()
            fashion_item_data = FashionSaveList.objects.get(slug=slug)
            fashion_list_data = FashionItemList.objects.filter(FSL__slug=slug).all()

            brand_tag = ''
            
            for split_value in fashion_list_data:
                brand_tag += split_value.using_item + ','
            context = {
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data,
                'brand_tag': brand_tag,
            }
            return render(request, 'app/fashion/fashion_customize_edit.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            if request.session['FashionTempItem'] and request.session['FashionTempBrandTag']:
                
                user = request.user.id
                slug = self.kwargs['slug']
                FashionTempItem = request.session['FashionTempItem']

                fashion_item_data = FashionSaveList.objects.get(slug=slug)
                request.session['FashionItemID'] = fashion_item_data.id
                request.session['FashionTempBrandTag'] = fashion_item_data.brand
                
                form = FashionSaveForm(
                request.POST or None,
                initial = {
                    'title': fashion_item_data.title,
                    'clothing': fashion_item_data.clothing,
                    'season': fashion_item_data.season,
                    'sex': fashion_item_data.sex,
                    'color': fashion_item_data.color,
                    'description': fashion_item_data.description,
                    'publish': fashion_item_data.publish,
                }
            )
                
                

            if form.is_valid():
                title = form.cleaned_data["title"]
                clothing = form.cleaned_data["clothing"]
                category = "カスタマイズ"
                season = form.cleaned_data["season"]
                brand = request.session['FashionTempBrandTag']
                description = form.cleaned_data["description"]
                publish = form.cleaned_data["publish"]
                sex = form.cleaned_data["sex"]
                color = form.cleaned_data["color"]
                author = request.user.id
                
                obj = FashionSaveList(
                title=title, clothing=clothing, season=season, category=category,
                brand=brand, color=color, description=description, publish=publish,
                sex=sex, slug=slug, author=author,
                user_id=request.user.id
                )

                obj.save()

                for save_value in FashionTempItem:
                    if save_value != '':
                        item_save = FashionItemList(
                            FSL_id=slug,
                            using_item = save_value
                        )
                        item_save.save()

                response = redirect('fashion_view', slug)
                return response
            response = redirect('fashion_customize')
            return response

class FashionFieldEdit(View):
    def get(self, request, *args, **kwargs):
        
        context = {}
        if request.method == 'GET':
            user = request.user.id
            slug = self.kwargs['slug']

            fashion_item_data = FashionSaveList.objects.get(slug=slug)
            request.session['FashionItemID'] = fashion_item_data.id
            request.session['FashionTempBrandTag'] = fashion_item_data.brand
            form = FashionSaveForm(
            request.POST or None,
            initial = {
                'title': fashion_item_data.title,
                'clothing': fashion_item_data.clothing,
                'season': fashion_item_data.season,
                'sex': fashion_item_data.sex,
                'color': fashion_item_data.color,
                'description': fashion_item_data.description,
                'publish': fashion_item_data.publish,
            }
        )
            item_data = Item.objects.all()
            
            fashion_list_data = FashionItemList.objects.filter(Q(FSL__id=user) & Q(FSL__slug=slug)).all()
            context={
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data,
                'form': form
            }
            return render(request, 'app/fashion/fashion_field_edit.html', context)
        else:
                response = redirect('Index')
                return response
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = FashionSaveForm(request.POST)
            user = request.user.id
            slug = self.kwargs['slug']
            ItemID = request.session['FashionItemID']
            if form.is_valid():
                title = form.cleaned_data["title"]
                category = "カスタマイズ"
                clothing = form.cleaned_data["clothing"]
                season = form.cleaned_data["season"]
                color = form.cleaned_data["color"]
                brand = request.session['FashionTempBrandTag']
                description = form.cleaned_data["description"]
                publish = form.cleaned_data["publish"]
                sex = form.cleaned_data["sex"]
                author = user
                obj = FashionSaveList(
                id=ItemID, title=title, clothing=clothing, season=season, category=category,
                brand=brand, color=color, description=description, publish=publish,
                sex=sex, slug=slug, author=author,
                user_id=user
                )
                obj.save()
                response = redirect('fashion_view', slug)
                return response


class FashionMyList(View):
    def get(self, request, *args, **kwargs):

        context = {}
        if request.method == 'GET':
            item_data = Item.objects.all()
            fashion_item_data = FashionSaveList.objects.filter(user_id=request.user.id)
            fashion_list_data = FashionItemList.objects.filter(FSL__user__id=request.user.id).all()
            
            paginator = Paginator(fashion_item_data, 5)
            p = request.GET.get('p')
            fashion_item_data = paginator.get_page(p)
            
            context={
                'item_data': item_data,
                'fashion_item_data': fashion_item_data,
                'fashion_list_data': fashion_list_data
            }
            return render(request, 'app/fashion/fashion_mylist.html', context)
        else:
                response = redirect('Index')
                return response
        

class FashionCustomizeDelete(View):
    def post(self, request, *args, **kwargs):
        FashionData = FashionSaveList.objects.get(Q(user_id=request.user.id) | Q(slug=self.kwargs['slug']))
        FashionData.delete()
        return redirect('fashion_my_list')

def like_for_post(request):
    item_pk = request.POST.get('item_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    post = get_object_or_404(Item, slug=item_pk)
    like = LikeForPost.objects.filter(target=post, user=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=post, user=request.user)
        context['method'] = 'create'

    context['like_for_post_count'] = post.likeforpost_set.count()

    return JsonResponse(context)