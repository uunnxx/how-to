from typing import NewType
from pydantic import BaseModel


PatientId = NewType('PatientId', int)
PrescriptionId = NewType('PrescriptionId', int)


class Patient(BaseModel):
    patient_id: PatientId
    first_name: str
    last_name: str
    phone: str


class ActiveComponent(BaseModel):
    name: str
    unit: str
    amount: float


class Medicine(BaseModel):
    name: str
    active_component: ActiveComponent


class Prescription(BaseModel):
    prescription_id: PrescriptionId
    assign_date: Date
    patient: Patient
    medicines: list[Medicine]

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def get_patientt(self, patient_repository: IPatientRepository):
        return patient_repository.get(self.patient_id)

    def get_alternative_medicine(self, medicine_repository: IMedicineRepository):
        for medicine in self.medicines:
            yield medicine_repository.get_by_active_component_name(medicine.active_component.name)

