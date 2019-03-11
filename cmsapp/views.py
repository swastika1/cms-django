from django.shortcuts import render, redirect
from django.views.generic import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http import JsonResponse
import json as simplejson
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
# Create your views here.

# backend ko dai haru ko lagi

# class AjaxableResponseMixin(object):
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         if self.request.is_ajax():
#             data = {
#                 'id': self.object.id,
#             }
#             return JsonResponse(data)
#         else:
#             return response


class AdminMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Admin']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(AdminMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin'] = Admin.objects.get(
            user=self.request.user)
        return context



class ReceptionistMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Receptionist']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(ReceptionistMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptionist'] = Receptionist.objects.get(
            user=self.request.user)
        return context


class ConsultantMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Consultant']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(ConsultantMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultant'] = Consultant.objects.get(
            user=self.request.user)
        context['appointments'] = Appointment.objects.filter(
            consultant =self.request.user.consultant)
        context['appointmenter'] = Appointment.objects.filter(
            created_by =self.request.user)
        return context



class TeacherMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Teacher']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(TeacherMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = Teacher.objects.get(
            user=self.request.user)
        return context


class LeadMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Lead']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(LeadMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead'] = Lead.objects.get(
            user=self.request.user)
        return context


class StudentMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Student']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(StudentMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(
            user=self.request.user)
        return context


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sendlist'] = Task.objects.filter(
            assigned_to=self.request.user)
        context['receivelist'] = Task.objects.filter(
            assigned_by=self.request.user)
        context['receivedlist'] = Message.objects.filter(
            receiver=self.request.user)
        context['sentlist'] = Message.objects.filter(
            sender=self.request.user)
        context['feedlist'] = Feed.objects.all()
        context['feedform'] = FeedForm
        context['commentform'] = CommentForm
        # context['formset'] = DocumentFormSet
        return context


class ReceptionistRegistrationView(AdminMixin, CreateView):
    template_name = 'receptionisttemplates/receptionistcreate.html'
    form_class = ReceptionistRegistrationForm
    success_url = reverse_lazy('cmsapp:adminreceptionistlist')
    success_message = "Receptionist created successfully"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Receptionist")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class StudentRegistrationView(ReceptionistMixin, CreateView):
    template_name = 'receptionisttemplates/receptioniststudentcreate.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('cmsapp:receptioniststudentlist')
    success_message = 'Student Created Successfully'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Student")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class TeacherRegistrationView(ReceptionistMixin, CreateView):
    template_name = 'teachertemplates/teachercreate.html'
    form_class = TeacherRegistrationForm
    success_url = reverse_lazy('cmsapp:receptionistpanel')
    success_message = "Teacher created succesfully"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Teacher")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class AdminTeacherUpdateView(AdminMixin, UpdateView):
    template_name = 'teachertemplates/teachercreate.html'
    form_class = AdminTeacherUpdateForm
    success_url = reverse_lazy('cmsapp:adminteacherlist')
    model = Teacher
    success_message = "Teacher updated succesfully"
    context_object_name = 'teacherdetail'


class ConsultantRegistrationView(AdminMixin, CreateView):
    template_name = 'consultanttemplates/consultantcreate.html'
    form_class = ConsultantRegistrationForm
    success_url = reverse_lazy('cmsapp:adminconsultantlist')
    success_message = 'consultant created successfully.'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Consultant")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class ConsultantUpdateView(AdminMixin, UpdateView):
    template_name = 'consultanttemplates/consultantupdate.html'
    form_class = ConsultantUpdateForm
    success_url = reverse_lazy('cmsapp:adminconsultantlist')
    model = Consultant
    success_message = "Consultant updated succesfully"
    context_object_name = 'consultantupdate'


class LeadRegistrationView(ConsultantMixin, CreateView):
    template_name = 'leadtemplates/leadcreate.html'
    form_class = LeadRegistrationForm
    success_url = reverse_lazy('cmsapp:consultantleadlist')
    success_message = "Lead registered succesfully"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Lead")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class AjaxLeadCourseSelectView(View):
#     # def post(self, request, **kwargs):
#     #     return

    def get(self, request):
        pk = request.GET.get("id")
        print(pk)
        course = Course.objects.get(id=pk)
        print(course)
        university = University.objects.filter(course=course)
        print(university)
        data = {
        "id" : university
        }
        print(data)
        return JsonResponse(data)
        # print(data)
        # return render(request, '()' )
        # datas = json.dumps(data)
        # print (datas)
        # return HttpResponse(datas, content_type='application/json')


class VisitorRegistrationView(ReceptionistMixin, CreateView):
    template_name = 'visitortemplates/visitorcreate.html'
    form_class = VisitorRegistrationForm
    success_url = reverse_lazy('cmsapp:receptionistpanel')
    success_message = "Visitor created succesfully"


class AdminRegistrationView(AdminMixin, CreateView):
    template_name = 'admintemplates/admincreate.html'
    form_class = AdminRegistrationForm
    success_url = reverse_lazy('cmsapp:adminlist')
    success_message = "New Admin created succesfully"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Admin")
        group.user_set.add(user)
        form.instance.user = user

        return super().form_valid(form)


class AdminUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminupdate.html'
    model = Admin
    form_class = AdminUpdateForm
    success_url = reverse_lazy("cmsapp:adminlist")
    success_message = "Admin updated succesfully"
    context_object_name = 'admindetail'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
#     # success_url = reverse_lazy("cmsapp:adminlist")

#     def get(self,request):
#         if request.user.is_authenticated:
#             return render(self.request, 'admintemplates/adminbase.html')
#         return super().get(request)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if Receptionist.objects.filter(user=user).exists():
                messages.success(self.request,'You were successfully logged in.')
                self.success_url = reverse_lazy('cmsapp:receptionistpanel')
            elif Admin.objects.filter(user=user).exists():
                messages.success(self.request,'You were successfully logged in.')
                self.success_url = reverse_lazy('cmsapp:adminpanel')
            elif Teacher.objects.filter(user=user).exists():
                messages.success(self.request,'You were successfully logged in.')
                self.success_url = reverse_lazy('cmsapp:teacherpanel')
            elif Consultant.objects.filter(user=user).exists():
                messages.success(self.request,'You were successfully logged in.')
                self.success_url = reverse_lazy('cmsapp:consultantpanel')
            elif Lead.objects.filter(user=user).exists():
                messages.success(self.request,'You were successfully logged in.')
                self.success_url = reverse_lazy('cmsapp:leadpanel')
            elif Student.objects.filter(user=user).exists():
                messages.success(self.request,'You were successfully logged in.')
                self.success_url = reverse_lazy('cmsapp:studentpanel')
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'errors': "Please correct username or password "
            })
        return super().form_valid(form)


    # def get(self,request):
    #     if request.user.is_authenticated:
    #         return render(self.request, self.get_success_url)
    #     return super().get(request)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('cmsapp:login')


# Receptionist panel content


class ReceptionistPanelView(ReceptionistMixin, BaseMixin, TemplateView):
    template_name = 'receptionisttemplates/receptionistpanel.html'


class ReceptionistListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistlist.html'
    model = Consultant
    context_object_name = 'receptionistlist'


class ReceptionistLeadListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistleadlist.html'
    model = Lead
    context_object_name = 'receptionistleadlist'


class ReceptionistTeacherListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistteacherlist.html'
    model = Teacher
    context_object_name = 'receptionistteacherlist'


class ReceptionistConsultantListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistconsultantlist.html'
    model = Consultant
    context_object_name = 'receptionistconsultantlist'


class ReceptionistStudentListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptioniststudentlist.html'
    model = Student
    context_object_name = 'receptioniststudentlist'


class ReceptionistVisitorListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistvisitorlist.html'
    model = Visitor
    context_object_name = 'receptionistvisitorlist'


class ReceptionistTaskListView(ReceptionistMixin, BaseMixin, ListView):
    template_name = 'receptionisttemplates/receptionisttasklist.html'
    model = Task
    context_object_name = 'tasklist'


class ReceptionistAppointmentListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistappointmentlist.html'
    model = Appointment
    context_object_name = 'receptionistappointmentlist'


class ReceptionistUniversityListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistuniversitylist.html'
    model = University
    context_object_name = 'receptionistuniversitylist'


class ReceptionistLanguageCourseListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistlanguagecourselist.html'
    model = LanguageCourse
    context_object_name = 'receptionistlanguagecourselist'


class ReceptionistCourseListView(ReceptionistMixin, ListView):
    template_name = 'receptionisttemplates/receptionistcourselist.html'
    model = Course
    context_object_name = 'receptionistcourselist'

    # Receptionist panel detail views


class ReceptionistConsultantDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptionistconsultantdetail.html'
    model = Consultant
    context_object_name = 'receptionistconsultantdetail'


class ReceptionistDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptionistdetail.html'
    model = Receptionist
    context_object_name = 'receptionistdetail'


class ReceptionistStudentDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptioniststudentdetail.html'
    model = Student
    context_object_name = 'receptioniststudentdetail'


class ReceptionistLeadDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptionistleaddetail.html'
    model = Lead
    context_object_name = 'receptionistleaddetail'


class ReceptionistTeacherDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptionistteacherdetail.html'
    model = Teacher
    context_object_name = 'receptionistteacherdetail'


class ReceptionistVisitorDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptionistvisitordetail.html'
    model = Visitor
    context_object_name = 'receptionistvisitordetail'


class ReceptionistCourseDetailView(ReceptionistMixin, DetailView):
    template_name = 'receptionisttemplates/receptionistcoursedetail.html'
    model = Course
    context_object_name = 'receptionistcoursedetail'



# Receptionist panel create views

class ReceptionistVisitorCreateView(ReceptionistMixin, CreateView ):
    template_name = 'receptionisttemplates/receptionistvisitorcreate.html'
    form_class = VisitorRegistrationForm
    success_url = reverse_lazy('cmsapp:receptionistvisitorlist')
    success_message = "Visitor created succesfully"


class ReceptionistLeadCreateView(ReceptionistMixin, CreateView ):
    template_name = 'receptionisttemplates/receptionistleadcreate.html'
    form_class = LeadRegistrationForm
    success_url = reverse_lazy('cmsapp:receptionistleadlist')
    success_message = "Lead created succesfully"


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Lead")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class ReceptionistCourseCreateView(ReceptionistMixin, CreateView):
    template_name = 'receptionisttemplates/receptionistcoursecreate.html'
    form_class = CourseForm
    success_url = reverse_lazy('cmsapp:receptionistcourselist')
    success_message = "Course created succesfully"


class ReceptionistUniversityCreateView(ReceptionistMixin,CreateView):
    template_name = 'receptionisttemplates/receptionistuniversitycreate.html'
    form_class = UniversityForm
    success_url = reverse_lazy('cmsapp:receptionistuniversitylist')
    success_message = "University created succesfully"


class ReceptionistLanguageCourseCreateView(ReceptionistMixin, CreateView):
    template_name = 'receptionisttemplates/receptionistlanguagecoursecreate.html'
    form_class = LanguageCourseForm
    success_url = reverse_lazy('cmsapp:receptionistlanguagecourselist')
    success_message = "Language Course created succesfully"


class ReceptionistTaskCreateView(ReceptionistMixin,BaseMixin, CreateView):
    template_name = 'receptionisttemplates/receptionisttaskcreate.html'
    form_class = TaskForm
    success_url = reverse_lazy('cmsapp:receptionisttasklist')
    success_message = "Task created succesfully"

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)

class ReceptionistAppointmentCreateView(ReceptionistMixin, CreateView):
    template_name = 'receptionisttemplates/receptionistappointmentcreate.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('cmsapp:receptionistappointmentlist')
    success_message = "Appointment created succesfully"


# class ReceptionistStudentCreateView(ReceptionistMixin,CreateView):
#     template_name = 'receptionisttemplates/receptioniststudentcreate.html'
#     form_class = StudentRegistrationForm
#     success_url = reverse_lazy('cmsapp:receptioniststudentlist')
#     success_message = "student created successfully"

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password2']
#         user = User.objects.create_user(username, "", password)
#         group = Group.objects.get(name="Student")
#         group.user_set.add(user)
#         form.instance.user = user
#         # lead = form.save()
#         # documents = self.request.FILES.getlist('documents')
#         # for f in documents:
#         #     document = Document.objects.create(
#         #         title='hello', file=f, lead=lead)
#         return super().form_valid(form)

# Receptionist panel update views

class ReceptionistCourseUpdateView(ReceptionistMixin, UpdateView):
    template_name = 'receptionisttemplates/receptionistcoursecreate.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy("cmsapp:receptionistcourselist")
    success_message = "Course updated succesfully"


class ReceptionistTaskUpdateView(ReceptionistMixin, BaseMixin, UpdateView ):
    template_name = 'receptionisttemplates/receptionisttaskcreate.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("cmsapp:receptionisttasklist")
    success_message = "Task updated succesfully"

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)


class ReceptionistUniversityUpdateView(ReceptionistMixin, UpdateView ):
    template_name = 'receptionisttemplates/receptionistuniversitycreate.html'
    model = University
    form_class = UniversityForm
    success_url = reverse_lazy("cmsapp:receptionistuniversitylist")
    success_message = "University updated succesfully"


class ReceptionistStudentUpdateView(ReceptionistMixin, UpdateView):
    template_name = 'receptionisttemplates/receptioniststudentupdate.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy("cmsapp:receptioniststudentlist")
    success_message = "Student updated succesfully"
    context_object_name = 'studentdetail'


class ReceptionistVisitorUpdateView(ReceptionistMixin, UpdateView):
    template_name = 'receptionisttemplates/receptionistvisitorcreate.html'
    model = Visitor
    form_class = VisitorRegistrationForm
    success_url = reverse_lazy("cmsapp:receptionistvisitorlist")
    success_message = "Student updated succesfully"


class ReceptionistLanguageCourseUpdateView(ReceptionistMixin, UpdateView):
    template_name = 'receptionisttemplates/receptionistlanguagecoursecreate.html'
    model = LanguageCourse
    form_class = LanguageCourseForm
    success_url = reverse_lazy("cmsapp:receptionistlanguagecourselist")
    success_message = "Language Course updated succesfully"


