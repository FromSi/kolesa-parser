from django.contrib import admin
from . import models


admin.site.register(models.City)
admin.site.register(models.Mark)
admin.site.register(models.Type)
admin.site.register(models.Ad)
admin.site.register(models.Picture)
admin.site.register(models.Profile)


"""

+auto-car-grbody     -- тип машины
+region              -- город
+price[from]         -- цена от
+price[to]           -- цена до

+/cars/[mark]/       -- марка машины
+/[mark]/[model]/    -- модель машины

_sys-hasphoto=2     -- c фото
_sys-torg=1         -- срочно, торг
auto-custom=2       -- растаможен

"""