
while True:
     print("1. Books Menu ")
     print("2. Students Menu ")
     print("3. Exit ")
     choice= input("Enter your choice: ")

     #BOOKS MENU
     if choice == "1":
         while True:
             print("1.1 Add New Books ")
             print("1.2 Edit Book Status ")
             print("1.3 Discard Books ")
             print("1.4 Search Book based on BookID")
             print("1.5 List books written by an author")
             choice2= input("Enter your choice: ")
             #to add new books
             if choice2 == "1.1":
                  import pickle
                  record= []
                  data= []
                  while True:
                       bookname= input("Enter book name: ")
                       authorname= input("Enter author name: ")
                       bookstatus= "available"
                       bookid= input("Enter book ID: ")
                       data=[bookname, authorname, bookstatus, bookid]
                       record.append(data)
                       choice= input("Do you have more data to enter? (Y/N): ")
                       if choice.upper()=="N":
                            break
                  f= open("Books.dat","ab+")
                  pickle.dump(record,f)
                  print("New data added")                  
                  f.close()
                  break
             #to edit book status    
             elif choice2 == "1.2":
                 import pickle
                 f= open("Books.dat","rb+")             
                 bookrec= pickle.load(f)
                 found= 0
                 bookn= input("Enter book name to edit status: ")
                 for R in bookrec:
                      bn= R[0]                    
                      if bn == bookn:
                           print("Current status: ", R[2])
                           R[2]= input("New status: ")
                           found= 1
                    
                 if found == 1:
                      f.seek(0)
                      pickle.dump(bookrec, f)
                      print("Book status updated")
                 f.close()
                 break
            
             #to delete book    
             elif choice2 == "1.3":
                  import pickle
                  import os
                  f= open( "Books.dat", "rb")
                  f1= open("Temp.dat", "wb")
                  reclst= []
                  r= input("Enter book name to be removed: ")
                  while True:
                       try:
                            reclst= pickle.load(f)
                            for x in reclst:
                                 if x[0] != r:
                                      pickle.dump(reclst,f1)
                                 else:
                                      print("Book not found")
                                 
                       except EOFError:
                            break
                  f.close()
                  f1.close()
                  os.remove("Books.dat")
                  os.rename("Temp.dat", "Books.dat")
                  print("Book removed")
             
             #to search book based on book id
             elif choice2 == "1.4":
                  import pickle
                  book_rec=[]
                  g = open("Books.dat", "rb+")
                  book_rec = pickle.load(g)
                  i= input("Enter book id to search book: ")
                  for r in book_rec:
                       if r[3]== i:
                            print(r[0], r[1])
                  g.close()                       
                  break 

             #to search book by author name
             elif choice2 == "1.5":
                  import pickle
                  book_rec=[]
                  g = open("Books.dat", "rb+")
                  book_rec = pickle.load(g)
                  i= input("Enter author name to search book: ")
                  for r in book_rec:
                       if r[1]== i:
                            print(r[0], r[1])
                  g.close()                       
                  break 
                 

     #STUDENTS MENU
     elif choice == "2":
          while True:
             print("2.1 Add New Students ")
             print("2.2 Issue a Book to a Student ")
             print("2.3 Book Return ")
             print("2.4 List all Students")
             print("2.5 List Students Witholding Books")
             choice3= input("Enter your choice: ")

             #to add new student
             if choice3 == "2.1":
                 import pickle
                 record= []
                 data1= []
                 while True:
                      studentname= input("Enter student name: ")
                      studentrecord= "0"
                      data1=[studentname, studentrecord]
                      record.append(data1)
                      
                      choice= input("Do you have more data to enter? (Y/N): ")
                      if choice.upper()=="N":
                           break
                 f= open("Students.dat","ab+")
                 pickle.dump(record,f)
                 print("New student added")                  
                 f.close()
                 break

             #to issue a book to a student
             elif choice3 == "2.2":
                  studentname1= input("Enter student name to be issued: ")
                  bookn= input("Enter book name to be issued: ")
                  import pickle
                  f= open("Books.dat","rb+")
                  f1= open("Students.dat", "rb+")
                  bookrec= pickle.load(f)
                  studentrec= pickle.load(f1)
                  found= 0
                  for R in bookrec:                    
                       if R[0] == bookn:
                            R[2]= "issued"
                            for S in studentrec:
                                 if (S[0] == studentname1 and S[1] == "0"):
                                      
                                      S[1] = R[3]
                                      found= 1
                                      break
                                      
                    
                  if found == 1:
                       f.seek(0)
                       pickle.dump(bookrec, f)
                       pickle.dump(studentrec, f1)
                       print("Book & Student status updated")
          
                  f.close()
                  break
                  
             #to return a book
             elif choice3 == "2.3":
                  studentname1= input("Enter student name to return: ")
                  bookn= input("Enter book name to be returned: ")
                  import pickle
                  f= open("Books.dat","rb+")
                  f1= open("Students.dat", "rb+")
                  bookrec= pickle.load(f)
                  studentrec= pickle.load(f1)
                  found= 0
                 
                  for R in bookrec:
                                           
                       if R[0] == bookn:
                            
                            R[2]= "available"
                            temp= R[3]
                            for S in studentrec:
                                 if S[0] == studentname1: 
                                      S[1] = "0"
                                      found= 1
                                
                     
                    
                  if found == 1:
                       f.seek(0)
                       pickle.dump(bookrec, f)
                       pickle.dump(studentrec, f1)
                       print("Book & Student status updated")
          
                  f.close()
                  break

             #to list all students
             elif choice3 == "2.4":
                  import pickle
                  stud_rec=[]
                  g = open("Students.dat", "rb+")
                  stud_rec = pickle.load(g)
                  print("Content of the Student file are:")
                  for r in stud_rec:
                       print(r[0], r[1])
                  g.close()                       
                  break
                  
             #to list all students witholding books
             elif choice3 == "2.5":
                  import pickle
                  student1=[]
                  f= open("Students.dat","rb+")
               
                  student1= pickle.load(f)
                  print("Students witholding books are:")
                  for re in student1:
                       if re[1]!= "0":
                            print(re)
                  pickle.dump(student1,f)
                  f.close()
                  break

     #EXIT                  
     elif choice == "3":
          print("You have exited")
          break
     
                  
          
             
 
                  
                 
                            
                            
                  

   


    


    

                 
         
         
                
     


    
    