class ReceptionistAppointmentUpdateView(ReceptionistMixin, UpdateView):
    template_name = 'receptionisttemplates/receptionistappointmentcreate.html'
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("cmsapp:receptionistappointmentlist")
    success_message = "Appointment updated succesfully"


class ReceptionistLeadUpdateView(ReceptionistMixin, UpdateView):
    template_name = 'receptionisttemplates/receptionistleadupdate.html'
    model = Lead
    form_class = LeadUpdateForm
    success_url = reverse_lazy("cmsapp:receptionistleadlist")
    success_message = "Lead updated succesfully"

# Receptionist panel delete views
class ReceptionistCourseDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionisttemplates/receptionistcoursedelete.html'
    model = Course
    success_url = reverse_lazy('cmsapp:receptionistcourselist')
    success_message = "Course  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReceptionistCourseDeleteView, self).delete(request, *args, **kwargs)


class ReceptionistLeadDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionisttemplates/receptionistleaddelete.html'
    model = Lead
    success_url = reverse_lazy('cmsapp:receptionistleadlist')
    success_message = "Lead  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReceptionistLeadDeleteView, self).delete(request, *args, **kwargs)


class ReceptionistUniversityDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionisttemplates/receptionistuniversitydelete.html'
    model = University
    success_url = reverse_lazy('cmsapp:receptionistuniversitylist')
    success_message = "University  deleted successfully."


class ReceptionistAppointmentDeleteView(ReceptionistMixin, DeleteView ):
    template_name = 'receptionisttemplates/receptionistappointmentdelete.html'
    model = Appointment
    success_url = reverse_lazy('cmsapp:receptionistappointmentlist')
    success_message = "Appointment  deleted successfully."


class ReceptionistStudentDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionisttemplates/receptioniststudentdelete.html'
    model = Student
    success_url = reverse_lazy('cmsapp:receptioniststudentlist')
    success_message = "Student deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReceptionistStudentDeleteView, self).delete(request, *args, **kwargs)


class ReceptionistVisitorDeleteView(ReceptionistMixin, DeleteView ):
    template_name = 'receptionisttemplates/receptionistvisitordelete.html'
    model = Visitor
    success_url = reverse_lazy('cmsapp:receptionistvisitorlist')
    success_message = "Visitor deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReceptionistVisitorDeleteView, self).delete(request, *args, **kwargs)


class ReceptionistLanguageCourseDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionisttemplates/receptionistlanguagecoursedelete.html'
    model = LanguageCourse
    success_url = reverse_lazy('cmsapp:receptionistlanguagecourselist')
    success_message = "Language Course deleted successfully."


class ReceptionistTaskDeleteView( ReceptionistMixin, BaseMixin, DeleteView):
    template_name = 'receptionisttemplates/receptionisttaskdelete.html'
    model = Task
    success_url = reverse_lazy('cmsapp:receptionisttasklist')
    success_message = "Task  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReceptionistTaskDeleteView, self).delete(request, *args, **kwargs)

# Student Panel content


class StudentPanelView(StudentMixin, BaseMixin, TemplateView):
    template_name = 'studenttemplates/studentpanel.html'


class StudentTeacherListView(StudentMixin, ListView):
    template_name = 'studenttemplates/studentteacherlist.html'
    model = Consultant
    context_object_name = 'studentteacherlist'


class StudentReceptionistListView(StudentMixin, ListView):
    template_name = 'studenttemplates/studentreceptionistlist.html'
    model = Receptionist
    context_object_name = 'studentreceptionistlist'

    # Student panel detail views


class StudentDetailView(StudentMixin, DetailView):
    template_name = 'studenttemplates/studentdetail.html'
    model = Student
    context_object_name = 'studentdetail'

    # Lead panel content


class LeadPanelView(LeadMixin, BaseMixin, TemplateView):
    template_name = 'leadtemplates/leadpanel.html'


class LeadConsultantListView(LeadMixin, ListView):
    template_name = 'leadtemplates/leadconsultantlist.html'
    model = Consultant
    context_object_name = 'leadconsultantlist'


class LeadReceptionistListView(LeadMixin, ListView):
    template_name = 'leadtemplates/leadreceptionistlist.html'
    model = Receptionist
    context_object_name = 'leadreceptionistlist'


class LeadDocumentListView(LeadMixin, ListView):
    template_name = 'leadtemplates/leaddocumentlist.html'
    model = Document
    context_object_name = 'leaddocumentlist'

    # lead panel detail views


class LeadDetailView(LeadMixin, DetailView):
    template_name = 'leadtemplates/leaddetail.html'
    model = Lead
    context_object_name = 'leaddetail'

    # Visitor Panel content


class VisitorPanelView(TemplateView):
    template_name = 'visitortemplates/visitorpanel.html'

# Teacher Panel content


class TeacherPanelView(TeacherMixin, BaseMixin, TemplateView):
    template_name = 'teachertemplates/teacherpanel.html'


class TeacherListView(TeacherMixin, ListView):
    template_name = 'teachertemplates/teacherlist.html'
    model = Teacher
    context_object_name = 'teacherlist'


class TeacherConsultantListView(TeacherMixin, ListView):
    template_name = 'teachertemplates/teacherconsultantlist.html'
    model = Consultant
    context_object_name = 'teacherconsultantlist'


class TeacherReceptionistListView(TeacherMixin, ListView):
    template_name = 'teachertemplates/teacherreceptionistlist.html'
    model = Receptionist
    context_object_name = 'teacherreceptionistlist'


class TeacherStudentListView(TeacherMixin, ListView):
    template_name = 'teachertemplates/teacherstudentlist.html'
    model = Student
    context_object_name = 'teacherstudentlist'


class TeacherTaskListView(TeacherMixin, BaseMixin, ListView):
    template_name = 'teachertemplates/teachertasklist.html'
    model = Task
    context_object_name = 'teachertasklist'


class TeacherUniversityListView(TeacherMixin, BaseMixin, ListView):
    template_name = 'teachertemplates/teacheruniversitylist.html'
    model = University
    context_object_name = 'teacheruniversitylist'


# teacherpanel detail views


class TeacherDetailView(TeacherMixin, DetailView):
    template_name = 'teachertemplates/teacherdetail.html'
    model = Teacher
    context_object_name = 'teacherdetail'


class TeacherStudentDetailView(TeacherMixin, DetailView):
    template_name = 'teachertemplates/teacherstudentdetail.html'
    model = Teacher
    context_object_name = 'teacherstudentdetail'

class TeacherStudyMaterialsListView(TeacherMixin, ListView):
    template_name = 'teachertemplates/teacherstudymaterialslist.html'
    model = StudyMaterials
    context_object_name = 'teacherstudymaterialslist'



# teacherpanel create views

