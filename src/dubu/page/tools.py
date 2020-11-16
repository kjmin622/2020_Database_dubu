from .models import *
from django.db import connection

class staff():
    
    def insert_staff(dataDir): 
        # staff_id, rank, status, depart_id,/ staff_id, first_name, last_name, phone, bank, account,
        # / staff_id, wide_area_unit, street, basic_unit, si_gu, eub_myeon, building_number, detail_address
        try:
            staff_id = dataDir["staff_id"];rank = dataDir["rank"];status = dataDir["status"];depart_id = dataDir["depart_id"];first_name = dataDir["first_name"];last_name = dataDir["last_name"];phone = dataDir["phone"];bank = dataDir["bank"];account = dataDir["account"];wide_area_unit = dataDir["wide_area_unit"];street = dataDir["street"];basic_unit = dataDir["basic_unit"];si_gu = dataDir["si_gu"];eub_myeon = dataDir["eub_myeon"];building_number = dataDir["building_number"];detail_address = dataDir["detail_address"]
            cursor = connection.cursor()
            sqlStr1 = f"insert into page_staff(staff_id,rank,status,depart_id) values({staff_id},{rank},{status},{depart_id})"
            sqlStr2 = f"insert into page_staff_info(staff_id,first_name,last_name,phone,bank,account) values({staff_id},{first_name},{last_name},{phone},{bank},{account})"
            sqlStr3 = f"insert into page_staff_address(staff_id,wide_area_unit,streeet,basic_unit,si_gu,eub_myeon,building_number,detail_address) values({staff_id},{wide_area_unit},{street},{basic_unit},{si_gu},{eub_myeon},{building_number},{detail_address})"
            cursor.execute(sqlStr1);cursor.fetchall()
            cursor.execute(sqlStr2);cursor.fetchall()
            cursor.execute(sqlStr3);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False

    def delete_staff(dataDir):
        try:
            staff_id = dataDir["staff_id"]
            sqlStr1 = f"delete from page_staff where staff_id='{staff_id}'"
            sqlStr2 = f"delete from page_staff_info where staff_id='{staff_id}'"
            sqlStr3 = f"delete from page_staff_address where staff_id='{staff_id}'"
            sqlStr4 = f"delete from page_staff_working_info where staff_id='{staff_id}'"
            sqlStr5 = f"delete from page_staff_day_off_info where staff_id='{staff_id}'"
            sqlStr6 = f"delete from page_team_staff where staff_id='{staff_id}'"
            cursor1 = connection.cursor();cursor1.execute(sqlStr1);cursor1.fetchall();connection.commit();connection.close()
            cursor2 = connection.cursor();cursor2.execute(sqlStr2);cursor2.fetchall();connection.commit();connection.close()
            cursor3 = connection.cursor();cursor3.execute(sqlStr3);cursor3.fetchall();connection.commit();connection.close()
            cursor4 = connection.cursor();cursor4.execute(sqlStr4);cursor4.fetchall();connection.commit();connection.close()
            cursor5 = connection.cursor();cursor5.execute(sqlStr5);cursor5.fetchall();connection.commit();connection.close()
            cursor6 = connection.cursor();cursor6.execute(sqlStr6);cursor6.fetchall();connection.commit();connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False