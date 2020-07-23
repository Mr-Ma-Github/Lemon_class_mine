from robot.api import logger
from openpyxl import load_workbook


class myExcelLibrary(object):#类名与模块名保持一致
    '''
                自定义的Excel操作库
                所有的关键字
    '''
    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    
    def __init__(self,flag = None):
        logger.info("初始化一个Excel类")
        pass

    def open_excel(self,filepath):
        '''
        Hello Excel.open it!
        '''
        logger.info("打开Excel文件")
        pass
    
    def select_sheet(self,sheetname=None):
        '''
        select a sheet!
        '''
        logger.info("选择一个表单操作")
        pass
    
    def read_data(self,row,column):
        logger.info("读取数据")
        pass
    
    def add_function(self,a,b):
        return int(a)+int(b)