class TeacherStudyMaterialsCreateView(TeacherMixin, FormView):
    template_name = 'teachertemplates/teacherstudymaterialscreate.html'
    form_class = TeacherStudyMaterialsForm
    success_url = reverse_lazy('cmsapp:teacherstudymaterialslist')
    success_message = "Study materials added successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = StudyMaterialsFormset(
            queryset=StudyMaterials.objects.none())
        return context

    def form_valid(self, form):
        studymaterialsformset =StudyMaterialsFormset(self.request.POST, self.request.FILES).save()
        language_course = form.cleaned_data['language_course']
        for studymaterials in studymaterialsformset:
            studymaterials.language_course = language_course
            studymaterials.save()
        return super().form_valid(form)

# teacherpanel update views
class TeacherStudyMaterialsUpdateView(TeacherMixin, UpdateView):
    template_name = 'teachertemplates/teacherstudymaterialscreate.html'
    model = StudyMaterials
    form_class = StudyMaterialsForm
    success_url = reverse_lazy("cmsapp:teacherstudymaterialslist")
    success_message = "Study Materials updated succesfully"



# teacherpanel delete views
class TeacherStudyMaterialsDeleteView(TeacherMixin, DeleteView):
    template_name = 'teachertemplates/teacherstudymaterialsdelete.html'
    model = StudyMaterials
    success_url = reverse_lazy('cmsapp:teacherstudymaterialslist')
    success_message = "Study Materials deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TeacherStudyMaterialsDeleteView, self).delete(request, *args, **kwargs)




# consultant panel content


