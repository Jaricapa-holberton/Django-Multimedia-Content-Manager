"""Contents Models."""

from slugify import slugify

# Django
from django.db import models
from django.db.models.expressions import Random
from admin_async_upload.models import AsyncFileField

# Utils
from pedagogy_manager.utils.models import CreatedUpdateBaseModel
from ckeditor.fields import RichTextField


class Content(CreatedUpdateBaseModel):
    """Content type format."""
    title = models.TextField()
    slug_name = models.SlugField(unique=True, max_length=40)
    url = models.URLField(
        'Url Field',
        max_length=500,
        null=True,
        blank=True
    )

    html_content = RichTextField()

    audio_file = AsyncFileField(upload_to='contents/audios',
                                null=True, blank=True)

    blog = models.ForeignKey(
        'contents.Blog',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contents'
    )

    subtitled = models.BooleanField(
        'Subtitled',
        default=False,
        help_text='Set to true when content is subtitled.'
    )

    skip = models.BooleanField(
        'Skip url validation',
        default=False
    )

    copy = RichTextField()

    footer = RichTextField()

    creation_date = models.DateField(
        'Creation date content',
        null=True,
        blank=True
    )

    def __str__(self):
        """Return content title."""
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.title, separator="-")
        return super().save(*args, **kwargs)


class ContentModule(CreatedUpdateBaseModel):
    """Content Module."""
    content = models.ForeignKey(
        to='contents.Content',
        null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='content_modules',
    )
    module = models.ForeignKey(
        to='contents.Module',
        null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='content_modules',
    )
    position = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.content} at position: {self.position}'

    class Meta:
        # Restrict content ordering.
        unique_together = ('module', 'position')


class Blog (CreatedUpdateBaseModel):
    """
    Creates the Blog's model data
    """
    content = RichTextField()
    title = models.CharField(max_length=500, blank=False, null=False)
    slug_name = models.SlugField(unique=True, max_length=100, blank=False, null=False)
    owner = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(max_length=500)
    publication_date = models.DateField(
        auto_now_add=False,
        auto_now=False, null=True,
        blank=True)
    header_image = models.ImageField(
        upload_to='blog/headers/',
        null=True, blank=True)

    def __str__(self):
        return f'Blog {self.title}'

    def random_image(self):
        return Random.choice(range(1, 5))

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.title, separator="-")
        return super().save(*args, **kwargs)


class Area(CreatedUpdateBaseModel):
    """Content Area for the route."""

    name = models.CharField(max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)
    is_displayable = models.BooleanField(
        'Displayable', default=True,
        help_text='Set to false when you need to not see in forms.'
    )

    def __str__(self):
        """Return content area name."""
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name, separator="-")
        return super().save(*args, **kwargs)


class Route(CreatedUpdateBaseModel):
    name = models.CharField(max_length=150)
    slug_name = models.SlugField(
        unique=True,
        max_length=40)
    route_issuer = models.CharField(max_length=150)
    corporative = models.BooleanField(
        default=False,
        help_text='Set to true when the route is corporative.')
    area = models.ForeignKey(
        to='contents.Area',
        null=False, blank=False,
        on_delete=models.CASCADE,
        help_text='Area for route.',
        related_name='routes'
    )
    company = models.ForeignKey(
        to='contents.Company',
        null=True, blank=True,
        on_delete=models.CASCADE,
        help_text='Company for route.',
        related_name='routes'
    )

    def __str__(self):
        """Return content title."""
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name, separator="-")
        return super().save(*args, **kwargs)


class Company(CreatedUpdateBaseModel):
    """Company content model.
    Companie models holds all information about corporative.
    """
    name = models.CharField('Company name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name, separator="-")
        return super().save(*args, **kwargs)


class RouteModule(CreatedUpdateBaseModel):
    route = models.ForeignKey(
        to='Route', null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='route_modules'
    )
    module = models.ForeignKey(
        to='Module',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='route_modules'
    )
    position = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.route.name)

    class Meta:
        # Restrict content ordering.
        unique_together = ('route', 'position')


class Module(CreatedUpdateBaseModel):
    name = models.CharField(max_length=150)
    slug_name = models.SlugField(unique=True, max_length=40)
    description = models.TextField()

    def __str__(self):
        """Return content title."""
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name, separator="-")
        return super().save(*args, **kwargs)
