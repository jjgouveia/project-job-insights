from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    salaries = read(path)

    max_salary = 0

    for salary in salaries:
        param = salary["max_salary"]

        if param == '':
            max_salary = max_salary
        elif param != 'invalid' and int(param) > max_salary:
            max_salary = int(param)

    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    salaries = read(path)

    min_salary = get_max_salary("data/jobs.csv")

    for salary in salaries:
        param = salary["min_salary"]

        if param == '':
            min_salary = min_salary
        elif param != 'invalid' and int(param) < min_salary:
            min_salary = int(param)

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
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
    try:

        MIN_SALARY = int(job["min_salary"])
        MAX_SALARY = int(job["max_salary"])

        if MIN_SALARY > MAX_SALARY:
            raise ValueError

        salary_range = MIN_SALARY <= int(salary) <= MAX_SALARY
        return salary_range

    except (KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
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
    job_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list.append(job)

        except (KeyError, TypeError, ValueError) as error:
            print(error)

    return job_list
