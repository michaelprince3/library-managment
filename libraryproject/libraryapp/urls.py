from django.urls import include, path
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('library/form', library_form, name='library_form')
]