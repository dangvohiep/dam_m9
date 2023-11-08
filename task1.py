import json
import pandas as pd

source = {
    "albums": 
    [
        {
            "title"     : "Dangerous: The Double Album",
            "artist"    : "Morgan Wallen",
            "songs"     : [
                "Sand in My Boots",
                "Wasted on You",
                "Somebody's Problem",
                "More Surprised than Me",
                "865",
            ],
        },
        {
            "title"     : "The Mockingbird & the Crow",
            "artist"    : "Hardy",
            "songs"     : [
                "Beer",
                "Red",
                "Wait in the Truck",
                "Drink One for Me",
                "I in Country",
            ],
        },
        {
            "title"     : "Speak Now",
            "artist"    : "Taylor Swift",
            "songs"     : [
                "Mine",
                "Sparks Fly",
                "Back to December",
                "Speak Now",
                "Dear John",
            ],
        }
    ]
}

# print(json.dumps(source, indent=2))
print(pd.DataFrame(data=source["albums"]).to_html(index=False))

