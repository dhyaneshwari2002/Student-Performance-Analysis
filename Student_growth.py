# import pymysql
# # conn=pymysql.connect(host='localhost', user='root', password="", db='',)
# # cursor=conn.cursor()
# # query="CREATE DATABASE Project_Student"
# # try:
# #     cursor.execute(query)
# #     print("Database Created")
# # except Exception as e:
# #     print("Error: ", e)
# # finally:
# #     conn.close()
#
# # conn = pymysql.connect(host='localhost', user='root', password="", db='Project_Student', )
# # cursor = conn.cursor()
# # query = "create table Student(Student_ID int(11) auto_increment primary key, Student_Name varchar(200) NOT NULL, Physics int(20), Chemistry int(20), Mathematics int(20), Standard varchar(30), Remark varchar(30))"
# # try:
# #     cursor.execute(query)
# #     print("Table Created")
# # except Exception as e:
# #     print("Error: ", e)
# # finally:
# #     conn.close()
#
# # conn = pymysql.connect(
# #     host='localhost',
# #     user='root',
# #     password='',
# #     db='Project_Student'
# # )
# #
# # try:
# #     cursor = conn.cursor()
# #
# #     # Define the SQL insert query
# #     query = """
# #     INSERT INTO Student (Student_Name, Physics, Chemistry, Mathematics, Standard, Remark)
# #     VALUES (%s, %s, %s, %s, %s, %s)
# #     """
# #
# #     # List of 20 sample student records
# #     students = [
# #         ("Rohan Mehta", 78, 82, 89, "10th", "Good"),
# #         ("Sneha Sharma", 88, 91, 84, "10th", "Excellent"),
# #         ("Amit Yadav", 65, 70, 60, "10th", "Average"),
# #         ("Priya Verma", 92, 95, 97, "10th", "Outstanding"),
# #         ("Ankit Singh", 55, 60, 58, "10th", "Needs Improvement"),
# #         ("Kavya Jain", 83, 79, 88, "10th", "Good"),
# #         ("Rahul Chauhan", 45, 50, 40, "10th", "Poor"),
# #         ("Neha Dubey", 90, 93, 91, "10th", "Excellent"),
# #         ("Mohit Agarwal", 76, 74, 80, "10th", "Good"),
# #         ("Simran Kaur", 68, 72, 69, "10th", "Average"),
# #         ("Arjun Desai", 88, 85, 90, "10th", "Excellent"),
# #         ("Ishita Rao", 95, 98, 97, "10th", "Outstanding"),
# #         ("Ravi Patel", 54, 52, 59, "10th", "Needs Improvement"),
# #         ("Tanvi Bansal", 73, 75, 70, "10th", "Good"),
# #         ("Nikhil Reddy", 60, 65, 63, "10th", "Average"),
# #         ("Pooja Joshi", 86, 90, 88, "10th", "Excellent"),
# #         ("Sahil Khan", 47, 49, 45, "10th", "Poor"),
# #         ("Ritika Gupta", 78, 76, 80, "10th", "Good"),
# #         ("Aditya Sinha", 91, 89, 92, "10th", "Excellent"),
# #         ("Meena Kumari", 66, 64, 61, "10th", "Average"),
# #     ]
# #
# #     # Insert all rows
# #     cursor.executemany(query, students)
# #
# #     # Commit the changes
# #     conn.commit()
# #
# #     print("20 student records inserted successfully!")
# #
# # except Exception as e:
# #     print("Error: ", e)
# #
# # finally:
# #     conn.close()
#
# import pymysql
# import matplotlib.pyplot as plt
# #
# # # Connect to the MySQL database
# # conn = pymysql.connect(
# #     host='localhost',
# #     user='root',
# #     password='',
# #     db='Project_Student'
# # )
# #
# # try:
# #     cursor = conn.cursor()
# #
# #     # Query to calculate average marks for each subject
# #     query = """
# #     SELECT
# #         AVG(Physics),
# #         AVG(Chemistry),
# #         AVG(Mathematics)
# #     FROM Student
# #     """
# #
# #     cursor.execute(query)
# #     result = cursor.fetchone()  # Fetch single row with 3 averages
# #
# #     subjects = ['Physics', 'Chemistry', 'Mathematics']
# #     avg_marks = list(result)
# #
# #     # Plotting
# #     plt.figure(figsize=(8, 5))
# #     plt.bar(subjects, avg_marks, color=['#4CAF50', '#2196F3', '#FF5722'])
# #     plt.title('Subject-wise Average Marks')
# #     plt.xlabel('Subjects')
# #     plt.ylabel('Average Marks')
# #     plt.ylim(0, 100)  # Assuming marks are out of 100
# #     plt.grid(axis='y', linestyle='--', alpha=0.7)
# #
# #     # Annotate bar values
# #     for i, val in enumerate(avg_marks):
# #         plt.text(i, val + 1, f"{val:.2f}", ha='center', fontsize=10)
# #
# #     plt.tight_layout()
# #     plt.show()
# #
# # except Exception as e:
# #     print("Error:", e)
# #
# # finally:
# #     conn.close()
#
#
# # Input the student ID you want to analyze
# Standard = (input("Enter Standard: "))
#
# # Connect to the MySQL database
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     db='Project_Student'
# )
#
# try:
#     cursor = conn.cursor()
#
#     # Query to fetch student name and marks based on Student_ID
#     query = """
#     SELECT Student_Name, Physics, Chemistry, Mathematics
#     FROM Student
#     WHERE Standard = %s
#     """
#
#     cursor.execute(query, (Standard,))
#     results = cursor.fetchall()
#
#     if results:
#         for result in results:
#             student_name = result[0]
#             subjects = ['Physics', 'Chemistry', 'Mathematics']
#             marks = list(result[1:])
#
#         # Plotting
#         plt.figure(figsize=(8, 5))
#         plt.bar(subjects, marks, color=['#03A9F4', '#8BC34A', '#FF9800'])
#         plt.title(f"{student_name}'s Performance (ID: {Standard})")
#         plt.xlabel('Subjects')
#         plt.ylabel('Marks')
#         plt.ylim(0, 100)  # Assuming marks are out of 100
#         plt.grid(axis='y', linestyle='--', alpha=0.7)
#
#         # Annotate bar values
#         for i, val in enumerate(marks):
#             plt.text(i, val + 1, str(val), ha='center', fontsize=10)
#
#         plt.tight_layout()
#         plt.show()
#     else:
#         print("No students found in that standard")
#
# except Exception as e:
#     print("Error:", e)
#
# finally:
#     conn.close()
#
# import pymysql
# import matplotlib.pyplot as plt
#
#
# def plot_student_performance(name, standard, marks):
#     subjects = ['Physics', 'Chemistry', 'Mathematics']
#
#     plt.figure(figsize=(8, 5))
#     plt.bar(subjects, marks, color=['#03A9F4', '#8BC34A', '#FF9800'])
#     plt.title(f"{name}'s Performance (Standard: {standard})")
#     plt.xlabel('Subjects')
#     plt.ylabel('Marks')
#     plt.ylim(0, 100)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#
#     for i, val in enumerate(marks):
#         plt.text(i, val + 1, str(val), ha='center', fontsize=10)
#
#     plt.tight_layout()
#     plt.show()
#
#
# # Connect to the MySQL database
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     db='Project_Student'
# )
#
# try:
#     cursor = conn.cursor()
#
#     print("\nChoose an option:")
#     print("1. View individual student by ID")
#     print("2. View all students in a specific standard")
#     print("3. View all students in the database")
#
#     choice = input("Enter your choice (1/2/3): ")
#
#     if choice == '1':
#         student_id = input("Enter Student ID: ")
#         query = """
#             SELECT Student_Name, Standard, Physics, Chemistry, Mathematics
#             FROM Student
#             WHERE Student_ID = %s
#         """
#         cursor.execute(query, (student_id,))
#         result = cursor.fetchone()
#
#         if result:
#             name, standard = result[0], result[1]
#             marks = list(result[2:])
#             plot_student_performance(name, standard, marks)
#         else:
#             print("No student found with that ID.")
#
#     elif choice == '2':
#         standard = input("Enter Standard: ")
#         query = """
#             SELECT Student_Name, Physics, Chemistry, Mathematics
#             FROM Student
#             WHERE Standard = %s
#         """
#         cursor.execute(query, (standard,))
#         results = cursor.fetchall()
#
#         if results:
#             for result in results:
#                 name = result[0]
#                 marks = list(result[1:])
#                 plot_student_performance(name, standard, marks)
#         else:
#             print("No students found in that standard.")
#
#     elif choice == '3':
#         query = """
#             SELECT Student_Name, Standard, Physics, Chemistry, Mathematics
#             FROM Student
#         """
#         cursor.execute(query)
#         results = cursor.fetchall()
#
#         if results:
#             for result in results:
#                 name, standard = result[0], result[1]
#                 marks = list(result[2:])
#                 plot_student_performance(name, standard, marks)
#         else:
#             print("No student records found.")
#
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")
#
# except Exception as e:
#     print("Error:", e)
#
# finally:
#     conn.close()

