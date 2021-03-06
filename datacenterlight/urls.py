from django.conf.urls import url

from .views import IndexView, BetaProgramView, LandingProgramView, BetaAccessView, PricingView, SuccessView, OrderView


urlpatterns = [
    url(r'^/?$', IndexView.as_view(), name='index'),
    url(r'^/beta-program/?$', BetaProgramView.as_view(), name='beta'),
    url(r'^/landing/?$', LandingProgramView.as_view(), name='landing'),
    url(r'^/pricing/?$', PricingView.as_view(), name='pricing'),
    url(r'^/order/?$', OrderView.as_view(), name='order'),
    url(r'^/order-success/?$', SuccessView.as_view(), name='success'),
    url(r'^/beta_access?$', BetaAccessView.as_view(), name='beta_access'),
]
