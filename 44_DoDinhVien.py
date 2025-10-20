# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    new_student = {
        'name': name,
        'year_of_birth': year_of_birth,
        'address': address
    }
    student_list.append(new_student)
   """ print(f"Da them sinh vien {name} thanh cong.") """

def print_student_list():
    if not student_list:
        print("Danh sach trong")
        return  
    for student in student_list:
        print(f"Tên: {student['name']}, Năm sinh: {student['year_of_birth']}, Địa chỉ: {student['address']}")
