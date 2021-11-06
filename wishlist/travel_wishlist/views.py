""" views is the ui of the app. gets the data needed to satisfy requests via models.py 
and renders data to the user via template(text file.eg HTML).
This view module fetches the list of not-visited places from the database"""


from django.shortcuts import render,redirect,get_object_or_404
from .models import Place
from .forms import NewPlaceForm
# Create your views here.
def place_list(request):
    """ :param: request, the http object, what the user is requesting. 
    :returns: place list. """
    if request.method == 'POST':
        #create a new place to add to list
        form = NewPlaceForm(request.POST) #create form from the data in the request
        place = form.save()     
        if form.is_valid(): #verify it meets db constraint
            place.save()        # Saves to the database 
            return redirect('place_list')    # redirects to home page 
    
    
    places = Place.objects.filter(visited=False).order_by('name') # sort visited by name
    new_place_form = NewPlaceForm() #creates html form
    return render(request, 'wishlist/wishlist.html', {'places':places, 'new_place_form':new_place_form})


def about(request):
    author = 'Saida'
    about = 'A website to create list of places to visit'
    return render(request, 'about.html',{'author': author, 'about':about}) #about  page.

def places_visited(request):
    """ :param: request is user requesting list of places visited.
    :returns: the wishlist """
    visited = Place.objects.filter(visited=True)
    return render(request,'wishlist/visited.html',{'visited':visited})
    
def place_was_visited(request, place_pk):
    """ :param: request object for a place that was visited.
        :param: place_pk matches page number user visited """
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk) #if object not found return 404 response 
        place.visited = True 
        place.save()
    return redirect('place_list') #redirect to place list