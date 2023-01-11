Lager = {
    "name": "Lager",
    "type": "Model",
    "origin" : "Plant",
    "entries" :[],
    "children":[
        ("Einzelstation","PackstationGehäusehälften"),
        ("Einzelstation","PackstationRitzelwellen"),
        ("Puffer","Buffer"),
        ("Quelle","QuelleGitterbox"),
        ("Quelle","QuelleLager")
    ]
}

Einzelstation = {        
            "type" : "Einzelstation",

            "attr" : ["Bearbeitungszeit" ,
                        "Rüstzeit" ,
                        "Erholzeit" ,
                        "Zykluszeit" ,
                   
                    ],
            "PackstationRitzelwellen":{  "name":"PackstationRitzelwellen",
                    "origin" : "Lager",
                    "relations":[
                    ("PackstationRitzelwellen","Buffer")
                        ],},
            "PackstationGehäusehälften":{  "name":"PackstationGehäusehälften",
                    "origin" : "Lager",
                    "relations":[
                    ("PackstationGehäusehälften","Buffer")
                        ],},
            
   
        }

Quelle = {
    "type":"Quelle",
    "attr" : [
                "Abstand" ,
                "Start" ,
                "Stop" ,
                "BE"
                    ],
    "QuelleLager":{  "name":"QuelleLager",
                    "origin" : "Lager",
                    "relations":[
                    ("QuelleLager","PackstationRitzelwellen"),
                    ("QuelleLager","PackstationGehäusehälften"),
                    ("QuelleLager","Buffer")
                        ],},
    "QuelleGitterbox":{  "name":"QuelleGitterbox",
                    "origin" : "Lager",
                    "relations":[
                    ("QuelleGitterbox","PackstationRitzelwellen"),
                    ("QuelleGitterbox","PackstationGehäusehälften"),
                    ("QuelleGitterbox","Buffer")
                        ],},
}

Puffer = {  "type":"Puffer",
    "attr" : ["Kapazität",
            "Puffertyp"],
    "Buffer":{"name" : "Buffer",
                "origin":"Lager",
                "relations":[]
    }
            }