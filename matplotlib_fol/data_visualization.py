import matplotlib.pyplot as plt

# Line Plot 
months = ["Jan","Feb","Mar","Apr","May"]
sales = [200,250,300,280,350]

plt.plot(months, sales, color="blue", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.savefig("line_sales.png")
plt.show()


# Bar Chart 
departments = ["HR","IT","Sales","Marketing"]
employees = [10,25,18,15]

plt.bar(departments, employees, color="purple")
plt.title("Employees in Departments")
plt.xlabel("Departments")
plt.ylabel("Number of Employees")
plt.savefig("bar_employees.png")
plt.show()


# Scatter Plot 
study_hours = [1,2,3,4,5]
marks = [40,50,65,70,85]

plt.scatter(study_hours, marks, color="green")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("scatter_marks.png")
plt.show()


# Histogram 
ages = [18,19,20,21,22,20,19,23,24,21]

plt.hist(ages, bins=5, color="orange", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("histogram_age.png")
plt.show()


# Pie Chart 
courses = ["Python","Java","C++","Data Science"]
students = [35,25,20,20]

plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Enrollment Percentage")
plt.savefig("pie_courses.png")
plt.show()

# Area plot
days = [1,2,3,4,5]
visitors = [100,120,150,170,200]

plt.fill_between(days, visitors, color="skyblue")
plt.title("Website Visitors Growth")
plt.xlabel("Days")
plt.ylabel("Visitors")
plt.savefig("area_visitors.png")
plt.show()