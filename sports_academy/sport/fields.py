from rest_framework.serializers import RelatedField


class SportBaseField(RelatedField):
	def to_representation(self, value):
		from .serializers import SportSerializer
		return SportSerializer(value, context=self.context).data


class SportDetailBaseField(RelatedField):
	def to_representation(self, value):
		from .serializers import SportDetailSerializer
		return SportDetailSerializer(value, context=self.context).data
