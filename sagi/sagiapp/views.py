from django.shortcuts import render,redirect
from .models import Cadastro
from django.db.models import IntegerField
from django.db.models.functions import Cast



def home(request):
    erro = ''
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        try:
            usuario = Cadastro.objects.get(matricula=matricula, pwd=senha, ativo='1')
            # Salva os dados do usuário na sessão
            request.session['usuario_id'] = usuario.matricula
            request.session['usuario_nome'] = usuario.nome
            return redirect('dashboard')  # ou outra página
        except Cadastro.DoesNotExist:
            erro = 'Matrícula ou senha inválida.'

    return render(request, 'home.html',{'erro': erro})

def dashboard(request):
    if not request.session.get('usuario_id'):
        return redirect('home')
    
    cadastros_ativos = Cadastro.objects.filter(ativo='1')
    total_ativos = cadastros_ativos.count()
    cadastro = Cadastro.objects.get(matricula=request.session['usuario_id'])
    usuario_nome = cadastro.nome
    context = {
        'total_membros': 320,
        'total_entradas': 18500.00,
        'total_saidas': 9600.00,
        'tarefas_pendentes': 12,
        'total_ativos': total_ativos,
        'usuario_id': usuario_nome,
    }
    return render(request, 'dashboard.html', context)

def membros(request):
    if not request.session.get('usuario_id'):
        return redirect('home')
    cadastros = Cadastro.objects.filter(ativo='1')
    return render(request, 'membros.html', {'cadastros': cadastros})

def logout_view(request):
    request.session.flush()
    return redirect('home')


def cadastro(request):
    if not request.session.get('usuario_id'):
        return redirect('home')

    # Cast para inteiro e ordena corretamente
    ultimo = (
        Cadastro.objects
        .annotate(matricula_int=Cast('matricula', IntegerField()))
        .order_by('-matricula_int')
        .first()
    )

    if ultimo:
        nova_matricula = str(ultimo.matricula_int + 1).zfill(4)
    else:
        nova_matricula = '0001'

    return render(request, 'cadastro.html', {
        'proxima_matricula': nova_matricula
    })

def edit(request):
     
     matricula = request.GET.get('matricula')
     cad = Cadastro.objects.get(matricula=matricula)
     context = {
        'cadastro': cad,
        'total_entradas': 18500.00,
        'total_saidas': 9600.00,
        'tarefas_pendentes': 12,
        
      }


     return render(request, 'edit.html',context)