from django.contrib import admin

<<<<<<< Updated upstream
from base.models import Personal
from .models import Personal


admin.site.register(Personal)
=======
from.models import Person

admin.site.register(Person)
>>>>>>> Stashed changes

# Register your models here.
