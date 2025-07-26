# Sample dashboard - CDSH

Downloaded the Health & Human Services Program dataset available to the public at [data.chhs.ca.gov](https://data.chhs.ca.gov/dataset/health-and-human-services-program-counts). This dataset contains information on the California Health and Human Services (CalHHS) single and multi-program participation counts with demographics by year and geography, including both the Annual (cumulative) and July (point in time). 

## Preprocessing
1. Selected the annual dataset.
2. Leveraged Excel to filter by counties, remove simultaneous counts in several programs and set missing data to 0. 
3. Exported the dataset to a CSV file.
4. Used Python to pivot the demographic columns (Age, Gender, Ethnicity) into three columns including (i) Category indicating whether the row is about Gender, Age, or Ethnicity, (ii) Group: indicating the group name (e.g., Male, 18-64, Hispanic) and (iii)Value: the number of participants in that group. This was done to facilitate the development of the stacked bar chart.

## Dashboard development
1. Loaded both dataset in Tableau Public.
2. Developed a California map displaying the number of participants as a function of the year and program.
3. Developed a stacked bar chart showing a data breakdown by category as a function of the selected county and program.
4. Leveraged both plots to construct a dashboard applying the year and program filters to both items (map and bar chart).
5. Finally, added a filter action allowing the user to select a county (in the map) and automatically updating the data breakdown (bar chart) according to such selection.

The final result can be found [here](https://public.tableau.com/views/cdsh_sample/Dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
