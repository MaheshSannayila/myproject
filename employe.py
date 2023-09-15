def get_employe_details(employe_name,domain,emp_id,email):

    a={"suresh":{"name":"suresh","domain":"testing","emp_id":182729,"email":"suresh@gmail.com"}}

    a[employe_name]={"employe_name":employe_name,"domain":domain,"emp_id":emp_id,"email":email}
    print(" ")
    print(" ")

    for i ,j in a[employe_name].items():
        print(i,":",j)
        
employe_name=input("name: ")
domain=input("domain: ")
emp_id=input("emp_id: ")
email=input("email: ")
get_employe_details(employe_name,domain,emp_id,email)


            

