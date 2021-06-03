import requests

def get_content(html):
	findStr = '"subscriberCountText":{"runs":[{"text":"'
	i = html.index(findStr) + len(findStr)
	count = ''
	while html[i] != '"':
		count += html[i]
		i += 1
	return count

def parser(channel_url):
	html = requests.get('https://www.youtube.com/channel/'+channel_url)
	if html.status_code == 200:
		return get_content(html.text)
	else:
		print("Ошибка!")


print( parser('UCTW2IRG_7ZONYsJZEsB7xdg') )