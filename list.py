shopping_list = ["Milk","Bread","spam","Tea","Biscuit"]
# for item in shopping_list:
#     print("buy {}".format(item))

# for item in shopping_list:
#     if item != "spam":
#         print("buy {}".format(item))
 # examples of continue :
# for item in shopping_list:
#     if item =="spam":
#         continue
#     print("buy {}".format(item))

item_to_find = "spam"
found_at = None
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("{0} is at {1}".format(item_to_find,found_at))