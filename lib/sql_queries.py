select_all_female_bears_return_name_and_age = """
      SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT *
    FROM bears
    WHERE age > 5;
"""

select_all_alive_bears_names_ages_order_youngest_to_oldest = """
    SELECT name, age
    FROM bears
    WHERE alive = 1
    ORDER BY age;
"""


select_oldest_bear_and_returns_name_and_age = """
    Write your SQL query here
"""
select_youngest_bear_and_returns_name_and_age = """
    Write your SQL query here
"""