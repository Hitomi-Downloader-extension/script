def test_download(client):
    r = session.post("http://localhost:8000/download", json={"gal_num": "1570712"})
    assert r.json == {"status":"ok"}
