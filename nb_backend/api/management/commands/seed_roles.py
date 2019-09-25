"""Custom seed roles Django management command."""

from django.core.management.base import BaseCommand
from api.models.role import Role

# pylint: disable=broad-except, no-member, unused-argument


class Command(BaseCommand):
    """Define custom Django management commands."""

    help = "Seeds initial roles."

    def handle(self, *args, **options):
        """Handle seeding of roles."""
        role_types = [
            "superadmin", "admin", "user", "guest", "moderator"]
        for role in role_types:
            if not Role.objects.filter(role_type=role).exists():
                Role.objects.create(role_type=role)