# Sample data: list of dictionaries representing sales records
sales_data = [
    {'fruit': 'peaches', 'price': 1.41, 'quantity': 3},
    {'fruit': 'pears', 'price': 1.21, 'quantity': 2},
    {'fruit': 'mangoes', 'price': 0.56, 'quantity': 3},
]
# Using a lambda function to calculate total sales for each record

# **entry es una forma de desempaquetar el diccionario
transformed_data = list(
                        map(
                            lambda entry: {**entry, 'total_sales': round(entry['price'] * entry['quantity'], 2)},
                            sales_data
                        )
                    )

# Print the transformed data
for record in transformed_data:
    print(record)