#
# import pymysql
# import matplotlib.pyplot as plt
#
# # Connect to the MySQL database
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     db='Project_Student'
# )
#
# try:
#     cursor = conn.cursor()
#
#     # Query to count number of students in each remark category
#     query = """
#     SELECT Remark, COUNT(*)
#     FROM Student
#     GROUP BY Remark
#     """
#
#     cursor.execute(query)
#     result = cursor.fetchall()
#
#     # Separate data into labels and counts
#     labels = [row[0] for row in result]
#     counts = [row[1] for row in result]
#
#     # --- Pie Chart ---
#     plt.figure(figsize=(6, 6))
#     plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
#     plt.title("Remark Distribution (Pie Chart)")
#     plt.axis('equal')  # Equal aspect ratio ensures the pie is a circle
#     plt.tight_layout()
#     plt.show()
#
#     # --- Bar Chart ---
#     plt.figure(figsize=(8, 5))
#     plt.bar(labels, counts, color=plt.cm.Pastel1.colors)
#     plt.title("Remark Distribution (Bar Chart)")
#     plt.xlabel("Remark")
#     plt.ylabel("Number of Students")
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#
#     # Annotate bar values
#     for i, val in enumerate(counts):
#         plt.text(i, val + 0.5, str(val), ha='center', fontsize=10)
#
#     plt.tight_layout()
#     plt.show()
#
# except Exception as e:
#     print("Error:", e)
#
# finally:
#     conn.close()