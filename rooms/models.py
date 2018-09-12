from django.db import models


class Supplies(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class States(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=150)
    room_ubication = models.CharField(max_length=150)
    capacity = models.IntegerField()
    scheduler = models.CharField(max_length=150, blank=True, null=True)
    supplies = models.ManyToManyField(Supplies)
    state = models.ForeignKey(States, on_delete=models.CASCADE)

    def get_supplies(self):
        return "\n".join([str(p) for p in self.supplies.all()])

    def __str__(self):
        return "{0}".format(self.name)


class Reservations(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    date = models.DateField()
    hour_initial = models.TimeField(help_text='format to hour 00:00:00')
    hour_finish = models.TimeField(help_text='format to hour 00:00:00')
    quorum = models.IntegerField()
    supplies = models.ManyToManyField(Supplies)
    state = models.ForeignKey(States, default=4, on_delete=models.CASCADE, editable=False)

    def get_supplies(self):
        return "\n".join([str(p) for p in self.supplies.all()])

    def __unicode__(self):
        return self.room



