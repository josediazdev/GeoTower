from django.contrib.auth.views import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Question, Response
from .forms import ResponseForm
from django.contrib import messages
from django.views.generic import (
        ListView, 
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    ordering = ['-date_posted']
    paginate_by = 3


class UserQuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'forum/user_question_list.html'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Question.objects.filter(author=user).order_by('-date_posted')


@login_required
def QuestionDetail(request, question_id):

    question = get_object_or_404(Question, id=question_id)
    
    responses = Response.objects.filter(base_question=question_id)
    # Generamos las respuestas disponibles en función del ID de la pregunta para renderizarlas

    if request.method == "POST":
        form = ResponseForm(request.POST)

        if form.is_valid():
            form.instance.author = request.user
            # Asigna el usuario actual como el autor de la respuesta.

            form.instance.base_question = question
            # Asigna la pregunta base a la cual pertenece la respuesta.

            form.save()

            messages.success(request, 'Answer posted successfully')
            return redirect('forum:question-detail-response', question_id)

    else:
        form = ResponseForm()

    context = {'question': question, 'form': form, 'responses': responses}

    return render(request, 'forum/question_detail_response.html', context)


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):

    model = Question

    fields = ["question", "description"]

    def form_valid(self, form):
        """
        Sobreescribe el método form_valid para asignar el autor de la pregunta.

        Args:
            form: El formulario enviado.

        Returns:
            El resultado del método form_valid de la clase padre.
        """
        form.instance.author = self.request.user
        # Asigna el usuario actual como el autor de la pregunta.

        return super().form_valid(form)
        # Llama al método form_valid de la clase padre para guardar la pregunta.


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Question

    fields = ["question", "description"]


    def test_func(self):
        """
        Verifica si el usuario actual es el autor de la pregunta.

        Returns:
            True si el usuario es el autor, False en caso contrario.
        """
        question = self.get_object()
        # Obtiene la pregunta que se va a actualizar.

        if self.request.user == question.author:
            # Verifica si el usuario actual es el autor de la pregunta.

            return True
        return False
        # Si el usuario no es el autor, devuelve False, impidiendo la actualización.


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = "/forum/"
    # Especifica la URL a la que se redirigirá al usuario después de eliminar la pregunta.

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


@login_required
def DeleteResponse(request, response_id):
    """
    Elimina una respuesta específica y redirige al usuario a la página de detalles de la pregunta.

    Args:
        response_id: El ID de la respuesta que se va a eliminar.

    Returns:
        Si la solicitud es POST, redirige a la página de detalles de la pregunta.
        De lo contrario, renderiza la página de confirmación de eliminación.
    """
    response = get_object_or_404(Response, id=response_id)

    question = get_object_or_404(Question, id=response.base_question.id)
    # Obtiene la pregunta asociada a la respuesta, o devuelve error 404 si no existe.

    if request.method == "POST":
        response.delete()
        # Elimina la respuesta de la base de datos.

        messages.success(request, 'Answer deleted successfully')

        return redirect('forum:question-detail-response', question.id)

    context = {'response': response}

    return render(request, 'forum/delete_confirm_response.html', context)
