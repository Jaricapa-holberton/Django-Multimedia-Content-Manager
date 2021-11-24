"""Main users views."""

# Django

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, FormView, UpdateView, DetailView, DeleteView
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Models
from pedagogy_manager.contents.models.contents import Content, Blog, Route, RouteModule, Module
from pedagogy_manager.utils.preview import blog_preview_edit, blog_preview_see, content_preview_edit, content_preview_see
from .forms import Contentform, BlogForm, RouteFormList, ModuleForm, RouteForm

User = get_user_model()


class RouteCreate(LoginRequiredMixin, FormView):
    """Allows you to create a route"""
    model = Route
    template_name = 'contents/route_create.html'
    form_class = RouteForm
    success_url = reverse_lazy('users:index')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)


class RouteEdit(LoginRequiredMixin, UpdateView):
    """Edit a Route object"""
    form_class = RouteForm
    model = Route
    template_name = 'contents/route_edit.html'
    success_url = reverse_lazy('users:route-list')
    success_message = _("Information successfully updated")

    def dispatch(self, request, *args, **kwargs):
        self.route_id = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)


class RouteList(LoginRequiredMixin, ListView):
    """
    List all the Routes object
    """
    model = Route
    template_name = 'contents/route_list.html'


class RouteRemove(LoginRequiredMixin, DeleteView):
    """
    Delete a specific Route
    """
    model = Route
    form_class = RouteForm
    template_name = 'contents/route_remove.html'
    success_url = reverse_lazy('users:route-list')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)

    def __str__(self):
        return self.title


class ModuleCreate(LoginRequiredMixin, FormView):
    """Allows you to create a module"""
    template_name = 'contents/module_create.html'
    form_class = ModuleForm
    success_url = reverse_lazy('users:index')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)


class ListModule(LoginRequiredMixin, FormView):
    """List all the modules object"""
    template_name = 'contents/index.html'
    form_class = RouteFormList

    def dispatch(self, request, *args, **kwargs):
        self.route = None
        self.route_id = request.GET.get('routes')
        if self.route_id:
            self.route = get_object_or_404(Route, pk=self.route_id)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.route:
            context['route'] = self.route
            context['route_modules'] = self.route.route_modules.all()
        return context

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        initial = super().get_initial()
        initial['routes'] = self.route_id
        return initial


class ModuleEdit(LoginRequiredMixin, UpdateView):
    """
    Allows edit a Module
    """
    form_class = ModuleForm
    model = Module
    template_name = 'contents/module_edit.html'
    success_url = reverse_lazy('users:module-list')
    success_message = _("Information successfully updated")


class ModuleList(LoginRequiredMixin, ListView):
    """
    List all the Modules
    """
    model = Module
    template_name = 'contents/module_list.html'


class ModuleRemove(LoginRequiredMixin, DeleteView):
    """
    Delete a specific Module
    """
    model = Module
    form_class = ModuleForm
    template_name = 'contents/module_remove.html'
    success_url = reverse_lazy('users:module-list')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)

    def __str__(self):
        return self.title


class ContentCreate(LoginRequiredMixin, FormView):
    """
    Allows you to create a Content
    """
    model = Content
    template_name = 'contents/content_create.html'
    form_class = Contentform
    success_url = reverse_lazy('users:content-list')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)


class ContentList(LoginRequiredMixin, ListView):
    """
    Creates a Content object for render a template
    that list all the posts on the Content model
    """
    model = Content
    template_name = 'contents/content_list.html'


class ContentEdit(LoginRequiredMixin, UpdateView):
    """
    Edit a Content object
    """
    form_class = Contentform
    model = Content
    template_name = 'contents/content_edit.html'
    success_url = reverse_lazy('users:content-list')
    success_message = _("Information successfully updated")

    def dispatch(self, request, *args, **kwargs):
        self.content_id = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = int(self.content_id)
        query_obj = Content.objects.filter(id=content).get()
        content_preview = content_preview_edit(query_obj)
        content_preview_safe = mark_safe(content_preview)
        context = super().get_context_data(**kwargs)
        context['content'] = content
        context['url'] = content_preview_safe
        return context


