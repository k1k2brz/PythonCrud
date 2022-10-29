"""
참고한 사이트 links:
http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
http://www.pythoncentral.io/introduction-to-sqlite-in-python/
https://gist.github.com/techsharif/7868666b6c6de97cda20941cd2f8c6be
https://blog.naver.com/PostView.nhn?blogId=hankrah&logNo=221929249131

"""


import sqlite3
import subprocess as sp

"""
database code
"""


# 테이블생성
def create_table():
	# DB 오픈
	conn = sqlite3.connect('testdb2.sqlite')
# cursor란 하나의 DB connection에 대하여 독립적으로 SQL 문을 실행할 수 있는 작업환경을 제공하는 객체.
# 하나의 connection에 동시에 한개의 cursor만 생성가능
	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS student(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT,
	        phone TEXT
	    )
	'''
#  SQL 쿼리를 실행
	cursor.execute(query)
# 커밋하고 닫기
	conn.commit()
	conn.close()


# Create
def add_student(roll,name,phone):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO student( roll, name, phone )
	    	        VALUES ( ?,?,? )
	'''

	cursor.execute(query,(roll,name,phone))

	conn.commit()
	conn.close()


# READ
def get_students():
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    SELECT roll, name, phone
	    FROM student
	'''

	cursor.execute(query)
	#  데이터 fetch (배열 형식으로 저장해주는 fetchall)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def get_student_by_roll(roll):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    SELECT roll, name, phone
	    FROM student
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

# Update
def update_student(roll,name,phone):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    UPDATE student
	    SET name = ?, phone = ?
	    WHERE roll = ?
	'''

	cursor.execute(query,(name,phone,roll))

	conn.commit()
	conn.close()

# Delete
def delete_student(roll):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM student
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



create_table()



"""
main code
"""

# Create
def add_data(id_,name,phone):
	add_student(id_,name,phone)
	
def get_data():
	return get_students()

# Read
def show_data():
	students = get_data()
	# 정렬 후 리스트 하나씩 뽑기
	students.sort()
	lst = list(map(list,students))
	for student in lst:
		print(student)

# id번호로 read
def show_data_by_id(id_):
	students = get_student_by_roll(id_)
	lst = list(map(list,students))
	result = []
	for item in lst:
		result.extend(item)
	if not result:
		print("회원번호가 존재하지 않습니다.",id_)
	else:
		print (result)

def select():
	# sp.call('clear',shell=True)
	sel = input("회원정보 추가(c), 리스트 보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)\n\n")
	
	if sel=='c':
		# sp.call('clear',shell=True)
		k = input('회원번호,이름,전화번호 입력: ').split(',')
		id_ = k[0]
		name = k[1]
		phone = k[2]
		add_data(id_,name,phone)
		pr = id_,name,phone
		lst_c = list(pr)
		print(lst_c)
	elif sel=='r':
		# sp.call('clear',shell=True)
		show_data()
		input("\n\n뒤로 가려면 Enter키를 눌러주세요:")
	elif sel=='s':
		# sp.call('clear',shell=True)
		id__ = int(input('검색할 회원번호: '))
		show_data_by_id(id__)
		input("\n\n뒤로 가려면 Enter키를 눌러주세요:")
	elif sel=='u':
		# sp.call('clear',shell=True)
		id__ = int(input('수정할 회원번호: '))
		show_data_by_id(id__)
		print()
		id_ = int(input('회원번호: '))
		name = input('이름: ')
		phone = input('전화번호: ')
		update_student(id__,name,phone)
		input("\n\n데이터가 업데이트 되었습니다. \n뒤로 가려면 Enter키를 눌러주세요:")
	elif sel=='d':
		# sp.call('clear',shell=True)
		id__ = int(input('삭제할 회원번호: '))
		show_data_by_id(id__)
		delete_student(id__)
		input("\n\n데이터가 삭제 되었습니다. \n뒤로 가려면 Enter키를 눌러주세요:")
	else:
		return 0;
	return 1;


while(select()):
	pass