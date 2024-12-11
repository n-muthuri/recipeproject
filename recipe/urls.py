from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='my_index'),
    path('contact/', views.contact, name='my_contact'),
    path('about-us/', views.about, name='my_about'),
    path('blog/', views.blog_list, name='my_blog'),
    path('add-recipe/', views.add_recipe, name='my_add_recipe'),
    path('login/', views.login_view, name='my_login'),  # Login page
    path('register/', views.register, name='my_register'),  # Register page


path('create/', views.RecipeCreateView.as_view(), name='my_create_recipe'),
       path('<int:pk>/update/', views.RecipeUpdateView.as_view(), name='my_update_recipe'),
       path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='my_delete_recipe'),
   ]




