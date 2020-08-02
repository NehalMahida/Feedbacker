class PDF:
    '''facultyname = ""
    subname = ""
    subcode = ""
    program = ""
    department = ""
    semester = ""
    aca_year = ""
    totalStudent = ""
    totalFeedback = ""'''

    def __init__(self, f_name, s_name, c_name, p_name, dept_name, sem, year, t_s, t_f):
        self.facultyname = f_name
        self.subcode = c_name
        self.subname = s_name
        self.program = p_name
        self.department = dept_name
        self.semester = sem
        self.aca_year = year
        self.totalFeedback = t_f
        self.totalStudent = t_s

    def getFacultyname(self):
        return self.facultyname

    def getSubName(self):
        return self.subname

    def getSubcode(self):
        return self.subcode

    def getprogram(self):
        return self.program

    def getDept(self):
        return self.department

    def getSem(self):
        return self.semester
    
    def getAcayear(self):
        return self.aca_year

    def getTotalFeed(self):
        return self.totalFeedback
    
    def getTotalStu(self):
        return self.totalStudent
