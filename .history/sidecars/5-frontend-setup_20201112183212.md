
```py
#api/views.py
from rest_framework import routers

from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet, 'todos')
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')

urlpatterns = router.urls
```

We will create the frontend/index.html file later. Don’t worry about it now.

Add a new urls.py file to the same directory and create the URL conf:

```py
# frontend/urls.py

from django.urls import path

from .views import index, TodoDetailView

urlpatterns = [
    path('', index),
    path('edit/<int:pk>', TodoDetailView.as_view()),
    path('delete/<int:pk>', TodoDetailView.as_view()),
]

```

Although the path for the Django admin site is left, we are not going to use it in this tutorial.

As a final part of this chapter, we will make a new migration file and apply changes to our databases by running the commands below:

# migrate
    python manage.py makemigrations
    python manage.py migrate

