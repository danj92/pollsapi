from django.urls import path
from .apiviews import PollListViewset#, PollDetailViewset
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'polls', PollListViewset, base_name='polls_list')
# router.register(r'polls', PollDetailViewset, base_name='polls_detail')

# urlpatterns = [
#     path("polls/", PollList.as_view(), name="polls_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
# ]
