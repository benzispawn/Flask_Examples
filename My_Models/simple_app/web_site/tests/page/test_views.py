from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        """ Se a funcionar irá responder sucesso 200 """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200
