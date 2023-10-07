# with open('old-tsetmc.txt', 'r') as file:
#     data = file.read()
# lines = data.split('@')
# for line in lines:
#     company_data = line.split(';')
#     for line in lines:
#             company_data = line.split(',')
#             company_name = company_data[-1]
#             company_symbol = company_data[-2]

#             print("نام شرکت:", company_name, "، نماد شرکت:", company_symbol)

with open('old-tsetmc.txt', 'r') as file:
    lines = file.readlines()
line = lines[2]
company_data = line.split(',')
company_name = company_data[-1]
company_symbol = company_data[-2]

print("نام شرکت:", company_name, "، نماد شرکت:", company_symbol)





data = "14020716,61232,0,100,100,0,0,0,0,0,100,,1,154,3,72,1000000.00,1.00,1000,320,,698;2501140308536677,IROATVAF0081,ضتوان1200,اختيارخ توان-15000-"
company_data = data.split(',')
company_name = company_data[-1]
company_symbol = company_data[-2]
print("نام شرکت:", company_name, "، نماد شرکت:", company_symbol)