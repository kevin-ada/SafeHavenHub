from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'components/index.html'


class SignUpView(TemplateView):
    template_name = 'components/signup.html'


class SignInView(TemplateView):
    template_name = 'components/sign_in.html'
