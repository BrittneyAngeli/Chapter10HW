import PatientClass as pat
import ProcedureClass as proc

# The main function 
def main():

    #Create an object from the Patient class 
    patient = pat.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)
    procedure1 = proc.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    procedure2 = proc.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    procedure3 = proc.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

    print("*** Patient Bill ***")
    print("Name:", patient.get_patientName())
    print("Address:", patient.get_address())
    print("Phone:", patient.get_phone())

    
    print()


    print("Procedure:", patient.get)


main()