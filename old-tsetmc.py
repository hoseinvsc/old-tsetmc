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
company_data = line.split('@')[1]
company_data = line.split(';')[5]
company_data = line.split(',')
company_name = company_data[-1]
company_symbol = company_data[-2]
print (company_name)
print("نام شرکت:", company_name, "، نماد شرکت:", company_symbol)




# import requests
# from bs4 import BeautifulSoup

# # آدرس صفحه وب مورد نظر
# url = "http://old.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0"

# # درخواست GET به سرور
# response = requests.get(url)

# # بررسی موفقیت درخواست
# if response.status_code == 200:
#     # تبدیل محتوای صفحه به شیء BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # یافتن تمام اطلاعات مربوط به شرکت‌ها
#     company_data = soup.find_all("tr")
    
#     for data in company_data:
#         # استخراج نام و نماد شرکت از هر خط
#         columns = data.find_all("td")
#         if len(columns) >= 3:
#             company_name = columns[1].text.strip()
#             company_symbol = columns[0].text.strip()
            
#             print("نام شرکت:", company_name, "، نماد شرکت:", company_symbol)
# else:
#     print("خطا در درخواست وب")
