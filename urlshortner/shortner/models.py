from django.conf import settings
from django.db import models
from django.utils.encoding import smart_text
#from django.core.urlresolvers import reverse
# from django_hosts.resolvers import reverse
# Create your models here.
from .utils1 import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class URLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(URLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = URL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class URL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add=True) #when model was created
    active      = models.BooleanField(default=True)

    objects = URLManager()
 

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url and not "https":
            self.url = "http://" + self.url
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.url)


class AnalyseUrl(models.Model):
    shortcode = models.ForeignKey(URL,on_delete=models.CASCADE)
    result = models.IntegerField()
    site_popularity = models.IntegerField()
    length_of_url = models.IntegerField()
    existing_dns_record = models.IntegerField()
    age_of_domain = models.IntegerField()
    ports = models.IntegerField()
    reliable_ip = models.IntegerField()
    shortened_url = models.IntegerField()
    contains_at_the_rate = models.IntegerField()
    cotains_double_slash = models.IntegerField()
    contains_hyphen = models.IntegerField()
    https_token = models.IntegerField()
    subdomain_length = models.IntegerField()
    has_https = models.IntegerField()
    dns_record = models.IntegerField()
    a_tag = models.IntegerField(default=-1)
    form_tag = models.IntegerField(default=-1)
    using_mail = models.IntegerField(default=-1)
    abnormal_url = models.IntegerField(default=-1)
    google_index = models.IntegerField(default=-1)






