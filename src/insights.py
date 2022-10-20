from src.jobs import read


def get_unique_job_types(path):
    """ retornar uma lista de valores únicos presentes na coluna job_type. """
    all_jobs = read(path)
    unique_job_types = set()  # inicializa um conjunto/coleção de elementos.

    for job in all_jobs:
        unique_job_types.add(job["job_type"])
    return list(unique_job_types)


def filter_by_job_type(jobs, job_type):
    """ retornar uma lista com todos os empregos onde a
    coluna job_type corresponde ao parâmetro job_type. """
    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):
    """ retornar uma lista de valores únicos presentes na coluna industry. """
    all_industries = read(path)
    unique_industries = set()  # inicializa um conjunto/coleção de elementos.

    for industrie in all_industries:
        if industrie["industry"] != "":
            unique_industries.add(industrie["industry"])
    return list(unique_industries)


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
    """ retornar um valor inteiro com o maior salário
    presente na coluna max_salary. """
    salarys = read(path)
    max_salary = list()

    for salary in salarys:
        coin = salary["max_salary"]
        if coin.isdigit():
            max_salary.append(int(coin))

    pass
    return max(max_salary)


def get_min_salary(path):
    """ retornar um valor inteiro com o menor salário
    presente na coluna min_salary """
    salarys = read(path)
    min_salary = list()

    for salary in salarys:
        coin = salary["min_salary"]
        if coin.isdigit():
            min_salary.append(int(coin))

    pass
    return min(min_salary)


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
