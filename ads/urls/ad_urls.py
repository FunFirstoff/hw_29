from django.urls import path

from ads.views import AdsDetailView, AdsUploadView, AdListView, AdsCreateView

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>/', AdsDetailView.as_view()),
    path('create/', AdsCreateView.as_view()),
    path('<int:pk>/upload_image/', AdsUploadView.as_view()),
]
