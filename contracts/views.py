from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from setuptools.command.bdist_egg import analyze_egg
from .utils import get_last_qa_context

from contracts.forms import ContractForm
from .models import Contract, ContractQuestion
from ai_analysis.utils import extract_text_from_file, analyze_contract_text, answer_question


# Create your views here.
@login_required()
def upload_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.user = request.user
            contract.save()
            return redirect('contract_details', pk = contract.pk)
        else:
            messages.error(request, 'Invalid form')
    else:
        form = ContractForm()
    return render(request, 'contracts/upload.html', {'form': form})

@login_required()
def contract_details(request, pk):
    contract = get_object_or_404(Contract, pk=pk, user = request.user)

    if not contract.extracted_text:
       contract.extracted_text = extract_text_from_file(contract.file)
       contract.save()

    if not contract.analysis_result and contract.extracted_text:
        contract.analysis_result = analyze_contract_text(contract.extracted_text)
        contract.save()

    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            context = get_last_qa_context(contract, request.user)
            answer =  answer_question(contract.extracted_text,question,context)

            ContractQuestion.objects.create(
                contract=contract,
                user=request.user,
                question=question,
                answer=answer
            )
    qa_history = ContractQuestion.objects.filter(contract=contract, user = request.user).order_by('created_at')

    return render(request, 'contracts/detail.html', {'contract': contract, 'qa_history': qa_history})
