from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from loaders.models import Loader, Passport, PayMethodList, Specialization, Status
from loaders.forms import CreateLoaderForm, CreatePassportForm, CreatePayMethodForm, CreatePayMethodList, CreateSpecializationForm, CreateStatusForm
from shedule.utils import create_call_result, workdays_bulk_create


class ListLoaderView(LoginRequiredMixin, ListView):
    queryset = Loader.objects.filter(is_active=True)
    template_name = 'loaders/list.html'


class CreateLoaderView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Loader
    form_class = CreateLoaderForm
    template_name = 'loaders/create.html'
    success_message = 'Профиль грузчика успешно добавлен'
    success_url = reverse_lazy('loaders:list')

    def get_success_url(self):
        workdays_bulk_create(self.object.id)
        create_call_result(self.object.id)
        return reverse_lazy('loaders:detail', args=(self.object.id,))


class DetailUpdateLoaderViewSet(LoginRequiredMixin, SuccessMessageMixin, DetailView, UpdateView):
    model = Loader
    form_class = CreateLoaderForm
    template_name = 'loaders/detail.html'
    success_message = 'Профиль грузчика успешно сохранен'

    def get_success_url(self):
        return reverse_lazy('loaders:detail', args=(self.object.id,))
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        passport_form = CreatePassportForm(request.GET or None)
        context = self.get_context_data(object=self.object)
        context['passport_form'] = passport_form
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        passport_form = CreatePassportForm(request.POST or None)
        if passport_form.is_valid():
            passport = passport_form.save()
            passport.save()
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class CreatePassportView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Passport
    parent_model = Loader
    form_class = CreatePassportForm
    template_name = 'loaders/passport_add.html'
    success_message = 'Паспортные данные успешно сохранены'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loader'] = self.get_parent(self.request)
        return context

    def get_parent(self, request):
        return get_object_or_404(self.parent_model, pk=self.kwargs['pk'])
    
    def post(self, request, *args, **kwargs):
        parent_obj = self.get_parent(request)
        form = self.get_form()
        if form.is_valid():
            passport = form.save(commit=False)
            passport.save()
            parent_obj.passport = passport
            parent_obj.save()
            return self.form_valid(form)
        return self.form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('loaders:detail', kwargs={'pk': self.kwargs['pk']})


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


class CreatePayMethodView(CreatePassportView):
    model = Passport
    parent_model = Loader
    form_class = CreatePayMethodForm
    template_name = 'loaders/pay_method_add.html'
    success_message = 'Способ оплаты успешно сохранен'
    
    def post(self, request, *args, **kwargs):
        parent_obj = self.get_parent(request)
        form = self.get_form()
        if form.is_valid():
            pm = form.save(commit=False)
            pm.save()
            parent_obj.pay_method = pm
            parent_obj.save()
            return self.form_valid(form)
        return self.form_invalid(form)