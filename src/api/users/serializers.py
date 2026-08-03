from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=5, max_length=50)
    password = serializers.CharField(min_length=8)
    is_admin = serializers.BooleanField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        is_admin = attrs.get("is_admin")


        if is_admin==True and len(password) < 15:
            raise serializers.ValidationError("Admin password mst be at least 15 characters")
        if not 'hiit' in password.lower():
            raise serializers.ValidationError("Password doesn't follow company's policy")
        if not email.endswith('hiit.com'):
            raise serializers.ValidationError("Email must contain hiit")

        return attrs