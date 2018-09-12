from django.contrib import admin
from django.db.models import Q

from rooms.models import Rooms, Supplies, Reservations, States


class StatesAdmin(admin.ModelAdmin):

    list_display = ('name', )


class SuppliesAdmin(admin.ModelAdmin):

    list_display = ('name', )


class ReservationsAdmin(admin.ModelAdmin):

    list_display = ('room', 'date', 'hour_initial', 'hour_finish', 'quorum', 'get_supplies', 'state')

    def get_form(self, request, obj=None, **kwargs):
        form = super(ReservationsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['room'].queryset = Rooms.objects.filter(Q(
            state__name__exact='Disponible') | Q(state__name__iexact='Reservada'))
        return form


class RoomsAdmin(admin.ModelAdmin):

    list_display = ('name', 'room_ubication', 'capacity', 'get_supplies', 'state')


admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Supplies, SuppliesAdmin)
admin.site.register(Reservations, ReservationsAdmin)
admin.site.register(States, StatesAdmin)
