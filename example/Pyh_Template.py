#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pyh import *

page = PyH('接口测试报告')
page.addCSS('https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css')
Container = page << body(id='Body', cl='bg-warning') << div(id="container",cl="container")

# 报告标题 start
Headrow = Container << div(id="Headrow", cl="row")
Headrow << h1(id="HeadH1",align="center") << strong("API_AutoTest_Report  ",id="HeadTxt") + small("Sonny.zhang", id="author")
Headrow << br()
# 报告标题 end

# 数据统计 start
Totalrow = Container << div(id="Totalrow", cl="Totalrow") << div(cl="jumbotron")
# --测试使用时间，测试用例总数--
test_time_txt = ["测试总耗时：", "0:00:04.307585"]
case_num = ["用例总数：", "7"]
UTimerow = Totalrow << div(id="UTimerow", cl="row")
UTimerow << div(cl="col-xs-12 col-md-6") << p(role="presentation") << span(test_time_txt[0]) << span(test_time_txt[1], cl="label label-default")
UTimerow << div(cl="col-xs-12 col-md-6") << p(role="presentation") << span(case_num[0]) << span(case_num[1],cl="label label-primary")
# --用例失败成功统计--
Num1_txt = ["成功用例数(Pass)：", "3"]
Num2_txt = ["失败用例数(Fail)：", "2"]
Num3_txt = ["出错用例数(Error)：", "2"]
Num4_txt = ["未执行用例数(Block)：", "1"]
Amountrow = Totalrow << div(id="Amountrow", cl="row")
Num1 = Amountrow << div(id="Num1", cl="col-xs-12 col-md-3") << p(role="presentation") << span() << small(Num1_txt[0]) << span(Num1_txt[1], cl="label label-success")
Num2 = Amountrow << div(id="Num2", cl="col-xs-12 col-md-3") << p(role="presentation") << span() << small(Num2_txt[0]) << span(Num2_txt[1], cl="label label-danger")
Num3 = Amountrow << div(id="Num3", cl="col-xs-12 col-md-3") << p(role="presentation") << span() << small(Num3_txt[0]) << span(Num3_txt[1], cl="label label-warning")
Num4 = Amountrow << div(id="Num4", cl="col-xs-12 col-md-3") << p(role="presentation") << span() << small(Num4_txt[0]) << span(Num4_txt[1], cl="label label-default")
# 数据统计 end

# 测试计划 start
Plans = Container << div(id="plans", cl="row")
# --栏目标题--
plans_title = "测试用例摘要"
PlansTitle = Plans << div(id="plans-title", cl="panel panel-primary") << div(cl="panel-heading") << strong() << center(plans_title, cl="text-uppercase")

# --一个测试计划-- start
Plan1 = Plans << div(id="plan1") << table(cl="table table-striped  bg-success")
# ---一个标题--
plan1_title = "测试计划【项目名称：APItest, 计划名称：user_operation】"
Plan1 << center() << caption(plan1_title)
# --一个列表--
# 表头
thead1 = ["ID", "执行编号", "用例ID", "用例外部ID", "用例名称", "用例套件", "执行结果", "运行时间"]
Thead1 = Plan1 << thead()
Thead1 << tr() << th(thead1[0]) + th(thead1[1]) + th(thead1[2]) + th(thead1[3]) + th(thead1[4]) + th(thead1[5]) + th(thead1[6]) + th(thead1[7])
# 表体
tbody1 = ["151", "20180804110924", "1079", "APItest-1", "获取token", "获取token", "Pass", "2018-08-04 11:09:24"]
Error = "Error"
Tbody1 = Plan1 << tbody()
Tbody1 <<tr() << th(tbody1[0], scope="row") + td(tbody1[1]) + td(tbody1[2]) + td(tbody1[3]) + td(tbody1[4]) + td(tbody1[5]) + td(tbody1[6]) + td(tbody1[7])
Tbody1 <<tr() << th(tbody1[0], scope="row") + td(tbody1[1]) + td(tbody1[2]) + td(tbody1[3]) + td(tbody1[4]) + td(tbody1[5]) + td(p(Error, cl="label label-danger")) + td(tbody1[7])
# --一个测试计划-- end
# 测试计划 end

