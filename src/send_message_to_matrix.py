from ebbs import Builder
import requests
import logging

class send_message_to_matrix(Builder):
	def __init__(this, name="Send Message To Matrix"):
		super().__init__(name)
		this.requiredKWArgs.append('homeserver')
		this.requiredKWArgs.append('room')
		this.requiredKWArgs.append('token')
		this.requiredKWArgs.append('message')
		
	def Build(this):
		this.message = this.message.replace('"', '\\"')
		this.message = this.message.replace('\n', '\\n')
		response = requests.post(
			this.homeserver + "/_matrix/client/r0/rooms/" + this.room + "/send/m.room.message",
			headers = {
				"Authorization": "Bearer " + this.token
			},
			json = {
				"msgtype": "m.text",
				"body": this.message
			}
		)
		logging.info(response.text)