from django import forms
from posts.models import Post
from posts.models import Category

class PostForm(forms.Form):
    image = forms.ImageField(required=True)
    title = forms.Field(max_length=200, min_length=5,  required=True)
    content = forms.CharField(max_length=1000, min_length=10, required=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content can't be the same")
        return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "content"]

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("Title cannot be python")
        return title
    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, min_length=1, required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    orderings = (
        ("created_at", 
         "Date of create"),
        ("title", 
         "Name"),
        ("rate", 
         "of rating"),
        ("-created_at", 
         "of date create in down"),
        ("-title", 
         "Of name in down"), 
        ("-rate", 
         "of rate in down"),
        (
            None,
            "---",
        )
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)