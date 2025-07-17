from django.core.management.base import BaseCommand
import pandas as pd
from inventory.models import ExardProduct

class Command(BaseCommand):
    help = 'Import products from master_data.xlsx into the database'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('master_data.xlsx')
        for _, row in df.iterrows():
            ExardProduct.objects.create(
                # product_name=row['Product Name'],
                alpha_number=row['Alpha Number'],
                bap_number=row['Bap Number'],
                quantity=row['Quantity'],
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))