from .models import *
from django.db import connection
import time
import datetime

class Staff():

    def get_staff(staff_id=""):
        try:
            cursor = connection.cursor()
            #sqlStr = "select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id, first_name, last_name, bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info on page_staff_info.staff_id = page_staff_address.staff_id))"
            sqlStr = "select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name,depart_name,position from page_depart natural join (select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id, first_name, last_name, bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info on page_staff_info.staff_id = page_staff_address.staff_id)))"
            result = cursor.execute(sqlStr)
            datas = cursor.fetchall()

            output_data = []

            for data in datas:
                output_data.append({'staff_id':data[0], 'first_name':data[1], 'last_name':data[2], 'rank':data[3],
                                    'depart_id':data[4], 'status':data[5], 'bank':data[6], 'account':data[7],
                                    'phone':data[8],'wide_area_unit':data[9],'basic_unit':data[10],'street':data[11],'si_gu':data[12],'eub_myeon':data[13],'buildding_number':data[14],'detail_address':data[15], 'team':data[16], 'depart_name':data[17],'depart_position':data[18], 'rooms':[]})
                sqlStr = f"select room_num from page_rooms where team_name='{data[16]}'"
                cursor.execute(sqlStr);result=cursor.fetchall()
                for room_number in result:
                    output_data[-1]["rooms"].append(room_number[0])
                output_data[-1]["rooms"] = str(output_data[-1]["rooms"]).replace('[','').replace(']','')
            
            connection.close()
            if(staff_id!=""):
                for data in output_data:
                    if(data["staff_id"]==staff_id):
                        return data
                raise ValueError

            return output_data

        except:
            connection.rollback()
            connection.close()
        return None

    def insert_staff(dataDir): 
        # staff_id, rank, status, depart_id,/ staff_id, first_name, last_name, phone, bank, account,
        # / staff_id, wide_area_unit, street, basic_unit, si_gu, eub_myeon, building_number, detail_address
        try:
            staff_id = datetime.datetime.now().strftime("s%Y%m%d%H%M%S%f")[:-6];team=dataDir["team"];rank = dataDir["rank"];status = dataDir["status"];depart_id = dataDir["depart_id"];first_name = dataDir["first_name"];last_name = dataDir["last_name"];phone = dataDir["phone"];bank = dataDir["bank"];account = dataDir["account"];wide_area_unit = dataDir["wide_area_unit"];street = dataDir["street"];basic_unit = dataDir["basic_unit"];si_gu = dataDir["si_gu"];eub_myeon = dataDir["eub_myeon"];building_number = dataDir["building_number"];detail_address = dataDir["detail_address"]
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



