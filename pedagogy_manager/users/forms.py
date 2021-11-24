from pedagogy_manager.contents.models.contents import Blog, Content
from pedagogy_manager.contents.models.contents import RouteModule, ContentModule
from pedagogy_manager.contents.models.contents import Route, Module, Company, Area
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class RouteFormList(forms.Form):
    routes = forms.ModelChoiceField(
        queryset=Route.objects.all(),
        widget=forms.Select(attrs={'class': "form-control"}
                            )
    )


class BlogForm(forms.ModelForm):
    """
    Blog model form
    """

    content = forms.CharField(widget=forms.Textarea(attrs={'name': 'content', 'id': 'editor'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'name': 'title', 'id': 'title', 'type': 'text', 'class': 'form-control'}))
    slug_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    owner = forms.CharField(widget=forms.TextInput(attrs={'name': 'owner', 'id': 'exampleCity', 'type': 'text', 'class': 'form-control'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'name': 'url', 'id': 'url', 'type': 'text', 'class': 'form-control'}))
    publication_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'data-toggle': 'datepicker-button'}))
    header_image = forms.ImageField(required=False)

    class Meta:
        """
        Form settings.
        """
        model = Blog
        fields = [
            'content',
            'title',
            'slug_name',
            'owner',
            'url',
            'publication_date',
            'header_image'
            ]
        labels = {
            'Content': 'Body text',
            'title': 'Post title',
            'slug_name': 'Post slug name',
            'owner': 'Author name',
            'url': 'URL',
            'publication_date': 'Publication date',
            'header_image': 'Upload a header image'
        }


class Contentform(forms.ModelForm):
    """
    Content model form
    """

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    html_content = forms.CharField(required=False, widget=forms.Textarea(attrs={'name': 'html_content', 'id': 'html_content'}))
    audio_file = forms.FileField(required=False, widget=forms.ClearableFileInput())
    blog = forms.ModelChoiceField(required=False, queryset=Blog.objects.all(), widget=forms.Select())
    subtitled = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'name': 'subtitled'}))
    skip = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'name': 'skip'}))
    copy = forms.CharField(required=False, widget=forms.Textarea(attrs={'name': 'copy', 'id': 'copy'}))
    footer = forms.CharField(required=False, widget=forms.Textarea(attrs={'name': 'footer', 'id': 'footer'}))
    creation_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'data-toggle': 'datepicker-button'}))

    class Meta:

        model = Content

        fields = [
            'title',
            'slug_name',
            'url',
            'html_content',
            'audio_file',
            'blog',
            'subtitled',
            'skip',
            'copy',
            'footer',
            'creation_date'
        ]
        labels = {
            'title': 'Title:',
            'slug_name': 'Slug name:',
            'url': 'Url:',
            'html_content': 'HTML Content:',
            'audio_file': 'Audio:',
            'blog': 'Blog:',
            'subtitled': 'Subtitled:',
            'skip': 'Skip url validation:',
            'copy': 'Copy Content:',
            'footer': 'Footer Content:',
            'creation_date': 'Creation date content:',
        }


class RouteForm(forms.ModelForm):
    """
    Route model form
    """

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug_name = forms.SlugField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    route_issuer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    corporative = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'name': 'content', 'id': 'editor'}))
    area = forms.ModelChoiceField(required=False, queryset=Area.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
    company = forms.ModelChoiceField(required=False, queryset=Company.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
    module = forms.ModelChoiceField(required=False, queryset=Module.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
    position = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:

        model = Route

        fields = [
            'name',
            'slug_name',
            'route_issuer',
            'corporative',
            'area',
            'company',
            'module',
            'position'
        ]
        labels = {
            'name': 'Name:',
            'slug_name': 'Slug_name:',
            'route_issuer': 'Route Issuer:',
            'corporative': 'Corporative:',
            'area': 'Area:',
            'company': 'Company:',
            'module': 'Module:',
            'position': 'Position:'
        }

    def save(self):
        data = self.cleaned_data
        route = Route.objects.create(
            name=data['name'],
            slug_name=data['slug_name'],
            route_issuer=data['route_issuer'],
            corporative=data['corporative'],
            area=data['area'],
            company=data['company']
        )
        moduleData = RouteModule(route=route, module=data['module'], position=data['position'])
        moduleData.save()


class ModuleForm(forms.ModelForm):
    """
    Module model form
    """

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug_name = forms.SlugField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    content = forms.ModelChoiceField(required=False, queryset=Content.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
    position = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Module
        fields = [
            'name',
            'slug_name',
            'description',
            'content',
            'position'
        ]
        labels = {
            'name': 'Name:',
            'slug_name': 'Slug name:',
            'description': 'Description:',
            'content': 'Content:',
            'position': 'Position:'
        }

    def save(self):
        data = self.cleaned_data
        module = Module.objects.create(
            name=data['name'],
            slug_name=data['slug_name'],
            description=data['description']
        )
        contentData = ContentModule(content=data['content'], module=module, position=data['position'])
        contentData.save()
