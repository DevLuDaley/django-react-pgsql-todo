
# setup model.py

First, we will create a simple model. Open the models.py file and write the following code:

```py

# todos/models.py

from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

```


Next, we will build a simple model-backed API using REST framework. Let’s create a new folder named api and create new files __init__.py, serializers.py, views.py and urls.py in it:

Since the api is a module, we need to include __init__.py file.

```py
todos/
  api/
    __init__.py
    serializers.py
    urls.py
    views.py
```


The ModelSerializer class will create fields that correspond to the Model fields.

Next, we will define the view behavior in the api/views.py file:
```py
# todos/api/views.py

from rest_framework import viewsets

from .serializers import TodoSerializer
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

