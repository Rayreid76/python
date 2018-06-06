class patient(object):
    id_number = 0
    def __init__(self,name,allergies):
        self.id = patient.id_number
        self.name = name
        self.allergies = allergies
        self.bed_num = None
        patient.id_number += 1

class hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds = self.assign_bed()

    def assign_bed(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "Bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"