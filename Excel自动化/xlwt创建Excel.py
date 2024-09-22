import xlwt

# 创建一个Excel
wb = xlwt.Workbook()
# 选择工作簿
sh = wb.add_sheet("电影")
# 写入数据到单元格中
sh.write(0, 0, "复仇者联盟")
# 保存文件
wb.save("电影数据.xls")
