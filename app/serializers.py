from rest_framework import serializers
from .models import *

class WhoIsSerializer(serializers.ModelSerializer):         
    class Meta:
        model = WhoIsData
        fields = "__all__"
        extra_kwargs = {
            'server_ip': {'validators': []},
        }

class InstagramSearchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InstagramSearches
        fields = "__all__"
        extra_kwargs = {
            'id': {'validators': []},
        }

class GoogleSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoogleSearches
        fields = "__all__"
        extra_kwargs = {
            'link': {'validators': []},

        }

class LeakedCreditCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeakedCreditCardDetails
        fields = "__all__"
        extra_kwargs = {
            'leaked_url': {'validators': []},
        }
    
class OTXSerializer(serializers.ModelSerializer):

    class Meta:
        model = OTXPulseData
        fields = "__all__"
        extra_kwargs = {
            'server_ip': {'validators': []},
        }

class ShodanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShodanData
        fields = "__all__"

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateData
        fields = "__all__"
        extra_kwargs = {
            'issuer_ca_id': {'validators': []},
        }

class CensysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensysData
        fields = "__all__"
        
class TrendingKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingKeywordData
        fields = "__all__"
        extra_kwargs = {
            'name': {'validators': []},
        }

class WebsiteMonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteMonitoringData
        fields = "__all__"
        extra_kwargs = {
            'domain_name': {'validators': []},
        }

class TwistedDnsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwistedDnsData
        fields = "__all__"
        extra_kwargs = {
            'twisted_dns': {'validators': []},
        }

class TwitterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterData
        fields = "__all__"

class EmailDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailData
        fields = "__all__"
        extra_kwargs = {
            'query': {'validators': []},
        }