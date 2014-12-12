from django.core.management.base import NoArgsCommand
from browser.models import Item
from django.templatetags.static import static
from django.conf import settings
import json
import os

class Command(NoArgsCommand):
   help = 'Resets the database from the JSON file.'

   def handle_noargs(self, **options):
      filename = static('items.json')

      # clear database
      Item.objects.all().delete()

      with open(os.path.join(settings.BASE_DIR, filename.lstrip('/')), 'r') as cvfile:
         jsonObj = json.load(cvfile)

      for record in jsonObj:
         item = Item.objects.create(**record)
         self.stdout.write('Successfully added item "%s"' % item)
