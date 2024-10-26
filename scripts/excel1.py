from openpyxl import Workbook

wb = Workbook()

ws1 = wb.create_sheet("Linki")
ws2 = wb.create_sheet("Filmweb")
ws3 = wb.create_sheet("Todos")
wb.remove(wb['Sheet'])

ws1 = wb.active

ws1['A4'] = 5
ws2['A4'] = "Hello"

wb.save("Zacniewski-SiST-2024-2025.xlsx")
