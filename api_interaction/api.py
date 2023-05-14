import requests
import json
import time

endpoint = 'https://api-eu.restb.ai/vision/v2/multipredict'


def get_data_from_image(image_url):
	api_methods = ['caption', 're_features_v4', 're_roomtype_international', 're_condition_r1r6_global']
	image_data = {}
	for api_solution in api_methods:
		payload = {
			# Add the client key to the parameters dictionary
			"client_key": "2882ce7dd9bdae86831d8c60783bf22e1160b02facdc768494e872e387838f73",
			"model_id": api_solution,
			"image_url": image_url
		}
		headers = {
			"X-Client-ID": "01a9a73e",
			"X-Property-ID": "637f2e8ab2cc"
		}

		response = requests.get(endpoint, params=payload, headers=headers)
		data = response.json()
		image_data[api_solution] = data
		time.sleep(3)

	return image_data

	#with open('data.json', 'w', encoding='utf-8') as f:
	#json.dump(image_data, f, ensure_ascii=False, indent=4)




def get_attributes_from_data(image_data):
	try:
		caption = ''
		if image_data['caption'].get('error') == 'false':
			caption = image_data['caption'].get('response').get('solutions').get('caption').get('description')
	except:
		caption = None
	try:
		features = []
		if image_data['re_features_v4'].get('error' == 'false'):
			for detection in image_data['re_features_v4'].get('detections'):
				features.append(detection.get('label'))
	except:
		features = None
	try:
		room_type = ''
		if image_data['re_roomtype_international'].get('error') == 'false':
			room_type = image_data['re_roomtype_international'].get('response').get('solutions').get(
				're_roomtype_international').get('top_prediction').get('label')
	except:
		room_type = None
	try:
		score = 0
		if image_data['re_condition_r1r6_global'].get('error') == 'false':
			score = image_data['re_condition_r1r6_global'].get('response').get('solutions').get(
				're_condition_r1r6_global').get('score')
	except:
		score = None

	info_features = {
		'caption': caption,
		'features': features,
		'room_type': room_type,
		'score': score
	}

	return info_features


def create_estate_description(image_urls):
	for image_url in image_urls:
		data = get_data_from_image(image_url)
		info_photo = get_attributes_from_data(data)


