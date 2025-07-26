# Sample dashboard - CDSH

This dashboard is based on the Health & Human Services Program dataset, publicly available at [data.chhs.ca.gov](https://data.chhs.ca.gov/dataset/health-and-human-services-program-counts). The dataset contains information on California Health and Human Services (CalHHS) single- and multi-program participation counts, including demographic breakdowns by year and geography. It includes both Annual (cumulative) and July (point-in-time) data.

## Preprocessing
1. Selected the annual dataset.
2. Used Excel to filter by counties, remove duplicated counts across multiple programs, and set missing values to 0.
3. Exported the cleaned dataset to a CSV file.
4. Used Python to pivot the demographic columns (Age, Gender, Ethnicity) into three standardized columns: 
    - Category: Indicates whether the row refers to Gender, Age, or Ethnicity
    - Group: Specifies the group name (e.g., Male, 18–64, Hispanic)
    - Value: Represents the number of participants in that group

This transformation was done to facilitate the development of a stacked bar chart.

## Dashboard development
1. Loaded both dataset in Tableau Public.
2. Created a California map displaying the number of participants by year and program.
3. Built a stacked bar chart showing demographic breakdowns (by selected category) as a function of county and program.
4. Combined both visualizations into a dashboard, applying year and program filters to both the map and bar chart.
5. Finally, added a filter action that allows users to click on a county (in the map) and automatically update the demographic breakdown (bar chart) based on the selection.

The final result can be found [here](https://public.tableau.com/views/cdsh_sample/Dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
