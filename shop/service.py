from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout


from .forms import LoginForm, RegisterForm, ReviewForm
from .models import Product


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.name = request.user
            form.email = request.user.email
            form.save()
        return redirect(product.get_absolute_url())


def register(request):
    """Регистрация"""

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'EEEE регистрация')
            return redirect('register')
        else:
            messages.error(request, 'Какая-то обшибка')

    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})


def user_login(request):
    """Вход в аккаунт"""

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'shop/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# class RegisterUser(CreateView):
#     """Регистрация пользователя"""
#     form_class = RegisterForm
#     template_name = 'shop/register.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('index')


# class LoginUser(LoginView):
#     """Авторизация пользователя"""

#     form_class = LoginForm
#     template_name = 'shop/login.html'

#     def get_success_url(self) -> str:
#         return reverse_lazy('index')
