from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from setuptools.command.bdist_egg import analyze_egg

from contracts.forms import ContractForm
from .models import Contract
from ai_analysis.utils import extract_text_from_file, analyze_contract_text


# Create your views here.
@login_required()
def upload_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.user = request.user
            #contract.extracted_text = extract_text_from_file(contract.file)  # función que vamos a crear
            #contract.analysis_result = analyze_contract_text(contract.extracted_text)  # IA
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


    return render(request, 'contracts/detail.html', {'contract': contract})
