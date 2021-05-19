class Person:
    def person_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_persondet(self):
        print(self.name)
        print(self.age)
        print(self.gender)

class Doctor(Person):
    def doctor_det(self, specialisation,hospital, salary):
        self.specialisation=specialisation
        self.hospital=hospital
        self.salary = salary

    def print_doctor(self):
        print(self.specialisation)
        print(self.hospital)
        print(self.salary)


class Patient(Person):
    def patient_details(self, patient_id,doctor_consulted,disease):
        self.patient_id=patient_id
        self.doctor_consulted=doctor_consulted
        self.disease=disease

    def print_patientdetails(self):
        print(self.patient_id)
        print(self.doctor_consulted)
        print(self.disease)




per = Person()
doc=Doctor()
patnt=Patient()

patnt.person_details("raghu",45,"male")
patnt.print_persondet()
patnt.patient_details("UIY-0986","Dr.Selin","Fever")
patnt.print_patientdetails()

doc.person_details("Dr Selin",47,"female")
doc.print_persondet()
doc.doctor_det("General Medicine","Little Flower Hospital",90000)
doc.print_doctor()
