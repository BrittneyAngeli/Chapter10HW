

class Procedure: 

    def __init__(self, proc_name, proc_date, pract_name, proc_charge, patientID):
        self.__proc_name = proc_name 
        self.__proc_date = proc_date
        self.__pract_name = pract_name 
        self.__proc_charge = proc_charge
        self.__patientID = patientID 

    def get_proc_name(self):
        return self.__proc_name

    def get_proc_date(self):
        return self.__proc_date

    def get_pract_name(self):
        return self.__pract_name

    def get_proc_charge(self):
        return self.__proc_charge

    def get_patientID(self):
        return self.__patientID