# 测试用例 start
Cases = Container << div(cl="row")
# --栏目标题--
cases_title = "用例执行明细"
CasesTitle = Cases << div(cl="panel panel-primary") << div(cl="panel-heading") << strong(center(cases_title, cl="text-uppercase"))
# --一个计划标题--
Cplan_title = "这是测试计划标题"
CplanTitle = Cases << center() << div(cl="panel panel-danger", style="width:1000px") << div(cl="panel-heading") << strong(center(Cplan_title, cl="text-uppercase"))
# --一个测试用例-- start
Case1 = Cases << div() << table(cl="table table-striped  bg-success")
# ---一个用例标题--
case1_title = "测试计划【项目名称：APItest, 计划名称：user_operation】"
Case1 << center() << caption(case1_title)
# --一个列表--
# 表头
thead1 = ["ID", "执行编号", "用例ID", "用例外部ID", "用例名称", "用例套件", "执行结果", "运行时间"]
Case1Thead1 = Case1 << thead() << tr()
Case1Thead1 << th(thead1[0]) + th(thead1[1]) + th(thead1[2]) + th(thead1[3]) + th(thead1[4]) + th(thead1[5]) + th(thead1[6]) + th(thead1[7])
# 表体
tbody1 = ["151", "20180804110924", "1079", "APItest-1", "获取token", "获取token", "Pass", "2018-08-04 11:09:24"]
Error = "Error"
Case1Tbody1 = Case1 << tbody()
Case1Tbody1 << tr() << th(tbody1[0], scope="row") + td(tbody1[1]) + td(tbody1[2]) + td(tbody1[3]) + td(tbody1[4]) + td(tbody1[5]) + td(tbody1[6]) + td(tbody1[7])
Case1Tbody1 << tr() << th(tbody1[0], scope="row") + td(tbody1[1]) + td(tbody1[2]) + td(tbody1[3]) + td(tbody1[4]) + td(tbody1[5]) + td(p(Error, cl="label label-danger")) + td(tbody1[7])
# --一个测试用例-- end


# --一个计划标题--
Cplan_title = "这是测试计划标题"
CplanTitle = Cases << center() << div(cl="panel panel-danger", style="width:1000px") << div(cl="panel-heading") << strong(center(Cplan_title, cl="text-uppercase"))
# --一个测试用例-- start
Case1 = Cases << div() << table(cl="table table-striped  bg-success")
# ---一个用例标题--
case1_title = "测试计划【项目名称：APItest, 计划名称：user_operation】"
Case1 << center() << caption(case1_title)
# --一个列表--
# 表头
thead1 = ["ID", "执行编号", "用例ID", "用例外部ID", "用例名称", "用例套件", "执行结果", "运行时间"]
Case1Thead1 = Case1 << thead() << tr()
Case1Thead1 << th(thead1[0]) + th(thead1[1]) + th(thead1[2]) + th(thead1[3]) + th(thead1[4]) + th(thead1[5]) + th(thead1[6]) + th(thead1[7])
# 表体
tbody1 = ["151", "20180804110924", "1079", "APItest-1", "获取token", "获取token", "Pass", "2018-08-04 11:09:24"]
Error = "Error"
Case1Tbody1 = Case1 << tbody()
Case1Tbody1 << tr() << th(tbody1[0], scope="row") + td(tbody1[1]) + td(tbody1[2]) + td(tbody1[3]) + td(tbody1[4]) + td(tbody1[5]) + td(tbody1[6]) + td(tbody1[7])
Case1Tbody1 << tr() << th(tbody1[0], scope="row") + td(tbody1[1]) + td(tbody1[2]) + td(tbody1[3]) + td(tbody1[4]) + td(tbody1[5]) + td(p(Error, cl="label label-danger")) + td(tbody1[7])
# --一个测试用例-- end

# 测试用例 end

page.printOut('Pyh_Template.html')