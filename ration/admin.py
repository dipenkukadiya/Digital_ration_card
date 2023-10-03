from django.contrib import admin

from .models import registerdb
from .models import familydb
from .models import pricedb
from .models import pricebpl
from .models import feedbackdb
from .models import rationdb
from .models import tokondb

admin.site.register(registerdb)
admin.site.register(rationdb)
admin.site.register(familydb)
admin.site.register(pricedb)
admin.site.register(pricebpl)
admin.site.register(feedbackdb)
admin.site.register(tokondb)