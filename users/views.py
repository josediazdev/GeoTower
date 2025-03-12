from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    """
    Vista para el registro de nuevos usuarios.

    Maneja las solicitudes POST para crear nuevos usuarios y muestra el formulario de registro.

    Returns:
        Si la solicitud es POST y el formulario es válido, redirige a la página de inicio de sesión.
        De lo contrario, renderiza la página de registro con el formulario.
    """

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # Crea una instancia del formulario UserRegisterForm con los datos de la solicitud POST.

        if form.is_valid():
            # Verifica si los datos del formulario son válidos.

            form.save()
            # Guarda el nuevo usuario en la base de datos.

            username = form.cleaned_data.get('username')
            # Obtiene el nombre de usuario del formulario limpio.

            messages.success(request, f'Your account {username} was created successfully!')

            return redirect('users-login')
            # Redirige al usuario a la página de inicio de sesión.

    else:
        form = UserRegisterForm()
        # Crea una instancia vacía del formulario UserRegisterForm.

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Vista para mostrar y actualizar el perfil de usuario.

    Maneja las solicitudes GET y POST para mostrar y actualizar la información del perfil del usuario.

    Returns:
        Si la solicitud es POST y los formularios son válidos, actualiza el perfil y redirige.
        De lo contrario, renderiza la página de perfil con los formularios.
    """
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Crea una instancia del formulario UserUpdateForm con los datos POST
        # y la instancia del usuario actual.

        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # Crea una instancia del formulario ProfileUpdateForm con los datos POST
        # los archivos subidos y la instancia del perfil del usuario.

        if u_form.is_valid() and p_form.is_valid():
            # Verifica si ambos formularios son válidos.

            u_form.save()
            # Guarda los cambios en el formulario de usuario.

            p_form.save()
            # Guarda los cambios en el formulario de perfil.

            messages.success(request, f'Your account was updated successfully!')
            
            return redirect('users-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        # Crea una instancia del formulario UserUpdateForm con la instancia del
        # usuario actual para mostrar los datos existentes.

        p_form = ProfileUpdateForm(instance=request.user.profile)
        # Crea una instancia del formulario ProfileUpdateForm con la instancia del
        # perfil del usuario actual para mostrar los datos existentes.

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile',
    }

    return render(request, 'users/profile.html', context)
