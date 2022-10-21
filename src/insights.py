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
    """ retornar uma lista de dicionários com todos os empregos onde
    a coluna industry corresponde ao parâmetro industry. """
    list_industry = []
    for job in jobs:
        if job["industry"] == industry:
            list_industry.append(job)
    return list_industry


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
    """ A função deve retornar True se o salário procurado
    estiver dentro da faixa salarial ou False se não estiver.

    ----------
    Os dicionários possuem um método específico
    para busca de valores, o get() """
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")
    if (
        min_salary is None
        or max_salary is None
        or not type(job["min_salary"]) is int
        or not type(job["max_salary"]) is int
        or not type(salary) is int
        or min_salary > max_salary
    ):
        raise ValueError
    pass
    return int(min_salary) <= salary <= int(max_salary)


def filter_by_salary_range(jobs, salary):
    """ Para esta filtragem, podemos usar a função auxiliar implementada
    no requisito anterior -- tomando o cuidado de descartar os empregos
    que apresentarem faixas salariais inválidas.

    ----------
    A função deve retornar uma lista com todos os empregos onde o salário
    salary estiver entre os valores da coluna min_salary e max_salary.
"""
    list_salary_range = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_salary_range.append(job)
        except ValueError:
            print("Something went wrong")
    return list_salary_range
