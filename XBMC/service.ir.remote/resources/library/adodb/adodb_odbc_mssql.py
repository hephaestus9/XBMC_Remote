########################################################################
# Vers 2.10 16 July 2008, (c)2004-2008 John Lim (jlim#natsoft.com) All Rights Reserved
# Released under a BSD-style license. See LICENSE.txt.
# Download: http://adodb.sourceforge.net/#pydownload
########################################################################

import adodb,adodb_odbc,datetime

try:
    True, False
except NameError:
    # Maintain compatibility with Python 2.2
    True, False = 1, 0
        
class adodb_odbc_mssql(adodb_odbc.adodb_odbc):
    databaseType = 'odbc_mssql'
    dataProvider = 'odbc'
    sysDate = 'convert(datetime,convert(char,GetDate(),102),102)'
    sysTimeStamp = 'GetDate()'
    
    def _newcursor(self,rs):
        return cursor_odbc_mssql(rs,self)    
        
class cursor_odbc_mssql(adodb_odbc.cursor_odbc):
    def __init__(self,rs,conn):
        adodb_odbc.cursor_odbc.__init__(self,rs,conn)

    def Affected_Rows(self):
        return self._conn.GetOne('select @@rowcount')

    def Insert_ID(self):
        return self._conn.GetOne('select @@IDENTITY')

if __name__ == '__main__':
    db = adodb_odbc_mssql()
    db.Connect("Driver={SQL Server};Server=localhost;Database=northwind;")
    adodb.Test(db)