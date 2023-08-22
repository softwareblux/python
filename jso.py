 response = requests.get(“10.0.0.50”, params=params, headers=
headers)

 

            parsed =
json.dumps(response.json())

            alist =
json.loads(parsed)

           

            meteringPointId = alist['periodsSummaryResponses'][0]['sensor']['meteringPointId']

            sensorType = alist['periodsSummaryResponses'][0]['sensor']['sensorType']

            direction = alist['periodsSummaryResponses'][0]['sensor']['direction']

           

 

            for h in range(5
):

                year = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['year'
]

               

               

                for f in range(12
):

                    month = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['summaryValues'][f]['unitOfTimeValue'
]

                    max_value = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['summaryValues'][f]['max']['value'
]

                    max_time = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['summaryValues'][f]['max']['time'
]

                    min_value = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['summaryValues'][f]['min']['value'
]

                    min_time = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['summaryValues'][f]['min']['time'
]

                    sum_value = alist['periodsSummaryResponses'][0]['result']['periodsSummaryResults'][0]['unitsOfTime'][h]['summaryValues'][f]['sum'
]

 

                    list_row = [str
(meteringPointId), sensorType, direction,year,month,max_value,max_time,min_value,min_time,(sum_value)]

                    df.loc[len(df)] =
list_row

 

 

 

{

    "periodsSummaryResponses": [

        {

            "result": {

                "periodsSummaryResults": [

                    {

                        "unitOfTime": "Year",

                        "unitsOfTime": [

                            {

                                "summaryValues": [

                                    {

                                        "max": {

                                            "time": "2020-10-19T10:00:00+02:00",

                                            "value": 18

                                        },

                                        "min": {

                                            "time": "2020-09-21T01:00:00+02:00",

                                            "value": 0

                                        },

                                        "sum": 69215,

                                        "unitOfTimeValue": "2020"

                                    }

                                ],

                                "year": "2020"

                            },

                            {

                                "summaryValues": [

                                    {

                                        "max": {

                                            "time": "2021-01-14T08:00:00+01:00",

                                            "value": 19

                                        },

                                        "min": {

                                            "time": "2021-06-01T16:00:00+02:00",

                                            "value": 3

                                        },

                                        "sum": 79426,

                                        "unitOfTimeValue": "2021"

                                    }

                                ],

                                "year": "2021"

                            },

                            {

                                "summaryValues": [

                                    {

                                        "max": {

                                            "time": "2022-02-03T13:00:00+01:00",

                                            "value": 3798.1152

                                        },

                                        "min": {

                                            "time": "2022-02-03T23:00:00+01:00",

                                            "value": 0

                                        },

                                        "sum": 13009.9776,

                                        "unitOfTimeValue": "2022"

                                    }

                                ],

                                "year": "2022"

                            }

                        ]

                    }

                ]

            },

            "sensor": {

                "direction": "Downstream",