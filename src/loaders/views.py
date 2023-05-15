from typing import Any, Dict
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from passports.forms import PassportForm
from loaders.models import Loader, PayMethod, PayMethodList, Specialization, Status
from loaders.forms import CreateLoaderForm, CreatePayMethodForm, CreatePayMethodList, CreateSpecializationForm, CreateStatusForm
from shedule.utils import create_call_result


class ListLoaderView(LoginRequiredMixin, ListView):
    queryset = Loader.objects.filter(is_active=True)
    template_name = 'loaders/list.html'


class CreateLoaderView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Loader
    form_class = CreateLoaderForm
    template_name = 'loaders/create.html'
    success_message = 'Профиль успешно добавлен'

    def get_success_url(self):
        create_call_result(self.object.id)
        return reverse_lazy('loaders:detail', args=(self.object.id,))


class DetailLoaderView(LoginRequiredMixin, DetailView):
    model = Loader
    template_name = 'loaders/detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CreateLoaderForm(instance=self.get_object())
        return context


class UpdateLoaderView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Loader
    form_class = CreateLoaderForm
    success_message = 'Профиль успешно сохранен!'

    def get_success_url(self) -> str:
        return reverse_lazy('loaders:detail', kwargs={'pk': self.object.id})


class ListSpecializationView(LoginRequiredMixin, ListView):
    queryset = Specialization.objects.all()
    template_name = 'specializations/spec_list.html'


class CreateSpecializationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Specialization
    form_class = CreateSpecializationForm
    template_name = 'specializations/spec_add.html'
    success_url = reverse_lazy('loaders:spec_list')
    success_message = 'Специализация успешно сохранена'


class EditSpecializationView(CreateSpecializationView, UpdateView):
    template_name = 'specializations/spec_edit.html'


class DeleteSpecializationView(LoginRequiredMixin, DeleteView):
    model = Specialization
    success_url = reverse_lazy('loaders:spec_list')
    
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Специализация успешно удален')
        return self.post(request, *args, **kwargs)


class ListStatusView(LoginRequiredMixin, ListView):
    queryset = Status.objects.all()
    template_name = 'statuses/status_list.html'


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = CreateStatusForm
    template_name = 'statuses/status_add.html'
    success_url = reverse_lazy('loaders:status_list')
    success_message = 'Статус успешно сохранен'


class EditStatusView(CreateStatusView, UpdateView):
    template_name = 'statuses/status_edit.html'


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('loaders:status_list')
    
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Статус успешно удален')
        return self.post(request, *args, **kwargs)


class ListPayMethodListView(LoginRequiredMixin, ListView):
    queryset = PayMethodList.objects.all()
    template_name = 'pay_method/list.html'


class CreatePayMethodListView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PayMethodList
    form_class = CreatePayMethodList
    template_name = 'pay_method/add.html'
    success_url = reverse_lazy('loaders:pay_method_list')
    success_message = 'Способ оплаты успешно сохранен'


class EditPayMethodListView(CreatePayMethodListView, UpdateView):
    template_name = 'pay_method/edit.html'


class DeletePayMethodListView(LoginRequiredMixin, DeleteView):
    model = PayMethodList
    success_url = reverse_lazy('loaders:pay_method_list')
    
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Способ оплаты успешно удален')
        return self.post(request, *args, **kwargs)


# class CreatePayMethodView(CreatePassportView):
#     model = PayMethod
#     parent_model = Loader
#     form_class = CreatePayMethodForm
#     template_name = 'loaders/pay_method_add.html'
#     success_message = 'Способ оплаты успешно сохранен'
    
#     def post(self, request, *args, **kwargs):
#         parent_obj = self.get_parent(request)
#         form = self.get_form()
#         if form.is_valid():
#             pm = form.save(commit=False)
#             pm.save()
#             parent_obj.pay_method = pm
#             parent_obj.save()
#             return self.form_valid(form)
#         return self.form_invalid(form)


# class UpdatePayMethodView(UpdatePassportView):
#     model = PayMethod
#     form_class = CreatePayMethodForm
#     template_name = 'loaders/pay_method_edit.html'
#     success_message = 'Способ оплаты успешно сохранен'

#     def get_object(self):
#         loader = Loader.objects.filter(id=self.kwargs['pk']).get()
#         return loader.pay_method