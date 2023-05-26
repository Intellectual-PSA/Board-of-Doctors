class Incident:
    def __init__(self, doctor_name, date, details):
        self.doctor_name = doctor_name
        self.date = date
        self.details = details

class Doctor:
    def __init__(self, name):
        self.name = name
        self.incidents = []

    def report_incident(self, date, details):
        incident = Incident(self.name, date, details)
        self.incidents.append(incident)

class BoardOfDirectors:
    def __init__(self):
        self.doctors = {}

    def add_doctor(self, doctor_name):
        if doctor_name not in self.doctors:
            self.doctors[doctor_name] = Doctor(doctor_name)

    def report_incident(self, doctor_name, date, details):
        if doctor_name in self.doctors:
            self.doctors[doctor_name].report_incident(date, details)

    def list_doctors_incidents(self):
        for doctor in self.doctors.values():
            if doctor.incidents:
                print(f"Doctor: {doctor.name}")
                for incident in doctor.incidents:
                    print(f'  Incident Date: {incident.date}, Details: {incident.details}')

# Sample usage
if __name__ == "__main__":
    board = BoardOfDirectors()
    board.add_doctor("Doctor X")
    board.add_doctor("Doctor Y")

    board.report_incident("Doctor X", "2023-05-01", "Suspicion of inappropriate behavior")
    board.report_incident("Doctor X", "2023-05-02", "Suspicion of espionage")
    board.report_incident("Doctor Y", "2023-05-03", "Suspicion of malpractice")

    board.list_doctors_incidents()
