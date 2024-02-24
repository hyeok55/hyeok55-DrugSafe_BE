# serializers.py
from rest_framework import serializers
from .models import *

# 메인페이지 내의 의도치 않은 복용 사례
class UnintendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnintendedDrugUsage
        fields = ['usage_id','usage_title','usage_ctnt','usage_image']  # 혹은 필요한 필드를 지정합니다.

class UnintendDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnintendedDrugUsage
        fields = '__all__'  # 혹은 필요한 필드를 지정합니다.


# 카테고리별 약물 페이지
class DrugCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['drug_id','drug_nm','medical_use','title_image','drug_type']  # 혹은 필요한 필å드를 지정합니다.


# 약물 상세페이지
class DrugAdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugAdr
        fields = ['adr_nm']  # 혹은 필요한 필드를 지정합니다.

class DrugFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugFeature
        fields = ['drug_feature']  # 혹은 필요한 필드를 지정합니다.  


class DrugImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugImage
        fields = ['image']  # 혹은 필요한 필드를 지정합니다.     


class DrugSerializer(serializers.ModelSerializer):

    images = DrugImageSerializer(source='drugimage_set', many=True)
    features = DrugFeatureSerializer(source='drugfeature_set', many=True)
    adrs = DrugAdrSerializer(source='drugadr_set', many=True)

    class Meta:
        model = Drug
        fields = ['drug_id', 'drug_nm', 'medical_use', 'drug_type', 'images', 'features', 'adrs']

