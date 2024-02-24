from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from .models import *
from .serializers import *

# 메인 페이지 의도치 않은 복용사례 전달
class UnintendListView(generics.ListAPIView):
    queryset = UnintendedDrugUsage.objects.all()
    serializer_class = UnintendSerializer

# 의도치 않은 사례 상세 페이지
class UnintendDetailRetrieveView(generics.RetrieveAPIView):
    serializer_class = UnintendDetailSerializer
    queryset = UnintendedDrugUsage.objects.all()  # 모든 항목을 가져올 필요 없음
    lookup_field = 'usage_id'

# 약물 카테고리
class DrugCatetgoryListView(generics.ListAPIView):
    serializer_class = DrugCategorySerializer
    lookup_field = 'ctgry_id'

    def get_queryset(self):
        ctgry_id = self.kwargs.get('ctgry_id')
        return Drug.objects.filter(ctgry_id=ctgry_id)

# 약물 상세
class DrugDetailRetrieveView(generics.RetrieveAPIView):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    lookup_field = 'drug_id'

# 검색창
class DrugSearchAPIView(generics.ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['drug_nm']