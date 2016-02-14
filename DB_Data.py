#
#   this module simulates fetching data from a customer datasource
#

Device_type = {'ASA': [101, 102, 400],
               'NX-OS': [101, 102, 400]
               }

User_ID = {101: {'name':'Paul Stange','mail':'spamm_1@unimatrix01.de','phone':'12345670'},
           102: {'name':'Michael Dombek','mail':'spamm_2@unimatrix01.de','phone':'12345670'},
           400: {'name':'Test User','mail':'spamm_3@unimatrix01.de','phone':'12345670'}}