from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from utils.mailer import BaseEmail

from .models import HostingOrder, HostingBill, HostingPlan


admin.site.register(HostingOrder)
admin.site.register(HostingBill)
admin.site.register(HostingPlan)
