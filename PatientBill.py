import PatientClass as pat
import ProcedureClass as proc

# The main function 
def main():

    #Create patient and procedure objects 
    matt_jones = pat.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)
    physical = proc.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    mri = proc.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    ct_scan = proc.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

    #Set discount and running total amounts 
    vet_discount = .40
    total_bill = 0

    #Display patient bill
    print("*** Patient Bill ***")
    print("Name:", matt_jones.get_patientName() + '\n' + \
        "Address:", matt_jones.get_address() + '\n' + \
        "Phone:", matt_jones.get_phone())
    print()

    #Check patient ID with each of the procedures
    if physical.get_patientID() == matt_jones.get_patientID():
        print("Procedure:", physical.get_proc_name() + '\n' + \
            "Date:", physical.get_proc_date() + '\n' + \
            "Practitioner:", physical.get_pract_name() + '\n' + \
            "Charge: $", format(physical.get_proc_charge(), ',.2f'), sep = '')

        total_bill += float(physical.get_proc_charge())

    print()
    if mri.get_patientID() == matt_jones.get_patientID():
        print("Procedure:", mri.get_proc_name() + '\n' + \
            "Date:", mri.get_proc_date() + '\n' + \
            "Practitioner:", mri.get_pract_name() + '\n' + \
            "Charge: $", format(mri.get_proc_charge(), ',.2f'), sep = '')

        total_bill += float(mri.get_proc_charge())

    print()
    if ct_scan.get_patientID() == matt_jones.get_patientID():
        print("Procedure:", ct_scan.get_proc_name() + '\n' + \
            "Date:", ct_scan.get_proc_date() + '\n' + \
            "Practitioner:", ct_scan.get_pract_name() + '\n' + \
            "Charge: $", format(ct_scan.get_proc_charge(), ',.2f'), sep = '')

        total_bill += float(ct_scan.get_proc_charge())

    #Calculate discounts and total amounts 
    discount_total = total_bill * vet_discount 
    bill_w_discount = total_bill - discount_total

    #Display total charges based on veteran status or not 
    if matt_jones.get_veteran_status() == True:
        print("Total Charges: $", format(bill_w_discount, ',.2f'), sep = '')
    else:
        print("Total Charges: $", format(total_bill, ',.2f'), sep = '')        

main()