import yaml
from django.core.management.base import BaseCommand, CommandError

from ...models import Country


class Command(BaseCommand):
    help = "Import countries from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import countries... wait...",
            )
        )
        # Region.objects.all().delete()
        try:
            with open(
                "apps/common/management/source/coutries.yaml",
                "r",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    Country.objects.create(
                        name=item["name_uz"],
                    )
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File countries yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} countries successfully imported"))