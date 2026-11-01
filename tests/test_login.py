import tests


def test_login(client_single):
    response = client_single.get('/admin/login')
    content = tests.decode(response)
    assert '<title>Admin - Login</title>' in content
    assert '>Anmelden<' in content
