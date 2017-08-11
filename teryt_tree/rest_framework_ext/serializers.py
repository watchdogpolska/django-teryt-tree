from rest_framework import serializers

from teryt_tree.models import JednostkaAdministracyjna
from teryt_tree.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'pk')


class JednostkaAdministracyjnaSerializer(serializers.HyperlinkedModelSerializer):
    teryt = serializers.CharField(source='pk', read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    category = CategorySerializer()
    children = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='jednostkaadministracyjna-detail'
    )

    class Meta:
        model = JednostkaAdministracyjna
        fields = ('url',
                  'parent',
                  'teryt',
                  'children',
                  'category',
                  'name',
                  'updated_on',
                  'active',
                  'level',)

# class SIMCSerializer(serializers.HyperlinkedModelSerializer):
#     simc = SIMCSerializer(many=True)
#     sym_pod = SIMCSerializer()
#     terc = JednostkaAdministracyjnaSerializer()

#     class Meta:
#         model = SIMC
#         fields = ['id', 'sym_pod', 'terc', 'name', 'updated_on']
