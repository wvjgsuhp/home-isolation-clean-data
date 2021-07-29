# Clean Data

Clean Data (จัดเรียงที่อยู่ที่ call center พิมพ์เข้าระบบ ให้เป็นคอลัมและถูกต้องตาม format thai address ค่ะ
ผลลัพธ์ที่เราอยากได้ คือ อยากให้ข้อมูลคลีนที่สุด และทดลองนำเข้าระบบ pinpoint geocoding api แล้วได้ผลลัพธ์การ matching ในระดับ B+ ขึ้นได้ คือ ได้พิกัดลึกถึงในหมู่บ้านเดียวกัน หรือซอย
- Quick win: เพื่อให้สามารถนำข้อมูลไปใช้ประโยชน์ได้เร็วที่สุด เบื้องต้นคือต้องคลีนข้อมูลคนไข้ที่เราได้รับมาแล้วให้เรียบร้อย
- Next step: ทำ cleaning script และทำ data pipeline ลิ้งค์กับระบบ call center หน้าบ้านเพื่อ automate การคลีนดาต้าที่จะเข้ามาในอนาคตให้ได้มากที่สุด

### ใครทำโปรเจคนี้ได้บ้าง?
- ใครก็ได้ ไม่จำกัด tools เลยค่ะ เน้นไวและได้ผลลัพธ์ที่ดี
- เนื่องจากข้อมูลที่จะได้รับเป็นข้อมูลคนไข้ และเราเปิด pinpoint api ให้ใช้โดยไม่คิดค่าใช้จ่ายใดๆ

### ขั้นตอนการมีส่วนร่วมในงานนี้
ให้ผู้ใช้ fork repository นี้และแก้ไขฟังก์ชั่น `process_addresses` ใน `model.py` โดยรายละเอียดฟังก์ชั่นจะสามารถอ่านได้จากใน docstring ผู้ใช้สามารถทดสอบได้ว่า output นั้นถูก format ได้หรือไม่ได้วยการรัน

```bash
$ python test.py
```

เพื่อทดสอบว่า output นั้นถูกต้องไหม หากสามารถรันได้โดยไม่มี error สามารถ pull request มาที่ branch นี้ได้

ไฟล์ `server.py` นั้นมีไว้เพื่อเขียนเป็น endpoint โดยจะเรียกฟังก์ชั่น process_address อีกที หากต้องการปรับเปลี่ยนการเขียน server สามารถ pull request มาได้เช่นกัน

### ข้อมูลตัวอย่างและ Output ที่คาดหวัง

สามารถดาวน์โหลดดูข้อมูลตัวอย่างและผลลัพธ์ที่คาดหวังได้ที่ [Sample Data - Train.xlsx](https://drive.google.com/file/d/19LNypJN7lVpLCdo3D9-RWud2W36YBxeA/view?usp=sharing)

#### JSON Format
```json
[
  {
    "id": 1,
    "HouseNumber": "174/243",
    "PremiseName": "คอนโดบ้านสวนอยู่นิรันดร์ ตึกB",
    "Moo": "",
    "SubStreetName": "ศรีพรสวรรค์",
    "StreetName": "",
    "SubDistrict": "สวนใหญ่",
    "District": "เมืองนนทบุรี",
    "Province": "นนทบุรี",
    "PostalCode": "",
    "Other": [
      
    ]
  },
  {
    ...
  }
]
```
