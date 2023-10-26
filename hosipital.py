# Q.Write a program to build a simple hospital management system using Python which can perform the following operations: 
# 1.write a method to takes details from the patient then store.
# 2.write a method to display all the details of patients.
# 3.write a method to search particular patient from the list. search by ID 
# 4.write a method to delete a particular patient details by ID.
# 5.write a method to update a selected patient details by ID. 

class hosipital():
    def __init__(self):
        self.patient_details={}

    def add_patient_details(self,p_name,p_id,p_diseases,op_no):
        self.patient_details[p_id]={"patient_name":p_name,"p_id":p_id,"p_diseases":p_diseases,"op_no":op_no}

    def display_patient_details(self):
        print(self.patient_details)

    def update_patient_details(self,p_name,p_id,p_diseases,op_no):
        self.patient_details[p_id]={"patient_name":p_name,"p_id":p_id,"p_diseases":p_diseases,"op_no":op_no}
    
    def delete_particular_method(self,p_id):
        del self.patient_details[p_id]

    def get_particular_patient_details(self,p_id):
        print(self.patient_details[p_id])

    def with_one_details_of_patient_get_all_details_of_patient(self,p_details):
        for i in self.patient_details:
            self.values=list(self.patient_details[i].values())
            # print(self.values)
            if p_details in self.values:
                print(self.patient_details[i])

h_obj=hosipital()
h_obj.add_patient_details("ganesh",233,"fivar",1)
h_obj.add_patient_details("suresh",234,"fivar",2)
h_obj.update_patient_details("suresh",234,"dengue",3)
# h_obj.display_patient_details()
h_obj.with_one_details_of_patient_get_all_details_of_patient("dengue")