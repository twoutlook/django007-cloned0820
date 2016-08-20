from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# class Customer(models.Model):
#     field1 = models.CharField(max_length=200)
#     field2 = models.CharField(max_length=200)
#     field3 = models.CharField(max_length=200)
#     field4 = models.CharField(max_length=200)
#     field5 = models.CharField(max_length=200)
#     def __str__(self):
#         return self.field1

class Spec(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200,verbose_name="規格說明")
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2
class Cust(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2


class Item000(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    field6 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.field1

class Item001(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="幾號機")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")
 
 
#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")

#--- code1 for model.py (end) -----

  
    def __str__(self):
        return self.field1
# 客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%	客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				

class Item003(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="壓鑄機編號")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")
 
 
#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")

#--- code1 for model.py (end) -----

  
    def __str__(self):
        return self.field1



class Item002(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="編號")
    field2 = models.CharField(default=".", max_length=200,verbose_name="客戶")
    field3 = models.CharField(default=".", max_length=200,verbose_name="品名")
    # field4 = models.CharField(default=".", max_length=200,verbose_name="欠料量")
    # field5 = models.CharField(default=".", max_length=200,verbose_name="欠備庫量")
    # field6 = models.CharField(default=".", max_length=200,verbose_name="客訴量")
    # field7 = models.CharField(default=".", max_length=200,verbose_name="模具壽命")
    field4 = models.CharField(default=".", max_length=200,verbose_name="計劃交貨日期")
    field5 = models.CharField(default=".", max_length=200,verbose_name="客戶需求數")
    field6 = models.CharField(default=".", max_length=200,verbose_name="實際出貨數")
    field7 = models.CharField(default=".", max_length=200,verbose_name="延交數量")
    def __str__(self):
        return self.field1
        
        
# class Item004(models.Model):
#     # field1 = models.CharField(primary_key=True,max_length=200,verbose_name="壓鑄機編號")
    
#     field1 = models.CharField(primary_key=True,max_length=200,verbose_name="編號")
#     field2 = models.CharField(default=".", max_length=200,verbose_name="客戶")
#     field3 = models.CharField(default=".", max_length=200,verbose_name="品名")
#     field4 = models.CharField(default=".", max_length=200,verbose_name="欠料量")
#     field5 = models.CharField(default=".", max_length=200,verbose_name="欠備庫量")
#     field6 = models.CharField(default=".", max_length=200,verbose_name="客訴量")
#     field7 = models.CharField(default=".", max_length=200,verbose_name="模具壽命")
#     def __str__(self):
        # return self.field1
class Item004(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="編號")
    field2 = models.CharField(default=".", max_length=200,verbose_name="客戶")
    field3 = models.CharField(default=".", max_length=200,verbose_name="品名")
    # field4 = models.CharField(default=".", max_length=200,verbose_name="欠料量")
    # field5 = models.CharField(default=".", max_length=200,verbose_name="欠備庫量")
    # field6 = models.CharField(default=".", max_length=200,verbose_name="客訴量")
    # field7 = models.CharField(default=".", max_length=200,verbose_name="模具壽命")
    field4 = models.CharField(default=".", max_length=200,verbose_name="計劃交貨日期")
    field5 = models.CharField(default=".", max_length=200,verbose_name="客戶需求數")
    field6 = models.CharField(default=".", max_length=200,verbose_name="實際出貨數")
    field7 = models.CharField(default=".", max_length=200,verbose_name="延交數量")
    def __str__(self):
        return self.field1
