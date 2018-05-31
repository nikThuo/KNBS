from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from manufacturing.models import Per_Change_In_Quantum_Indices_Of_Man_Production, \
    Quantum_Indices_Of_Manufacturing_Production


def manufacturing(request):
    return render(request, template_name='knbs_bi/manufacturing.html')

############################################Per_Change_In_Quantum_Indices_Of_Man_Production############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def percentageChange(request):
    per_change = Per_Change_In_Quantum_Indices_Of_Man_Production.objects.all()

    productions = []

    if per_change:
        for production in per_change:
            c = {'commodity': production.commodity, 'percentage_change': production.percentage_change,
                 'year': production.year}
            productions.append(c)
    else:
        pass
    return Response(productions)

#Launch Page
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def percentageChangeView(request):
    per_change = Per_Change_In_Quantum_Indices_Of_Man_Production.objects.all()

    productions = []

    if per_change:
        for production in per_change:
            c = {'id':production.percentage_change_id, 'commodity': production.commodity, 'percentage_change': production.percentage_change,
                 'year': production.year}
            productions.append(c)
            context = {'productions': productions}
    else:
        pass
    return render(request, 'knbs_bi/manufacturing_per_change_in_quantum_indices_of_man_production.html', context)

# Add View
def addPercentageChangeView(request):
    return render(request, 'knbs_bi/manufacturing_per_change_in_quantum_indices_of_man_production_add.html')

# Edit View
def editPercentageChangeView(request):
    return render(request, 'knbs_bi/manufacturing_per_change_in_quantum_indices_of_man_production_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPercentageChange(request):
    change_add = Per_Change_In_Quantum_Indices_Of_Man_Production(commodity=request.data['commodity'], percentage_change=request.data['change'],
                                                    year=request.data['year'])
    if change_add:
        change_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPercentageChange(request):
    change_edit = Per_Change_In_Quantum_Indices_Of_Man_Production.objects.get(percentage_change_id=request.data['percent_id'])

    if 'commodity' in request.data:
        change_edit.commodity = request.data['commodity']
    if 'change' in request.data:
        change_edit.percentage_change = request.data['change']
    if 'year' in request.data:
        change_edit.year = request.data['year']

    change_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Quantum_Indices_Of_Manufacturing_Production############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quantumIndices(request):
    quan_indice = Quantum_Indices_Of_Manufacturing_Production.objects.all()

    indices = []

    if quan_indice:
        for indice in quan_indice:
            c = {'commodity': indice.commodity, 'quantum_indice': indice.quantum_indice,
                 'year': indice.year}
            indices.append(c)
    else:
        pass
    return Response(indices)


# Launch Page
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quantumIndicesView(request):
    quan_indice = Quantum_Indices_Of_Manufacturing_Production.objects.all()

    indices = []

    if quan_indice:
        for indice in quan_indice:
            c = {'id': indice.quantum_indice_id, 'commodity': indice.commodity, 'quantum_indice': indice.quantum_indice,
                 'year': indice.year}
            indices.append(c)
            context = {'indices': indices}
    else:
        pass
    return render(request, 'knbs_bi/manufacturing_quantum_indices_of_manufacturing_production.html', context)


# Add View
def addQuantumIndicesView(request):
    return render(request, 'knbs_bi/manufacturing_quantum_indices_of_manufacturing_production_add.html')


# Edit View
def editQuantumIndicesView(request):
    return render(request, 'knbs_bi/manufacturing_quantum_indices_of_manufacturing_production_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addQuantumIndices(request):
    indice_add = Quantum_Indices_Of_Manufacturing_Production(commodity=request.data['commodity'],
                                                                 quantum_indice=request.data['indice'],
                                                                 year=request.data['year'])
    if indice_add:
        indice_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editQuantumIndices(request):
    indice_edit = Quantum_Indices_Of_Manufacturing_Production.objects.get(quantum_indice_id=request.data['quantum_id'])

    if 'commodity' in request.data:
        indice_edit.commodity = request.data['commodity']
    if 'indice' in request.data:
        indice_edit.quantum_indice = request.data['indice']
    if 'year' in request.data:
        indice_edit.year = request.data['year']

    indice_edit.save()
    return Response(status=status.HTTP_201_CREATED)
