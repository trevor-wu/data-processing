import pandas as pd
import numpy as np
import os
from pathlib import Path
from fremontdropbox_flow import get_dropbox_location

dropbox_dir = get_dropbox_location()
ADT_dir = dropbox_dir + '/Private Structured data collection/Data processing/Raw/Demand/Flow_speed/ADT'
PeMs_dir = dropbox_dir + '/Private Structured data collection/Data processing/Raw/Demand/PeMs'
local_download =  str(os.path.join(Path.home(), "Downloads"))
Processed_dir = dropbox_dir + '/Private Structured data collection/Data processing/Temporary exports to be copied to processed data/Flow_processed'
#directory to year reformat
City_dir = Processed_dir + "/" + "City"

def parse_2013(line, w):
    year = 2013
    splitted = line.split(",")
    if len(splitted) == 2:
        id_flow, title = splitted
    else: 
        id_flow, title = splitted[0], splitted[1]
    title = title.replace('\n', '')
    if title == '':
        return
    if "EB " not in title and "WB " not in title:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/" + title.split('.x')[0] + ".csv")
        for c in data.columns:
            if data[c].count() == 0:
                data = data.drop(columns=c)
        col = data.columns
        day = data[col[1]][0]
        direction1 = data[col[3]].to_numpy()[:data[col[3]].count()]
        direction2 = data[col[4]].to_numpy()[:data[col[4]].count()]
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + col[3] + "," + day)
        for i in direction1:
            w.write("," + str(((int)(i))))
        w.write("\n" + str(year) + "," + title + "," + str(((int)(id_flow)) + 1) + "," + col[4] + "," + day)
        for i in direction2:
            w.write("," + str(((int)(i))))
    else:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/" + title.split('.x')[0] + ".csv")
        for c in data.columns:
            if data[c].count() == 0:
                data = data.drop(columns=c)
        col = data.columns
        day = data[col[1]][0]
        direction = data[col[3]].to_numpy()[:data[col[3]].count()]
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + col[3] + "," + day)
        for i in direction:
            w.write("," + str(((int)(i))))


def parse_2015(line, w):
    year = 2015
    id_flow, title = line.split(",")
    title = title.replace('\n', '')
    if title == '':
        return
    if "EB " not in title and "WB " not in title:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/" + title.split('.x')[0] + ".csv")
        for c in data.columns:
            if data[c].count() == 0:
                data = data.drop(columns=c)
        col = data.columns
        day = data[col[1]][0]
        direction1 = data[col[3]].to_numpy()[:data[col[3]].count()]
        direction2 = data[col[4]].to_numpy()[:data[col[4]].count()]
        
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + col[3] + "," + day)
        for i in direction1:
            w.write("," + str(((int)(i))))
        w.write("\n" + str(year) + "," + title + "," + str(((int)(id_flow)) + 1) + "," + col[4] + "," + day)
        for i in direction2:
            w.write("," + str(((int)(i))))
    else:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/" + title.split('.x')[0] + ".csv")
        for c in data.columns:
            if data[c].count() == 0:
                data = data.drop(columns=c)
        col = data.columns
        day = data[col[1]][0]
        direction = data[col[3]].to_numpy()[:data[col[3]].count()]
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + col[3] + "," + day)
        for i in direction:
            w.write("," + str(((int)(i))))


def parse_2017(line, w):
    year = 2017
    splitted = line.split(",")
    if len(splitted) == 2:
        id_flow, title = splitted
    else: 
        id_flow, title = splitted[0], splitted[1]
    title = title.replace('\n', '')
    if title == '':
        return
    if ".pdf" in title:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/Format from pdf/" + title.split('.p')[0] + ".csv")
        day = data['Day'][0]
        direction = data['Count'].to_numpy()
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + title.split('.p')[0][-2:] + "," + day)
        for i in direction:
            w.write("," + str(((int)(i))))
    elif ".x" in title:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/Format from xlsx/" + title.split('.x')[0] + ".csv")
        day = data['Date'][0]
        col = data.columns
        direction1 = data[col[3]].to_numpy()[:data[col[3]].count()]
        direction2 = data[col[4]].to_numpy()[:data[col[4]].count()]
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + col[3] + "," + day)
        for i in direction1:
            w.write("," + str(((int)(i))))
        w.write("\n" + str(year) + "," + title + "," + str(((int)(id_flow)) + 1) + "," + col[4] + "," + day)
        for i in direction2:
            w.write("," + str(((int)(i))))
    else:
        print('2017 error')
        print("ERROR HERE")
        return -1


