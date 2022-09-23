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

    filtered_industries = []

    for j in jobs:

        if industry == j["industry"]:
            filtered_industries.append(j)

    return filtered_industries


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
    def is_int(value):
        return type(value) == int

    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not is_int(job["min_salary"])
        or not is_int(job["max_salary"])
        or not is_int(salary)
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Invalid values")

    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True

    return False


def filter_by_salary_range(jobs, salary):

    filtered_jobs = []

    for j in jobs:
        try:
            verify_salary_range = matches_salary_range(j, salary)
            if verify_salary_range:
                filtered_jobs.append(j)
        except ValueError:
            pass

    return filtered_jobs
