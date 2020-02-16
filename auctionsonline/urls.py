from django.contrib import admin
from django.urls import path, include
from website import views as web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_views.index, name='index'),
    path('login/', web_views.login_page, name='login_view'),
    path('logout/', web_views.logout_page, name='logout_view'),
    path('register/', web_views.register_page, name='register_page'),
    path('register/new_user/', web_views.register, name='register'),
    path('category/<str:category>/', web_views.filter_auctions, name='filter_auctions'),
    path('watchlist/<int:auction_id>/', web_views.watchlist, name='watchlist'),
    path('balance/', web_views.balance, name='balance'),
    path('balance/topup/', web_views.topup, name='topup'),
    path('watchlist/', web_views.watchlist_page, name='watchlist'),
    path('bid/<int:auction_id>/', web_views.bid_page, name='bid_page'),
    path('bid/<int:auction_id>/comment/', web_views.comment, name='comment'),
    path('bid/<int:auction_id>/raise_bid/', web_views.raise_bid, name='raise_bid'),
]