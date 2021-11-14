from .models import Category

def category_renderer(request):
    # order by name here as the filter disctsort is not working in templates
    return {
        'all_cats': Category.objects.values_list("name", flat=True).order_by('name'),
        
    }
