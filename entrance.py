students_db = [
('Tolu','Paid'),
('Maimunah','Half-paid'),
('Habeeb','No-paid')


]
staff_db=[
('Femi','21'),
('Yemi','02'),

]

user = input(''' 
             WELCOME TO SQI COLLEGE OF ICT
      
      Kindly clarify your identity
      1.Staff
      2.Student
      3.Visitor
      4.None of the above

      option:
''').strip()

if user == '1' or user.capitalize() == 'Staff':
    staff_id = input('ID: ').strip()
    staff_fname= input('first name: ').strip().capitalize()

    fnames = []
    IDs = []

    for fname,id in staff_db:
        fnames.append(fname)
        IDs.append(id)

    if staff_fname in fnames and staff_id in IDs:
        print('Access granted!')    
    else:    
        print('Access denied!')    

elif user == '2' or user.strip().capitalize() == 'Student':
    student_fname = input('First name: ').strip().capitalize()

    student_firstnames = []
    payment_status = []

    for stud,status in students_db:
        student_firstnames.append(stud)
        payment_status.append(status)

    if student_fname in student_firstnames:
        print(f'Welcome {student_fname},Kindly wait,lets verify your payment status')

        _index = student_firstnames.index(student_fname)
        _status = payment_status[_index]
         
        if _status == 'Paid':
            print(f'Great,Welcome to class {student_fname}')
        else:    
            print(f"{student_fname},Your payment status is '{_status}',Kindly visit the frontdesk for clarification")
    else:
        print('Record not found.Try again later or visit the frontdesk')