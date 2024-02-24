from django.urls import path

from safeguardian import views

urlpatterns = [
    path('', views.UnintendListView.as_view()), # 메인 페이지
    # path('death_rate', views.index),
    # path('ai_predict', views.index),
    path('drug/<int:ctgry_id>', views.DrugCatetgoryListView.as_view()), # 카테고리별
    path('drug_type/<int:drug_id>',views.DrugDetailRetrieveView.as_view()), # 카테고리 페이지에서 상세 약물 페이지 요청
    path('search/', views.DrugSearchAPIView.as_view()),  # 마약 검색
    path('unintention/<int:usage_id>',views.UnintendDetailRetrieveView.as_view()), # 메인 페이지에서 의도치 않은 약물 사례 페이지로 전달

]

