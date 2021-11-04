""" views is the ui of the app. gets the data needed to satisfy requests via models.py 
and renders data to the user via template(text file.eg HTML)."""
from django.shortcuts import render,redirect,get_object_or_404
from .models import Place
# Create your views here.
def place_list(request):
    """ :param: request is the http object 
    :returns: the wishlist """
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()     # Create a new Place from the form
        if form.is_valid():     # Checks against DB constraints, for example, are required fields present? 
            place.save()        # Saves to the database 
            return redirect('place_list')    # redirects to GET view with name place_list - which is this same view 
        
    
    places = Place.objects.filter(visited=False).order_by('name') #orm
    new_place_form = NewPlaceForm()
    return render(request, 'wishlist.html', {'places':places, 'new_place_form':new_place_form})

def places_visited(request):
    """ :param: request is the http object 
    :returns: the wishlist """
    visited = Place.objects.filter(visited=True)
    return render(request,'visited.html',{'visited':visited})
    
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True 
        place.save()
    
    return redirect('place_list')