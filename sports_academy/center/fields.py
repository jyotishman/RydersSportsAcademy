from rest_framework.serializers import RelatedField


class CenterBaseField(RelatedField):
	def to_representation(self, value):
		from .serializers import CenterSerializer
		return CenterSerializer(value, context=self.context).data


class CenterDetailBaseField(RelatedField):
	def to_representation(self, value):
		from .serializers import CenterDetailSerializer
		return CenterDetailSerializer(value, context=self.context).data
