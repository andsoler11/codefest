from django.db import models

# Create your models here.
class disasters19002021(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=0)
    seq = models.IntegerField(default=0)
    glide = models.CharField(max_length=255, null=True, blank=True)
    disaster_group = models.CharField(max_length=255, null=True, blank=True)
    disaster_subgroup = models.CharField(max_length=255, null=True, blank=True)
    disaster_type = models.CharField(max_length=255, null=True, blank=True)
    disaster_subtype = models.CharField(max_length=255, null=True, blank=True)
    disaster_subsubtype = models.CharField(max_length=255, null=True, blank=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    iso = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    continent = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    associated_dis = models.CharField(max_length=255, null=True, blank=True)
    associated_dis2 = models.CharField(max_length=255, null=True, blank=True)
    ofda_response = models.CharField(max_length=255, null=True, blank=True)
    appeal = models.CharField(max_length=255, null=True, blank=True)
    declaration = models.CharField(max_length=255, null=True, blank=True)
    aid_contribution = models.CharField(max_length=255, null=True, blank=True)
    dis_mag_value = models.IntegerField(default=0)
    dis_mag_scale = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    local_time = models.CharField(max_length=255, null=True, blank=True)
    river_basin = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(default=0)
    start_month = models.IntegerField(default=0)
    start_day = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    end_month = models.IntegerField(default=0)
    end_day = models.IntegerField(default=0)
    total_deaths = models.IntegerField(default=0)
    no_injured = models.IntegerField(default=0)
    no_affected = models.IntegerField(default=0)
    no_homeless = models.IntegerField(default=0)
    total_affected = models.IntegerField(default=0)
    insured_damages = models.IntegerField(default=0)
    total_damages = models.IntegerField(default=0)
    cpi = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    adm_level = models.CharField(max_length=255, null=True, blank=True)
    admin1_code = models.TextField(null=True, blank=True)
    admin2_code = models.TextField(null=True, blank=True)
    geo_locations = models.TextField(null=True, blank=True)
    reconstruction_costs = models.IntegerField(default=0)


class disasters19702021(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=0)
    seq = models.IntegerField(default=0)
    glide = models.CharField(max_length=255, null=True, blank=True)
    disaster_group = models.CharField(max_length=255, null=True, blank=True)
    disaster_subgroup = models.CharField(max_length=255, null=True, blank=True)
    disaster_type = models.CharField(max_length=255, null=True, blank=True)
    disaster_subtype = models.CharField(max_length=255, null=True, blank=True)
    disaster_subsubtype = models.CharField(max_length=255, null=True, blank=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    iso = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    continent = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    associated_dis = models.CharField(max_length=255, null=True, blank=True)
    associated_dis2 = models.CharField(max_length=255, null=True, blank=True)
    ofda_response = models.CharField(max_length=255, null=True, blank=True)
    appeal = models.CharField(max_length=255, null=True, blank=True)
    declaration = models.CharField(max_length=255, null=True, blank=True)
    aid_contribution = models.CharField(max_length=255, null=True, blank=True)
    dis_mag_value = models.IntegerField(default=0)
    dis_mag_scale = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    local_time = models.CharField(max_length=255, null=True, blank=True)
    river_basin = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(default=0)
    start_month = models.IntegerField(default=0)
    start_day = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    end_month = models.IntegerField(default=0)
    end_day = models.IntegerField(default=0)
    total_deaths = models.IntegerField(default=0)
    no_injured = models.IntegerField(default=0)
    no_affected = models.IntegerField(default=0)
    no_homeless = models.IntegerField(default=0)
    total_affected = models.IntegerField(default=0)
    insured_damages = models.IntegerField(default=0)
    total_damages = models.IntegerField(default=0)
    cpi = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    adm_level = models.CharField(max_length=255, null=True, blank=True)
    admin1_code = models.TextField(null=True, blank=True)
    admin2_code = models.TextField(null=True, blank=True)
    geo_locations = models.TextField(null=True, blank=True)
    reconstruction_costs = models.IntegerField(default=0)

class Disasters(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=0)
    seq = models.IntegerField(default=0)
    glide = models.CharField(max_length=255, null=True, blank=True)
    disaster_group = models.CharField(max_length=255, null=True, blank=True)
    disaster_subgroup = models.CharField(max_length=255, null=True, blank=True)
    disaster_type = models.CharField(max_length=255, null=True, blank=True)
    disaster_subtype = models.CharField(max_length=255, null=True, blank=True)
    disaster_subsubtype = models.CharField(max_length=255, null=True, blank=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    iso = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    continent = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    associated_dis = models.CharField(max_length=255, null=True, blank=True)
    associated_dis2 = models.CharField(max_length=255, null=True, blank=True)
    ofda_response = models.CharField(max_length=255, null=True, blank=True)
    appeal = models.CharField(max_length=255, null=True, blank=True)
    declaration = models.CharField(max_length=255, null=True, blank=True)
    aid_contribution = models.CharField(max_length=255, null=True, blank=True)
    dis_mag_value = models.IntegerField(default=0)
    dis_mag_scale = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    local_time = models.CharField(max_length=255, null=True, blank=True)
    river_basin = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(default=0)
    start_month = models.IntegerField(default=0)
    start_day = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    end_month = models.IntegerField(default=0)
    end_day = models.IntegerField(default=0)
    total_deaths = models.IntegerField(default=0)
    no_injured = models.IntegerField(default=0)
    no_affected = models.IntegerField(default=0)
    no_homeless = models.IntegerField(default=0)
    total_affected = models.IntegerField(default=0)
    insured_damages = models.IntegerField(default=0)
    total_damages = models.IntegerField(default=0)
    cpi = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    adm_level = models.CharField(max_length=255, null=True, blank=True)
    admin1_code = models.TextField(null=True, blank=True)
    admin2_code = models.TextField(null=True, blank=True)
    geo_locations = models.TextField(null=True, blank=True)
    reconstruction_costs = models.IntegerField(default=0)
