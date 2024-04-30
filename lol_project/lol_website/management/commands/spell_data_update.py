from lol_website.models import Spell, Version

from django.core.management.base import BaseCommand, CommandError
import requests
import json

class Command(BaseCommand):
    help = 'Populates the database with spell data from the Riot API'

    def handle(self, *args, **options):
        version_response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
        version_data = version_response.json()
        version = version_data[0]
        # Update version
        version_object = Version.objects.filter(version=version).first()
        if version_object:
            pass
        else:
            version_object = Version(version=version)
            version_object.save()
        # Get spell data from Riot API
        spell_response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/summoner.json')
        spell_data = spell_response.json()
        spells_data = spell_data['data']

        for spell_name, spell_info in spells_data.items():
            # Check if spell already exists in database
            if "Placeholder" in spell_info['name']:
                continue
            spell = Spell.objects.filter(name=spell_info['name']).first()
            if spell:
                spell.name = spell_info['name']
                spell.description = spell_info['description']
                spell.image = spell_info['image']['full']
                spell.cooldown = spell_info['cooldown'][0]
                spell.range = spell_info['range'][0]
                spell.save()
                print(f'{spell.name} updated to database')
            else:
                spell = Spell(
                    name=spell_info['name'],
                    description=spell_info['description'],
                    image=spell_info['image']['full'],
                    cooldown=spell_info['cooldown'][0],
                    range=spell_info['range'])[0]
                spell.save()
                print(f'{spell.name} added to database')