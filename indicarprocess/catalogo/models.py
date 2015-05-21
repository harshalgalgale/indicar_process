from django.contrib.gis.db import models


class CatalogoLandsat(models.Model):

    objectid = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=255, unique=True)
    path = models.CharField(max_length=500)
    url_tms = models.CharField(max_length=500)
    data = models.DateField()
    shape = models.PolygonField(srid=4674, null=True, blank=True)

    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CatalogoLandsat, self).save(*args, **kwargs)

    def __str__(self):
        return self.image

    class Meta:
        db_table = 'catalogo_landsat'