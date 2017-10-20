from rest_framework import serializers
from .models import URL




# class ProjectDetailSerializer(serializers.ModelSerializer):
# 	comments = CommentRetrieveSerializer(many=True,read_only=True)
# 	likes_count = serializers.SerializerMethodField()
# 	is_liked_by_user = serializers.SerializerMethodField()
# 	rating_by_user = serializers.SerializerMethodField()
# 	area = AreaSerializer()
# 	ward = WardSerializer()
# 	class Meta:
# 		model = Project
# 		fields = '__all__'

# 	def get_likes_count(self, obj):
# 		return len(obj.all_liked_users())

# 	def get_is_liked_by_user(self,obj):
# 		user = self.context['request'].user
# 		return obj.is_liked_by_user(user=user)

# 	def get_rating_by_user(self,obj):
# 		user = self.context['request'].user
# 		if user.is_authenticated:
# 			if user.is_er():
# 				return obj.average_rating
# 			else:
# 				return obj.get_rating_by_user(user)
# 		return 0

class URLCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = URL
		fields = ['url']

