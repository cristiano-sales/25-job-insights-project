from src.jobs import read


def get_unique_job_types(path):

    data = read(path)

    list_of_job_types = []

    for row in data:
        job_type = row["job_type"]
        list_of_job_types.append(job_type)

    return list(set(list_of_job_types))


def filter_by_job_type(jobs, job_type):

    filtered_jobs = []

    for j in jobs:
        if job_type == j["job_type"]:
            filtered_jobs.append(j)
    return filtered_jobs


def get_unique_industries(path):

    data = read(path)

    list_of_industry_types = []

    for row in data:
        industry_type = row["industry"]

        if industry_type != "":
            list_of_industry_types.append(industry_type)

    return list(set(list_of_industry_types))


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):

    data = read(path)

    salaries = []

    for row in data:
        salary = row["max_salary"]

        if salary not in salaries and salary != "" and salary.isdigit():
            salaries.append(int(salary))

    return max(salaries)


def get_min_salary(path):

    data = read(path)

    salaries = []

    for row in data:
        salary = row["min_salary"]

        if salary not in salaries and salary != "" and salary.isdigit():
            salaries.append(int(salary))

    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
