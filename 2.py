class Website:
    def setDomain(self,domain):
        self.__domain=domain


    def getDomain(self):
        return self.__domain


obj=Website()
obj.setDomain("example.com")
print(obj.getDomain())