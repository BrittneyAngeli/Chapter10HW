

class Patient: 

    def __init__(self, patientID, patientName, address, phone, veteran_status):
        self.__patientID = patientID
        self.__patientName = patientName
        self.__address = address
        self.__phone = phone 
        self.__veteran_status = veteran_status

    def get_patientID(self):
        return self.__patientID

    def get_patientName(self):
        return self.__patientName 

    def get_address(self):
        return self.__address 

    def get_phone(self):
        return self.__phone 

    def get_veteran_status(self):
        return self.__veteran_status