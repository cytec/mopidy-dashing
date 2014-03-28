from __future__ import unicode_literals

import pykka
import urllib2
import logging
import json

from mopidy import core

logger = logging.getLogger(__name__)

class DashingFrontend(pykka.ThreadingActor, core.CoreListener):
	def __init__(self, config, core):
		super(DashingFrontend, self).__init__()
		self.config = config	
		self.core = core

		self.url = "http://%s:%s%s" % (
			config['dashing']['hostname'], 
			config['dashing']['port'], 
			config['dashing']['widget'],
		)
		self.auth_token = config['dashing']['auth_token']

		self.req = urllib2.Request(self.url)
		self.req.add_header('Content-Type', 'application/json')

	def on_start(self):
		logger.debug(self.url)

	def on_stop(self):
		message = json.dumps({
			"auth_token": self.auth_token,
			"title": "Stopped"
		})

		logger.info(message)

#		urllib2.urlopen(self.req, message)

	def track_playback_started(self, tl_track):
		artists = []

		for artist in tl_track.track.artists:
			artists.append(artist.name)			
		
		message = json.dumps({ 
			"auth_token": self.auth_token, 
			"title": tl_track.track.name,
			"text": "%s - %s" % ("/".join(artists), tl_track.track.album.name),
		})

		logger.info(message)

		urllib2.urlopen(self.req, message)

	def track_playback_ended(self, tl_track, time_position):

		message = json.dumps({
			"auth_token": self.auth_token,
			"title": "Stopped"
		})

		logger.info(message)

		urllib2.urlopen(self.req, message)
		
