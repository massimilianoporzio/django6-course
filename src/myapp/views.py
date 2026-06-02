from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")

def item(request, item_id=None):
    return HttpResponse(
        "<h1>this is a generic item</h1>"
        if item_id is None
        else f"<h1>Hello, world. You're looking at item {item_id}.</h1>  "
    )