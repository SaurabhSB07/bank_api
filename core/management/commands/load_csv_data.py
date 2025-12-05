from django.core.management.base import BaseCommand
import csv
from core.models import Bank, Branch

class Command(BaseCommand):
    help = 'Load data from bank.csv and branch.csv into the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting CSV import...'))

        # ---------- Load Bank CSV ----------
        bank_mapping = {}  # CSV bank_id -> Bank object
        with open('core/data/banks.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bank_name = row['name']
                bank_obj, created = Bank.objects.get_or_create(name=bank_name)
                bank_mapping[row['id']] = bank_obj  # map CSV id to Bank object
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Bank created: {bank_name}'))
                else:
                    self.stdout.write(f'Bank already exists: {bank_name}')

        # ---------- Load Branch CSV ----------
        with open('core/data/branches.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bank_id = row['bank_id']
                bank_obj = bank_mapping.get(bank_id)
                if not bank_obj:
                    self.stdout.write(self.style.ERROR(
                        f'Bank ID {bank_id} not found. Skipping branch {row["branch"]}.'
                    ))
                    continue

                branch_obj, created = Branch.objects.get_or_create(
                    ifsc=row['ifsc'],
                    defaults={
                        'bank': bank_obj,
                        'branch': row['branch'],
                        'address': row.get('address', ''),
                        'city': row.get('city', ''),
                        'district': row.get('district', ''),
                        'state': row.get('state', ''),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f'Branch created: {row["branch"]} ({row["ifsc"]})'
                    ))
                else:
                    self.stdout.write(
                        f'Branch already exists: {row["branch"]} ({row["ifsc"]})'
                    )

        self.stdout.write(self.style.SUCCESS('CSV import finished!'))
