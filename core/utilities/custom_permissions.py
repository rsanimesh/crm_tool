from rest_framework.permissions import BasePermission
from functools import wraps
from core.models import Role
from django.shortcuts import redirect
import traceback


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            path = request.path
            allowed_urls = request.user.profile.role.permission.values_list('url', flat=True)
            if path in allowed_urls:
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False
