from blogs.models import Blog, Category
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'features_image', 'short_description', 'blog_body', 'status', 'is_featured')