from src.sorting import sort_by

mock_jobs = [
    {
        "min_salary": 5000,
        "max_salary": 8000,
        "date_posted": "2020-04-08",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "2020-05-08",
    }
]

order_salary_min = [mock_jobs[1], mock_jobs[0]]
order_salary_max = [mock_jobs[0], mock_jobs[1]]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == order_salary_min

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == order_salary_max
