# class Student():
#     def __init__(self, name, department, professor, phone, address, grade):
#         self.name = name
#         self.department = department
#         self.professor = professor
#         self.phone = phone
#         self.address = address
#         self.grade = grade

#     def student_info(self):
#         print("-" * 20)
#         print(self.name)
#         print(self.department)
#         print(self.professor)
#         print(self.phone)
#         print(self.address)
#         print(self.grade)
# student1 = Student("emily", "computer engineering", "james", "010-1234-5678", "seoul", "A")
# student2 = Student("alice", "chmical engineering", "david", "010-4321-8765", "busan", "B")
# student1.student_info()
# student2.student_info()
# print(student1.name)

# class WaffleMachine:
#     pass

# waffle = WaffleMachine()

# print(waffle)

# class computer:
#     def set_spac(self, cpu, ram, vga, ssd):
#         self.cpu = cpu
#         self.ram = ram
#         self.vga = vga
#         self.ssd = ssd
        
#     def hardwear_info(self):
#         print("CPU = {}".format(self.cpu))
#         print("RAM = {}".format(self.ram))
#         print("VGA = {}".format(self.vga))
#         print("SSD = {}".format(self.ssd))

# desktop = computer()
# desktop.set_spac("i7", "16GB", "GTX1080", "512GB")
# desktop.hardwear_info()

# notebook = computer()
# notebook.set_spac("i5", "8GB", "MX300", "256GB")
# notebook.hardwear_info()

class Calculator:
    def input_expr(self):
        expr = input("수식을 입력하세요 >> ")
        self.expr = expr
    
    def calculator(self):
        return eval(self.expr)

calc = Calculator()
calc.input_expr()
print("수식 결과는 {} 입니다".format(calc.calculator()))