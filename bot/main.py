from jobs.jobsearch import JobSearch



try:
    with JobSearch() as bot:
        bot.land_first_page()
        bot.enter_job_type(job_type = "software engineer")
        bot.enter_job_location(location = "Sydney")
        bot.click_search()
        bot.results_report()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from the command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise