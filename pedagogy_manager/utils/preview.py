from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
"""
Extra function used for display the post preview
"""


def blog_preview_edit(object):
    """
    Retrives the pk of a post and return
    to the template that pk for render
    """
    if object:
        pk_send = str(object.pk)
        url = reverse_lazy('users:post-preview', kwargs={'pk': pk_send})
        return mark_safe(f'<iframe height="667" width="375"  frameborder="0" src="{url}"></iframe>')


def blog_preview_see(object):
    """
    Retrives the pk of a post and return
    to the template that pk for render
    """
    if object:
        pk_send = str(object.pk)
        url = reverse_lazy('users:post-preview', kwargs={'pk': pk_send})
        return mark_safe(f'<iframe frameborder="0" style="height:1800px;width:100%;border:none;overflow: hidden;" src="{url}"></iframe>')


def content_preview_edit(object):
    """
    Retrives the pk of a post and return
    to the template that pk for render
    """
    if object:
        pk_send = str(object.pk)
        url = reverse_lazy('users:content-preview', kwargs={'pk': pk_send})
        return mark_safe(f'<iframe height="667" width="375"  frameborder="0" src="{url}"></iframe>')


def content_preview_see(object):
    """
    Retrives the pk of a post and return
    to the template that pk for render
    """
    if object:
        pk_send = str(object.pk)
        url = reverse_lazy('users:content-preview', kwargs={'pk': pk_send})
        return mark_safe(f'<iframe frameborder="0" style="height:1800px;width:100%;border:none;overflow: hidden;" src="{url}"></iframe>')
