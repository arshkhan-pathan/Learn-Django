from django.urls import path
from . import views



urlpatterns=[

    path('tasks/',views.getTasks,name='product-list'),
    path('tasks/<int:pk>/',views.TaskDetailAPIVIEW.as_view(),name='product-detail'),   #generics api
    path('tasks/create/',views.TaskCreateAPIVIEW.as_view()),
    path('tasks/list/',views.TaskProductListAPIVIEW.as_view()),
    # path('tasks/listcreate/',views.TaskCreateListAPIVIEW.as_view()),
    # path('tasks/alt/',views.product_alt_view),
    # path('tasks/alt/<int:pk>',views.product_alt_view),
    path('tasks/<int:pk>/update/',views.TaskUpdateAPIVIEW.as_view(),name="product-edit"),
    # path('tasks/<int:pk>/delete/',views.TaskDeleteAPIVIEW.as_view()),
    # path('tasks/mixins/',views.TaskMixinView.as_view()),
    # path('tasks/mixins/<int:pk>/',views.TaskMixinView.as_view()),
   




]