# # -*- coding:utf-8 -*-
# # /usr/bin/env python
# """
# Author: Tong Du
# date: 2020/2/29 21:33
# Email: dtshare@126.com
# desc:
# """
# from .fund_simu import SimuAgent
#
# simu_agent = SimuAgent()
#
#
# def login(username, password):
#     user_info, msg = simu_agent.login(username, password)
#     return user_info, msg
#
#
# def load_data():
#     df_fundlist, msg = simu_agent.load_data()
#     return df_fundlist, msg
#
#
# def get_fund_list():
#     return simu_agent.get_fund_list()
#
#
# def get_fund_nav(fund_id, time_span=0):
#     return simu_agent.get_fund_nav(fund_id, time_span)
