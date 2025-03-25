def get_order_detail_object(order_detail) -> dict:
    return {
        "id": str(order_detail['_id']),
        "customer_name": order_detail['customer_name'],
        "product_name": order_detail['product_name'],
        "quantity": order_detail['quantity'],
        "price": order_detail['price'],
        "date_time": order_detail['date_time']
    }

def list_order_detail_objects(order_details) -> list:
    return [get_order_detail_object(order_detail) for order_detail in order_details]
