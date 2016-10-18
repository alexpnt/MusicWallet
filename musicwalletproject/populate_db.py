import os,django
import json
os.environ["DJANGO_SETTINGS_MODULE"] = "musicwalletproject.settings.development"
django.setup()

from musicwalletapp.models import Music

def populate_music_db(dump_file):
	dump_file=open(dump_file,'r').read()
	json_data = json.JSONDecoder().decode(dump_file)
	tracks=json_data['aTracks']
	print 'Populating music db ...'
	for t in tracks:
		t=Music(title=t['track_title'],artist=t['artist_name'],album=t['album_title'])
		t.save()
	print 'Done'

if __name__ == '__main__':
	populate_music_db('data/recent.json')

