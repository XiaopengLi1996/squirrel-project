# Tools for Analytics Project : Squirrel sightings Tracking Web

This is a README file intended to describe our squirrel sightings tracking tools. This application can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data. 

## Content
- [Brief Introduction](#heading)
- [Database](#heading-2)
- [Clone the repo](#heading-3)
- [Dependencies](#heading-4)
- [Management Commandds](#heading-5)
- [API](#heading-6)
- [Project Team](#heading-7)


<a name="heading"></a>
## Brief Introduction

This application is a **Django** based suqirrel sighting tracker and keeps track of the recorded squirrels in 2018 at the Central Park. We can import the squirrel tracking data from a csv file or export the data into a csv file. We can add a new squirrel information, update an existing squirrel file, counts the numeber of squirrels which have the same attribute, and we can show a map that displays the location of the squirrel sightings on a **OpenStreets map**.

<a name="heading-2"></a>
## Database

The squirrel sightings data can be gathered from **2018 Central Park Squirrel Census**. And it was published by the [**Squirrel Census Comminity**](https://www.thesquirrelcensus.com/) in 2019. It contains about 3,000 different squirrel sightings, it provides the lattitude and longitude of the sightings as well as squirrels' age, fur color, date and other informations.

<a name="heading-3"></a>
## Clone the Repo
For those who are interested, feel free to clone our repository by running in terminal:
```bash
git clone git@github.com:XiaopengLi1996/squirrel-project.git
```

<a name="heading-4"></a>
## Dependencies

We specified all dependencies (supplemental packages required for our project to operate correctly) in the requirements.txt file by using this code:
``` bash
$ pip install -r requirements.txt
```
<a name="heading-5"></a>
## Management Commands

We create management commands to import and export the data:

> **Import**: A command used to import the data from a csv file. The file path should be specified at the command line after the name of the management command.

```bash
$ python manage.py import_squirrel_data /path/to/file.csv
```

> **Export**: A command used to export the data from a csv file. The file path should be specified at the command line after the name of the management command. 

```bash
$ python manage.py export_squirrel_data /path/to/file.csv
```
<a name="heading-6"></a>
## API
Run the server and then go to the brower. Add different views location to the url will lead to different API with specific function.

> **Map**:  
* **Behavior**: Map is a app that shows a map that displays the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/).
* **Located at**: /map
* **Note**: Do not plot 100 squirrels at once, otherwise the browser may freeze for a while.
 
> **Sightings**: 
* **Behavior**: Sightings is a app that lists all squirrel sightings with links to edit and add sightings.
* **Located at**: /sightings
 
> **Update**: 
* **Behavior**: Update is a view to update a particular sighting. Add a specific unique squirrel id in the location to check and update the individual information of a squirrel.
* **Located at**: /sightings/<unique-squirrel-id>
 
> **Add**: 
* **Behavior**: Add is a view to create a new sighting. Open the link by clicking the squirrel unique ID and input the necessary information.
* **Located at**: /sightings/add
 
> **Stats**: 
* **Behavior**: Stats will show the statistic information. It calculates the number of squirrels who have a specific attribute. 
* **Located at**: /sightings/stats

<a name="heading-7"></a>
## Project Team

**Group**: Proejct Group 70, Section 2      

**Team Member**: Xiaopeng Li,  Jianfeng Yin 

**UNIs**: [xl2914, jy3033]


