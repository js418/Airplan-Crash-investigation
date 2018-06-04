create database crash;

create table Crash (Date text,Time text,City text,Country text,Operator text,Route text,Type text,Manufacture text,Aboard int,Fatalities int,Summary text,Category text);
\copy Crash from 'C:\Users\tensa\Desktop\courses\data_visualization\project\sql_data.csv' DELIMITER ',' CSV;

update crash set country = "China" where country = "Hong Kong" or country = "Taiwan";

update crash set country = "Russia" where country = "USSR";

//show the top 20 countries for air crash
select distinct country, count(*) from crash group by country order by count(*) desc limit 20;
/*
    country    | count
---------------+-------
 United States |  1432
 Russia        |   238
 Brazil        |   190
 Canada        |   150
 Colombia      |   149
 China         |   136
 France        |   135
 England       |   108
 India         |   100
 Indonesia     |    87
 Mexico        |    86
 Germany       |    83
 Australia     |    81
 Italy         |    79
 Vietnam       |    74
 Philippines   |    69
 Spain         |    65
 Venezuela     |    59
 Peru          |    54
 Bolivia       |    47
(20 rows)
*/

select distinct manufacture, count(*) from crash group by manufacture order by count(*) desc limit 20;
/*
           manufacture           | count
---------------------------------+-------
 Douglas                         |   956
 Boeing                          |   337
 Antonov                         |   244
 Cessna                          |   171
 de Havilland Canada  Twin Otter |   120
 McDonnell Douglas               |   119
 Curtiss                         |   114
 Beechcraft                      |   102
 Piper                           |    95
 Tupolev                         |    94
 Ilyushin                        |    94
 Junkers                         |    84
 Convair                         |    82
 Lockheed  Hercules              |    76
 Fokker  Friendship              |    73
 Lockheed                        |    72
 Fairchild                       |    66
 Britten-Norman  Islander        |    50
 Yakovlev                        |    50
 Bell                            |    48
(20 rows)
*/

 