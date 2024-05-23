
from django.urls import path
from . import views 

urlpatterns = [
   #localhost:8000/batman/
    path("" , views.dishant , name="dishant"),

    #now here other routes ocalhost:8000/batman/otherRoutes

    path("<int:chai_id>/" , views.chai_detail , name="chai_detail"),
    
]
