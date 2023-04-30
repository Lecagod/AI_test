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
        print("execute successful")
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
def create_select_querry_byName(name):
    return f"""select * from `face_info` where face_name = '{name}'"""

#lay du lieu theo id
def create_select_querry_byMSV(MSV):
    return f"""select * from `face_info` where MSV = {MSV}"""

def create_update_state_querry(face_name,MSV):
    return f"""UPDATE	`face_info` SET	IsTrain = 'Y' WHERE	face_name ='{face_name}' AND MSV = '{MSV}'"""

def create_select_nottrain_querry():
    return f"""SELECT	face_name, MSV FROM `face_info` WHERE IsTrain ='N'"""

def create_select_trained_querry():
    return f"""SELECT	face_name, MSV FROM `face_info` WHERE IsTrain ='Y'"""

#them du lieu vao database
def insert_data(cnx,face_name,MSV):
    cursor = cnx.cursor()
    querry = create_insert_querry(face_name,MSV)
    execute_querry(cursor,querry)
    cnx.commit()

#lay du lieu theo ten
def get_data_byName(cursor,name):
    
    querry = create_select_querry_byName(name)
    return get_data_execute(cursor,querry)

#lay du lieu theo id
def get_data_byMSV(cursor,MSV):
    querry = create_select_querry_byMSV(MSV)
    return get_data_execute(cursor,querry)
 
def get_select_data(cursor,face_name,MSV):
    querry = create_select_querry(face_name,MSV)
    return get_data_execute(cursor,querry)

def update_state(cnx,face_name,MSV):
    querry = create_update_state_querry(face_name,MSV)
    execute_querry(cnx.cursor(),querry)
    cnx.commit()

def get_list_to_train(cursor):
    return get_data_execute(cursor,create_select_nottrain_querry())

def get_list_trained(cursor):
    return get_data_execute(cursor,create_select_trained_querry())


#cau lenh tao data base  
createDB_querry = """
CREATE DATABASE IF NOT EXISTS `face_data`;
"""
#Cau lenh lua cho db luc tao
select_DB = """USE `face_data`;"""

#Cau lenh tao table
createTB_querry ="""
CREATE TABLE IF NOT EXISTS `face_info`   (
	`face_id` INT(11) NOT NULL AUTO_INCREMENT,
	`face_name` VARCHAR(50) NULL DEFAULT 'Human' COLLATE 'utf8mb4_general_ci',
    `MSV` VARCHAR(10) NULL DEFAULT 'Ma sinh vien' COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`face_id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;
"""

# # # #Code chay:
# cnx = connect_to_db('127.0.0.1','root','vlo136fv',1306,'face_data')
# cursor = cnx.cursor()
# # insert_data(cnx,"Phuc","2019601247")
# update_state(cnx,"Phuc","2019601247")
# # data = get_select_data(cursor,"Phuc","2019601247")
# data = get_list_trained(cursor)
# #data = get_data_byName(cursor,"Name")
# print(data)
# close_cnc(cnx)
