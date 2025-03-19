# Scratchpad

Goal: Learn DBT, Airflow, and Databricks. 


## TODO 

## DONE
    PLE 70028551 - Data Engineering with dbt
        https://www.linkedin.com/learning/data-engineering-with-dbt/

## Env Setup/Commands
    python -m venv .venv
        create virtual env in repo root
    .venv\Scripts\activate
        activate venv

    python.exe -m pip install --upgrade pip
    
    pip install dbt-core
    pip install dbt-duckdb
    pip install duckdb
    pip install dbt-snowflake

    dbt init
        give project name, creates folder with boilerplate files/folders
    dbt_project.yml
        configure to store test failures or not

    cd nyc_parking_violations
        make sure you are in porject dir when running dbt commands or for profiles.yml

    touch profiles.yml
        not created by default (depending on db type)...see docs for templates
        touch is linux/mac command..windows us "type nul > profiles.yml"

    dbt debug
        Checks to see if your configuration files are setup correctly and recognized by dbt Core.
        When you run dbt from the CLI, it reads your dbt_project.yml file to find the profile name, and then looks for a profile with the same name in your profiles.yml file. This profile contains all the information dbt needs to connect to your data platform.
        
    dbt compile
        Runs all the dbt models end-to-end, but doesn't execute the models' SQL code nor materialize the tables; which is useful for quickly checking if your dbt models have any errors.
    
    dbt run
        Runs all the dbt models end-to-end, executes the SQL code, and materialize the tables based on the profile configurations.

    dbt run --target prod 
        to specifically update our new production database.

    dbt docs generate
        goes into /target

    dbt docs serve
        opens doc on browser localhost

    /models/docs/schema.yml
         configuration file that enables us to establish documentation and tests for our dbt project

    /models/docs/docs_blocks.md
        uses "jinja" to support dynamic variables in schema.yml, avoids repeats, complys with DRY principal
        '{{ doc("<docs blocks name>") }}'

    dbt test
        will execute all tests in your dbt project and provide a summary of the results.


    /.github/workflows/run-dbt-prod.yml
        what/when to run github action

    DBT_PROFILES_DIR
        environment variable
    DBT_PROJECT_DIR
        environment variable


## Misc Notes
    /models/table_name.sql
        the name of this file will be the name of the table created in the db

    FROM {{ref('first_model')}}

## Resources
    https://github.com/LinkedInLearning/data-engineering-with-data-build-tool-dbt-4458303/blob/main/assets/tutorial_files/dbt_project_walkthrough.md
    https://medium.com/@c4caesar/automating-daily-csv-updates-with-github-actions-a-quick-tutorial-86f2c3d77e9a
    https://github.com/caesarw0/BC-ChildCare-API/blob/main/.github/workflows/update_csv.yml
    https://docs.getdbt.com/docs/build/python-models