class ConsultantPanelView(BaseMixin, ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantpanel.html'
    model = Task
    context_object_name = 'consultanttasklist'


 # consultant list views


class ConsultantListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantlist.html'
    model = Consultant
    context_object_name = 'consultantlist'


class ConsultantLeadListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantleadlist.html'
    model = Lead
    context_object_name = 'consultantleadlist'


class ConsultantTeacherListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantteacherlist.html'
    model = Teacher
    context_object_name = 'consultantteacherlist'


class ConsultantReceptionistListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantreceptionistlist.html'
    model = Receptionist
    context_object_name = 'consultantreceptionistlist'


class ConsultantStudentListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantstudentlist.html'
    model = Student
    context_object_name = 'consultantstudentlist'


class ConsultantVisitorListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantvisitorlist.html'
    model = Visitor
    context_object_name = 'consultantvisitorlist'


class ConsultantTaskListView(BaseMixin, ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultanttasklist.html'
    model = Task
    context_object_name = 'consultanttasklist'


class ConsultantAppointmentListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantappointmentlist.html'
    model = Appointment
    context_object_name = 'consultantappointmentlist'



class ConsultantDocumentListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantdocumentlist.html'
    model = Document
    context_object_name = 'consultantdocumentlist'


class ConsultantUniversityListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantuniversitylist.html'
    model = University
    context_object_name = 'consultantuniversitylist'\

class ConsultantCourseListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantcourselist.html'
    model = Course
    context_object_name = 'consultantcourselist'

class ConsultantActivityListView(ConsultantMixin, ListView):
    template_name = 'consultanttemplates/consultantactivitylist.html'
    model = Activity
    context_object_name = 'consultantactivitylist'


# consultant create views
class ConsultantDocumentCreateView(ConsultantMixin, FormView):
    template_name = 'consultanttemplates/consultantdocumentcreate.html'
    form_class = LeadDocumentForm
    success_url = reverse_lazy('cmsapp:consultantleadlist')
    success_message = "Document created succesfully"
    context_object_name = 'document'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = DocumentFormset(
            queryset=Document.objects.none())
        return context

    def form_valid(self, form, **kwargs):
        documentformset = DocumentFormset(self.request.POST, self.request.FILES).save()
        lead = form.cleaned_data['lead']
        # lead = Lead.objects.get(id=self.kwargs['lead_pk'])
        # print(lead)

        for document in documentformset:
            document.lead = lead
            document.save()

        return super().form_valid(form)


class ConsultantTaskCreateView( ConsultantMixin, BaseMixin, CreateView):
    template_name = 'consultanttemplates/consultanttaskcreate.html'
    form_class = TaskForm
    success_url = reverse_lazy('cmsapp:consultanttasklist')
    success_message = "Task created succesfully"

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)



class ConsultantAppointmentCreateView( BaseMixin, ConsultantMixin, CreateView):
    template_name = 'consultanttemplates/consultantappointmentcreate.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('cmsapp:consultantappointmentlist')
    success_message = "Appointment created succesfully"



class ConsultantUniversityCreateView( BaseMixin, ConsultantMixin, CreateView):
    template_name = 'consultanttemplates/consultantuniversitycreate.html'
    form_class = UniversityForm
    success_url = reverse_lazy('cmsapp:consultantuniversitylist')
    success_message = "University created succesfully"


class ConsultantCourseCreateView( BaseMixin, ConsultantMixin, CreateView):
    template_name = 'consultanttemplates/consultantcoursecreate.html'
    form_class = CourseForm
    success_url = reverse_lazy('cmsapp:consultantcourselist')
    success_message = "Course created succesfully"

class ConsultantActivityCreateView( BaseMixin, ConsultantMixin, CreateView):
    template_name = 'consultanttemplates/consultantactivitycreate.html'
    form_class = ActivityForm
    success_url = reverse_lazy('cmsapp:consultantactivitylist')
    success_message = "Activity created succesfully"

    def form_valid(self, form):
        user = self.request.user.consultant
        form.instance.consultant = user
        return super().form_valid(form)



# consultant update views
class ConsultantTaskUpdateView( BaseMixin,ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultanttaskcreate.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("cmsapp:consultanttasklist")
    success_message = "Task updated succesfully"

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)


class ConsultantAppointmentUpdateView(ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultantappointmentcreate.html'
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("cmsapp:consultantappointmentlist")
    success_message = "Appointment updated succesfully"


class ConsultantLeadUpdateView(ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultantleadupdate.html'
    model = Lead
    form_class = LeadUpdateForm
    success_url = reverse_lazy("cmsapp:consultantleadlist")
    success_message = "Lead updated succesfully"
    context_object_name = 'consultantleadupdate'



class ConsultantDocumentUpdateView(ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultantdocumentcreate.html'
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy("cmsapp:consultantdocumentlist")
    success_message = "Document updated succesfully"


class ConsultantCourseUpdateView(ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultantcoursecreate.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy("cmsapp:consultantcourselist")
    success_message = "Course updated succesfully"

class ConsultantUniversityUpdateView(ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultantuniversitycreate.html'
    model = University
    form_class = UniversityForm
    success_url = reverse_lazy("cmsapp:consultantuniversitylist")
    success_message = "University updated succesfully"

class ConsultantActivityUpdateView(ConsultantMixin, UpdateView):
    template_name = 'consultanttemplates/consultantactivitycreate.html'
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy("cmsapp:consultantactivitylist")
    success_message = "Activity updated succesfully"
    context_object_name = 'consultantactivityupdate'


# consultant delete views


class ConsultantTaskDeleteView( BaseMixin, ConsultantMixin, DeleteView):
    template_name = 'consultanttemplates/consultanttaskdelete.html'
    model = Task
    success_url = reverse_lazy('cmsapp:consultanttasklist')
    success_message = "Task  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ConsultantTaskDeleteView, self).delete(request, *args, **kwargs)


class ConsultantAppointmentDeleteView( ConsultantMixin, DeleteView):
    template_name = 'consultanttemplates/consultantappointmentdelete.html'
    model = Appointment
    success_url = reverse_lazy('cmsapp:consultantappointmentlist')
    success_message = "Appointment deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ConsultantAppointmentDeleteView, self).delete(request, *args, **kwargs)


class ConsultantDocumentDeleteView(ConsultantMixin, DeleteView):
    template_name = 'consultanttemplates/consultantdocumentdelete.html'
    model = Document
    success_url = reverse_lazy('cmsapp:consultantdocumentlist')
    success_message = "Document deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ConsultantDocumentDeleteView, self).delete(request, *args, **kwargs)



# consultant panel detail views


class ConsultantDetailView(ConsultantMixin, DetailView):
    template_name = 'consultanttemplates/consultantdetail.html'
    model = Consultant
    context_object_name = 'consultantdetail'


class ConsultantVisitorDetailView(ConsultantMixin, DetailView):
    template_name = 'consultanttemplates/consultantvisitordetail.html'
    model = Visitor
    context_object_name = 'consultantvisitordetail'


class ConsultantStudentDetailView(ConsultantMixin, DetailView):
    template_name = 'consultanttemplates/consultantstudentdetail.html'
    model = Student
    context_object_name = 'consultantstudentdetail'


class ConsultantLeadDetailView(ConsultantMixin, DetailView):
    template_name = 'consultanttemplates/consultantleaddetail.html'
    model = Lead
    context_object_name = 'consultantleaddetail'


class ConsultantUniversityDetailView(ConsultantMixin, DetailView):
    template_name = 'consultanttemplates/consultantuniversitydetail.html'
    model = University
    context_object_name = 'consultantuniversitydetail'

class ConsultantTaskDetailView(ConsultantMixin, DetailView):
    template_name = 'consultanttemplates/consultanttaskdetail.html'
    model = Task
    context_object_name = 'consultanttaskdetail'

# admin panel content
# class TaskStatusView(ConsultantMixin, View):
#     # template_name = 'admintemplates/adminpanel.html'
    
#     def get_context_data(self, **kwargs):
#         # print(self.request.POST.get('verify_status'))
#         context= super().get_context_data(**kwargs)
#         task = Task.objects.get(id=self.kwargs['pk'])
#         print(task)
#         return context

#     def get(self, request, **kwargs):
#         if request.method == 'GET':
#             print ('Hello')
#             # return redirect(self.HTTP_REFERRER)


class TaskStatusView(View):
   def get(self, request, **kwargs):
        print(request.GET.get('task_id'))
        task = Task.objects.get(id=request.GET.get('task_id'))
        status = request.GET.get('task_status')
        task.status = status
        task.save()
        return JsonResponse({'pk': task.id, 'status': task.status})


class AdminPanelView(AdminMixin,BaseMixin,TemplateView):
    template_name = 'admintemplates/adminpanel.html'


class AdminConsultantListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminconsultantlist.html'
    model = Consultant
    context_object_name = 'adminconsultantlist'


class AdminLeadListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminleadlist.html'
    model = Lead
    context_object_name = 'adminleadlist'


class AdminTeacherListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminteacherlist.html'
    model = Teacher
    context_object_name = 'adminteacherlist'


class AdminReceptionistListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminreceptionistlist.html'
    model = Receptionist
    context_object_name = 'adminreceptionistlist'


class AdminStudentListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminstudentlist.html'
    model = Student
    context_object_name = 'adminstudentlist'


class AdminVisitorListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminvisitorlist.html'
    model = Visitor
    context_object_name = 'adminvisitorlist'


class AdminTaskListView(AdminMixin, BaseMixin, ListView):
    template_name = 'admintemplates/admintasklist.html'
    model = Task
    context_object_name = 'tasklist'


class AdminAppointmentListView(AdminMixin, BaseMixin, ListView):
    template_name = 'admintemplates/adminappointmentlist.html'
    model = Appointment
    context_object_name = 'adminappointmentlist'


class AdminUniversityListView(AdminMixin, BaseMixin, ListView):
    template_name = 'admintemplates/adminuniversitylist.html'
    model = University
    context_object_name = 'adminuniversitylist'


class AdminCourseListView(AdminMixin, BaseMixin, ListView):
    template_name = 'admintemplates/admincourselist.html'
    model = Course
    context_object_name = 'admincourselist'

class AdminActivityListView(AdminMixin, BaseMixin, ListView):
    template_name = 'admintemplates/adminactivitylist.html'
    model = Activity
    context_object_name = 'adminactivitylist'

# admin panel create views

class AdminTeacherRegistrationView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminteachercreate.html'
    form_class = TeacherRegistrationForm
    success_url = reverse_lazy('cmsapp:adminteacherlist')
    success_message = 'Teacher registered successfully'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Teacher")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class AdminReceptionistRegistrationView(AdminMixin, CreateView):
    template_name = 'receptionisttemplates/receptionistcreate.html'
    form_class = ReceptionistRegistrationForm
    success_url = reverse_lazy('cmsapp:adminreceptionistlist')
    success_message = 'Receptionist registered successfully'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Receptionist")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class AdminStudentRegistrationView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminstudentcreate.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('cmsapp:adminstudentlist')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Student")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class AdminLeadRegistrationView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminleadcreate.html'
    form_class = LeadRegistrationForm
    success_url = reverse_lazy('cmsapp:adminleadlist')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Lead")
        group.user_set.add(user)
        form.instance.user = user
        return super().form_valid(form)


class AdminTaskCreateView(AdminMixin, BaseMixin, CreateView):
    template_name = 'admintemplates/admintaskcreate.html'
    form_class = TaskForm
    success_url = reverse_lazy("cmsapp:admintasklist")
    success_message = 'Task created successfully'

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)

class AdminUniversityCreateView(AdminMixin, BaseMixin, CreateView):
    template_name = 'admintemplates/adminuniversitycreate.html'
    form_class = UniversityForm
    success_url = reverse_lazy("cmsapp:adminuniversitylist")
    success_message = 'University created successfully'

class AdminCourseCreateView(AdminMixin, BaseMixin, CreateView):
    template_name = 'admintemplates/admincoursecreate.html'
    form_class = CourseForm
    success_url = reverse_lazy("cmsapp:admincourselist")
    success_message = 'Course created successfully'



# admin panel detail views

class AdminDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/admindetail.html'
    model = Admin
    context_object_name = 'admindetail'


class AdminConsultantDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminconsultantdetail.html'
    model = Consultant
    context_object_name = 'adminconsultantdetail'


class AdminReceptionistDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminreceptionistdetail.html'
    model = Receptionist
    context_object_name = 'adminreceptionistdetail'


class AdminStudentDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminstudentdetail.html'
    model = Student
    context_object_name = 'adminstudentdetail'


class AdminLeadDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminleaddetail.html'
    model = Lead
    context_object_name = 'adminleaddetail'


class AdminTeacherDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminteacherdetail.html'
    model = Teacher
    context_object_name = 'adminteacherdetail'


# Admin feed views 


class AdminFeedCreateView(AdminMixin, BaseMixin, CreateView):
    template_name = 'admintemplates/adminfeedlist.html'
    form_class = FeedForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        self.feed_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cmsapp:adminfeedlist")


class AdminFeedListView(AdminMixin, BaseMixin, generic.ListView):
    template_name = 'admintemplates/adminfeedlist.html'
    queryset = Feed.objects.all().order_by('-id')
    model = Feed
    context_object_name = 'feedlist'


class AdminFeedDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminfeedlist.html'
    model = Feed
    success_url = '/adminfeed/list/'


class AdminFeedCommentCreateView(AdminMixin, BaseMixin, CreateView):
    template_name = 'admintemplates/adminfeedlist.html'
    form_class = CommentForm
    success_url = '/adminfeed/list/'

    def form_valid(self, form):
        feed_id = self.kwargs['pk']
        feed = Feed.objects.get(id=feed_id)
        form.instance.post = feed
        form.instance.comment_by = self.request.user

        return super().form_valid(form)


class AdminFeedCommentDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminfeedlist.html'
    model = Feed
    success_url = '/adminfeed/list/'



# consultant feed views 


class ConsultantFeedCreateView(BaseMixin, ConsultantMixin, CreateView):
    template_name = 'consultanttemplates/consultantfeedlist.html'
    form_class = FeedForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        self.feed_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cmsapp:consultantfeedlist")


class ConsultantFeedListView(BaseMixin, ConsultantMixin, generic.ListView):
    template_name = 'consultanttemplates/consultantfeedlist.html'
    model = Feed
    context_object_name = 'feedlist'


class ConsultantFeedDeleteView(ConsultantMixin, DeleteView):
    template_name = 'consultanttemplates/consultantfeedlist.html'
    model = Feed
    success_url = '/consultantfeed/list/'


class ConsultantFeedCommentCreateView(BaseMixin, ConsultantMixin, CreateView):
    template_name = 'consultanttemplates/consultantfeedlist.html'
    form_class = CommentForm
    success_url = '/consultantfeed/list/'

    def form_valid(self, form):
        feed_id = self.kwargs['pk']
        feed = Feed.objects.get(id=feed_id)
        form.instance.post = feed
        form.instance.comment_by = self.request.user

        return super().form_valid(form)


class ConsultantFeedCommentDeleteView(ConsultantMixin, DeleteView):
    template_name = 'consultanttemplates/consultantfeedlist.html'
    model = Feed
    success_url = '/consultantfeed/list/'


# # Admin Panel Update Views
# class AdminConsultantUpdateView(AdminMixin, UpdateView):
#     template_name = 'admintemplates/adminconsultantcreate.html'
#     form_class = ConsultantRegistrationForm
#     success_url = reverse_lazy('cmsapp:adminconsultantlist')
#     model = Consultant
#     success_message = "Consultant updated succesfully"


class AdminTeacherUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminteacherupdate.html'
    form_class = AdminTeacherUpdateForm
    success_url = reverse_lazy('cmsapp:adminteacherlist')
    model = Teacher
    success_message = "Teacher updated succesfully"
    context_object_name = 'teacherdetail'


class AdminReceptionistUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminreceptionistupdate.html'
    form_class = ReceptionistUpdateForm
    success_url = reverse_lazy('cmsapp:adminreceptionistlist')
    model = Receptionist
    success_message = "Receptionist updated succesfully"
    context_object_name = 'receptionistdetail'

class AdminUniversityUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminuniversitycreate.html'
    form_class = UniversityForm
    success_url = reverse_lazy('cmsapp:adminuniversitylist')
    model = University
    success_message = "University updated succesfully"
    context_object_name = 'Universitydetail'

class AdminCourseUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/admincoursecreate.html'
    form_class = CourseForm
    success_url = reverse_lazy('cmsapp:admincourselist')
    model = Course
    success_message = "Course updated succesfully"
    context_object_name = 'coursedetail'


class AdminLeadUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminleadcreate.html'
    form_class = LeadUpdateForm
    success_url = reverse_lazy('cmsapp:adminleadlist')
    model = Lead
    success_message = "Lead updated succesfully"
    context_object_name = 'leaddetail'


class AdminStudentUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminstudentupdate.html'
    form_class = StudentUpdateForm
    success_url = reverse_lazy('cmsapp:adminstudentlist')
    model = Student
    success_message = "Student updated succesfully"
    context_object_name = 'studentdetail'


# Admin Panel Delete Views

class AdminConsultantDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminconsultantdelete.html'
    model = Consultant
    success_url = reverse_lazy('cmsapp:adminconsultantlist')
    success_message = "Consultant  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminConsultantDeleteView, self).delete(request, *args, **kwargs)


class AdminLeadDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminleaddelete.html'
    model = Lead
    success_url = reverse_lazy('cmsapp:adminleadlist')
    success_message = "Lead  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminLeadDeleteView, self).delete(request, *args, **kwargs)



class AdminLeadDeleteView(AdminMixin,BaseMixin, DeleteView):
    template_name = 'admintemplates/adminleaddelete.html'
    model = Lead
    success_url = reverse_lazy('cmsapp:adminleadlist')
    success_message = "Lead deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminLeadDeleteView, self).delete(request, *args, **kwargs)


class AdminStudentDeleteView(AdminMixin,BaseMixin, DeleteView):
    template_name = 'admintemplates/adminstudentdelete.html'
    model = Student
    success_url = reverse_lazy('cmsapp:adminstudentlist')
    success_message = "Student deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminStudentDeleteView, self).delete(request, *args, **kwargs)

class AdminTeacherDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminteacherdelete.html'
    model = Teacher
    success_url = reverse_lazy('cmsapp:adminteacherlist')
    success_message = "Teacher deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminTeacherDeleteView, self).delete(request, *args, **kwargs)


class AdminReceptionistDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminreceptionistdelete.html'
    model = Receptionist
    success_url = reverse_lazy('cmsapp:adminreceptionistlist')
    success_message = "Receptionist deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminReceptionistDeleteView, self).delete(request, *args, **kwargs)


class AdminStudentDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminstudentdelete.html'
    model = Student
    success_url = reverse_lazy('cmsapp:adminstudentlist')
    success_message = "Student deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminStudentDeleteView, self).delete(request, *args, **kwargs)

class AdminVisitorDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminvisitordelete.html'
    model = Visitor
    success_url = reverse_lazy('cmsapp:adminvisitorlist')
    success_message = "Visitor deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminVisitorDeleteView, self).delete(request, *args, **kwargs)

class AdminTaskDeleteView(AdminMixin, BaseMixin, DeleteView):
    template_name = 'admintemplates/admintaskdelete.html'
    model = Task
    success_url = reverse_lazy('cmsapp:admintasklist')
    success_message = "Task  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminTaskDeleteView, self).delete(request, *args, **kwargs)

class AdminActivityDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminactivitydelete.html'
    model = Activity
    success_url = reverse_lazy('cmsapp:adminactivitylist')
    success_message = "Activity deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminActivityDeleteView, self).delete(request, *args, **kwargs)

class AdminUniversityDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminuniversitydelete.html'
    model = University
    success_url = reverse_lazy('cmsapp:adminuniversitylist')
    success_message = "University deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminUniversityDeleteView, self).delete(request, *args, **kwargs)

class AdminCourseDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/admincoursedelete.html'
    model = Course
    success_url = reverse_lazy('cmsapp:admincourselist')
    success_message = "Course deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminCourseDeleteView, self).delete(request, *args, **kwargs)


# receptionist feed views 


class ReceptionistFeedCreateView(ReceptionistMixin, BaseMixin, CreateView):
    template_name = 'receptionisttemplates/receptionistfeedlist.html'
    form_class = FeedForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        self.feed_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cmsapp:receptionistfeedlist")


class ReceptionistFeedListView(ReceptionistMixin, BaseMixin, generic.ListView):
    template_name = 'receptionisttemplates/receptionistfeedlist.html'
    model = Feed
    context_object_name = 'feedlist'


class ReceptionistFeedDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionisttemplates/receptionistfeedlist.html'
    model = Feed
    success_url = '/receptionistfeed/list/'


class ReceptionistFeedCommentCreateView(ReceptionistMixin, BaseMixin, CreateView):
    template_name = 'receptionistemplates/receptionistfeedlist.html'
    form_class = CommentForm
    success_url = '/receptionistfeed/list/'

    def form_valid(self, form):
        feed_id = self.kwargs['pk']
        feed = Feed.objects.get(id=feed_id)
        form.instance.post = feed
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class ReceptionistFeedCommentDeleteView(ReceptionistMixin, DeleteView):
    template_name = 'receptionistemplates/receptionistfeedlist.html'
    model = Feed
    success_url = '/receptionistfeed/list/'



# teacher feed views 



class TeacherFeedCreateView(TeacherMixin, BaseMixin, CreateView):
    template_name = 'teachertemplates/teacherfeedlist.html'
    form_class = FeedForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        self.feed_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cmsapp:teacherfeedlist")


class TeacherFeedListView(TeacherMixin, BaseMixin, generic.ListView):
    template_name = 'teachertemplates/teacherfeedlist.html'
    model = Feed
    context_object_name = 'feedlist'


class TeacherFeedDeleteView(TeacherMixin, DeleteView):
    template_name = 'teachertemplates/teacherfeedlist.html'
    model = Feed
    success_url = '/teacherfeed/list/'


class TeacherFeedCommentCreateView(TeacherMixin, BaseMixin, CreateView):
    template_name = 'teacheremplates/teacherfeedlist.html'
    form_class = CommentForm
    success_url = '/teacherfeed/list/'

    def form_valid(self, form):
        feed_id = self.kwargs['pk']
        feed = Feed.objects.get(id=feed_id)
        form.instance.post = feed
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class TeacherFeedCommentDeleteView(TeacherMixin, DeleteView):
    template_name = 'teacheremplates/teacherfeedlist.html'
    model = Feed
    success_url = '/teacherfeed/list/'



# lead feed views 


class LeadFeedCreateView(LeadMixin, BaseMixin, CreateView):
    template_name = 'leadtemplates/leadfeedlist.html'
    form_class = FeedForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        self.feed_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cmsapp:leadfeedlist")


class LeadFeedListView(LeadMixin, BaseMixin, generic.ListView):
    template_name = 'leadtemplates/leadfeedlist.html'
    model = Feed
    context_object_name = 'feedlist'


class LeadFeedDeleteView(LeadMixin, DeleteView):
    template_name = 'leadtemplates/leadfeedlist.html'
    model = Feed
    success_url = '/leadfeed/list/'


class LeadFeedCommentCreateView(LeadMixin, BaseMixin, CreateView):
    template_name = 'leadtemplates/leadfeedlist.html'
    form_class = CommentForm
    success_url = '/leadfeed/list/'

    def form_valid(self, form):
        feed_id = self.kwargs['pk']
        feed = Feed.objects.get(id=feed_id)
        form.instance.post = feed
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class LeadFeedCommentDeleteView(LeadMixin, DeleteView):
    template_name = 'leadtemplates/leadfeedlist.html'
    model = Feed
    success_url = '/leadfeed/list/'


# student feed views 


class StudentFeedCreateView(BaseMixin, CreateView):
    template_name = 'studenttemplates/studentfeedlist.html'
    form_class = FeedForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        self.feed_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cmsapp:studentfeedlist")


class StudentFeedListView(BaseMixin, generic.ListView):
    template_name = 'studenttemplates/studentfeedlist.html'
    model = Feed
    context_object_name = 'feedlist'


class StudentFeedDeleteView(DeleteView):
    model = Feed
    success_url = '/studentfeed/list/'


class StudentFeedCommentCreateView(BaseMixin, CreateView):
    template_name = 'studenttemplates/studentfeedlist.html'
    form_class = CommentForm
    success_url = '/studentfeed/list/'

    def form_valid(self, form):
        feed_id = self.kwargs['pk']
        feed = Feed.objects.get(id=feed_id)
        form.instance.post = feed
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class StudentFeedCommentDeleteView(DeleteView):
    template_name = 'studenttemplates/studentfeedlist.html'
    model = Feed
    success_url = '/studentfeed/list/'


class AdminPasswordChangeView(AdminMixin, FormView):
    template_name = 'admintemplates/adminpasswordchange.html'
    form_class = PasswordChangeForm
    success_url = '/adminpanel/'

    def form_valid(self, form):
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = self.request.user
        user.set_password(confirm_new_password)
        user.save()
        return super().form_valid(form)


class ConsultantPasswordChangeView(ConsultantMixin, FormView):
    template_name = 'consultanttemplates/consultantpasswordchange.html'
    form_class = PasswordChangeForm
    success_url = '/consultantpanel'

    def form_valid(self, form):
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = self.request.user
        user.set_password(confirm_new_password)
        user.save()
        return super().form_valid(form)


class LeadPasswordChangeView(LeadMixin, FormView):
    template_name = 'leadtemplates/leadpasswordchange.html'
    form_class = PasswordChangeForm
    success_url = '/leadpanel'

    def form_valid(self, form):
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = self.request.user
        user.set_password(confirm_new_password)
        user.save()
        return super().form_valid(form)


class ReceptionistPasswordChangeView(ReceptionistMixin, FormView):
    template_name = 'receptionisttemplates/receptionistpasswordchange.html'
    form_class = PasswordChangeForm
    success_url = 'receptionistpanel/'

    def form_valid(self, form):
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = self.request.user
        user.set_password(confirm_new_password)
        user.save()
        return super().form_valid(form)


class TeacherPasswordChangeView(TeacherMixin, FormView):
    template_name = 'teachertemplates/teacherpasswordchange.html'
    form_class = PasswordChangeForm
    success_url = '/teacherpanel'

    def form_valid(self, form):
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = self.request.user
        user.set_password(confirm_new_password)
        user.save()
        return super().form_valid(form)


class StudentPasswordChangeView(StudentMixin, FormView):
    template_name = 'studenttemplates/studentpasswordchange.html'
    form_class = PasswordChangeForm
    success_url = '/studentpanel'

    def form_valid(self, form):
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = self.request.user
        user.set_password(confirm_new_password)
        user.save()
        return super().form_valid(form)

        # Front end ko vura haru ko lagi


# Create your views here.

# backend ko dai haru ko lagi


# Front end ko vura haru ko lagi

# class FeedCreateView(BaseMixin, CreateView):
#     template_name = 'feedlist.html'
#     form_class = FeedForm

#     def form_valid(self, form):
#         user = self.request.user
#         form.instance.feed_by = user
#         self.feed_id = form.save().id
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy("cmsapp:feedlist")


# class FeedListView(BaseMixin, generic.ListView):
#     template_name = 'feedlist.html'
#     model = Feed
#     context_object_name = 'feedlist'


# class FeedDetailView(DetailView):
#     template_name = 'feeddetail.html'
#     model = Feed
#     context_object_name = 'feeddetail'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['commentform'] = CommentForm
#         return context


# class CommentCreateView(BaseMixin, CreateView):
#     template_name = 'feedlist.html'
#     form_class = CommentForm
#     success_url = '/feed/list/'

#     def form_valid(self, form):
#         feed_id = self.kwargs['pk']
#         feed = Feed.objects.get(id=feed_id)
#         form.instance.post = feed
#         form.instance.comment_by = self.request.user

#         return super().form_valid(form)


# class MessageCreateView(BaseMixin, CreateView):
#     template_name = 'messagecreate.html'
#     form_class = MessageForm
#     success_url = '/'

#     def form_valid(self, form):
#         user = self.request.user
#         form.instance.sender = user
#         return super().form_valid(form)

# Task


class TaskCreateView(BaseMixin, CreateView):
    template_name = 'taskcreate.html'
    form_class = TaskForm
    success_url = reverse_lazy("cmsapp:tasklist")

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)


class TaskListView(BaseMixin, ListView):
    template_name = 'tasklist.html'
    model = Task
    context_object_name = 'tasklist'


class TaskBoardView(BaseMixin, ListView):
    template_name = 'taskboard.html'
    model = Task
    context_object_name = 'tasklist'


class TaskDetailView(DetailView):
    template_name = 'taskdetail.html'
    model = Task
    context_object_name = 'taskdetail'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['commentform'] = CommentForm
    #     return context


class TaskUpdateView(UpdateView):
    template_name = 'taskcreate.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("cmsapp:tasklist")
    success_message = "Task updated succesfully"

    def form_valid(self, form):
        user = self.request.user
        form.instance.assigned_by = user
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    template_name = 'taskdelete.html'
    model = Task
    success_url = reverse_lazy('cmsapp:tasklist')
    success_message = "Task  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDeleteView, self).delete(request, *args, **kwargs)


class AppointmentCreateView(AdminMixin, BaseMixin, CreateView):
    template_name = 'admintemplates/adminappointmentcreate.html'
    form_class = AppointmentForm
    success_url = reverse_lazy("cmsapp:adminappointmentlist")

    def form_valid(self, form):
        return super().form_valid(form)


class AppointmentListView(AdminMixin, BaseMixin, ListView):
    template_name = 'appointmentlist.html'
    model = Appointment
    context_object_name = 'appointmentlist'


class AppointmentDetailView(AdminMixin, DetailView):
    template_name = 'appointmentdetail.html'
    model = Appointment
    context_object_name = 'appointmentdetail'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['commentform'] = CommentForm
    #     return context


class AppointmentUpdateView(UpdateView):
    template_name = 'appointmentcreate.html'
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("cmsapp:appointmentlist")
    success_message = "Appointment updated succesfully"


class AppointmentDeleteView(DeleteView):
    template_name = 'appointmentdelete.html'
    model = Appointment
    success_url = reverse_lazy('cmsapp:appointmentlist')
    success_message = "Appointment deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AppointmentDeleteView, self).delete(request, *args, **kwargs)


class MessageListView(BaseMixin, ConsultantMixin, ListView):
    template_name = 'messagelist.html'
    model = Message
    context_object_name = 'messagelist'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['commentform'] = CommentForm
    #     return context


class LanguageCourseCreateView(CreateView):
    template_name = 'languagecoursecreate.html'
    form_class = LanguageCourseForm
    success_url = reverse_lazy("cmsapp:languagecourselist")


class LanguageCourseListView(BaseMixin, ListView):
    template_name = 'languagecourselist.html'
    model = LanguageCourse
    context_object_name = 'languagecourselist'

# University


class UniversityCreateView(BaseMixin, CreateView):
    template_name = 'universitycreate.html'
    form_class = UniversityForm
    success_url = reverse_lazy("cmsapp:universitylist")


class UniversityListView(ListView):
    template_name = 'universitylist.html'
    model = University
    context_object_name = 'universitylist'


class UniversityDetailView(DetailView):
    template_name = 'universitydetail.html'
    model = University
    context_object_name = 'universitydetail'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['commentform'] = CommentForm
    #     return context


class UniversityUpdateView(UpdateView):
    template_name = 'universitycreate.html'
    model = University
    form_class = UniversityForm
    success_url = reverse_lazy("cmsapp:universitylist")
    success_message = "University updated succesfully"


class UniversityDeleteView(DeleteView):
    template_name = 'universitydelete.html'
    model = University
    success_url = reverse_lazy('cmsapp:universitylist')
    success_message = "University  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UniversityDeleteView, self).delete(request, *args, **kwargs)

# class OrganizationCreateView(BaseMixin, CreateView):
#     template_name = 'organizationcreate.html'
#     form_class = OrganizationForm
#     success_url = '/'


class StudentListView(ListView):
    template_name = 'studenttemplates/studentlist.html'
    model = Student
    context_object_name = 'studentlist'



class ReceptionListView(ListView):
    template_name = 'receptionisttemplates/receptionistlist.html'
    model = Receptionist
    context_object_name = 'receptionistlist'


class LeadListView(ListView):
    template_name = 'leadtemplates/leadlist.html'
    model = Lead
    context_object_name = 'leadlist'


class AdminListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminlist.html'
    model = Admin
    context_object_name = 'adminlist'


class VisitorListView(ListView):
    template_name = 'visitortemplates/visitorlist.html'
    model = Visitor
    context_object_name = 'visitorlist'

# Course


class CourseCreateView(BaseMixin, CreateView):
    template_name = 'coursecreate.html'
    form_class = CourseForm
    success_url = reverse_lazy("cmsapp:courselist")


class CourseListView(ListView):
    template_name = 'courselist.html'
    model = Course
    context_object_name = 'courselist'


class CourseDetailView(DetailView):
    template_name = 'coursedetail.html'
    model = Course
    context_object_name = 'coursedetail'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['commentform'] = CommentForm
    #     return context


class CourseUpdateView(UpdateView):
    template_name = 'coursecreate.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy("cmsapp:courselist")
    success_message = "Course updated succesfully"


class CourseDeleteView(DeleteView):
    template_name = 'coursedelete.html'
    model = Course
    success_url = reverse_lazy('cmsapp:courselist')
    success_message = "Course deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)
