from rest_framework import serializers

from .models import Blogs, Category,Rating

class BlogsSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Blogs
        fields = ['id', 'title', 'body', 'author', 'average_rating', 'category', 'created_at']
        read_only_fields = ['author', 'average_rating']

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            return sum(rating.rating for rating in ratings) / ratings.count()
        return None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [ 'id','blog', 'rating', 'user']
    
    def save(self):
        blog = self.validated_data['blog']
        rating = self.validated_data['rating']
        user = self.validated_data['user']
        print("rating->>", rating)
        if Rating.objects.filter(user=user, blog=blog).exists():
            raise serializers.ValidationError("You have already rated this blog.")
        rating_obj = Rating(blog=blog, rating=rating, user=user)
        rating_obj.save()
        print("ratobj",rating_obj)
        return rating_obj
    