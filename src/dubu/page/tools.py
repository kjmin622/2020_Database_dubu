from .models import *
from django.db import connection

class staff():
    
    def get_staff(dataDir={}):
        try:
            if(dataDir=={}):
                cursor = connection.cursor()
                sqlStr = "select staff_id,first_name,last_name,rank,depart_id,status,bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address,team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id,first_name,last_name,bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info))"
                result = cursor.execute(sqlStr)
                datas = cursor.fetchall()
                connection.close()

                output_data = []
                for data in datas:
                    output_data.append({'staff_id':data[0], 'first_name':data[1], 'last_name':data[2], 'rank':data[3],
                                        'depart_id':data[4], 'status':data[5], 'bank':data[6], 'account':data[7],
                                        'phone':data[8],'wide_area_unit':data[9],'basic_unit':data[10],'street':data[11],'si_gu':data[12],'eub_myeon':data[13],'buildding_number':data[14],'detail_address':data[15], 'team':data[16]})


                return output_data

        except:
            connection.rollback()
            connection.close()
        return None

    def insert_staff(dataDir): 
        # staff_id, rank, status, depart_id,/ staff_id, first_name, last_name, phone, bank, account,
        # / staff_id, wide_area_unit, street, basic_unit, si_gu, eub_myeon, building_number, detail_address
        try:
            staff_id = dataDir["staff_id"];team=dataDir["team"];rank = dataDir["rank"];status = dataDir["status"];depart_id = dataDir["depart_id"];first_name = dataDir["first_name"];last_name = dataDir["last_name"];phone = dataDir["phone"];bank = dataDir["bank"];account = dataDir["account"];wide_area_unit = dataDir["wide_area_unit"];street = dataDir["street"];basic_unit = dataDir["basic_unit"];si_gu = dataDir["si_gu"];eub_myeon = dataDir["eub_myeon"];building_number = dataDir["building_number"];detail_address = dataDir["detail_address"]
            cursor = connection.cursor()
            sqlStr1 = f"insert into page_staff(staff_id,rank,status,depart_id) values('{staff_id}','{rank}','{status}','{depart_id}')"
            sqlStr2 = f"insert into page_staff_info(staff_id,first_name,last_name,phone,bank,account) values('{staff_id}','{first_name}','{last_name}','{phone}','{bank}','{account}')"
            sqlStr3 = f"insert into page_staff_address(staff_id,wide_area_unit,street,basic_unit,si_gu,eub_myeon,building_number,detail_address) values('{staff_id}','{wide_area_unit}','{street}','{basic_unit}','{si_gu}','{eub_myeon}','{building_number}','{detail_address}')"
            sqlStr4 = f"insert into page_team_staff(staff_id,team_name) values('{staff_id}','{team}')"
            cursor.execute(sqlStr1);cursor.fetchall()
            cursor.execute(sqlStr2);cursor.fetchall()
            cursor.execute(sqlStr3);cursor.fetchall()
            cursor.execute(sqlStr4);cursor.fetchall()
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
            cursor1 = connection.cursor();cursor1.execute(sqlStr1);cursor1.fetchall()
            cursor2 = connection.cursor();cursor2.execute(sqlStr2);cursor2.fetchall()
            cursor3 = connection.cursor();cursor3.execute(sqlStr3);cursor3.fetchall()
            cursor4 = connection.cursor();cursor4.execute(sqlStr4);cursor4.fetchall()
            cursor5 = connection.cursor();cursor5.execute(sqlStr5);cursor5.fetchall()
            cursor6 = connection.cursor();cursor6.execute(sqlStr6);cursor6.fetchall()
            connection.commit();connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False
    
    def edit_staff(dataDir):
        try:
            staff_id = dataDir["staff_id"];team=dataDir["team"];rank = dataDir["rank"];status = dataDir["status"];depart_id = dataDir["depart_id"];first_name = dataDir["first_name"];last_name = dataDir["last_name"];phone = dataDir["phone"];bank = dataDir["bank"];account = dataDir["account"];wide_area_unit = dataDir["wide_area_unit"];street = dataDir["street"];basic_unit = dataDir["basic_unit"];si_gu = dataDir["si_gu"];eub_myeon = dataDir["eub_myeon"];building_number = dataDir["building_number"];detail_address = dataDir["detail_address"]
            sqlStr1 = f"update page_staff set rank='{rank}',status='{status}',depart_id='{depart_id}' where staff_id={staff_id}"
            sqlStr2 = f"update page_staff_info set first_name='{first_name}',last_name='{last_name}',phone='{phone}',bank='{bank}',account='{account}') where staff_id={staff_id}"
            sqlStr3 = f"update page_staff_address(wide_area_unit='{wide_area_unit}',street='{street}',basic_unit='{basic_unit}',si_gu='{si_gu}',eub_myeon='{eub_myeon}',building_number='{building_number}',detail_address='{detail_address}') where staff_id={staff_id}"
            sqlStr4 = f"update page_team_staff set team_name='{team}' where staff_id={staff_id}"
            cursor = connection.cursor()
            cursor.execute(sqlStr1);cursor.fetchall()
            cursor.execute(sqlStr2);cursor.fetchall()
            cursor.execute(sqlStr3);cursor.fetchall()
            cursor.execute(sqlStr4);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

