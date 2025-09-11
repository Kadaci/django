from django import forms
from posts.models import Post

class PostForm(forms.Form):
    image = forms.ImageField(required=True)
    title = forms.CharField(max_length=200, min_length=5,  required=True)
    content = forms.CharField(max_length=1000, min_length=10, required=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content can't be the same")
        return cleaned_data


# class PostForm2(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["image", "title", "content"]

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("Title cannot be python")
        return title