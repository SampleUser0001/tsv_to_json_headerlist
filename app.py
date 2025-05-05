#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys

def load_config():
    with open("config.json", "r") as f:
        config = json.loads(f.read())
    return config

def load_tsv(tsv, conf):
    def set_to_dict(header, line, index, d):
        d[header[index]] = line[index]
        return d

    def set_to_list(header, line, index, d, conf):
        if conf["name"] in d: 
            l = d[conf["name"]]
        else:
            l = []

        if line[index] in conf["flag"]:
            l.append(header[index])
        d[conf["name"]] = l
        
        return d
    
    return_list = []

    header = []
    with open(tsv, "r") as f:
        for _ in f.read().splitlines():
            line = _.split("\t")
            if header == []:
                header = line
            else:
                line_data = {}
                name_flg = False
                for i in range(len(header)):
                    if name_flg == False:
                        if conf["start_index"] == i:
                            name_flg = True
                    
                    if name_flg:
                        line_data = set_to_list(header, line, i, line_data, conf)
                    else:
                        line_data = set_to_dict(header, line, i, line_data)
                    
                    if name_flg == True:
                        if conf["end_index"] == i:
                            name_flg = False

                return_list.append(line_data)
            # print(data)
    return return_list
def main(tsv):
    conf = load_config()
    print(json.dumps(load_tsv(tsv, conf)))

if __name__ == "__main__":
    args = sys.argv
    
    tsv = args[1]
    main(tsv)