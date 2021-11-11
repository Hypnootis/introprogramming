# MANUFACTURER_PRODUCTNAME_MODEL_YEAR_MONTH_DAY_C_CATEGORY
products = ["PHILIPS_Boiler_HD4646_2020_09_21_C_1",
            "KENWOOD_KitchenMachine_KVL8300S_2015_09_22_C_3",
            "BOSCH_Blender_MMB65G5M_2016_05_07_C_3",
            "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1",
            "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2",
            "ELECTROLUX_Fridge_ERF4114AOW_2017_11_07_C_2"]

neat_products = []

for i in range(len(products)):
    # Returns a list of the product, variables are list indexes
    split_product = products[i].split("_")

    # Append the product type depending on the category number
    product_type = split_product[-1]
    if product_type == "1":
        product_type = "Small electronics"
        split_product.append(product_type)
    elif product_type == "2":
        product_type = "Appliances"
        split_product.append(product_type)
    elif product_type == "3":
        product_type = "Blenders"
        split_product.append(product_type)
    else:
        product_type = "Other"   # Accounting for other types of products
        split_product.append(product_type)

    neat_products.append(split_product)   # Add the modified product to the list

# neat_products is a list, which contains the products which themselves are lists
# i.e neat_products = [["product1_brand", "product1_specs", "more_specs"],
#                      ["product2_brand", "product2_specs", "more_specs"]]

for i in neat_products:   # Print the variables by accessing the indexes of a product
    print(f"Brand: {i[0]}")
    print(f"Name and model: {i[1]} ({i[2]})")
    print(f"Category: {i[8]}")
    print(f"Addition date: {i[3]}.{i[4]}.{i[5]}\n")
