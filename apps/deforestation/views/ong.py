from django.shortcuts import render,redirect
from ..models.ambientalist_ong import AmbientalistOng  # Ajusta la ruta para importar correctamente
# Create your views here.
def home(request):
    ongs = AmbientalistOng.objects.all()
    return render(request, 'ong/ong.html', {'ongs': ongs})

def add_ong(request):
    ongs = AmbientalistOng.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        register_number = request.POST['register_number']
        country = request.POST['country']
        mission = request.POST['mission']
        activities_type = request.POST['activities_type']
        focus_area = request.POST['focus_area']
        annual_budget = request.POST['annual_budget']
        employees_quantity = request.POST['employees_quantity']
        problematic = request.POST['problematic']
        current_projects = request.POST['current_projects']
        obtained_results = request.POST['obtained_results']
        foundation_date = request.POST['foundation_date']
        
        if (request.POST['name']  and
            request.POST['register_number'] and
            request.POST['country'] and
            request.POST['mission'] and
            request.POST['activities_type'] and
            request.POST['focus_area'] and
            request.POST['annual_budget'] and
            request.POST['employees_quantity'] and
            request.POST['problematic'] and
            request.POST['current_projects'] and
            request.POST['obtained_results']):
        
            ong = AmbientalistOng(name=name,
                                country=country,
                                mission=mission,
                                foundation_date=foundation_date,
                                register_number=register_number,
                                activities_type=activities_type,
                                focus_area=focus_area,
                                annual_budget=annual_budget,
                                employees_quantity=employees_quantity,
                                problematic=problematic,
                                current_projects=current_projects,
                                obtained_results=obtained_results
                                )
            ong.save()
            return redirect('/ongs')
        
        return render(request, 'ong/ong.html', {'ongs': ongs})

def edit_ong(request, id_ong):
    ong = AmbientalistOng.objects.get(id_ong=id_ong)
    return render(request, 'ong/edit_ong.html', {'ong': ong})

def update_ong(request, id_ong):
    ong = AmbientalistOng.objects.get(id_ong=id_ong)
    if request.method == 'POST':
        if (request.POST['name']  and
            request.POST['register_number'] and
            request.POST['country'] and
            request.POST['mission'] and
            request.POST['activities_type'] and
            request.POST['focus_area'] and
            request.POST['annual_budget'] and
            request.POST['employees_quantity'] and
            request.POST['problematic'] and
            request.POST['current_projects'] and
            request.POST['obtained_results']):
            
            name = request.POST['name']
            register_number = request.POST['register_number']
            country = request.POST['country']
            mission = request.POST['mission']
            activities_type = request.POST['activities_type']
            focus_area = request.POST['focus_area']
            annual_budget = request.POST['annual_budget']
            employees_quantity = request.POST['employees_quantity'] 
            problematic = request.POST['problematic']
            current_projects = request.POST['current_projects']
            obtained_results = request.POST['obtained_results']
            foundation_date = request.POST['foundation_date']
            
            
            ong.name = name
            ong.register_number = register_number
            ong.country = country
            ong.mission = mission
            ong.activities_type = activities_type
            ong.focus_area = focus_area
            ong.annual_budget = annual_budget
            ong.employees_quantity = employees_quantity
            ong.problematic = problematic
            ong.current_projects = current_projects
            ong.obtained_results = obtained_results
            ong.foundation_date = foundation_date
            ong.save()
            return redirect('/ongs')
        return render(request, 'ong/ong.html.html', {'ong': ong})

def delete_ong(_, id_ong):
    ong = AmbientalistOng.objects.get(id_ong=id_ong)
    ong.delete()
    return redirect('/ongs')