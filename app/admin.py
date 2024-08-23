from django.contrib import admin
from .models import students,ThingsToCarry,Trek,Trekcategory,TrekHeroImages,TrekPlan,Location

# @admin.register(index)
class enquiryadmin(admin.ModelAdmin):
    list_display = ('Name','fathers_name','mothers_name', 'age', 'address', 'pincode', 'mobile')
    search_fields = ('Name', 'age', 'mobile')
    list_filter = ('Name', 'age', 'mobile')


admin.site.register(students, enquiryadmin)

class Locationadmin(admin.ModelAdmin):
    list_display  =  ('locationid','locationname','CreatedAt', 'UpdatedAt')
    search_fields =  ('locationid','locationname','CreatedAt', 'UpdatedAt')
    list_filter   =  ('locationid','locationname','CreatedAt', 'UpdatedAt')

admin.site.register(Location, Locationadmin)

class TrekPlanadmin(admin.ModelAdmin):
    list_display = ('TrekPlanTitle', 'Trekid', 'TrekDay','TrekplanDescription')
    search_fields = ('TrekPlanTitle', 'Trekid', 'TrekDay','TrekplanDescription')
    list_filter = ('TrekDay',)

admin.site.register(TrekPlan, TrekPlanadmin)

class TrekCategoryAdmin(admin.ModelAdmin):
    list_display = ('TrekCategory',)
    search_fields =('TrekCategory',)
    list_filter =('TrekCategory',)


admin.site.register(Trekcategory, TrekCategoryAdmin)


class TrekHeroImagesAdmin(admin.ModelAdmin):
    list_display = ('Location', 'TrekHeroImagesUrl',)
    search_fields = ('Location', 'TrekHeroImagesUrl',)
    list_filter = ('Location',)


admin.site.register(TrekHeroImages, TrekHeroImagesAdmin)


class ThingsToCarryAdmin(admin.ModelAdmin):
    list_display = ('Description',)
    search_fields = ('Description',)

admin.site.register(ThingsToCarry, ThingsToCarryAdmin)

class TrekAdmin(admin.ModelAdmin):
    list_display = ('Overview', 'Trek_category', 'LocationTag', 'RegularPrice', 'DicountedPrice', 'TotalDay', 'TotalNight',)
    search_fields = ('Overview', 'Pickupfrom', 'DropTo', 'Trekcategory__Trek_category', 'LocationTag__locationname',)
    list_filter = ('Trek_category', 'LocationTag', 'TotalDay', 'TotalNight',)

admin.site.register(Trek, TrekAdmin)