class ContentRemove(LoginRequiredMixin, DeleteView):
    """
    Delete a specific content
    """
    model = Content
    form_class = Contentform
    template_name = 'contents/content_remove.html'
    success_url = reverse_lazy('users:content-list')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)

    def __str__(self):
        return self.title


class ContentPreview(LoginRequiredMixin, DetailView):
    """
    Creates a Blog object for render a template that render a preview of the post
    """

    model = Content
    template_name = 'contents/hacku_content_preview.html'

    def get_context_data(self, **kwargs):
        """Add blog to context."""
        context = super().get_context_data(**kwargs)
        context['blog'] = self.object
        return context


class ContentsModuleDetailView(LoginRequiredMixin, DetailView, FormView):
    """Allows to display the contents of a module"""
    template_name = 'contents/content.html'
    queryset = RouteModule.objects.all()
    context_object_name = "route"
    form_class = RouteFormList

    def dispatch(self, request, *args, **kwargs):
        self.route = None
        self.route_id = request.GET.get('routes')
        if self.route_id:
            self.route = get_object_or_404(Route, pk=self.route_id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.route:
            return HttpResponseRedirect(reverse_lazy('users:index') + f'?routes={self.route.id}')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        route_module = self.get_object()
        context = super().get_context_data(**kwargs)
        context['route'] = route_module.route
        context['route_modules'] = route_module.route.route_modules.all()
        context['contents'] = route_module.module.content_modules.all()
        return context


class ContentDetail(LoginRequiredMixin, DetailView):
    """
    Creates a Blog object for render a template that display a specific post
    """
    model = Content
    template_name = 'contents/content_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.content_id = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = int(self.content_id)
        query_obj = Content.objects.filter(id=content).get()
        content_preview = content_preview_see(query_obj)
        content_preview_safe = mark_safe(content_preview)
        context = super().get_context_data(**kwargs)
        context['content'] = content
        context['url'] = content_preview_safe
        return context


class ListBlog(LoginRequiredMixin, ListView):
    """
    Creates a Blog object for render a template that list all the posts on the Blog model
    """
    model = Blog
    template_name = 'contents/blog_list.html'


class DetailBlog(LoginRequiredMixin, DetailView):
    """
    Display a specific post
    """
    model = Blog
    template_name = 'contents/blog_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.blog_id = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        blog = int(self.blog_id)
        query_obj = Blog.objects.filter(id=blog).get()
        blog_preview = blog_preview_see(query_obj)
        blog_preview_safe = mark_safe(blog_preview)
        context = super().get_context_data(**kwargs)
        context['blog'] = blog
        context['url'] = blog_preview_safe
        return context


class CreateBlog(LoginRequiredMixin, FormView):
    """
    Creates a Blog object for render a template that allows create a post
    """
    model = Blog
    form_class = BlogForm
    template_name = 'contents/blog_create.html'
    success_url = reverse_lazy('users:list-blog')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)

    def __str__(self):
        return self.title


class DeleteBlog(LoginRequiredMixin, DeleteView):
    """
    Delete a Blog object
    """
    model = Blog
    form_class = BlogForm
    template_name = 'contents/blog_remove.html'
    success_url = reverse_lazy('users:list-blog')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return super().form_valid(form)

    def __str__(self):
        return self.title


class EditBlog(LoginRequiredMixin, UpdateView):
    """
    Edit a Blog object
    """
    form_class = BlogForm
    model = Blog
    template_name = 'contents/blog_edit.html'
    success_url = reverse_lazy('users:list-blog')
    success_message = _("Information successfully updated")

    def dispatch(self, request, *args, **kwargs):
        self.blog_id = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        blog = int(self.blog_id)
        query_obj = Blog.objects.filter(id=blog).get()
        blog_preview = blog_preview_edit(query_obj)
        blog_preview_safe = mark_safe(blog_preview)
        context = super().get_context_data(**kwargs)
        context['blog'] = blog
        context['url'] = blog_preview_safe
        return context


class BlogPreview(LoginRequiredMixin, DetailView):
    """
    Blog object for render a template that render a preview of the post
    """

    model = Blog
    template_name = 'contents/hacku_preview.html'

    def get_context_data(self, **kwargs):
        """Add blog to context."""
        context = super().get_context_data(**kwargs)
        context['blog'] = self.object
        return context
