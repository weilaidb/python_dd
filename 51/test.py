#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,os,sys
from time import ctime,sleep;
reload(sys)
sys.setdefaultencoding('utf8')

print "good,good!"
print 62 *'='  
#write code here begin
# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    print colnames
    list =[]
    list.append(colnames)
    # for rownum in range(1,nrows):
         # row = table.row_values(rownum)
         # if row:
             # app = {}
             # for i in range(len(colnames)):
                # app[colnames[i]] = row[i]
             # list.append(app)
    return list
	
def excel_table_rows(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    return nrows
	
def main():
   # excelfilename = 'test.xlsx'
   excelfilename = u'数据库索引规则.xlsx'
   savetxtfile   = 'cardlog.txt'
   # tables = excel_table_byindex(excelfilename)

   # for row in tables:
       # print row
   log = open(savetxtfile,'w')	   
   rows = excel_table_rows(excelfilename)
   for i in range(0,rows):
      tables = excel_table_byname(excelfilename,i)
      for row in tables:
          print row
          try:
             log.write('\t'.join(row))
          except IOError,e:
		     log.write('no txns this month\n')
		     log.close()
		     return
      log.write('\n')
   log.close()
def progressbar(used,total):
   showchar = '='
   showlen = 30  #显示字符串的总长度
   usedrate = (used * 1.0 /total) 
   unusedrate = ((total - used) * 1.0 /total) 
   usedcharlen = int(showlen * usedrate)
   unusedcharlen = int(showlen -  usedcharlen)
   print '[' + showchar * usedcharlen + ' ' * unusedcharlen +']' + '(' + str(int(100 * usedrate)) + '%)'

if __name__=="__main__":
    main()
    progressbar(10,30)
    progressbar(10,40)	
    progressbar(10,50)
    progressbar(10,60)
    progressbar(10,1000)	
    print '-' * 100
    # sleep(100)