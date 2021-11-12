from .models import Category

def category_renderer(request):
    # hello = Category.objects.values_list("name", flat=True)
    return {
        'all_cats': Category.objects.values_list("name", flat=True).order_by('name'),
        
    }
