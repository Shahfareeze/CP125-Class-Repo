def compare_prices(store_a, store_b):
    # TODO: Your code here

    products = {
        "only_a": [],
        "a_cheaper": [],
        "b_cheaper": []
    }

    for product in store_a:
        if product not in store_b:
            products["only_a"].append(product)
            continue

        if store_a[product] < store_b[product]:
            products["a_cheaper"].append(product)
        elif store_a[product] > store_b[product]:
            products["b_cheaper"].append(product)


    products["only_a"] = sorted(products["only_a"])
    products["a_cheaper"] = sorted(products["a_cheaper"])
    products["b_cheaper"] = sorted(products["b_cheaper"])

    return products



store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
