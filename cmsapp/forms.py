from django import forms
from django.forms import Select
from .models import *
from django.forms import modelformset_factory

# back end ko dai haru ko lagi


class ReceptionistRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Receptionist
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'about', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),

        }

    def clean(self):
        cleaned_data = super(ReceptionistRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ReceptionistUpdateForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ['name', 'phone', 'address', 'email', 'about', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),

        }


class VisitorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'phone', 'address', 'email',
                  'source', 'purpose', 'about', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'source': forms.Select(attrs={
                'class': 'form-control',
                'class': 'js-example-basic-single',
                'placeholder': 'Enter Address',
            }),
            'purpose': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Purpose of visit',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),

        }


        

class LeadUpdateForm(forms.ModelForm):
    # course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
    #     'class': 'form-control form-control-primary',
    # }),)
    # university = forms.ModelChoiceField(queryset=University.objects.all(), widget=forms.Select(attrs={
    #     'class': 'form-control form-control-primary',
    # }),)

    class Meta:
        model = Lead
        fields = ['university',
                  'name', 'email', 'address', 'phone', 'visa_status', 'about', 'image', 'course']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'visa_status': forms.Select(attrs={
                'class': 'form-control',
                'class': 'js-example-basic-single',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),
            'university': forms.Select(attrs={
                'class': 'form-control',
                'class': 'js-example-basic-single',
            }),
            'course': forms.Select(attrs={
                'class': 'form-control',
                'class': 'js-example-basic-single',
            }),


        }


# class UniversityUpdateForm(forms.ModelForm):
#     course = forms.ModelChoiceField(queryset=Course.objects.all())
#     university = forms.ModelChoiceField(queryset=University.objects.none())

#     class Meta:
#         model = Lead
#         fields = ['university',
#                   'course']
#         widgets = {
#             'course': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Course',
#             }),
#             'university': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select university',
#             })
#         }

    # def get(self, request):
    #     course = self.instance.course
    #     course_id = course.id
    #     return course_id


class LeadRegistrationForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control form-control-primary',
    }),)
    university = forms.ModelChoiceField(queryset=University.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control form-control-primary',
    }),)
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    # documents = forms.FileField(widget=forms.ClearableFileInput(attrs={
    #     'class': 'form-control',
    #     'multiple': True,
    #     'placeholder': 'Upload Documents',
    # }),
    # )

    class Meta:
        model = Lead
        fields = ['username', 'password1', 'password2',
                  'name', 'email', 'address', 'phone', 'course', 'university', 'visa_status', 'about', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),

            'visa_status': forms.Select(attrs={
                'class': 'form-control form-control-primary',
                'class': 'js-example-basic-single',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),

        }

    def clean(self):
        cleaned_data = super(LeadRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Student
        fields = ['username', 'password1', 'password2', 'assigned_to',
                  'name', 'email', 'phone', 'address', 'language_course', 'about', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter Email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'language_course': forms.Select(attrs={
                'class': 'form-control form-control-primary',
                'class': 'js-example-basic-single',
                'label': 'Category',

            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-control form-control-primary',
                'label': 'assigned to',
                'class': 'js-example-basic-single',

            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),



        }

    def clean(self):
        cleaned_data = super(StudentRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['assigned_to', 'name', 'email', 'phone',
                  'address', 'language_course', 'about', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter Email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'language_course': forms.Select(attrs={
                'class': 'form-control form-control-primary',
                'label': 'Category',
                'class': 'js-example-basic-single',

            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-control form-control-primary',
                'label': 'assigned to',
                'class': 'js-example-basic-single',

            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),



        }


class ConsultantRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Consultant
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'about', 'image']

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Consultant Image',
            }),
        }

    def clean(self):
        cleaned_data = super(ConsultantRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ConsultantUpdateForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = ['name', 'phone', 'address', 'email', 'about', 'image']

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Consultant Image',
            }),
        }


class TeacherRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Teacher
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'experience', 'qualification', 'about', 'image']

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Experience',
            }),
            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Qualification',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter about',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),
        }

    def clean(self):
        cleaned_data = super(TeacherRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class AdminTeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'phone', 'address', 'email',
                  'experience', 'qualification', 'about', 'image']

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Experience',
            }),
            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Qualification',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter about',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image',
            }),
        }


class AdminRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Admin
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'about', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Image',
            }),

        }

    def clean(self):
        cleaned_data = super(AdminRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'phone', 'address', 'email', 'about', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Detail',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Image',
            }),

        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Username',
    }),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        remember_me = cleaned_data.get('remember_me')
        if remember_me is True:
            SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        else:
            SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        return


class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))

    def clean(self):
        cleaned_data = super(PasswordChangeForm, self).clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New password and confirm new password didn't match")
        return confirm_new_password


class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['post']

        widgets = {
            'post': forms.Textarea(attrs={
                'placeholder': 'Write Something...',
                'rows': '5',
                'cols': '50',
                'class': 'form-control',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write Something...',
                'rows': '5',
                'cols': '50',
                'class': 'form-control',
            }),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['msg_content', 'receiver']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['lead', 'consultant', 'subject','appointment_date','status','note']
        widgets = {
            'lead': forms.Select(attrs={
                'placeholder': 'Enter Lead Name',
                'class': 'form-control',
                'class': 'js-example-basic-single',
            }),
            'consultant': forms.Select(attrs={
                'placeholder': 'Enter Consultant Name',
                'class': 'form-control',
                'class': 'js-example-basic-single',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'subject of appointment',
                'class': 'form-control',
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter necessary details',
            }),
            'status': forms.Select(attrs={
                'placeholder': 'Appointment Status',
                'class': 'form-control',
                'class': 'js-example-basic-single',
            }),
            'appointment_date': forms.DateTimeInput(attrs={
                'placeholder': 'Enter Appointment Date',
                'id':'datetime-local',
                'class': 'form-control',
            })
        }


class LeadDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['lead']

        widgets = {
            'lead': forms.Select(attrs={
                'placeholder': 'Lead Name',
                'class': 'js-example-basic-single',

            }),
        }


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'file']

        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'placeholder': 'File Title',
                'class': 'form-control',

            }),
        }


DocumentFormset = modelformset_factory(
    Document, form=DocumentForm, max_num=10, extra=2)

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['lead','note']

        widgets = {
            'lead': forms.Select(attrs={
                'placeholder': 'Lead Name',
                'class': 'js-example-basic-single',

            }),
            # 'consultant': forms.Select(attrs={
            #     'placeholder': 'consultant Name',

            # }),
            'note': forms.Textarea(attrs={
                'placeholder': 'Enter your log in details',

            }),
        }


class TeacherStudyMaterialsForm(forms.ModelForm):
    class Meta:
        model = StudyMaterials
        fields = ['language_course']

        widgets = {
            'language_course': forms.Select(attrs={
                'placeholder': 'Plz select the course',
                'class': 'js-example-basic-single',
                'class': 'form-control',

            }),
        }


class StudyMaterialsForm(forms.ModelForm):

    class Meta:
        model = StudyMaterials
        fields = ['title', 'study_file']

        widgets = {
            'study_file': forms.ClearableFileInput(attrs={
                'placeholder': 'File Title',
                'class': 'form-control',

            }),
        }


StudyMaterialsFormset = modelformset_factory(
    StudyMaterials, form=StudyMaterialsForm, max_num=10, extra=2)


