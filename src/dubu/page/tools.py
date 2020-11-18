from .models import *
from django.db import connection

class Staff():

    def get_staff(staff_id=""):
        try:
            cursor = connection.cursor()
            #sqlStr = "select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id, first_name, last_name, bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info on page_staff_info.staff_id = page_staff_address.staff_id))"
            sqlStr = "select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name,depart_name,position from page_depart natural join (select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id, first_name, last_name, bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info on page_staff_info.staff_id = page_staff_address.staff_id)))"
            result = cursor.execute(sqlStr)
            datas = cursor.fetchall()
            connection.close()

            if(staff_id!=""):
                for data in datas:
                    if(data[0]==staff_id):
                        return {'staff_id':data[0], 'first_name':data[1], 'last_name':data[2], 'rank':data[3],
                                    'depart_id':data[4], 'status':data[5], 'bank':data[6], 'account':data[7],
                                    'phone':data[8],'wide_area_unit':data[9],'basic_unit':data[10],'street':data[11],'si_gu':data[12],'eub_myeon':data[13],'buildding_number':data[14],'detail_address':data[15], 'team':data[16], 'depart_name':data[17],'depart_position':data[18]}
                return None

            output_data = []
            for data in datas:
                output_data.append({'staff_id':data[0], 'first_name':data[1], 'last_name':data[2], 'rank':data[3],
                                    'depart_id':data[4], 'status':data[5], 'bank':data[6], 'account':data[7],
                                    'phone':data[8],'wide_area_unit':data[9],'basic_unit':data[10],'street':data[11],'si_gu':data[12],'eub_myeon':data[13],'buildding_number':data[14],'detail_address':data[15], 'team':data[16], 'depart_name':data[17],'depart_position':data[18]})

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
            sqlStr1 = f"update page_staff set rank='{rank}',status='{status}',depart_id='{depart_id}' where staff_id='{staff_id}'"
            sqlStr2 = f"update page_staff_info set first_name='{first_name}',last_name='{last_name}',phone='{phone}',bank='{bank}',account='{account}' where staff_id='{staff_id}'"
            sqlStr3 = f"update page_staff_address set wide_area_unit='{wide_area_unit}',street='{street}',basic_unit='{basic_unit}',si_gu='{si_gu}',eub_myeon='{eub_myeon}',building_number='{building_number}',detail_address='{detail_address}' where staff_id='{staff_id}'"
            sqlStr4 = f"update page_team_staff set team_name='{team}' where staff_id='{staff_id}'"
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
    
    def get_staff_working():
        try:
            cursor = connection.cursor()
            sqlStr = "select staff_id, x_day, work_time_start, work_time_end, id from page_staff_working_info"
            result = cursor.execute(sqlStr)
            datas = cursor.fetchall()
            connection.close()
            output_data = []
            for data in datas:
                output_data.append({"staff_id":data[0],"x_day":data[1],"work_time_start":data[2],"work_time_end":data[3],"id":data[4]})
            return output_data
        except:
            connection.close()
            return None

    def get_staff_holiday():
        try:
            cursor = connection.cursor()
            sqlStr = "select staff_id, off_start, off_end, day_off_type, is_paid, id from page_staff_day_off_info"
            result = cursor.execute(sqlStr)
            datas = cursor.fetchall()
            connection.close()
            output_data = []
            for data in datas:
                output_data.append({"staff_id":data[0],"off_start":data[1],"off_end":data[2],"day_off_type":data[3],"is_paid":data[4], "id":data[5]})
            return output_data
        except:
            connection.close()
            return None
    
    def insert_staff_working(dataDir):
        try:
            cursor = connection.cursor()
            staff_id=dataDir['staff_id'];x_day=dataDir['x_day'].lower();start=dataDir['work_time_start'];end=dataDir['work_time_end']
            day = ["mon","tues","wednes",'thurs','fri','satur','sun']
            if(x_day.split('_')[0] not in day): raise(ValueError)
            start_h,start_m = list(map(int,start.split(':')))
            end_h,end_m = list(map(int,start.split(':')))
            sqlStr = f"insert into page_staff_working_info(staff_id,x_day,work_time_start,work_time_end) values ('{staff_id}','{x_day}','{start}','{end}')"
            cursor.execute(sqlStr)
            cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False

    def insert_staff_holiday(dataDir):
        try:
            cursor = connection.cursor()
            is_paid = 1 if dataDir['is_paid']=='True' or dataDir['is_paid']=='true' else 2
            sqlStr = f"insert into page_staff_day_off_info(staff_id,off_start,off_end,day_off_type,is_paid) values ('{dataDir['staff_id']}','{dataDir['off_start']}','{dataDir['off_end']}','{dataDir['day_off_type']}','{is_paid}')"
            cursor.execute(sqlStr)
            cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False

    def delete_staff_working(dataDir):
        try:
            cursor = connection.cursor()
            sqlStr = f"delete from page_staff_working_info where id={dataDir['id']}"
            cursor.execute(sqlStr)
            cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False

    def delete_staff_holiday(dataDir):
        try:
            cursor = connection.cursor()
            sqlStr = f"delete from page_staff_day_off_info where id={dataDir['id']}"
            print(sqlStr)
            cursor.execute(sqlStr)
            cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False
        return False
    
    def staff_login_check(request):
        if("staff_id" not in request.session.keys() or request.session["staff_id"] is None):
            return False
        return True

    def staff_working_day(staff_id):
        try:
            cursor = connection.cursor()
            sqlStr = f"select x_day,work_time_start,work_time_end from page_staff_working_info where staff_id='{staff_id}'"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            connection.close()
            datas = []
            for data in result:
                try:
                    datas.append({'x_day':data[0].split('_')[0],'start':data[1],'end':data[2]})
                except:
                    pass
            output = {"mon":[],"tues":[],"wednes":[],'thurs':[],'fri':[],'satur':[],'sun':[]}
            days = ["mon","tues","wednes",'thurs','fri','satur','sun']
            for day in days:
                for data in datas:
                    if(data['x_day']==day):
                        output[day].append(data['start']+'~'+data['end'])
            return output
        except:
            connection.close()
            return None
        
    def change_staff_status(dataDir):
        try:
            staff_id = dataDir["staff_id"];status=dataDir["status"]
            cursor = connection.cursor()
            sqlStr = f"update page_staff set status='{status}' where staff_id='{staff_id}'"
            cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False


            

