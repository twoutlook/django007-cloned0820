from django.contrib import admin

# Register your models here.
# from .models import Customer
from .models import Item000
from .models import Item001
from .models import Item002
from .models import Item003
from .models import Item004
from .models import Spec
from .models import Cust

from django.contrib import admin
# admin.site.register(Customer)

class Item000Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6']
admin.site.register(Item000,Item000Admin)


class SpecAdmin(admin.ModelAdmin):
    list_display=['field1','field2']
admin.site.register(Spec,SpecAdmin)

class CustAdmin(admin.ModelAdmin):
    list_display=['field1','field2']
admin.site.register(Cust,CustAdmin)

class Item002Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6','field7']
admin.site.register(Item002,Item002Admin)

class Item004Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6','field7']
admin.site.register(Item004,Item004Admin)

#  r01c2 = models.CharField(default=".",max_length=99,verbose_name="几号机")
#     r01c4 = models.CharField(default=".",max_length=99,verbose_name="吨位")
#     r01c6 = models.CharField(default=".",max_length=99,verbose_name="人员")
#     r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")
 
class Item001Admin(admin.ModelAdmin):
    fieldsets = [
        ('壓鑄機', {'fields': ['field1',]}),
        ('噸位人員日期', {'fields': [ 'field1a','r01c6','r01c8',], 'classes': ['collapse']}),
        # ('結構 - 格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
        # ('結構 - 機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
#--- code3 for admin.py (start) -----

        ('結構-格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
        ('結構-機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
        ('結構-模板', {'fields': ['r05c3','r05c4','r05c5','r05c6','r05c7',], 'classes': ['collapse']}),
        ('結構-合模', {'fields': ['r06c3','r06c4','r06c5','r06c6','r06c7',], 'classes': ['collapse']}),
        ('結構-間隙', {'fields': ['r07c3','r07c4','r07c5','r07c6','r07c7',], 'classes': ['collapse']}),
        ('結構-膜厚調節', {'fields': ['r08c3','r08c4','r08c5','r08c6','r08c7',], 'classes': ['collapse']}),
        ('液壓油-油管', {'fields': ['r10c3','r10c4','r10c5','r10c6','r10c7',], 'classes': ['collapse']}),
        ('液壓油-過濾', {'fields': ['r11c3','r11c4','r11c5','r11c6','r11c7',], 'classes': ['collapse']}),
        ('液壓油-油箱', {'fields': ['r12c3','r12c4','r12c5','r12c6','r12c7',], 'classes': ['collapse']}),
        ('液壓油-馬達', {'fields': ['r13c3','r13c4','r13c5','r13c6','r13c7',], 'classes': ['collapse']}),
        ('潤滑', {'fields': ['r15c3','r15c4','r15c5','r15c6','r15c7',], 'classes': ['collapse']}),
        ('氮氣', {'fields': ['r16c3','r16c4','r16c5','r16c6','r16c7',], 'classes': ['collapse']}),
        ('電控', {'fields': ['r17c3','r17c4','r17c5','r17c6','r17c7',], 'classes': ['collapse']}),
        ('自動噴霧', {'fields': ['r18c3','r18c4','r18c5','r18c6','r18c7',], 'classes': ['collapse']}),
        ('自動取出', {'fields': ['r19c3','r19c4','r19c5','r19c6','r19c7',], 'classes': ['collapse']}),
        ('自動切邊去毛', {'fields': ['r20c3','r20c4','r20c5','r20c6','r20c7',], 'classes': ['collapse']}),
    ]
#--- code3 for admin.py (end) -----    ]

    list_display=[
        'field1', 'field1a','r01c6','r01c8',
        # 'r03c3','r03c4','r03c5','r03c6','r03c7',
        # 'r04c3','r04c4','r04c5','r04c6','r04c7',
        
     ]
admin.site.register(Item001,Item001Admin)


class Item003Admin(admin.ModelAdmin):
    fieldsets = [
        ('壓鑄機', {'fields': ['field1',]}),
        ('噸位人員日期', {'fields': [ 'field1a','r01c6','r01c8',], 'classes': ['collapse']}),
        # ('結構 - 格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
        # ('結構 - 機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
#--- code3 for admin.py (start) -----

        ('結構-格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
        ('結構-機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
        ('結構-模板', {'fields': ['r05c3','r05c4','r05c5','r05c6','r05c7',], 'classes': ['collapse']}),
        ('結構-合模', {'fields': ['r06c3','r06c4','r06c5','r06c6','r06c7',], 'classes': ['collapse']}),
        ('結構-間隙', {'fields': ['r07c3','r07c4','r07c5','r07c6','r07c7',], 'classes': ['collapse']}),
        ('結構-膜厚調節', {'fields': ['r08c3','r08c4','r08c5','r08c6','r08c7',], 'classes': ['collapse']}),
        ('液壓油-油管', {'fields': ['r10c3','r10c4','r10c5','r10c6','r10c7',], 'classes': ['collapse']}),
        ('液壓油-過濾', {'fields': ['r11c3','r11c4','r11c5','r11c6','r11c7',], 'classes': ['collapse']}),
        ('液壓油-油箱', {'fields': ['r12c3','r12c4','r12c5','r12c6','r12c7',], 'classes': ['collapse']}),
        ('液壓油-馬達', {'fields': ['r13c3','r13c4','r13c5','r13c6','r13c7',], 'classes': ['collapse']}),
        ('潤滑', {'fields': ['r15c3','r15c4','r15c5','r15c6','r15c7',], 'classes': ['collapse']}),
        ('氮氣', {'fields': ['r16c3','r16c4','r16c5','r16c6','r16c7',], 'classes': ['collapse']}),
        ('電控', {'fields': ['r17c3','r17c4','r17c5','r17c6','r17c7',], 'classes': ['collapse']}),
        ('自動噴霧', {'fields': ['r18c3','r18c4','r18c5','r18c6','r18c7',], 'classes': ['collapse']}),
        ('自動取出', {'fields': ['r19c3','r19c4','r19c5','r19c6','r19c7',], 'classes': ['collapse']}),
        ('自動切邊去毛', {'fields': ['r20c3','r20c4','r20c5','r20c6','r20c7',], 'classes': ['collapse']}),
    ]
#--- code3 for admin.py (end) -----    ]

    list_display=[
        'field1', 'field1a','r01c6','r01c8',
        # 'r03c3','r03c4','r03c5','r03c6','r03c7',
        # 'r04c3','r04c4','r04c5','r04c6','r04c7',
        
     ]
admin.site.register(Item003,Item003Admin)


# admin.site.register(Item001)
# admin.site.register(Item002)
# admin.site.register(Item003)
# admin.site.register(Item004)
# admin.site.register(Spec)