def parse_2019(line, w):
    year = 2019  # Edson: I added this line, check if its correct
    splitted = line.split(",")
    if len(splitted) == 2:
        id_flow, title = splitted
    else: 
        id_flow, title = splitted[0], splitted[1]
    title = title.replace('\n', '')
    filename = get_file_name(title)

    # Don't parse files known to be erroneous
    if filename in ERRONEOUS_FILES:
        print("file not processed: ", filename)
        return

    if title == '':
        return
    if ".pdf" in title:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/Format from pdf/" + title.split('.p')[0] + ".csv")
        day = data['Day'][0]
        direction = data['Count'].to_numpy()

        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + title.split('.p')[0][-2:] + "," + day)
        for i in direction:
            w.write("," + str(((int)(i))))
    elif ".x" in title:
        data = pd.read_csv(Processed_dir + "/City/" + str(year) + " reformat/Format from xlsx/" + title.split('.x')[0] + ".csv")
        col = data.columns
        day = data[col[6]][0]
        for c in data.columns:
            if (data[c].sum() == 0):
                data = data.drop(columns=c)
        col = data.columns
        direction1 = data[col[2]].to_numpy()[:data[col[2]].count()]
        direction2 = data[col[3]].to_numpy()[:data[col[3]].count()]
        w.write("\n" + str(year) + "," + title + "," + id_flow + "," + col[2] + "," + day)
        for i in direction1:
            w.write("," + str(((int)(i))))
        w.write("\n" + str(year) + "," + title + "," + str(((int)(id_flow)) + 1) + "," + col[3] + "," + day)
        for i in direction2:
            w.write("," + str(((int)(i))))
    else:
        print('2019 error')
        print(line)
        print("ERROR HERE")
        return -1

def parse_PeMS(line, w):
    splitted = line.split(",")
    if len(splitted) == 2:
        id_flow, id_pems = splitted
    else: 
        id_flow, id_pems = splitted[0], splitted[1]
    id_pems = id_pems.replace('\n', '')
    data_flow = ""
    w.write("\nPeMS Detector " + id_pems + "," + id_flow)
    
    for year in [2013, 2015, 2017, 2019]:
        if (id_flow != "") and (id_pems != ""): 
            excel_dir = PeMs_dir + "/PeMS_" + str(year) + "/" + id_pems + "_" + str(year) + ".xlsx"
            #print(excel_dir)
            xl_file = pd.ExcelFile(excel_dir)
            dfs = {sheet_name: xl_file.parse(sheet_name)
                   for sheet_name in xl_file.sheet_names}
            data = dfs['Report Data']
            data_report = dfs['PeMS Report Description']
            name = data_report['Unnamed: 2'][12]
            if year == 2013:
                w.write("," + name)
            if data['5 Minutes'].shape[0] == 0:
                w.write(",Did not exist in " + str(year) + ",X")
                for k in range(3):
                    for i in range(24):
                        for j in range(4):
                            data_flow += ","
                continue
            day = data['5 Minutes'][0]
            obs = data["% Observed"].mean()
            direction_tmp = data['Flow (Veh/5 Minutes)'].to_numpy()
            direction = np.zeros(((int)(direction_tmp.shape[0] / 3)))
            for i in range(direction.shape[0]):
                data_flow += "," + str((int)(np.sum([direction_tmp[3 * i + k] for k in range(3)])))
            w.write("," + str(obs) + "," + str(day))
        w.write(data_flow)


def process_data():
    # contains list of processed file names from all years and
    # all file types and from city and PeMS data
    curr_file = open(Processed_dir + "/" + "Flow_processed_tmp.csv", "r", encoding= 'unicode_escape')#encoding='utf-8-sig').strip()
    w = open(Processed_dir + "/" +'Flow_processed_city.csv', 'w')
    w2 = open(Processed_dir + "/" +'Flow_processed_PeMS.csv', 'w')
    legend = "Year,Name,Id,Direction,Day 1"

    # legend for city csv
    for k in range(3):
        for i in range(24):
            for j in range(4):
                legend = legend + ",Day " + str(k + 1) + " - " + str(i) + ":" + str(15 * j)
    w.write(legend)

    # legend for pems csv
    legend2 = "Name,Id,Name PeMS,Observed 2013,Day 2013,Observed 2015,Day 2015,Observed 2017,Day 2017, Observed 2019,Day 2019"
    for year in [2013, 2015, 2017, 2019]:
        for k in range(3):
            for i in range(24):
                for j in range(4):
                    legend2 = legend2 + "," + str(year) + "-Day " + str(k + 1) + " - " + str(i) + ":" + str(15 * j)   
    w2.write(legend2)

    # parse flow processed temp file and write to city or pems csv
    year = 0
    pems = False

    for line in curr_file:
        #check whether we are processing PeMs data or ADT data 
        if 'PeMS' in line:
            pems = True
        elif "ADT" in line:
            pems = False
        #once we have determined which section we belong to, we could start process accordingly
        if pems:
            parse_PeMS(line, w2)
        elif "ADT" in line:
            year = (int)(line.split(',./')[1].split(' ')[0])
        elif year == 2013:
            if parse_2013(line, w) == -1:
                break
        elif year == 2015:
            if parse_2015(line, w) == -1:
                break        
        elif year == 2017:
            if parse_2017(line, w) == -1:
                break
        elif year == 2019:
            if parse_2019(line, w) == -1:
                break
        else:
            print(line)
            print("ERROR")
            break

    curr_file.close()
    w.close()
    w2.close()

def get_file_name(filename):
    filename, file_ext = os.path.splitext(filename)
    return filename

if __name__ == '__main__':
    process_data()
    pass