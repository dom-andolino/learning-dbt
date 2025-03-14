-- custom singular tests
{{ config(severity = 'warn') }}

SELECT count(*) as num_rows
FROM {{ref('ref_model')}}
HAVING
    NOT(num_rows > 1)