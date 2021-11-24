from pedagogy_manager.users import views as user_views
from django.urls import path


app_name = "users"
urlpatterns = [
    # URL for the base template - at the moment just for the Blog management

    path(
        route='',
        view=user_views.ListModule.as_view(),
        name='index'
    ),
    path(
        route='create-module/',
        view=user_views.ModuleCreate.as_view(),
        name='create-module',
    ),
    path(
        route='edit-module/<str:pk>/',
        view=user_views.ModuleEdit.as_view(),
        name='edit-module',
    ),
    path(
        route='remove-module/<str:pk>',
        view=user_views.ModuleRemove.as_view(),
        name='remove-module',
    ),
    path(
        route='module-list/',
        view=user_views.ModuleList.as_view(),
        name='module-list',
    ),
    path(
        route='create-route/',
        view=user_views.RouteCreate.as_view(),
        name='create-route',
    ),
    path(
        route='edit-route/<str:pk>/',
        view=user_views.RouteEdit.as_view(),
        name='edit-route',
    ),
    path(
        route='remove-route/<str:pk>',
        view=user_views.RouteRemove.as_view(),
        name='remove-route',
    ),
    path(
        route='route-list/',
        view=user_views.RouteList.as_view(),
        name='route-list',
    ),
    path(
        route='content-module/<str:pk>',
        view=user_views.ContentsModuleDetailView.as_view(),
        name='content-module-detail',
    ),
    # URL for blog list - list all post on the model
    path(
        route='blog/',
        view=user_views.ListBlog.as_view(),
        name='list-blog'
    ),
    # URL for blog detail - display a single post and their info
    path(
        route='seepost/<str:pk>',
        view=user_views.DetailBlog.as_view(),
        name='post-detail'
    ),
    # URL for create post - create a post
    path(
        route='addpost/',
        view=user_views.CreateBlog.as_view(),
        name='add-post'
    ),
    # URL for delete post - delete a post
    path(
        route='removepost/<str:pk>/',
        view=user_views.DeleteBlog.as_view(),
        name='delete-post'
    ),
    path(
        route='editpost/<str:pk>/',
        view=user_views.EditBlog.as_view(),
        name='edit-post'
    ),
    path(
        route='preview/<str:pk>/',
        view=user_views.BlogPreview.as_view(),
        name='post-preview'
    ),
    path(
        route='content-create/',
        view=user_views.ContentCreate.as_view(),
        name='content-create'
    ),
    path(
        route='content-list/',
        view=user_views.ContentList.as_view(),
        name='content-list'
    ),
    path(
        route='content-edit/<str:pk>/',
        view=user_views.ContentEdit.as_view(),
        name='content-edit'
    ),
    path(
        route='content-remove/<str:pk>',
        view=user_views.ContentRemove.as_view(),
        name='content-remove'
    ),
    path(
        route='content_preview/<str:pk>/',
        view=user_views.ContentPreview.as_view(),
        name='content-preview'
    ),
    path(
        route='seecontent/<str:pk>',
        view=user_views.ContentDetail.as_view(),
        name='content-detail'
    ),
]
