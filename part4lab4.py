#!/usr/bin/env python3

import os, datetime, reports
## the format of the report body is as follows
# name: Apple
# weight: 500 lbs
# [blank line]
# this repeats over until you are out of files
def generate_report_body(filelist):
    payload = []
    for filename in filelist:
        file = open(filename)
        format_name = 'name: {}<br/>'.format(file.readline().rstrip())
        payload.append(format_name)
        format_weight = 'weight: {}<br/>'.format(file.readline().rstrip())
        payload.append(format_weight)
        line_break = '<br/>'
        payload.append(line_break)
    file.close()
    return payload
def main():
    arr_files = os.listdir('/supplier-data/descriptions')
    report_body = generate_report_body(arr_files)
    today = datetime.datetime.today()
    report_title = 'Processed Update on {}'.format(today.strftime(r'%d/%m/%Y'))
    reports.generate_report('/tmp/processed.pdf', report_title, report_body)
if __name__ == "__main__":
    main()