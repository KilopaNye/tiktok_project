import matplotlib.pyplot as plt
from model.query_make import *


def plt_make(time_pick,y_set):
    plt.plot(time_pick, y_set,markersize="16", marker=".", label="likes")
    plt.xlabel("Pick_Time")
    plt.ylabel("total_nums")
    plt.legend()
    plt.show()

def total_plt_make(column_name,time_pick,y_set,color):
    plt.plot(time_pick, y_set,markersize="16",color=color, marker=".", label=column_name)
    plt.xlabel("Pick_Time")
    plt.ylabel("total_nums")
    plt.legend()
    plt.show()

def all_plt_make(time_pick,y_set):
    plt.plot(time_pick, y_set,markersize="16", marker=".", label=["likes","comments","shares","favorites"])
    plt.xlabel("Pick_Time")
    plt.ylabel("total_nums")
    plt.legend()
    plt.show()

def count_plt_make(time_pick,y_set):
    plt.plot(time_pick, y_set,markersize="16",color="green", label="post_count")
    plt.xlabel("Pick_Time")
    plt.ylabel("total_nums")
    plt.legend()
    plt.show()


def plt_qurey_make(post_id):
    set_limit=0
    response = True
    while response:
        print(set_limit)
        response = get_log(set_limit,post_id)
        if response:
            time_pick = []
            y_set = []
            for i in range(len(response)):
                y_set.append(response[i]["likes"])

                time_hour = response[i]["hourly_timestamp"]
                formatted_string = time_hour.strftime("%d%H")
                time_pick.append(formatted_string)
            set_limit+=20
            plt_make(time_pick,y_set)
        else:
            return False

def total_plt_qurey_make(column_name,color="blue"):
    set_limit=0
    response = True
    while response:
        print(set_limit)
        response = get_total_log(set_limit)
        if response:
            time_pick = []
            y_set = []
            for i in range(len(response)):
                y_set.append(response[i][column_name])

                time_hour = response[i]["hourly_timestamp"]
                formatted_string = time_hour.strftime("%d%H")
                time_pick.append(formatted_string)
            set_limit+=25
            
            total_plt_make(column_name,time_pick,y_set,color)
        else:
            return False

def all_plt_query_make():
    set_limit=0
    response = True
    while response:
        print(set_limit)
        response = get_all_log()
        if response:
            time_pick = []
            y_set = []
            for i in range(len(response)):
                y_set.append([
                            response[i]["likes"],
                            response[i]["comments"],
                            response[i]["shares"],
                            response[i]["favorites"]
                            ])

                time_hour = response[i]["hourly_timestamp"]
                formatted_string = time_hour.strftime("%d%H")
                time_pick.append(formatted_string)
            set_limit+=25
            
            all_plt_make(time_pick,y_set)
        else:
            return False

def count_plt_qurey_make():
    response = get_post_count()
    if response:
        time_pick = []
        y_set = []
        for i in range(len(response)):
            y_set.append(response[i]["post_count"])

            time_hour = response[i]["hourly_timestamp"]
            formatted_string = time_hour.strftime("%d%H")
            time_pick.append(formatted_string)
        
        count_plt_make(time_pick,y_set)
    else:
        return False