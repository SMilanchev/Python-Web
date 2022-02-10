from django.urls import path

from templates_advanced.pythons_auth.views import sign_in, sign_out, sign_up, SignUpView, SignInView

urlpatterns = [
    # path('sign-up/', sign_up, name='sign up'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', sign_out, name='sign out')
]