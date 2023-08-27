
from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, VerificationView, UserUpdateView , RestorePasswordView, UserListView, UserDeleteView, ChangeUserActiveView, ChangeUserStaffView

app_name = UsersConfig.name


# urlpatterns = [
#     path('', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('verification/<int:pk>/<int:key>', VerificationView, name='verification'),
#     path('profile/', UserUpdateView.as_view(), name='profile'),
#     path('restore_password/', RestorePasswordView.as_view(), name='restore_password'),
# ]

urlpatterns = [
    # path('', LoginView.as_view(), name='login'),
    # path('profile/', UserUpdateView.as_view(), name='profile'),
    path('<str:section>/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('<str:section>/users_list/', UserListView.as_view(), name='user_list'),
    path('<str:section>/delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
    path('<str:section>/change_active/<int:pk>', ChangeUserActiveView.as_view(), name='change_active'),
    path('<str:section>/change_staff/<int:pk>', ChangeUserStaffView.as_view(), name='change_staff'),
    path('<str:section>/logout/', LogoutView.as_view(), name='logout'),
    path('<str:section>/register/', RegisterView.as_view(), name='register'),
    path('<str:section>/verification/<int:pk>/<int:key>', VerificationView, name='verification'),
    path('<str:section>/profile/', UserUpdateView.as_view(), name='profile'),
    path('<str:section>/restore_password/', RestorePasswordView.as_view(), name='restore_password'),
]