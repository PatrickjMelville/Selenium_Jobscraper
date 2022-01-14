import jobs.constants as const
from selenium import webdriver
from jobs.job_results import JobResults
from prettytable import PrettyTable


class JobSearch(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(JobSearch, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def enter_job_type(self, job_type):
        search_field = self.find_element_by_id('q')
        search_field.clear()
        search_field.send_keys(job_type)

        first_result = self.find_element_by_id('autocomplete_list_1_item_0')
        first_result.click()

    def enter_job_location(self, location):
        location_field = self.find_element_by_id('l')
        location_field.clear()
        location_field.send_keys(location)

        first_result = self.find_element_by_id('autocomplete_list_2_item_0')
        first_result.click()
    
    def click_search(self):
        search_button = self.find_element_by_class_name('search-jobs-button')
        search_button.click()
    
    def results_report(self):
        job_boxes = self.find_element_by_id('jobresults')

        report = JobResults(job_boxes)
        table = PrettyTable(
            field_names=["Job Title", "Employer", "Location"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)


