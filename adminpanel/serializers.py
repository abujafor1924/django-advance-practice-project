from rest_framework import serializers
from authentication.models import RecordDocuments, User, Appointment, Payment

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AdminAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AdminPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class AdminRecordDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordDocuments
        fields = '__all__'