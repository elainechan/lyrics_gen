from rauth import OAuth2Service

genius = OAuth2Service(
	client_id="",
	client_secret="",
	name="",
	authorize_url="",
	access_token_url="",
	base_url="",
	)

redirect_uri = "",
params = {
	
	}

url = genius.get_authorize_url(**params)