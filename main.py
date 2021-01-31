# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:24:36 2021

@author: Mad_ToBy
"""
import schedule
import time
import healthreport_auto
import healthreport_gui
while not healthreport_gui.user :
    healthreport_gui.top.mainloop()
healthreport_auto.automateSign(healthreport_gui.user)
'''schedule.every().day.at("08:00").do(healthreport_auto.automateSign,healthreport_gui.user)
while True:
    schedule.run_pending()
    time.sleep(60) 
'''