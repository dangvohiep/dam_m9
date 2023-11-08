import json
import pandas as pd

albums = [
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


# print(json.dumps(albums, indent=2))
# print(pd.DataFrame(albums).to_html(index=False))

# table_from_json = pd.read_json(
#     "https://raw.githubusercontent.com/dangvohiep/dam_m9/master/albums.json"
# )
# table_from_html = pd.read_html(
#     "https://raw.githubusercontent.com/dangvohiep/dam_m9/master/albums.html"
# )