class Book():
    def get_parking_info():
        try:
            cursor = connection.cursor()
            sqlStr = "select booking_id, car_number, room_num, spot, team_name from page_booking_rooms natural join (select booking_id, car_number, team_name, spot from page_booking_parking natural join page_parking)"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            output = []
            for data in result:
                output.append({'booking_id':data[0],'car_number':data[1],'room_num':data[2],'spot':data[3],'team_name':data[4]})
            return output
        except:
            connection.close()
            return None
        
    def get_booking_info(member_id=""):
        try:
            cursor = connection.cursor()
            member_booking = []
            if(member_id!=""):
                sqlStr = f"select booking_id from page_member_customer where member_id = '{member_id}'"
                cursor.execute(sqlStr);result=cursor.fetchall()
                for data in result:
                    member_booking.append(data[0])         
            sqlStr = "select booking_id from page_booking"
            cursor.execute(sqlStr);result=cursor.fetchall()
            booking_ids = []
            for data in result:
                booking_ids.append(data[0])

            output = []
            for booking_id in booking_ids:
                if(member_id=="" or booking_id in member_booking):
                    sqlStr = f"select room_num from page_booking_rooms where booking_id = '{booking_id}'"
                    cursor.execute(sqlStr);is_room=cursor.fetchall()
                    if(is_room):
                        sqlStr = f"select booking_id, is_check_in, check_in, check_out,room_type,breakfast,adult_num,child_num,baby_num,extra_text,first_name,last_name,phone,room_num from page_booking natural join (select booking_id, room_num from page_booking_rooms) natural join (select booking_id, room_type, breakfast, adult_num, child_num, baby_num, extra_text from page_book_request) natural join (select booking_id, first_name, last_name from page_customer_info) natural join (select booking_id, phone from page_customer_phone) where booking_id='{booking_id}'"
                    else:
                        sqlStr = f"select booking_id, is_check_in, check_in, check_out, room_type,breakfast,adult_num,child_num,baby_num,extra_text,first_name,last_name,phone from page_booking natural join (select booking_id, room_type, breakfast, adult_num, child_num, baby_num, extra_text from page_book_request) natural join (select booking_id, first_name, last_name from page_customer_info) natural join (select booking_id, phone from page_customer_phone) where booking_id='{booking_id}'"
                    cursor.execute(sqlStr)
                    data=cursor.fetchall()[0]

                    output.append({'booking_id':data[0], 'is_check_in':data[1], 'check_in':data[2], 'check_out':data[3],'room_type':data[4],'breakfast':data[5],'adult_num':data[6],'child_num':data[7],'baby_num':data[8],'extra_text':data[9],'first_name':data[10],'last_name':data[11],'phone':data[12],'room_num': ""})
                    if(is_room):
                        output[-1]["room_num"] = data[13]

            connection.close()
            return output
        except:
            connection.close()
            return None

    def delete_booking(dataDir):
        try:
            cursor = connection.cursor()
            booking_id = dataDir["booking_id"]
            table = ["page_booking","page_booking_rooms","page_book_request",
                    "page_customer_info","page_customer_phone","page_member_customer",
                    "page_booking_parking","page_bill","page_invoice"]

            sqlStrs = []
            for sql in table:
                sqlStrs.append(f"delete from {sql} where booking_id='{booking_id}'")
            
            car_numbers = []
            sqlStr = f"select car_number from page_booking_parking where booking_id='{booking_id}'"
            cursor.execute(sqlStr);result=cursor.fetchall()
            for car in result:
                sqlStrs.append(f"delete from page_parking where car_number = '{car[0]}'")
            
            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()

            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def edit_booking(dataDir):
        try:
            booking_id=dataDir['booking_id'];is_check_in=dataDir['is_check_in'];check_in=dataDir['check_in'];check_out=dataDir['check_out'];room_num=dataDir['room_num'];room_type=dataDir['room_type'];breakfast=dataDir['breakfast'];adult_num=dataDir['adult_num'];child_num=dataDir['child_num'];extra_text=dataDir['extra_text'];first_name=dataDir['first_name'];last_name=dataDir['last_name'];phone=dataDir['phone']
            cursor = connection.cursor()
            sqlStrs = [
                f"update page_booking set is_check_in={is_check_in}, check_in='{check_in}', check_out='{check_out}' where booking_id='{booking_id}'",
                f"update page_booking_rooms set room_num={room_num} where booking_id='{booking_id}'",
                f"update page_book_request set room_type='{room_type}',breakfast='{breakfast}',adult_num='{adult_num}',child_num='{child_num}',baby_num='0',extra_text='{extra_text}' where booking_id='{booking_id}'",
                f"update page_customer_info set first_name='{first_name}',last_name='{last_name}' where booking_id='{booking_id}'",
                f"update page_customer_phone set phone='{phone}' where booking_id='{booking_id}'"
            ]
            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def insert_booking(dataDir):
        try:
            check_in=dataDir['check_in'];check_out=dataDir['check_out'];room_num=dataDir['room_num'];room_type=dataDir['room_type'];breakfast=dataDir['breakfast'];adult_num=dataDir['adult_num'];child_num=dataDir['child_num'];extra_text=dataDir['extra_text'];first_name=dataDir['first_name'];last_name=dataDir['last_name'];phone=dataDir['phone']
            cursor = connection.cursor()
            booking_id = int(time.strftime('%Y%m%d%H%M%S00'))
            FsqlStr = lambda x : f"select * from page_booking where booking_id = '{x}'"
            cursor.execute(FsqlStr(booking_id))
            is_booking = cursor.fetchall()
            while(is_booking):
                booking_id += 1
                cursor.execute(FsqlStr(booking_id))
                is_booking = cursor.fetchall()

            booking_id = str(booking_id)
            sqlStrs = [f"insert into page_booking(booking_id, is_check_in, check_in, check_out) values('{booking_id}',0,'{check_in}','{check_out}')",
                        f"insert into page_booking_rooms(booking_id, room_num) values('{booking_id}',{room_num})",
                        f"insert into page_book_request(booking_id, room_type, breakfast, adult_num, child_num, baby_num, extra_text) values('{booking_id}','{room_type}',{breakfast},{adult_num},{child_num},0,'{extra_text}')",
                        f"insert into page_customer_info(booking_id, first_name, last_name) values('{booking_id}','{first_name}','{last_name}')",
                        f"insert into page_customer_phone(booking_id, phone) values('{booking_id}','{phone}')"
                        ]

            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()
            
            connection.commit()
            connection.close()

            return True

        except:
            connection.rollback()
            connection.close()
            return False

    def insert_book(dataDir, member_id):
        try:
            #'bank': ['카카오'], 'card_1': ['1234'], 'card_2': ['2345'], 'card_3': ['3456'], 'card_4': ['4567'], 'cvc': ['123'], 'date_1': ['11'], 'date_2': ['24'],
            check_in=dataDir['check_in'].replace('-','')+"1600";check_out=dataDir['check_out'].replace('-','')+"1100";room_type=dataDir['room_type'];breakfast=dataDir['breakfast_num'];adult_num=dataDir['adult_num'];child_num=dataDir['child_num'];extra_text=dataDir['extra_text']
            bank=dataDir["bank"];card_1=dataDir["card_1"];card_2=dataDir["card_2"];card_3=dataDir["card_3"];card_4=dataDir["card_4"];cvc=dataDir["cvc"];date=dataDir["date_1"]+"/"+dataDir["date_2"]
            
            cursor = connection.cursor()
            sqlStr= f"select first_name, last_name, phone from page_member_info where member_id='{member_id}'"
            cursor.execute(sqlStr)
            result= cursor.fetchall()
            first_name=result[0][0];last_name=result[0][1];phone=result[0][2]
            
            dbsqlStr= f"insert into page_card_info(card_id, bank, card_number1, card_number2, card_number3, card_number4, cvc, expiration_date) values('{card_1}{card_2}{card_3}{card_4}','{bank}', '{card_1}', '{card_2}', '{card_3}', '{card_4}', '{cvc}', '{date}')"
            cursor.execute(dbsqlStr)
            cursor.fetchall()
            booking_id = int(time.strftime('%Y%m%d%H%M%S00'))
            FsqlStr = lambda x : f"select * from page_booking where booking_id = '{x}'"
            cursor.execute(FsqlStr(booking_id))
            is_booking = cursor.fetchall()
            while(is_booking):
                booking_id += 1
                cursor.execute(FsqlStr(booking_id))
                is_booking = cursor.fetchall()
            
            booking_id = str(booking_id)
            sqlStr=f"insert into page_bill(booking_id, paytime, payment, card_id) values('{booking_id}','','card','{card_1}{card_2}{card_3}{card_4}')"
            cursor.execute(sqlStr)
            cursor.fetchall()
            
            sqlStrs  = [f"insert into page_booking(booking_id, is_check_in, check_in, check_out) values('{booking_id}',0,'{check_in}','{check_out}')",
                        f"insert into page_book_request(booking_id, room_type, breakfast, adult_num, child_num, baby_num, extra_text) values('{booking_id}','{room_type}',{breakfast},{adult_num},{child_num},0,'{extra_text}')",
                        f"insert into page_customer_info(booking_id, first_name, last_name) values('{booking_id}','{first_name}','{last_name}')",
                        f"insert into page_customer_phone(booking_id, phone) values('{booking_id}','{phone}')",
                        f"insert into page_member_customer(booking_id, member_id) values('{booking_id}','{member_id}')"
                        ]

            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()

            connection.commit()
            connection.close()
            return True

        except:
            connection.rollback()
            connection.close()
            return False

    def insert_parking(dataDir):
        # car_number room_num spot team_name
        try:
            car_number=dataDir["car_number"];room_num=dataDir["room_num"];spot=dataDir["spot"];team_name=dataDir["team_name"]
            cursor = connection.cursor()
            sqlStr = f"select booking_id from page_booking_rooms where room_num = {room_num}"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            if(len(result)!=1):
                raise ValueError
            booking_id = str(result[0][0])

            sqlStr = f"select section from page_team where team_name='{team_name}'"
            cursor.execute(sqlStr);result=cursor.fetchall()
            if(not result):
                raise ValueError

            sqlStr = f"insert into page_parking(car_number,team_name,spot) values('{car_number}','{team_name}','{spot}')"
            cursor.execute(sqlStr);cursor.fetchall()
            sqlStr = f"insert into page_booking_parking(booking_id,car_number) values('{booking_id}','{car_number}')"
            cursor.execute(sqlStr);cursor.fetchall()

            return True
            
        except:
            connection.rollback()
            connection.close()
            return False

    def delete_parking(dataDir):
        try:
            car_number = dataDir["car_number"]
            cursor = connection.cursor()
            sqlStr = f"delete from page_parking where car_number='{car_number}'"
            cursor.execute(sqlStr);cursor.fetchall()
            sqlStr = f"delete from page_booking_parking where car_number='{car_number}'"
            cursor.execute(sqlStr);cursor.fetchall()
            return True
        except:
            connection.rollback()
            connection.close()
            return False


    def get_invoice():
        try:
            cursor = connection.cursor()
            sqlStr = "select booking_id, room_num, product_id, name, count, price, order_time, offer_time from ((select offer_time, page_invoice.booking_id booking_id, room_num, product_id, order_time, count, is_payment from page_booking_rooms inner join page_invoice on page_booking_rooms.booking_id = page_invoice.booking_id) natural join (select product_id, name, price from page_product natural join page_product_price)) where is_payment=0"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output = []
            for data in result:
                output.append({'booking_id':data[0], 'room_num':data[1], 'product_id':data[2], 'name':data[3], 'count':data[4], 'price':(str(int(data[5])*int(data[4]))+"("+str(data[5])+"*"+str(data[4])+")"), 'order_time':data[6], 'offer_time':data[7]})

            connection.close()
            return output
        except:
            connection.close()
            return None

    def get_coupon():
        try:
            cursor = connection.cursor()
            sqlStr = "select room_num, member_id, coupon_id, coupon_type, coupon_name, value, min_price from page_coupon_list inner join (select room_num, member_id mid from page_booking_rooms inner join page_member_customer on page_booking_rooms.booking_id=page_member_customer.booking_id) on mid = member_id"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output = []
            for data in result:
                output.append({'room_num':data[0], 'member_id':data[1], 'coupon_id':data[2], 'coupon_type':data[3], 'coupon_name':data[4], 'value':data[5], 'min_price':data[6]})
            connection.close()
            return output

        except:
            connection.close()
            return None

    def get_point():
        try:
            cursor = connection.cursor()
            sqlStr = "select room_num, point from (select room_num, member_id from page_booking_rooms inner join page_member_customer on page_booking_rooms.booking_id=page_member_customer.booking_id) natural join page_member_info"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output = []
            for data in result:
                output.append({'room_num':data[0],'point':data[1]})
            connection.close()
            return output
        except:
            connection.close()
            return None


    def insert_purchase(dataDir):
        try:
            booking_id=dataDir["booking_id"]
            product_id=dataDir["name"]
            order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-4]
            count=dataDir["count"]
            cursor = connection.cursor()

            sqlStr = f"select name from page_product where product_id='{product_id}'"
            cursor.execute(sqlStr);result=cursor.fetchall()
            if(len(result)==0):
                raise ValueError
            if(not count.isdigit()):
                raise ValueError

            sqlStr = f"insert into page_invoice(booking_id,product_id,count,order_time,offer_time,is_payment) values('{booking_id}','{product_id}',{count},'{order_time}','',0)"
            cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def offer_complete(dataDir):
        try:
            cursor = connection.cursor()
            booking_id = dataDir["booking_id"]
            product_id = dataDir["product_id"]
            order_time = dataDir["order_time"]
            offer_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%H:%S:%f")[:-4]
            sqlStr = f"update page_invoice set offer_time = '{offer_time}' where booking_id='{booking_id}' and product_id='{product_id}' and order_time='{order_time}'"
            cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def complete_bill(dataDir):
        try:
            cursor = connection.cursor()
            room_num = dataDir["room_num"];price=dataDir["price"];point=dataDir["point"];coupon_list=dict(dataDir)["coupon_list"]
            sqlStr = f"select page_booking_rooms.booking_id, member_id from page_booking_rooms inner join page_member_customer on page_booking_rooms.booking_id=page_member_customer.booking_id where room_num={room_num}"
            cursor.execute(sqlStr);result=cursor.fetchall()
            booking_id = result[0][0]
            member_id = result[0][1]

            sqlStr = f"update page_invoice set is_payment=1 where booking_id='{booking_id}'"
            cursor.execute(sqlStr);result=cursor.fetchall()

            sqlStr = f"update page_member_info set point=point-{point} where member_id='{member_id}'"
            cursor.execute(sqlStr);result=cursor.fetchall()

            now = datetime.datetime.today()
            strnow = now.strftime("%Y-%m-%d %H:%M:%S:%f")[:2]
            sqlStr = f"update page_bill set paytime={strnow} where booking_id='{booking_id}'"
            cursor.execute(sqlStr);result=cursor.fetchall()

            for coupon_id in coupon_list:
                sqlStr = f"delete from page_coupon_list where coupon_id = '{coupon_id}'"
                cursor.execute(sqlStr);result=cursor.fetchall()

            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def get_room_list():
        try:
            cursor=connection.cursor()
            sqlStr = "select room_num, team_name, room_type from page_rooms"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output = []
            for data in result:
                output.append({"room_num":data[0],"team_name":data[1],"room_type":data[2], "check_in_out":[]})
                sqlStr = f"select booking_id from page_booking_rooms where room_num = {data[0]}"
                cursor.execute(sqlStr);bookid_list=cursor.fetchall()
                for booking_id in bookid_list:
                    sqlStr = f"select check_in, check_out from page_booking where booking_id='{booking_id[0]}'"
                    cursor.execute(sqlStr);t=cursor.fetchall()
                    output[-1]["check_in_out"].append([t[0][0],t[0][1]])
            connection.close()
            return output

        except:
            connection.close()
            return None

    def select_room(dataDir):
        try:
            booking_id=dataDir["booking_id"]
            room_num=dataDir["room_num"]
            cursor = connection.cursor()
            sqlStr = f"select room_num from page_booking_rooms where booking_id='{booking_id}'"
            cursor.execute(sqlStr);result=cursor.fetchall()
            if(len(result)==0):
                sqlStr = f"insert into page_booking_rooms(booking_id,room_num) values('{booking_id}',{room_num})"
                cursor.execute(sqlStr);cursor.fetchall()
            else:
                sqlStr = f"update page_booking_rooms set room_num={room_num} where booking_id='{booking_id}'"
                cursor.execute(sqlStr);cursor.fetchall()
            
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False


