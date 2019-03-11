from django.urls import path, include
from .views import *
from .models import *
app_name = 'cmsapp'


urlpatterns = [

    # Bachelor Pass nabhako bharabhuri haru ko lagi
    path('consultant/create/', AjaxLeadCourseSelectView.as_view(),
         name='courseajax'),

    path('receptionist/registration/', ReceptionistRegistrationView.as_view(),
         name='receptionistregistration'),
    path('student/registration/', StudentRegistrationView.as_view(),
         name='studentregistration'),
    path('teacher/registration/', TeacherRegistrationView.as_view(),
         name='teacherregistration'),
    path('consultant/registration/', ConsultantRegistrationView.as_view(),
         name='consultantregistration'),
    path('lead/registration/', LeadRegistrationView.as_view(),
         name='leadregistration'),
    path('visitor/registration/', VisitorRegistrationView.as_view(),
         name='visitorregistration'),
    path('admin/registration/', AdminRegistrationView.as_view(),
         name='adminregistration'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # admin panel urls

    path('adminpanel/', AdminPanelView.as_view(), name='adminpanel'),
    path('admin/list/', AdminListView.as_view(), name='adminlist'),
    path('adminconsultant/list/', AdminConsultantListView.as_view(),
         name='adminconsultantlist'),
    path('adminlead/list/', AdminLeadListView.as_view(),
         name='adminleadlist'),
    path('adminteacher/list/', AdminTeacherListView.as_view(),
         name='adminteacherlist'),
    path('adminreceptionist/list/', AdminReceptionistListView.as_view(),
         name='adminreceptionistlist'),
    path('adminstudent/list/', AdminStudentListView.as_view(),
         name='adminstudentlist'),
    path('adminvisitor/list/', AdminVisitorListView.as_view(),
         name='adminvisitorlist'),
    path('admintask/list/', AdminTaskListView.as_view(),
         name='admintasklist'),
    path('adminappointment/list/', AdminAppointmentListView.as_view(),
         name='adminappointmentlist'),
    path('adminfeed/list/', AdminFeedListView.as_view(),
         name='adminfeedlist'),
    path('adminuniversity/list/', AdminUniversityListView.as_view(),
         name='adminuniversitylist'),
    path('admincourse/list/', AdminCourseListView.as_view(),
         name='admincourselist'),
    path('task/status/update/', TaskStatusView.as_view(),
         name='taskstatusupdate'),
    path('adminactivity/list/', AdminActivityListView.as_view(),
         name='adminactivitylist'),

    
    # adminpanel feed create views

    path('adminfeed/create/', AdminFeedCreateView.as_view(), name='adminfeedcreate'),
    path('adminfeed/<int:pk>/comment/create/',
         AdminFeedCommentCreateView.as_view(), name='adminfeedcommentcreate'),
    path('adminfeed/<int:pk>/delete/',
         AdminFeedDeleteView.as_view(), name='adminfeeddelete'),
    path('adminfeed/<int:pk1>/comment/<int:pk2>/delete/',
         AdminFeedCommentDeleteView.as_view(), name='adminfeedcommentdelete'),

    # adminpanel detail views urls

    path('adminconsultant/<int:pk>/detail/',
         AdminConsultantDetailView.as_view(), name='adminconsultantdetail'),
    path('adminreceptionist/<int:pk>/detail/',
         AdminReceptionistDetailView.as_view(), name='adminreceptionistdetail'),
    path('adminstudent/<int:pk>/detail/',
         AdminStudentDetailView.as_view(), name='adminstudentdetail'),
    path('adminlead/<int:pk>/detail/',
         AdminLeadDetailView.as_view(), name='adminleaddetail'),
    path('adminteacher/<int:pk>/detail/',
         AdminTeacherDetailView.as_view(), name='adminteacherdetail'),

    # admin create views urls
    path('adminteacher/registration/', AdminTeacherRegistrationView.as_view(),
         name='adminteacherregistration'),
    path('adminreceptionist/registration/', AdminReceptionistRegistrationView.as_view(),
         name='adminreceptionistregistration'),
    path('adminstudent/registration/', AdminStudentRegistrationView.as_view(),
         name='adminstudentregistration'),
    path('admintask/create/', AdminTaskCreateView.as_view(),
         name='admintaskcreate'),
    path('adminuniversity/create/', AdminUniversityCreateView.as_view(),
         name='adminuniversitycreate'),
    path('admincourse/create/', AdminCourseCreateView.as_view(),
         name='admincoursecreate'),
    path('adminlead/create/', AdminLeadRegistrationView.as_view(),
         name='adminleadregistration'),

    # adminpanel update views urls
    path('consultant/<int:pk>/update', ConsultantUpdateView.as_view(),
         name='consultantupdate'),
    path('admin/<int:pk>/update', AdminUpdateView.as_view(), name='adminupdate'),
    path('adminlead/<int:pk>/update', AdminLeadUpdateView.as_view(),
         name='adminleadupdate'),
    path('adminteacher/<int:pk>/update', AdminTeacherUpdateView.as_view(),
         name='adminteacherupdate'),
    path('adminreceptionist/<int:pk>/update', AdminReceptionistUpdateView.as_view(),
         name='adminreceptionistupdate'),
    path('adminstudent/<int:pk>/update', AdminStudentUpdateView.as_view(),
         name='adminstudentupdate'),
    path('adminuniversity/<int:pk>/update', AdminUniversityUpdateView.as_view(),
         name='adminuniversityupdate'),
    path('admincourse/<int:pk>/update', AdminCourseUpdateView.as_view(),
         name='admincourseupdate'),



    # adminpanel delete views url
    path('adminconsultant/<int:pk>/delete',
         AdminConsultantDeleteView.as_view(), name='adminconsultantdelete'),
    path('adminlead/<int:pk>/delete',
         AdminLeadDeleteView.as_view(), name='adminleaddelete'),
    path('adminteacher/<int:pk>/delete',
         AdminTeacherDeleteView.as_view(), name='adminteacherdelete'),
    path('adminreceptionist/<int:pk>/delete',
         AdminReceptionistDeleteView.as_view(), name='adminreceptionistdelete'),
    path('adminstudent/<int:pk>/delete',
         AdminStudentDeleteView.as_view(), name='adminstudentdelete'),
    path('adminvisitor/<int:pk>/delete',
         AdminVisitorDeleteView.as_view(), name='adminvisitordelete'),
    path('admintask/<int:pk>/delete',
         AdminTaskDeleteView.as_view(), name='admintaskdelete'),
    path('adminactivity/<int:pk>/delete',
         AdminActivityDeleteView.as_view(), name='adminactivitydelete'),
    path('adminuniversity/<int:pk>/delete',
         AdminUniversityDeleteView.as_view(), name='adminuniversitydelete'),
    path('admincourse/<int:pk>/delete',
         AdminCourseDeleteView.as_view(), name='admincoursedelete'),





    # student panel urls

    path('studentpanel/', StudentPanelView.as_view(), name='studentpanel'),
    path('studentteacher/list/', StudentTeacherListView.as_view(),
         name='studentteacherlist'),
    path('studentreceptionist/list/', StudentReceptionistListView.as_view(),
         name='studentreceptionistlist'),

    # studentpanel details urls

    path('student/<int:pk>/detail/',
         StudentDetailView.as_view(), name='studentdetail'),

    # studentpanel feed create views

    path('studentfeed/create/', StudentFeedCreateView.as_view(),
         name='studentfeedcreate'),
    path('studentfeed/<int:pk>/comment/create/',
         StudentFeedCommentCreateView.as_view(), name='studentfeedcommentcreate'),
    path('studentfeed/<int:pk>/delete/',
         StudentFeedDeleteView.as_view(), name='studentfeeddelete'),
    path('studentfeed/<int:pk1>/comment/<int:pk2>/delete/',
         StudentFeedCommentDeleteView.as_view(), name='studentfeedcommentdelete'),


    # teacher panel urls

    path('teacherpanel/', TeacherPanelView.as_view(), name='teacherpanel'),
    path('teacherconsultant/list/', TeacherConsultantListView.as_view(),
         name='teacherconsultantlist'),
    path('teacher/list/', TeacherListView.as_view(),
         name='teacherlist'),
    path('teacherreceptionist/list/', TeacherReceptionistListView.as_view(),
         name='teacherreceptionistlist'),
    path('teacherstudent/list/', TeacherStudentListView.as_view(),
         name='teacherstudentlist'),
    path('teachertask/list/', TeacherTaskListView.as_view(),
         name='teachertasklist'),
    path('teacheruniversity/list/', TeacherUniversityListView.as_view(),
         name='teacheruniversitylist'),
    path('teacherfeed/list/', TeacherFeedListView.as_view(), name='teacherfeedlist'),
    path('teacherstudymaterials/list/',
         TeacherStudyMaterialsListView.as_view(), name='teacherstudymaterialslist'),

    # teacherpanel feed create views

    path('teacherfeed/create/', TeacherFeedCreateView.as_view(),
         name='teacherfeedcreate'),
    path('teacherfeed/<int:pk>/comment/create/',
         TeacherFeedCommentCreateView.as_view(), name='teacherfeedcommentcreate'),
    path('teacherfeed/<int:pk>/delete/',
         TeacherFeedDeleteView.as_view(), name='teacherfeeddelete'),
    path('teacherfeed/<int:pk1>/comment/<int:pk2>/delete/',
         TeacherFeedCommentDeleteView.as_view(), name='teacherfeedcommentdelete'),


    # teacherpanel details views urls

    path('teacher/<int:pk>/detail/',
         TeacherDetailView.as_view(), name='teacherdetail'),
    path('teacherstudent/<int:pk>/detail/',
         TeacherStudentDetailView.as_view(), name='teacherstudentdetail'),

    # teacherpanel create views urls

    path('teacherstudymaterials/create/',
         TeacherStudyMaterialsCreateView.as_view(), name='teacherstudymaterialscreate'),

    # teacherpanel update views urls
    path('teacherstudymaterials/<int:pk>/update/',
         TeacherStudyMaterialsUpdateView.as_view(), name='teacherstudymaterialsupdate'),

    # teacherpanel delete views urls
    path('teacherstudymaterials/<int:pk>/delete/',
         TeacherStudyMaterialsDeleteView.as_view(), name='teacherstudymaterialsdelete'),


    # consultant list view urls
    path('consultantpanel/', ConsultantPanelView.as_view(), name='consultantpanel'),
    path('consultant/list/', ConsultantListView.as_view(),
         name='consultantlist'),
    path('consultant/documentlist/', ConsultantDocumentListView.as_view(),
         name='consultantdocumentlist'),
    path('consultantlead/list/', ConsultantLeadListView.as_view(),
         name='consultantleadlist'),
    path('consultantteacher/list/', ConsultantTeacherListView.as_view(),
         name='consultantteacherlist'),
    path('consultantreceptionist/list/', ConsultantReceptionistListView.as_view(),
         name='consultantreceptionistlist'),
    path('consultantstudent/list/', ConsultantStudentListView.as_view(),
         name='consultantstudentlist'),
    path('consultantvisitor/list/', ConsultantVisitorListView.as_view(),
         name='consultantvisitorlist'),
    path('consultanttask/list/', ConsultantTaskListView.as_view(),
         name='consultanttasklist'),
    path('consultantappointment/list/', ConsultantAppointmentListView.as_view(),
         name='consultantappointmentlist'),
    path('consultantfeed/list/', ConsultantFeedListView.as_view(),
         name='consultantfeedlist'),
    path('consultantcourse/list/', ConsultantCourseListView.as_view(),
         name='consultantcourselist'),
    path('consultantuniversity/list/', ConsultantUniversityListView.as_view(),
         name='consultantuniversitylist'),
    path('consultantactivity/list/', ConsultantActivityListView.as_view(),
         name='consultantactivitylist'),


    # consultant create view urls
    path('consultanttask/create/', ConsultantTaskCreateView.as_view(),
         name='consultanttaskcreate'),
    path('consultantappointment/create/', ConsultantAppointmentCreateView.as_view(),
         name='consultantappointmentcreate'),
    path('consultant/lead/<int:lead_pk>/document/create/', ConsultantDocumentCreateView.as_view(),
         name='consultantdocumentcreate'),
    path('consultantuniversity/create/', ConsultantUniversityCreateView.as_view(),
         name='consultantuniversitycreate'),
    path('consultantcourse/create/', ConsultantCourseCreateView.as_view(),
         name='consultantcoursecreate'),
    path('consultantactivity/create/', ConsultantActivityCreateView.as_view(),
         name='consultantactivitycreate'),


    # consultant update view urls
    path('consultanttask/<int:pk>/update/',
         ConsultantTaskUpdateView.as_view(), name='consultanttaskupdate'),
    path('consultantappointment/<int:pk>/update/',
         ConsultantAppointmentUpdateView.as_view(), name='consultantappointmentupdate'),
    path('consultantlead/<int:pk>/update/',
         ConsultantLeadUpdateView.as_view(), name='consultantleadupdate'),
    path('consultantdocument/<int:pk>/update/',
         ConsultantDocumentUpdateView.as_view(), name='consultantdocumentupdate'),
    path('consultantcourse/<int:pk>/update/',
         ConsultantCourseUpdateView.as_view(), name='consultantcourseupdate'),
    path('consultantuniversity/<int:pk>/update/',
         ConsultantUniversityUpdateView.as_view(), name='consultantuniversityupdate'),
    path('consultantactivity/<int:pk>/update/',
         ConsultantActivityUpdateView.as_view(), name='consultantactivityupdate'),


    # consultant delete view urls
    path('consultanttask/<int:pk>/delete/',
         ConsultantTaskDeleteView.as_view(), name='consultanttaskdelete'),
    path('consultantappointment/<int:pk>/delete/',
         ConsultantAppointmentDeleteView.as_view(), name='consultantappointmentdelete'),

    path('consultantdocument/<int:pk>/delete/',
         ConsultantDocumentDeleteView.as_view(), name='consultantdocumentdelete'),


    # consultantpanel feed create views

    path('consultantfeed/create/', ConsultantFeedCreateView.as_view(),
         name='consultantfeedcreate'),
    path('consultantfeed/<int:pk>/comment/create/',
         ConsultantFeedCommentCreateView.as_view(), name='consultantfeedcommentcreate'),
    path('consultantfeed/<int:pk>/delete/',
         ConsultantFeedDeleteView.as_view(), name='consultantfeeddelete'),
    path('consultantfeed/<int:pk1>/comment/<int:pk2>/delete/',
         ConsultantFeedCommentDeleteView.as_view(), name='consultantfeedcommentdelete'),


    # consultantpanel detail views urls
    path('consultant/<int:pk>/detail/',
         ConsultantDetailView.as_view(), name='consultantdetail'),
    path('consultantstudent/<int:pk>/detail/',
         ConsultantStudentDetailView.as_view(), name='consultantstudentdetail'),
    path('consultantlead/<int:pk>/detail/',
         ConsultantLeadDetailView.as_view(), name='consultantleaddetail'),
    path('consultantvisitor/<int:pk>/detail/',
         ConsultantVisitorDetailView.as_view(), name='consultantvisitordetail'),
    path('consultantuniversity/<int:pk>/detail/',
         ConsultantUniversityDetailView.as_view(), name='consultantuniversitydetail'),
    path('consultanttask/<int:pk>/detail/',
         ConsultantTaskDetailView.as_view(), name='consultanttaskdetail'),

    # receptionist panel urls
    path('receptionistpanel/', ReceptionistPanelView.as_view(),
         name='receptionistpanel'),
    path('receptionist/list/', ReceptionistListView.as_view(),
         name='receptionistlist'),
    path('receptionistconsultant/list/', ReceptionistConsultantListView.as_view(),
         name='receptionistconsultantlist'),
    path('receptionistlead/list/', ReceptionistLeadListView.as_view(),
         name='receptionistleadlist'),
    path('receptionistteacher/list/', ReceptionistTeacherListView.as_view(),
         name='receptionistteacherlist'),
    path('receptionist/list/', ReceptionistListView.as_view(),
         name='receptionistlist'),
    path('receptioniststudent/list/', ReceptionistStudentListView.as_view(),
         name='receptioniststudentlist'),
    path('receptionistvisitor/list/', ReceptionistVisitorListView.as_view(),
         name='receptionistvisitorlist'),
    path('receptionisttask/list/', ReceptionistTaskListView.as_view(),
         name='receptionisttasklist'),
    path('receptionistappointment/list/', ReceptionistAppointmentListView.as_view(),
         name='receptionistappointmentlist'),
    path('receptionistfeed/list/', ReceptionistFeedListView.as_view(),
         name='receptionistfeedlist'),
    path('receptionistuniversity/list/', ReceptionistUniversityListView.as_view(),
         name='receptionistuniversitylist'),
    path('receptionistcourse/list/', ReceptionistCourseListView.as_view(),
         name='receptionistcourselist'),
    path('receptionistlanguagecourse/list/', ReceptionistLanguageCourseListView.as_view(),
         name='receptionistlanguagecourselist'),


    # receptionistpanel create views

    path('receptionistfeed/create/', ReceptionistFeedCreateView.as_view(),
         name='receptionistfeedcreate'),
    path('receptionistfeed/<int:pk>/comment/create/',
         ReceptionistFeedCommentCreateView.as_view(), name='receptionistfeedcommentcreate'),
    path('receptionistuniversity/create/',
         ReceptionistUniversityCreateView.as_view(), name='receptionistuniversitycreate'),
    path('receptionistcourse/create/', ReceptionistCourseCreateView.as_view(),
         name='receptionistcoursecreate'),
    # path('receptioniststudent/create/', ReceptionistStudentCreateView.as_view(),
    #      name='receptioniststudentcreate'),
    path('receptionistvisitor/create/', ReceptionistVisitorCreateView.as_view(),
         name='receptionistvisitorcreate'),
    path('receptionistlanguagecourse/create/', ReceptionistLanguageCourseCreateView.as_view(),
         name='receptionistlanguagecoursecreate'),
    path('receptionisttask/create/', ReceptionistTaskCreateView.as_view(),
         name='receptionisttaskcreate'),
    path('receptionistappointment/create/', ReceptionistAppointmentCreateView.as_view(),
         name='receptionistappointmentcreate'),
    path('receptionistlead/create/', ReceptionistLeadCreateView.as_view(),
         name='receptionistleadcreate'),

    # receptionistpanel detail views urls

    path('receptionist/<int:pk>/detail/',
         ReceptionistDetailView.as_view(), name='receptionistdetail'),
    path('receptionistconsultant/<int:pk>/detail/',
         ReceptionistConsultantDetailView.as_view(), name='receptionistconsultantdetail'),
    path('receptionistvisitor/<int:pk>/detail/',
         ReceptionistVisitorDetailView.as_view(), name='receptionistvisitordetail'),
    path('receptioniststudent/<int:pk>/detail/',
         ReceptionistStudentDetailView.as_view(), name='receptioniststudentdetail'),
    path('receptionistlead/<int:pk>/detail/',
         ReceptionistLeadDetailView.as_view(), name='receptionistleaddetail'),
    path('receptionistteacher/<int:pk>/detail/',
         ReceptionistTeacherDetailView.as_view(), name='receptionistteacherdetail'),
    path('receptionistcourse/<int:pk>/detail/',
         ReceptionistCourseDetailView.as_view(), name='receptionistcoursedetail'),


    #receptionist delete view
    path('receptionistcourse/<int:pk>/delete/',
         ReceptionistCourseDeleteView.as_view(), name='receptionistcoursedelete'),
    path('receptionistuniversity/<int:pk>/delete/',
         ReceptionistUniversityDeleteView.as_view(), name='receptionistuniversitydelete'),
    path('receptioniststudent/<int:pk>/delete/',
         ReceptionistStudentDeleteView.as_view(), name='receptioniststudentdelete'),
    path('receptionistvisitor/<int:pk>/delete/',
         ReceptionistVisitorDeleteView.as_view(), name='receptionistvisitordelete'),
    path('receptionistlangugagecourse/<int:pk>/delete/',
         ReceptionistLanguageCourseDeleteView.as_view(), name='receptionistlanguagecoursedelete'),
    path('receptionistfeed/<int:pk>/delete/',
         ReceptionistFeedDeleteView.as_view(), name='receptionistfeeddelete'),
    path('receptionistfeed/<int:pk1>/comment/<int:pk2>/delete/',
         ReceptionistFeedCommentDeleteView.as_view(), name='receptionistfeedcommentdelete'),
    path('receptionisttask/<int:pk>/delete/',
         ReceptionistTaskDeleteView.as_view(), name='receptionisttaskdelete'),
    path('receptionistappointment/<int:pk>/delete/',
         ReceptionistAppointmentDeleteView.as_view(), name='receptionistappointmentdelete'),
    path('receptionistlead/<int:pk>/delete/',
         ReceptionistLeadDeleteView.as_view(), name='receptionistleaddelete'),

    # receptionistpanel update views urls
    path('receptionistcourse/<int:pk>/update/',
         ReceptionistCourseUpdateView.as_view(), name='receptionistcourseupdate'),
    path('receptionistappointment/<int:pk>/update/',
         ReceptionistAppointmentUpdateView.as_view(), name='receptionistappointmentupdate'),
    path('receptionistuniversity/<int:pk>/update/',
         ReceptionistUniversityUpdateView.as_view(), name='receptionistuniversityupdate'),
    path('receptioniststudent/<int:pk>/update/',
         ReceptionistStudentUpdateView.as_view(), name='receptioniststudentupdate'),
    path('receptionistvisitor/<int:pk>/update/',
         ReceptionistVisitorUpdateView.as_view(), name='receptionistvisitorupdate'),
    path('receptionistlanguagecourse/<int:pk>/update/',
         ReceptionistLanguageCourseUpdateView.as_view(), name='receptionistlanguagecourseupdate'),
    path('receptionisttask/<int:pk>/update/',
         ReceptionistTaskUpdateView.as_view(), name='receptionisttaskupdate'),
    path('receptionistlead/<int:pk>/update', ReceptionistLeadUpdateView.as_view(),
         name='receptionistleadupdate'),






    # lead panel urls

    path('leadpanel/', LeadPanelView.as_view(), name='leadpanel'),
    path('leadreceptionist/list/', LeadReceptionistListView.as_view(),
         name='leadreceptionistlist'),
    path('leadconsultant/list/', LeadConsultantListView.as_view(),
         name='leadconsultantlist'),
    path('leaddocument/list/', LeadDocumentListView.as_view(),
         name='leaddocumentlist'),
    path('leadfeed/list', LeadFeedListView.as_view(),
         name='leadfeedlist'),

    # leadpanel feed create views

    path('leadfeed/create/', LeadFeedCreateView.as_view(),
         name='leadfeedcreate'),
    path('leadfeed/<int:pk>/comment/create/',
         LeadFeedCommentCreateView.as_view(), name='leadfeedcommentcreate'),
    path('leadfeed/<int:pk>/delete/',
         LeadFeedDeleteView.as_view(), name='leadfeeddelete'),
    path('leadfeed/<int:pk1>/comment/<int:pk2>/delete/',
         LeadFeedCommentDeleteView.as_view(), name='leadfeedcommentdelete'),

    # leadpanel detail views urls




    # path('passwordchange/', PasswordChangeView.as_view(), name='passwordchange'),
    path('admin/<int:pk>/passwordchange/', AdminPasswordChangeView.as_view(),
         name='adminpasswordchange'),
    path('receptionist/<int:pk>/passwordchange/', ReceptionistPasswordChangeView.as_view(),
         name='receptionistpasswordchange'),
    path('consultant/<int:pk>/passwordchange/', ConsultantPasswordChangeView.as_view(),
         name='consultantpasswordchange'),
    path('teacher/<int:pk>/passwordchange/', TeacherPasswordChangeView.as_view(),
         name='teacherpasswordchange'),
    path('lead/<int:pk>/passwordchange/', LeadPasswordChangeView.as_view(),
         name='leadpasswordchange'),
    path('student/<int:pk>/passwordchange/', StudentPasswordChangeView.as_view(),
         name='studentpasswordchange'),


    # Appointment

    path('appointment/create/',
         AppointmentCreateView.as_view(), name='appointmentcreate'),
    path('appointment/list/', AppointmentListView.as_view(), name='appointmentlist'),
    path('appointment/<int:pk>/detail/',
         AppointmentDetailView.as_view(), name='appointmentdetail'),
    path('appointment/<int:pk>/update/',
         AppointmentUpdateView.as_view(), name='appointmentupdate'),
    path('appointment/<int:pk>/delete/',
         AppointmentDeleteView.as_view(), name='appointmentdelete'),
    # Task
    path('task/board/', TaskBoardView.as_view(), name='taskboard'),
    path('task/list/', TaskListView.as_view(), name='tasklist'),
    path('task/<int:pk>/detail/', TaskDetailView.as_view(), name='taskdetail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='taskupdate'),
    path('task/<int:pk>/delete/',
         TaskDeleteView.as_view(), name='taskdelete'),


    path('message/list/', MessageListView.as_view(), name='messagelist'),
    path('language/course/create/',
         LanguageCourseCreateView.as_view(), name='languagecoursecreate'),
    path('language/course/list/', LanguageCourseListView.as_view(),
         name='languagecourselist'),
    path('university/create/', UniversityCreateView.as_view(),
         name='universitycreate'),
    # University
    path('university/list/', UniversityListView.as_view(), name='universitylist'),
    path('university/create/', UniversityCreateView.as_view(),
         name='universitycreate'),
    path('university/<int:pk>/detail/',
         UniversityDetailView.as_view(), name='universitydetail'),
    path('university/<int:pk>/update/',
         UniversityUpdateView.as_view(), name='universityupdate'),
    path('university/<int:pk>/delete/',
         UniversityDeleteView.as_view(), name='universitydelete'),


    path('student/list/', StudentListView.as_view(), name='studentlist'),
    path('teacher/list/', TeacherListView.as_view(), name='teacherlist'),
    path('reception/list/', ReceptionListView.as_view(), name='receptionlist'),
    path('lead/list/', LeadListView.as_view(), name='leadlist'),
    path('consultant/list/', ConsultantListView.as_view(), name='consultantlist'),
    path('admin/list/', AdminListView.as_view(), name='adminlist'),
    path('visitor/list/', VisitorListView.as_view(), name='visitorlist'),
    path('admin/<int:pk>/detail/',
         AdminDetailView.as_view(), name='admindetail'),
    path('lead/<int:pk>/detail/',
         LeadDetailView.as_view(), name='leaddetail'),

    # courses
    path('course/list/', CourseListView.as_view(), name='courselist'),
    path('course/create/', CourseCreateView.as_view(),
         name='coursecreate'),
    path('course/<int:pk>/detail/',
         CourseDetailView.as_view(), name='coursedetail'),
    path('course/<int:pk>/update/',
         CourseUpdateView.as_view(), name='courseupdate'),
    path('course/<int:pk>/delete/',
         CourseDeleteView.as_view(), name='coursedelete'),

]
