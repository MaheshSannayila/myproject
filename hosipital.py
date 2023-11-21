# Q.Write a program to build a simple hospital management system using Python which can perform the following operations: 
# 1.write a method to takes details from the patient then store.
# 2.write a method to display all the details of patients.
# 3.write a method to search particular patient from the list. search by ID 
# 4.write a method to delete a particular patient details by ID.
# 5.write a method to update a selected patient details by ID. 

class hosipital():
    def __init__(self):
        self.patient_details={}

    def add_patient_details(self):
        p_name=input("enter_patient_name :")
        p_id =input("enther_empolye_id :")
        p_diseases=input("enter patien diseases :")
        op_no=int(input("enter_op_num :"))
        self.patient_details[p_id]={"patient_name":p_name,"p_id":p_id,"p_diseases":p_diseases,"op_no":op_no}

    def display_all_patient_details(self):
        print(self.patient_details)

    def update_patient_details(self):
        p_name=input("enter_patient_name :")
        p_id =input("enther_empolye_id :")
        p_diseases=input("enter patien diseases :")
        op_no=int(input("enter_op_num :"))
        self.patient_details[p_id]={"patient_name":p_name,"p_id":p_id,"p_diseases":p_diseases,"op_no":op_no}
    
    def delete_particular_method(self):
        p_id=input("enter_patient_id :")
        del self.patient_details[p_id]

    def get_particular_patient_details(self,p_id):
        p_id=input("enter_patient_id :")

        print(self.patient_details[p_id])

    def display_particulr_patient_details(self):
        p_details=input("enter_one_of patient_details :")
        for i in self.patient_details:
            self.values=list(self.patient_details[i].values())
            # print(self.values)
            if p_details in self.values:
                print(self.patient_details[i])

h_obj=hosipital()
h_obj.add_patient_details()
# h_obj.add_patient_details()

h_obj.display_all_patient_details()
h_obj.display_particulr_patient_details()