class Room():
    def get_room_info():
        try:
            cursor = connection.cursor()

            sqlStr = "select room_num, team_name, room_type from page_rooms"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output_rooms = []
            for data in result:
                output_rooms.append({"room_num":data[0],"team_name":data[1],"room_type":data[2]})
            sqlStr = "select room_type, price, mem_limit from page_room_type"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output_room_type = []
            for data in result:
                output_room_type.append({"room_type":data[0],"price":data[1],"mem_limit":data[2]})
            
            sqlStr = "select bed_type, bed_num, room_type from page_room_type_bed"
            cursor.execute(sqlStr);result=cursor.fetchall()
            output_room_type_bed = []
            for data in result:
                output_rooms.append({"bed_type":data[0],"bed_num":data[1],"room_type":data[2]})
            
            connection.close()
            return (output_rooms,output_room_type,output_room_type_bed)

        except:
            connection.close()
            return (None,None,None)

    def edit_room_type(dataDir):
        try:
            cursor = connection.cursor()
            room_type=dataDir["room_type"];price=dataDir["price"];mem_limit=dataDir["mem_limit"]
            sqlStr = (f"update page_room_type set price={price}, mem_limit={mem_limit} where room_type='{room_type}'")
            cursor.execute(sqlStr);cursor.fetchall()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False



class OtherTool():
    def get_engineering():
        try:
            cursor = connection.cursor()
            sqlStr = "select facility_id, facility_name, team_name, check_date, check_limit, status from page_engineering natural join (select team_name, facility_id from page_engineering_team)"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            output = []
            for data in result:
                output.append({"facility_id":data[0],"facility_name":data[1],"team_name":data[2],"check_date":data[3],"check_limit":data[4],"status":data[5]})
            connection.close()
            return output
        except:
            connection.close()
            return None

    def delete_engineering(dataDir):
        try:
            cursor = connection.cursor()
            facility_id = dataDir["facility_id"]
            sqlStrs = [f"delete from page_engineering where facility_id = '{facility_id}'",
                      f"delete from page_engineering_team where facility_id = '{facility_id}'"]
            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()

            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def edit_engineering(dataDir):
        try:
            cursor = connection.cursor()
            facility_id=dataDir["facility_id"];facility_name=dataDir["facility_name"];team_name=dataDir["team_name"];check_date=dataDir["check_date"];check_limit=dataDir["check_limit"];status=dataDir["status"]
            
            for date in [check_date,check_limit]:
                y,m,d = date.split('-')
                if(int(y)<2000 or int(m)<1 or int(m)>12 or int(d)>31 or int(d)<0):
                    raise ValueError
            
            sqlStr = f"select section from page_team where team_name='{team_name}'"
            cursor.execute(sqlStr);is_team=cursor.fetchall()
            if(not is_team):
                raise ValueError


            sqlStrs = [f"update page_engineering set facility_name='{facility_name}',check_date='{check_date}',check_limit='{check_limit}',status='{status}' where facility_id='{facility_id}'",
                       f"update page_engineering_team set team_name='{team_name}' where facility_id='{facility_id}'"]
            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def insert_engineering(dataDir):
        try:
            cursor = connection.cursor()
            facility_id=datetime.datetime.now().strftime("%Y%m%d");facility_name=dataDir["facility_name"];team_name=dataDir["team_name"];check_date=dataDir["check_date"];check_limit=dataDir["check_limit"];status=dataDir["status"]
            
            for date in [check_date,check_limit]:
                y,m,d = date.split('-')
                if(int(y)<2000 or int(m)<1 or int(m)>12 or int(d)>31 or int(d)<0):
                    raise ValueError
            
            sqlStr = f"select section from page_team where team_name='{team_name}'"
            cursor.execute(sqlStr);is_team=cursor.fetchall()
            if(not is_team):
                raise ValueError

            sqlStrs = [f"insert into page_engineering(facility_id,facility_name,check_date,check_limit,status) values('{facility_id}','{facility_name}','{check_date}','{check_limit}','{status}')",
                        f"insert into page_engineering_team(facility_id,team_name) values('{facility_id}','{team_name}')"]
            for sqlStr in sqlStrs :
                cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

class Product():
    def get_product():
        try:
            cursor = connection.cursor()
            sqlStr = "select product_id,name,price,count from page_product_price natural join page_product natural join page_in_storage"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            output = []
            for data in result:
                output.append({'product_id':data[0],'name':data[1],'price':data[2],'count':data[3]})
            
            connection.close()
            return output
        except:
            connection.close()
            return None

    def edit_product(dataDir):
        try:
            cursor = connection.cursor()
            product_id=dataDir["product_id"];name=dataDir["name"];count=dataDir["count"];price=dataDir["price"]
            sqlStrs = [f"update page_product set name='{name}' where product_id='{product_id}'",
                      f"update page_in_storage set count='{count}' where product_id='{product_id}'",
                      f"update page_product_price set price='{price}' where product_id='{product_id}'"
            ]
            for sqlStr in sqlStrs:
                cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def get_purchase():
        try:
            cursor = connection.cursor()
            sqlStr = "select purchase_id, order_date, delivery_date, is_purchase, staff_id from page_purchase_slip"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            output = []
            for data in result:
                output.append({"purchase_id":data[0],"order_date":data[1],"delivery_date":data[2],"is_purchase":data[3],"staff_id":data[4],"product":[]})
                sqlStr = f"select product_id, count from page_purchase_list where purchase_id={data[0]}"
                cursor.execute(sqlStr)
                product_datas = cursor.fetchall()
                for product in product_datas:
                    output[-1]["product"].append([product[0]])
                    output[-1]["product"][-1].append(product[1])
            return output
        except:
            connection.close()
            return None
    
    def insert_purchase(dataDir):
        try:
            cursor = connection.cursor()
            staff_id=dataDir["staff_id"];product_id_list = dataDir["product_id"];count_list=dataDir["count"]
            now = datetime.datetime.now()
            purchase_id = now.strftime('%Y%m%d%H%M%S')
            order_date = now.strftime('%Y-%m-%d')
            delivery_date = (now + datetime.timedelta(days=7)).strftime('%Y-%m-%d')

        
            sqlStr = f"insert into page_purchase_slip(purchase_id,delivery_date,is_purchase,staff_id,order_date) values('{purchase_id}','{delivery_date}',0,'{staff_id}','{order_date}')"
            cursor.execute(sqlStr);cursor.fetchall()
            
            for i in range(len(product_id_list)):
                sqlStr = f"insert into page_purchase_list(purchase_id,product_id,count) values('{purchase_id}','{product_id_list[i]}',{count_list[i]})"
                cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False

    def complete_purchase(dataDir):
        try:
            cursor = connection.cursor()
            purchase_id = dataDir["purchase_id"]
            sqlStr = f"update page_purchase_slip set is_purchase=1 where purchase_id = '{purchase_id}'"
            cursor.execute(sqlStr);cursor.fetchall()
            
            sqlStr = f"select product_id, count from page_purchase_list where purchase_id = '{purchase_id}'"
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            for data in result:
                sqlStr = f"select count from page_in_storage where product_id='{data[0]}'"
                cursor.execute(sqlStr)
                count = cursor.fetchall()[0][0]
                sqlStr = f"update page_in_storage set count={count+data[1]} where product_id='{data[0]}'"
                cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return True
        except:
            connection.rollback()
            connection.close()
            return False