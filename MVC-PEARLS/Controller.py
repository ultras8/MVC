from Model import Model
class Controller:
    def scholar_init(self,input_username,input_password,master):
        model = Model()
        check=0
        for i in model._get_data():
            if input_username == i[0] and input_password == i[1] :
                print("เข้าสู่ระบบสำเร็จ")
                check+=1
                break
        if check == 0:
            print("เข้าสู่ระบบล้มเหลว")
        n = int(input("ใส่ 0 เพื่อกลับไปหน้าแรก")) 
        if n == 0: master.deiconify()
    
    def gui_init(self,input_username,input_password):
        model = Model()
        for i in model._get_data():
            if input_username == i[0] and input_password == i[1] :
                return 1
        return 0