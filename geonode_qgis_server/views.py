# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	QGISServerLayer,
)


class QGISServerLayerCreateView(CreateView):

    model = QGISServerLayer


class QGISServerLayerDeleteView(DeleteView):

    model = QGISServerLayer


class QGISServerLayerDetailView(DetailView):

    model = QGISServerLayer


class QGISServerLayerUpdateView(UpdateView):

    model = QGISServerLayer


class QGISServerLayerListView(ListView):

    model = QGISServerLayer

