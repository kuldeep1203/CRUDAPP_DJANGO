from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from aimals import views as aimals_views 
from lineage import views as lineage_views
from habitat import views as habitat_views
from health import views as health_views
from migration import views as migration_views
from transfers import views as transfers_views

from django.views.i18n import JavaScriptCatalog
urlpatterns = [
    
    path('admin/',admin.site.urls),
    #path('lhome/',lineage_views.ho,name='lhome'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('',include('front.urls')),
    path('insert/',aimals_views.animals_insert,name='insert'),
    path('homepage/',include('front.urls')),
    path("homehabitat/",habitat_views.habitat_record,name="homehabitat"),
    path('habitatinsert/',habitat_views.habitat_create,name='habitatinsert.html'),
    path('update_health/<int:pk>/',health_views.health_update,name='update_health'),
    path('update_lineage/<int:pk>/',lineage_views.lineage_update,name='update_lineage'),
    #path('lhome/',lineage_views.line,name='lhome'),
    path('updatetransfer/<int:pk>/',transfers_views.transferupdate,name='updatetransfer'),
    path('update_migration/<int:pk>/',migration_views.migration_update,name='update_migration'),
    path('fauna/',aimals_views.fauna,name='fauna'),
    path('fauna/<int:pk>',aimals_views.animals_record,name='animal'),
    path('delete_fauna/<int:pk>',aimals_views.animals_delete,name='delete_fauna'),
    path('update_fauna/<int:pk>',aimals_views.animals_update,name='update_fauna'),
    path('searchfauna/',aimals_views.search_fauna,name='searchfauna'),
    path('update_habitat/<int:pk>',habitat_views.habitat_update,name='update_habitat'),
    path('searchhabitat/',habitat_views.search_habitat,name='searchhabitat'),
    path("homehabitat/<int:pk>",habitat_views.habitat_search,name="habitat"),
    path("delete_habitat/<int:pk>",habitat_views.habitat_Delete,name='delete_habitat'),
]   
admin.site.site_header="ABC Admin"
admin.site.site_title="ABC Admin"
admin.site.index_title="WELCOME TO THE ADMIN AREA"