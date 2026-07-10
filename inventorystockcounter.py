# Inventory Stock Counter

num_products = int(input("Enter the number of products: "))

product = 1

while product <= num_products:
    print("\nProduct", product)

    quantity = int(input("Enter quantity: "))
    box_size = int(input("Enter box size: "))

    boxes = 0
    packed = 0

    # Nested while loop to pack items into boxes
    while packed < quantity:
        count = 0

        while count < box_size and packed < quantity:
            packed += 1
            count += 1

        boxes += 1

    print("Boxes required:", boxes)

    product += 1

# Final Stock Report using nested for loops
print("\n========== STOCK REPORT ==========")

for i in range(1, num_products + 1):
    print("Product", i, ": ", end="")

    for j in range(5):
        print("*", end=" ")

    print()

print("==================================")