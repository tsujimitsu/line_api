# coding: utf-8

import os
import json
import requests
import ConfigParser

class LineApi:
    def __init__(self):
        # API endpoint
        self.api_endpoint = 'https://api.line.me/v2'
        
        # API token
        self.api_token = ''
        if os.environ.has_key('AUTH_TOKEN'):
            self.api_token = os.environ['AUTH_TOKEN']
            print('API TOKEN from environment variable.')

        else:
            try:
                config = ConfigParser.ConfigParser()
                config.read('api.env')
                self.api_token = config.get('auth', 'token')
                print('API TOKEN from config file.')
            except Exception as e:
                print e

        # API request header
        self.header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.api_token
        }

    def message_reply(self, reply_token, text):
        payload = {
            "replyToken": reply_token,
            "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
        }
        status = requests.post(self.api_endpoint + '/bot/message/reply', headers=self.header, data=json.dumps(payload))
        return ''

    def message_push(self, send_to, text):
        payload = {
            "to": send_to,
            "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
        }
        status = requests.post(self.api_endpoint + '/bot/message/push', headers=self.header, data=json.dumps(payload))
        return ''

