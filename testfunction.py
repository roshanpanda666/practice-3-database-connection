#for testing

from db import insert_data ,get_all_data, update_data, delete_data

user={"name": "sabyasachi", "age": 21, "role": "full-stack"}
insert_id=insert_data(user)
print("data inserted ",insert_id)


#read data 
print("\nAll Users:")
users = get_all_data()
for u in users:
    print(u)

# 🛠️ Update a record
update_result = update_data({"name": "Roshan"}, {"role": "Quantum Wizard"})
print("\nUpdated:", update_result.modified_count, "record(s)")

# ❌ Delete a record
delete_result = delete_data({"name": "Roshan"})
print("\nDeleted:", delete_result.deleted_count, "record(s)")