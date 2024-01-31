
from django.urls import path
from .views import recipe_list,recipe_detail,category_list,category_detail

app_name = 'recipe_app'
urlpatterns = [
    path('recipe/',recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('category/',category_list, name='category_list'),
    path('category/<slug:category>/', category_detail, name='category_detail')
]










# from recipe_app import views
# from django.urls import path
# urlpatterns = [
#     path("",views.index,name='recipe_app')
# ]