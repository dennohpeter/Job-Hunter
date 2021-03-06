import requests, pprint
from bs4 import BeautifulSoup
from django.conf import settings
from brighterMonday.updater import Update_Jobs

class Crawler:
    BRIGHTER_MONDAY_URL = settings.BRIGHTER_MONDAY_URL
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    def get_page(self, url):
        res = requests.get(url, headers=self.headers)
        try:
            res.raise_for_status()
        except Exception as exc:
            print("There was a problem: %s" % exc)
        return BeautifulSoup(res.text, 'html.parser')

    def fetch_jobs(self):
        all_jobs = {}
        brighter_monday_soup = self.get_page(self.BRIGHTER_MONDAY_URL)

        jobs_in_index_page = self._extract_jobs(brighter_monday_soup)
        all_jobs = jobs_in_index_page
        pages = brighter_monday_soup.select('.pagination a.page-link')[:-1]
        for page in pages:
            url = page.get('href')
            soup = self.get_page(url)
            jobs_from_other_pages = self._extract_jobs(soup)
            all_jobs['total_jobs'] += jobs_from_other_pages['total_jobs']
            all_jobs['jobs'] += jobs_from_other_pages['jobs']
        print('--------------done getting jobs--------------------')
        # calling update jobs class which updates jobs in the models
        pprint.pprint(all_jobs)
        update_jobs = Update_Jobs(all_jobs)
        update_jobs.update_models()


    def _extract_jobs(self, brighter_monday_soup):
        jobs_list = {'total_jobs': 0, 'jobs': []}
        all_articles = brighter_monday_soup.findAll(
            'article', class_='search-result')

        for each_job in all_articles:
            job_result_header = each_job.find(
                class_='search-result__header')
            job_result_title = job_result_header.find('a',
                                                      class_='search-result__job-title').getText().strip()
            job_result_meta = job_result_header.find(
                class_='search-result__job-meta').getText().strip()

            job_result_location = job_result_header.find(
                class_='search-result__location').getText().strip()
            job_result_type = job_result_header.find(
                class_='search-result__job-type').getText().strip()
            job_result_salary = job_result_header.find(
                class_='search-result__job-salary').getText().strip().replace("\n\n", ": ")
            try:
                job_result_function, time_posted = job_result_header.find(
                    class_='search-result__job-function').getText().strip().split("\n\n")[1:]
                time_posted = "%s ago" % time_posted
            except Exception as err:
                print(job_result_header.find(
                    class_='search-result__job-function').getText())
                print('\n------------------error----------------------\n%s' % err)

            job_result_body = each_job.find(class_='search-result__body')
            job_result_more_info_link = job_result_body.find(
                'a', class_='metrics-apply-now')['href']
            job_result_card_icon = None
            job_result_card_icon_alt = None
            try:
                job_result_card_icon = job_result_body.find('img',
                                                            class_='employer-logo__image')['data-src']
                job_result_card_icon_alt = job_result_body.find('img',
                                                                class_='employer-logo__image')['alt']
            except Exception as exc:
                print('--------image not found error------------------\n')
                print(exc)

            job_result_content = job_result_body.find(
                class_='search-result__content').getText().strip()
            (summary_title, summary, description_title,
             requirements) = self.more_info(job_result_more_info_link)
            res = {
                'job_result_title': job_result_title,
                'job_result_meta': job_result_meta,
                'job_result_location': job_result_location, 
                'job_result_type': job_result_type,
                'job_result_salary': job_result_salary, 
                'job_function': job_result_function,
                'time_posted': time_posted,
                'job_result_card_icon': job_result_card_icon,
                'job_result_card_icon_alt': job_result_card_icon_alt,
                'job_result_content': job_result_content,
                "summary_title": summary_title,
                "summary": summary,
                "description_title": description_title,
                "requirements": requirements
            }
            jobs_list['jobs'].append(res)
            jobs_list['total_jobs'] += 1
        return jobs_list

    def more_info(self, url):
        more_info_soup = self.get_page(url)
        search_main__content = more_info_soup.find("article", class_="job__details")
        more_info_card = search_main__content.find_all('div',
            class_='customer-card card--compact')
        print("---------- job summary------------------")
        card_summary = more_info_card[0].getText('\n').strip().split('\n')
        card_summary = [each.strip()
                    for each in card_summary if each.strip() != '']
        summary_title = card_summary[0]
        summary = "\n".join(card_summary[1:])
        print("---------- job description------------------")
        description = more_info_card[1].getText('\n').strip().split('\n')
        description = [each.strip()
                        for each in description if each.strip() != '']
        description_title = description[0]
        requirements = "\n".join(description[1:])

        return (summary_title, summary, description_title, requirements)
