import yaml
from django.core.management.base import BaseCommand, CommandError

from ...models import Region


class Command(BaseCommand):
    help = "Import regions from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import regions... wait...",
            )
        )
        # Region.objects.all().delete()
        try:
            with open(
                "apps/common/management/source/regions.yaml",
                "r",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    Command.objects.create(country_id=1,
                        name=item["name_uz"],
                    )
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File regions yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} regions successfully imported"))