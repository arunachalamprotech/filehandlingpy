name=input("enter name:")
emp_id=int(input("Enter ID:"))
with open("write.txt","a")as file:
    file.write(f"({name}-{emp_id})\n")
print("Completed")