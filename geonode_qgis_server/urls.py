# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^QGISServerLayer/~create/$",
        view=views.QGISServerLayerCreateView.as_view(),
        name='QGISServerLayer_create',
    ),
    url(
        regex="^QGISServerLayer/(?P<pk>\d+)/~delete/$",
        view=views.QGISServerLayerDeleteView.as_view(),
        name='QGISServerLayer_delete',
    ),
    url(
        regex="^QGISServerLayer/(?P<pk>\d+)/$",
        view=views.QGISServerLayerDetailView.as_view(),
        name='QGISServerLayer_detail',
    ),
    url(
        regex="^QGISServerLayer/(?P<pk>\d+)/~update/$",
        view=views.QGISServerLayerUpdateView.as_view(),
        name='QGISServerLayer_update',
    ),
    url(
        regex="^QGISServerLayer/$",
        view=views.QGISServerLayerListView.as_view(),
        name='QGISServerLayer_list',
    ),
	]
