from django.urls import path
from .views import Pagelistview, PageDetailView, PageCreateview, PageUpdateView, PageDeleteView

pages_patterns = ([
    path('', Pagelistview.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/',PageCreateview.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
],'pages')