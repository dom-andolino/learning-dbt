-- test/generic/generic_not_null.sql
-- source: https://docs.getdbt.com/guides/best-practices/writing-custom-generic-tests#generic-tests-with-default-config-values
-- Note that for simplicity, we are doing a simple not_null test that is a repeat of one of the out-of-box tests.
{% test generic_not_null(model, column_name) %}

    select *
    from {{ model }}
    where {{ column_name }} is null

{% endtest %}
