from django.conf.urls import url
from django.contrib import admin

from core.views import autocomplete_view, student_detail, HomePageView

urlpatterns = [
    # Examples:
    # url(r'^$', 'essearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^autocomplete/', autocomplete_view, name='autocomplete-view'),
    url(r'^student/', student_detail, name='student-detail'),
    url(r'^$/', HomePageView.as_view(), name='index-view'),
]
