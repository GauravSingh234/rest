from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import students
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = students
        fields = ['Name','fathers_name','mothers_name', 'age', 'address', 'pincode', 'mobile']



# View define the view behavior.
class studentsViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = UserSerializer

# URLS provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Students', studentsViewSet)        