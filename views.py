from django.shortcuts import render
from .forms import MovieForm
from .models import MovieInfo
from .filters import MovieInfoFilter
# Create your views here.

def index(request, *args, **qwargs):
        #return HttpResponse('Hello this is view from movie review')
       return render(request, "MovieReview/index.html")

def AddMovie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MovieForm()
    
    context = {
        'form': form
    }
    return render(request, "MovieReview/add_movie.html", context)

def ViewMovie(request):
    queryset = MovieInfo.objects.all()
    context = {
        "object_list": queryset
    }
    
    # context['filter'] = MovieInfoFilter
    return render(request, "MovieReview/view_movie.html", context)


def MovieFilter(request):
    filter = MovieInfoFilter(request.GET, queryset=MovieInfo.objects.all())
    return render(request, "MovieReview/view_movie.html", {'filter':filter})

# class MovieList(MovieInfo):
#     model = MovieInfo
#     template_name = "MovieReview/view_movie.html"

# def MovieFilter(request, **kwargs):
#     queryfilter = MovieInfo().objects.filter(movie_name__startswith='GOD')
#     context = MovieInfo().queryfilter(**kwargs)
    
#     context['filter'] = MovieInfoFilter(request)
#     return render(request, "MovieReview/view_movie.html", context)



# def get_context_data(self, **kwargs):
#     context = MovieInfo().get_context_data(**kwargs)
#     context['filter'] = MovieInfoFilter(self.request.GET, queryset=self.get_queryset())
#     return context
    

# def product_detail_view(request):
#     queryset = Product.objects.all() 
#     context = {
#            "object_list":queryset
#            }
#     return render(request, "products/product_details.html", context)       


    

    """from django.shortcuts import render, redirect
    from django.http import HttpResponse
    from .models import MovieInfo

    # Create your views here.
    def index(request):
        #return HttpResponse('Hello this is view from movie review')
        return render(request, "MovieReview/index.html")

    def AddMovie(request):
        #return HttpResponse('Add movie here')
        return render(request, "MovieReview/add_movie.html")

    
    def add_movie_form_submission(request):
        print("form submitted")
        movie_name = request.POST["movie_name"]
        movie_review = request.POST["movie_review"]
        movie_release_date = request.POST["movie_release_date"]
        movie_type = request.POST["movie_type"]
        movie_details = request.POST["movie_details"]

        movie_info = MovieInfo(movie_name=movie_name,movie_review=movie_review,movie_release_date=movie_release_date,
        movie_type=movie_type,movie_details=movie_details)
        movie_info.save()
        return render(request, 'MovieReview/index.html')"""
        
    