class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={
        'class': 'js-example-basic-multiple',
        'multiple': 'multiple',
    })
    )

    class Meta:
        model = Task

        fields = ['title', 'content', 'priority',
                  'due_date', 'assigned_to', 'status']

    widgets = {
        'title': forms.TextInput(attrs={
            'placeholder': 'Enter Your Name',
            'class': 'form-control',
        }),
        'due_date': forms.DateInput(attrs={
            'placeholder': 'Due date',
            'id': 'id_due_date'
        }),
        'status': forms.Select(attrs={
            'placeholder':'Task status',
            'class':'form-control',
        })

        # 'assigned_to': forms.SelectMultiple(attrs={
        #     'class': 'js-example-basic-multiple col-sm-12',
        #     'placeholder': 'Enter Your Name',
        #     'multiple': 'multiple',
        # })
    }


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ['status']

        widgets = {
            'status': forms.Select(attrs={
            'placeholder':'Task status',
            'class':'form-control',
        })
        }


class LanguageCourseForm(forms.ModelForm):
    class Meta:
        model = LanguageCourse
        fields = ['title', 'fee', 'schedule', 'seats',
                  'teacher', 'duration', 'books']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter Course Name',
                'class': 'form-control'
            }),
            'fee': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]+',
                'placeholder': 'Enter fee ',
            }),
            'schedule': forms.Textarea(attrs={
                'placeholder': 'Schedule of language course',
                'class': 'form-control'
            }),
            'seats': forms.Select(attrs={
                'placeholder': 'seat',
                'class': 'js-example-basic-single',
            }),
            'teacher': forms.Select(attrs={
                'placeholder': 'teacher',
                'class': 'js-example-basic-single',
            }),
            'duration': forms.TextInput(attrs={
                'placeholder': 'duration in months',
                'pattern': '[0-9]+',
                'class': 'form-control'
            }),
            'books': forms.TextInput(attrs={
                'placeholder': 'Name of the book if avaliable',
                'class': 'form-control'
            })

        }


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'email', 'about', 'address', 'country', 'deadline', 'relation',
                  'requirements', 'contact_person', 'term', 'phone', 'features', 'scholarship', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter University name',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter University email',
                'class': 'form-control'
            }),
            'about': forms.Textarea(attrs={
                'placeholder': 'Enter Informations of University ',
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Enter University address',
                'class': 'form-control'
            }),
            'country': forms.Select(attrs={
                'class': 'js-example-basic-single',
                'placeholder': 'Enter Country',
            }),
            'requirements': forms.Textarea(attrs={
                'placeholder': 'Enter admission requirement',
                'class': 'form-control'
            }),
            'deadline': forms.DateInput(attrs={
                'id': 'id_due_date',
                'placeholder': 'Enter deadline',
            }),
            'relation': forms.Select(attrs={
                'placeholder': 'Enter Choice',
                'class': 'js-example-basic-single',
            }),
            'contact_person': forms.Textarea(attrs={
                'placeholder': 'Enter Detail of contact Person',
                'class': 'form-control'
            }),
            'term': forms.Select(attrs={
                'placeholder': 'Term',
                'class': 'js-example-basic-single',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter Contact Number',
                'pattern':'[0-9]+',
                'class': 'form-control'
            }),
            'features': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter University Features',
            }),
            'scholarship': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter University Scholarship Scheme',
            }),
            'image': forms.ClearableFileInput(attrs={
                'placeholder': 'Enter University Image',
            })


        }


class CourseForm(forms.ModelForm):
    university = forms.ModelMultipleChoiceField(queryset=University.objects.all(), widget = forms.SelectMultiple(attrs={
        'class':'js-example-basic-multiple',
        'multiple':'multiple'
        }))
    class Meta:
        model = Course
        fields = ['title', 'fee_structure', 'university', 'about']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter Course title',
                'class': 'form-control'
            }),
            'fee_structure': forms.TextInput(attrs={
                'placeholder': 'Enter Course fee ',
                'pattern': '[0-9]+',
                'class': 'form-control',
            }),
            'about': forms.Textarea(attrs={
                'placeholder': 'Enter details of course ',
                'class': 'form-control'
            })
        }
