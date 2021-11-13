""" views is the ui of the app. gets the data needed to satisfy requests via models.py 
and renders data to the user via template(text file.eg HTML).
This view module fetches the list of not-visited places from the database"""

from django.shortcuts import render,redirect,get_object_or_404
from .models import Place
from .forms import NewPlaceForm,TripReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Create your views here.
@login_required
def place_list(request):
    """ :param: request, the http object, what the user is requesting. 
    :returns: place list. """
    form = NewPlaceForm()
    if request.method == 'POST':
        #create a new place to add to list
        form = NewPlaceForm(request.POST) #create form from the data in the request
        place = form.save(commit=False)
        place.user = request.user
        if form.is_valid(): #verify it meets db constraint
            form.save()        # Saves to the database 
            return redirect('place_list')    # redirects to home page 


    #filter places for the current user  
    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name') # sort visited by name
    new_place_form = NewPlaceForm() #creates html form
    context = {'places':places, 'new_place_form':new_place_form}
    return render(request, 'place_wishlist/wishlist.html',context)

@login_required 
def about(request):
    author = 'Saida'
    about = 'A website to create list of places to visit'
    return render(request, 'place_wishlist/about.html',{'author': author, 'about':about}) #about  page.

@login_required
def places_visited(request):
    """ :param: request is user requesting list of places visited.
    :returns: data  wishlist template."""
    
    visited = Place.objects.filter(user=request.user).filter(visited=True).order_by('name')
    return render(request,'place_wishlist/visited.html',{'visited':visited})

@login_required    
def place_was_visited(request, place_pk):
    """ verify and render a list of places the current user(pk) has visited. 
    :param: request object for a place that was visited.
        :param: place_pk matches page number user visited. """
        
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk) #if object not found return 404 response
        if place.user == request.user: 
            place.visited = True 
            place.save()
        else:
            return HttpResponseForbidden() #return 403 response
        
    return redirect('place_list') #redirect to place list


@login_required
def place_details(request,place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    #verify place belongs to current user
    if place.user != request.user:
        return HttpResponseForbidden()
    
    #validate form data if request == POST
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, instance=place) #encapsulates data sent from request
        if form.is_valid():
            form.save()
            messages.info(request, 'Trip information updated!')
        else:
            messages.error(request, form.errors)
            
        return redirect('place_details',place_pk =place_pk)

    
    #otherwise show place details and optional form.
    else:    
        if place.visited:
            review_form = TripReviewForm(instance=place)  # Pre-populate with data from this Place instance
            return render(request, 'place_wishlist/place_detail.html', {'place': place, 'review_form': review_form} )

        
        #dont show review form if not a GET req
        else:
            return render(request, 'place_wishlist/place_detail.html', {'place': place} )


@login_required
def delete_place(request,place_pk):
    """ verify and render a list of places the current user(pk) has visited. 
        :param: request object for a place that was visited.
        :param: place_pk matches page number user visited. """
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden()