from django.db import models

# Create your models here.

class account_info(models.Model):
    account = models.CharField(max_length=100, primary_key=True)   
    bank = models.CharField(max_length=30)    


class purchase_slip(models.Model):
    purchase_id = models.CharField(max_length=100, primary_key=True)   
    order_date = models.CharField(max_length=20)   
    delivery_date = models.CharField(max_length=20)    
    is_purchase = models.BooleanField()    
    staff_id = models.CharField(max_length=100)    


class team(models.Model):
    team_name = models.CharField(max_length=30, primary_key=True)
    section = models.CharField(max_length=100)


class staff(models.Model):
    staff_id = models.CharField(max_length=100, primary_key=True)   
    rank = models.CharField(max_length=100)   
    status = models.CharField(max_length=100)   
    depart_id = models.CharField(max_length=100)   


class rooms(models.Model):
    room_num = models.IntegerField(primary_key=True)  
    team_name = models.CharField(max_length=30)    
    room_type = models.CharField(max_length=100)   


class engineering(models.Model):
    facility_id = models.CharField(max_length=100, primary_key=True)   
    facility_name = models.CharField(max_length=30)    
    check_date = models.CharField(max_length=20)    
    check_limit = models.CharField(max_length=20)  
    status = models.CharField(max_length=100) 


class depart(models.Model):
    depart_id = models.CharField(max_length=100)   
    depart_name = models.CharField(max_length=100)   
    position = models.CharField(max_length=100)   


class parking(models.Model):
    car_number = models.CharField(max_length=100, primary_key=True)   
    team_name= models.CharField(max_length=30)    
    spot = models.CharField(max_length=100)   


class room_type(models.Model):
    room_type = models.CharField(max_length=100, primary_key=True)   
    price = models.IntegerField()  
    mem_limit = models.IntegerField()
    photo_url = models.CharField(max_length=100)


class event(models.Model):
    event_id = models.CharField(max_length=100, primary_key=True)   
    event_name = models.CharField(max_length=30)   
    start_date = models.CharField(max_length=20) 
    end_date = models.CharField(max_length=20)   
    contents = models.CharField(max_length=2000) 


class booking(models.Model):
    booking_id = models.CharField(max_length=100, primary_key=True)   
    is_check_in = models.BooleanField()    
    check_in = models.CharField(max_length=20)    
    check_out = models.CharField(max_length=20)  


class member_info(models.Model):
    member_id = models.CharField(max_length=100, primary_key=True)   
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=100) 
    membership = models.CharField(max_length=30)    
    point = models.IntegerField()
    birth = models.CharField(max_length=20)  
    is_sms = models.BooleanField()    
       
    


class card_info(models.Model):
    card_id = models.CharField(max_length=100)   
    bank = models.CharField(max_length=30)    
    cvc = models.IntegerField()  
    expiration_date = models.CharField(max_length=20)  
    card_number1 = models.CharField(max_length=10)  
    card_number2 = models.CharField(max_length=10)
    card_number3 = models.CharField(max_length=10)
    card_number4 = models.CharField(max_length=10)


class product(models.Model):
    product_id = models.CharField(max_length=100, primary_key=True)   
    name = models.CharField(max_length=30)    



class event_team(models.Model):
    team_name = models.CharField(max_length=30)    
    event_id = models.CharField(max_length=100)   


class engineering_team(models.Model):
    team_name = models.CharField(max_length=30)    
    facility_id = models.CharField(max_length=100)   


class room_type_bed(models.Model):
    bed_type = models.CharField(max_length=30)    
    bed_num = models.IntegerField()  
    room_type = models.CharField(max_length=100)   


class book_request(models.Model):
    booking_id = models.CharField(max_length=100)  
    room_type = models.CharField(max_length=100)   
    breakfast = models.IntegerField()  
    adult_num = models.IntegerField()  
    child_num = models.IntegerField()  
    baby_num = models.IntegerField()  
    extra_text = models.CharField(max_length=2000,null=True)   


class customer_info(models.Model):
    booking_id = models.CharField(max_length=100)    
    first_name = models.CharField(max_length=30)    
    last_name= models.CharField(max_length=30)    


class member_customer(models.Model):
    booking_id = models.CharField(max_length=100)  
    member_id = models.CharField(max_length=100)   


class booking_rooms(models.Model):
    room_num = models.IntegerField()  
    booking_id = models.CharField(max_length=100)   


class booking_parking(models.Model):
    booking_id = models.CharField(max_length=100)   
    car_number= models.CharField(max_length=100)   


class card_list(models.Model):
    card_id = models.CharField(max_length=100)   
    member_id = models.CharField(max_length=100)   


class invoice(models.Model):
    product_id = models.CharField(max_length=100)   
    order_time = models.CharField(max_length=20) 
    offer_time = models.CharField(max_length=20)   
    is_payment = models.BooleanField()    
    count = models.IntegerField()  
    booking_id = models.CharField(max_length=100)   


class product_price(models.Model):
    product_id = models.CharField(max_length=100)  
    price = models.IntegerField()  


class in_storage(models.Model):
    product_id = models.CharField(max_length=100)  
    count = models.IntegerField()  


class purchase_list(models.Model):
    product_id = models.CharField(max_length=100)   
    count = models.IntegerField()  
    purchase_id = models.CharField(max_length=100)   


class staff_info(models.Model):
    staff_id = models.CharField(max_length=100,primary_key=True)    
    first_name = models.CharField(max_length=30)    
    last_name = models.CharField(max_length=30)    
    phone = models.CharField(max_length=100)  
    bank = models.CharField(max_length=30)  
    account = models.CharField(max_length=100)  


class staff_address(models.Model):
    staff_id = models.CharField(max_length=100,primary_key=True)  
    wide_area_unit = models.CharField(max_length=30)    
    street = models.CharField(max_length=30)    
    basic_unit = models.CharField(max_length=30, null=True)    
    si_gu = models.CharField(max_length=30, null=True)    
    eub_myeon = models.CharField(max_length=30, null=True)    
    building_number = models.CharField(max_length=30)    
    detail_address = models.CharField(max_length=100, null=True)   


class customer_phone(models.Model):
    booking_id = models.CharField(max_length=100)   
    phone = models.CharField(max_length=100)   


class staff_working_info(models.Model):
    staff_id = models.CharField(max_length=100)   
    x_day= models.CharField(max_length=30)    
    work_time_start = models.CharField(max_length=20)   
    work_time_end = models.CharField(max_length=20)  


class staff_day_off_info(models.Model):
    staff_id = models.CharField(max_length=100)   
    off_start = models.CharField(max_length=20) 
    off_end = models.CharField(max_length=20) 
    day_off_type = models.CharField(max_length=100)   
    is_paid = models.BooleanField()    


class team_staff(models.Model):
    staff_id = models.CharField(max_length=100,primary_key=True)   
    team_name = models.CharField(max_length=30)    


class bill(models.Model):
    booking_id = models.CharField(max_length=100)  
    paytime = models.CharField(max_length=20)    
    payment = models.CharField(max_length=30)    
    card_id = models.CharField(max_length=100, null=True)  

class coupon_list(models.Model):
    coupon_id = models.CharField(max_length=100, primary_key=True)
    coupon_type = models.CharField(max_length=100)
    coupon_name = models.CharField(max_length=30)
    value = models.IntegerField()
    min_price = models.IntegerField()
    member_id = models.CharField(max_length=100)

