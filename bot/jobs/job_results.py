from selenium.webdriver.remote.webelement import WebElement
import time


class JobResults:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.job_boxes = self.pull_job_boxes()

    def pull_job_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name(
            'job-card'
        )

    def pull_job_box_attributes(self):
        collection = []
        for job_box in self.job_boxes:
            time.sleep(3)
            # Pulling the hotel name
            job_title = job_box.find_element_by_class_name(
                'job-link'
            ).get_attribute('innerHTML').strip()
            employer_title = job_box.find_element_by_class_name(
                'job-company'
            ).get_attribute('innerHTML').strip()
            job_location = job_box.find_element_by_class_name(
                'job-location'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [job_title, employer_title, job_location]
            )
        return collection