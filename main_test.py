import weather_app

def test_weather_app():
    weather_app.app.testing = True
    client = weather_app.app.test_client()

    r = client.get('/')
    assert r.status_code != 200
    #assert 'Hello I like to make AI Apps' in r.data.decode('utf-8')