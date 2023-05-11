import mariadb

#ket noi toi database
def connect_to_db(host_ip,user_name,passwd,port,db):  
    try:
        cnx = None
        cnx = mariadb.connect(
            host = host_ip,
            port = port,
            user = user_name,
            password = passwd,
            database = db)    
       # print("connect successful")
    except mariadb.Error as e:
        print(f"Error: {e}")
    return cnx

#ngat ket noi
def close_cnc(cnx):
    cnx.close()

#thuc hien cau lenh
def execute_querry(cursor,querry):
    try:       
        cursor.execute(querry)
        #print("execute successful")
    except mariadb.Error as e:
        print(f"Error: {e}")

#thuc hien cau lenh tra ve du lieu
def get_data_execute(cursor,querry):
    data = []
    try:      
        cursor.execute(querry)
        # print("execute successful")
    except mariadb.Error as e:
        print(f"Error: {e}")
    for i in cursor:
        data.append(i)
    return data

#tao cau lenh them du lieu
def create_insert_querry(face_name,MSV):
    return f"""insert into `face_info` (face_name, MSV) value ('{face_name}','{MSV}')"""

#cau lenh lay danh sach  
def create_select_querry(face_name,MSV):
    return f"""SELECT	* FROM	`face_info` WHERE face_name = '{face_name}' AND MSV = '{MSV}'"""

#tao cau lenh lay du lieu theo ten
def create_selectID_querry_byName(name):
    return f"""select `face_id` from `face_info` where face_name = '{name}'"""

#lay du lieu theo id
def create_select_querry_byMSV(MSV):
    return f"""select `face_name` from `face_info` where MSV = '{MSV}'"""

def create_select_list():
    return f"""SELECT	face_id,face_name, MSV FROM `face_info` """



#them du lieu vao database
def insert_data(cnx,face_name,MSV):
    cursor = cnx.cursor()
    querry = create_insert_querry(face_name,MSV)
    execute_querry(cursor,querry)
    cnx.commit()

#lay du lieu theo ten
def get_data_byName(cursor,name):
    querry = create_selectID_querry_byName(name)
    return get_data_execute(cursor,querry)

#lay du lieu theo id
def get_data_byMSV(cursor,MSV):
    querry = create_select_querry_byMSV(MSV)
    return get_data_execute(cursor,querry)
 
def get_select_data(cursor,face_name,MSV):
    querry = create_select_querry(face_name,MSV)
    return get_data_execute(cursor,querry)

def get_list(cursor):
    return get_data_execute(cursor,create_select_list())

def get_name_b_MSV(MSV,names):
            for name,msv in names:
                if msv == MSV:
                    return name