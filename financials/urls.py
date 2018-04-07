
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Financial : Financial_list

    path('', views.FinancialListView.as_view(), name='Financial_list'),

    # Path to create new Financial : Financial_new

    path('new/', views.FinancialCreateView.as_view(), name='Financial_new'),

    # Path to edit Financial : edit_list

    path('<int:pk>/edit', views.FinancialUpdateView.as_view(), name='Financial_edit'),

    # Path to delete Financial : Financial_delete

    path('<int:pk>/delete', views.FinancialDeleteView.as_view(), name='Financial_delete'),

    # Path to detail view of Financial : Financial_details

    path('<int:pk>', views.FinancialDetailView.as_view(), name='Financial_details')
]
