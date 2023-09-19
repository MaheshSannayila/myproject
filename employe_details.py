def get_emp_details(dict_a,domain):
    for i in dict_a:
        # print(dict_a[i])
        for j in dict_a[i]:
            if (dict_a[i][j]) in domain:
                print(dict_a[i])

def emp_addin_dict(no_emp,user_domain):
    dict_a={}
    for i in range(no_emp):
        name=input("name: ")
        domain=input("domain: ")
        emp_id=input("emp_id: ")
        email=input("email: ")

        dict_a[name]={"name":name,"domain":domain,"emp_id":emp_id,"email":email}
    get_emp_details(dict_a,user_domain)

no_emp=int(input("no_of_emp: "))
user_domain=input("which domain details you want: ")
emp_addin_dict(no_emp,user_domain)





