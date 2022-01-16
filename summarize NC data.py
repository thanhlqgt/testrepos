# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:42:19 2021

@author: TLe
"""

import pandas as pd
ncacc_file="//QNAS/Thanh_Data/_Project_work/HSIS_3/Received/NorthCarolina/Accidents/nc18acc.sas7bdat"
nc18acc=pd.read_sas(ncacc_file)

nc18acc.head()
print(nc18acc.groupby(["bikeflag"]).count())
