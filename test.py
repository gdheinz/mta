# Implements GTFS tests.
import sys
import re
import subprocess
import testcases
import os
import gtfs
            
class TestGtfsFeedvalidator(object):
    def __init__(self, testcases_xml, feedvalidator_results):
        self.testcases_xml = testcases_xml
        self.feedvalidator_results = feedvalidator_results
      
      
    def check_returned_values(self):
        verdict = 'PASS'
        w = testcases.TestCases(self.testcases_xml)
        for testcase in w.testcases:
            for result in self.feedvalidator_results:
                label, value = result
                if label == testcase.label:
                    testcase.found = True
                    if count != testcase.count:
                      verdict = 'FAIL'
                      # print 'check_returned_values: {} has incorrect value'.format(warninglabel)
        print '{}: check_returned_values'.format(verdict)
                    
    def check_unexpected_labels(self):
        verdict = 'PASS'
        expected = testcases.TestCases(self.testcases_xml)
        found = [False for e in expected.testcases]
        for testcase in expected.testcases:
            for i, result in enumerate(self.feedvalidator_results):
                _, act_label = result
                if act_label == testcase.label:
                    found[i] = True
        for i, testcase in enumerate(expected.testcases):
            if not found[i]:
                # print 'check_unexpected_labels: not found', act_label
                verdict = 'FAIL'
        print '{}: check_unexpected_labels'.format(verdict)
        

gtfs_dir = 'gtfs'
html_out = 'out.html'
temp_out = 'out.tmp'
testcases_xml = 'testcases.xml'

feedvalidator_results = gtfs.feedvalidator(gtfs_dir, html_out, temp_out)

test_gtfs = TestGtfsFeedvalidator(testcases_xml, feedvalidator_results)
test_gtfs.check_returned_values()
test_gtfs.check_unexpected_labels()
