
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet,NoteViewSet


# note_detail = NoteViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


# note_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user_view')
router.register(r'notes', NoteViewSet,basename='note_view')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]