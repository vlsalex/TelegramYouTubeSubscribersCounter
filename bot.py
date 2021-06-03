import telebot;
import requests

bot = telebot.TeleBot('<token>')

HEADERS = {
	'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
}

def get_content(html):
	findStr = '"subscriberCountText":{"runs":[{"text":"'
	if findStr in html:
		i = html.index(findStr) + len(findStr)
		count = ''
		while html[i] != '"':
			count += html[i]
			i += 1
		return count
	else:
		return None

def parser(channel_url):
	html = requests.get('https://www.youtube.com/channel/'+channel_url, headers=HEADERS)
	if html.status_code == 200:
		return get_content(html.text)
	else:
		return None

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	messageParts = message.text.split(' ')
	if len(messageParts) == 2 and messageParts[0] == '/get':
		count = parser(messageParts[1])
		if count == None:
			bot.send_message(message.from_user.id, 'Неправильный url канала')
		else:
			bot.send_message(message.from_user.id, count)
	else:
		bot.send_message(message.from_user.id, 'Неправильный синтаксис')

bot.polling(none_stop=True, interval=0)

# /get channel_url