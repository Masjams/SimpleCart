import json


def test_product_detail_by_id(client):
    # Test product detail by ID
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get("id")


def test_list_products(client):
    # Test listing products
    response = client.get("/api/products")
    assert response.status_code == 200
    # Optionally, add assertions related to the response content


def test_post_cart(client):
    url = f"/api/cart"
    coupon_code = ""
    shipping_fee = 0
    cart_items = [{"product_id": 6, "qty": 1}]
    payload = {
        "coupon_code": coupon_code,
        "shipping_fee": shipping_fee,
        "cart_items": cart_items,
    }
    response = client.post(url, json=payload)
    assert response.status_code == 200
    if response.status_code == 200:
        assert "data_created"
