# Core Django Imports
from django.conf.urls import include, url

# Import from Project Apps
from views import Pages
urlpatterns = [
    url(r'^index/', Pages.as_view()),
]


from views import Tasks
urlpatterns += [
	url(r'^tasks/$', Tasks.as_view()),
]


# from views import TaskSpecific
# urlpatterns += [
# 	url(r'^tasks/<>\d+/', TaskSpecific.as_view())
# ]
