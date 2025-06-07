# Predicting Vaccine Uptake Using Behavioral and Background Data

Author: [David Mburu](www.linkedin.com/in/david-g-mburu-b1268a1b7)


## Overview

In this project, we will take a look at vaccination, a key public health measure used to fight infectious diseases. Vaccines provide immunization for individuals, and enough immunization in a community can further reduce the spread of diseases through "herd immunity." 

Beginning in spring 2009, a pandemic caused by the H1N1 influenza virus, colloquially named "swine flu," swept across the world. Researchers estimate that in the first year, it was responsible for between 151,000 to 575,000 deaths globally.

A vaccine for the H1N1 flu virus became publicly available in October 2009. In late 2009 and early 2010, the United States conducted the National 2009 H1N1 Flu Survey. This phone survey asked respondents whether they had received the H1N1 and seasonal flu vaccines, in conjunction with questions about themselves. These additional questions covered their social, economic, and demographic background, opinions on risks of illness and vaccine effectiveness, and behaviors towards mitigating transmission. A better understanding of how these characteristics are associated with personal vaccination patterns can provide guidance for future public health efforts.


## Business Understanding 

### Business Problem
As the world struggled to vaccinate the global population against COVID-19, an understanding of how people’s backgrounds, opinions, and health behaviors are related to their personal vaccination patterns could provide guidance for future public health efforts.


### Problem Statement
The Kenya Medical Research Institute wants to find out the characteristics that influence people's response to vaccination drives to enhance how they go about public health vaccination efforts in future


To aid KEMRI in administering vaccines to Kenyans effectively in future, I have undertaken this project to determine how various characteristics influence vaccine uptake. 

There is still opportunity to continue going deeper into the dataset and gain more insights as the competition it is a part of goes on till 2026. However because of limited academic time, this project was limited to 7 days.

Some of the questions this project helps stakeholders to answer are:

1. How does the age group of an individual affect vaccine uptake?

2. How do people's beliefs influence their likelihood of getting vaccinated?

3. How does a person's economic status impact his vaccination chances?

4. How does the number of people in a household affect vaccine uptake?

The above questions hence make up the 4 objectives of this project in addition to finding the best model for predicting negative vaccine uptake cases


## Data Understanding

The [dataset](https://www.drivendata.org/competitions/66/flu-shot-learning/page/210/) is sourced from the DrivenData website and is part of an ongoing machine learning competition.

The data is provided courtesy of the United States [National Center for Health Statistics](https://www.cdc.gov/nchs/index.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnchs%2Findex.htm). The United States government conducted a Survey which helped gather data points that could be used in analysis to figure out the characteristics that mostly affect how people respond to vaccines. A better understanding of how these characteristics are associated with personal vaccination patterns can provide guidance for future public health efforts.

The dataset is made up of 26707 entries which are distributed across 36 columns representing the people's answers to these survey questions. As a result of how most surveys are done, this dataset is made up of binary values representing 'true' or 'false' and scaled entries representing the degree of the respondents' opinion about a question.

### Analysis and Results

A doctor's recommendation highly impacts vaccine uptake
![How doctor's recommendation and people's attitudes affect vaccine uptake](Images/EDA/vaccine%20uptake%20against%20people's%20attitude.png)


People's beliefs about the vaccine affect if they will take it or not
![People's beliefs](Images/EDA/Vaccine%20uptake%20against%20people's%20beliefs.png)


Age group is another contributing factor
![Age group](Images/EDA/Vaccine%20uptake%20against%20age%20group.png)


So is economic status and number of people in a household
![Economic Status](Images/EDA/Vaccine%20uptake%20against%20economic%20status.png)

![Number of People in Household](Images/EDA/Vaccine%20uptake%20against%20number%20of%20people%20in%20household.png)



The models I built used the above data points among others to predict the likelihood of a person getting a vaccine. The best performing model was a logistic regression model with this confusion matrix:

![Confusion Matrix](Images/Modeling/Best%20Model.png)

The model is most effective in predicting true negatives. These are the people who are not likely to get the vaccine. This is desirable so as to help KEMRI identify where to direct its vaccination efforts. 

The false negatives are also more than the false positives. This is also highly desirable because it's better to direct vaccination effort to more people than necessary even those who would have gotten vaccinated anyway than missing out on potential vaccination drives to hesitant people because they were classified as likely to get vaccinated on their own.


## Conclusion and Recommendations

In conclusion, the factors that highly impact a person's likelihood to get vaccinated are: age group, people's attitude about the disease, people's beliefs about the vaccine, doctor's recommendation to vaccinate, and economic status.

From these indicators, in the event of another disease outbreak or a pandemic, I would recommend KEMRI to:

1. Spread awareness about the effects about a disease to ensure people take vaccination seriously.
2. Engage in vaccination information campaigns to combat people's negative beliefs about vaccines.
3. Target people aged 18-44 as these are the least likely to get vaccines.
4. Subsidize vaccine costs to ensure people with a low economic status can get the vaccine.
5. Subsidize households with more than three people to ensure they all get vaccinated.
6. Encourage doctors and other medical professionals to personally recommend the vaccine to people.


## Next Steps

Build pipelines for the data preprocessing and modeling steps in preparation to deploy the model

Research on and build even more powerful models than the ones used in this project to get better predictions


## More Information

For a deeper look into how I went about the project, check out the [jupyter notebook](index.ipynb)

For a slide presentation with simple non-technical words, check out the [presentation](presentation.pdf)

Check the [images folder](./Images/) to see visualizations of how other features influence vaccine uptake

You can reach out to me by sending an email: [daveygmburu@gmail.com](mailto:daveygmburu@gmail.com)

Or send me a message on [LinkedIn](www.linkedin.com/in/david-g-mburu-b1268a1b7)