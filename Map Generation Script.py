import folium

# Creaite a folium map
start_location = [53.27502808213727, -6.61954164505005] # The location where the map begins at.
f_map = folium.Map(location= start_location, zoom_start=6,max_bounds=True, max_zoom=25)

# Details for each item
# Name
# Information
# Photo
points = [
    {
        "coordinates": [53.23322484496824, -6.6609925031662],
        "event name": "Your house",
        "description": "Omg your house :0. I was so scared to go there at first- but your family was so nice to me :) A lot of silly things happened here such as: Your brothers bed incident (I will not elaborate),  Playing The Game of life which traumatised us and seeing you make your billy shake for the first time",
        "image":"nerdspt3.jpg",
    },{
        "coordinates": [53.21940923166982, -6.666491031646729],
        "event name": "Canal",
        "description": "We walked here one of our first dates and I remeber a group of kids with a padding boat offering us a romantic ride which was pretty funny. I enjoy our walks cus we always end up rambleing",
        "image":"swan.jpeg",
    },{
        "coordinates": [53.3729986366394, -6.234204769134522],
        "event name": "Marino",
        "description": "Where we baked the cake! lowkey one of my fav times we spent togther-idk how we manged to baked something shit was impressive. Also here is were I slept in and left u in Connolly Station...I have learnt from my mistakes.",
        "image":"Cake!.jpeg",
    },{
        "coordinates": [53.34614498031253, -6.261632286530924],
        "event name": "Forbidden Planet",
        "description": "this photo is quite funny. I like how you can talk to me about your interests, I love when you ramble about them :)",
        "image":"forbiddenplanet.JPG",
    },{ 
        "coordinates": [53.4794953, -2.2371516],
        "event name": "Brittana hotel",
        "description": "Manchester! So fun, very even game of connect four was had. THe room did indeed have a window. I normaly dislike spending large amounts of time with people but it is different with you, I love every miniute no matter how tired we were",
        "image":"",
    },{  
            
        "coordinates": [53.466022550000005, -2.2330858190427176],
        "event name": "Manchester University",
        "description": "YO?! Loved exploring the city with you- we literally have gone international alert. This place was so cool ngl, and I really appreiacte how you were down to go with me even on the short notice",
        "image":"Man.jpg",
    },{
            
        "coordinates": [53.33849685320084, -6.259642839431764],
        "event name": "St Stephen Green",
        "description": "I like when we come here to chill, is super relaxing. Sometimes we characterise silly birds and swans which mean more entertaining to me then I let on",
        "image":"Dublinwalking.JPG",
    },{ 
        "coordinates": [53.22942936741504, -6.608233451843263],
        "event name": "Walk",
        "description": "Did I get a ladypass for this one? can't remeber. You simply did, and continue to, make me nervous- So i will continue to use my passes as I am sure I have an infite supply.",
        "image":"walk.jpg",
    },{
        "coordinates": [53.23310282977397, -6.61954164505005],
        "event name": "My House",
        "description": "When you asked me to be your Girlfriend :)",
        "image": "myhouse.jpg",
    },{
        "coordinates": [53.24984134930651, -6.5888839960098275],
        "event name": "Play",
        "description": "This was so funny. No one else could make an old irish play genuinally really enjoyable but you. It is a skill how you managed to make me smile the whole length of the play. I consider this our first date and it is one of my favorites. ",
        "image": "",
    },{
        "coordinates": [53.23210421866705, -6.639459729194641],
        "event name": "Cinema",
        "description": "We be watching funky moives do not lie. The commentary we deliever is top notch tho. Most iconic for me: the little mermaid. But honorable mentions to Dune, Inside out 2, and Barbie",
        "image": "",
    },{
        "coordinates": [53.32652885, -6.228932842105904],
        "event name": "RDS Careers day",
        "description": "It was like I found you in the wild. IN YOUR SCHOOL UNIFORM!!! was a nice surprise to my day",
        "image": "",
    },{
        "coordinates": [53.1844745909132, -6.79131031036377],
        "event name": "PBS maths quiz",
        "description": "THE COMPETITION OF COMPETITIONS. THE MOST PRESTEGIOUS OF CHALLENGES. ONLY THE RUTHLESS SURVIVE. was cute to see you in nerd form <3 since we tied I guess none of us have braging rights...yet",
        "image": "",
    },{
        "coordinates": [53.310300957073466, -6.6838932037353525],
        "event name": "Applied maths quiz",
        "description": "Where the beef with Clongoes began(or however they spell it), I remember I asked you for logtables and since then we have had MEGA PERSONAL BEEF. JK here I got to know you more and really enjoyed your company even if it was only for a little bit",
        "image": "",
    },{
        "coordinates": [53.21651837219013, -6.562957763671876],
        "event name": "Joes house (idk where is)",
        "description": "WE STARTED TALKING!! idk if we wanna thank Sam Manning or Sam Basin here but someone was skemming. I am super glad they were tho because that was when we started getting to know eachother and I loved everything about you, even tho you were BULLYING ME",
        "image": "talking.jpeg",
    },{
        "coordinates": [53.23294870482099, -6.659764051437378],
        "event name": "Halloween pt 1",
        "description": "We dressed up as Nerds, it was adorable lets not lie. Also may have kinda enjoyed when your sleeves got torn off or whatever...Also entertaining drama happened and I love how we dont get involved but we do a cheeky gossip on the side.",
        "image": "Nerds.png",
    },{
         "coordinates": [53.12612251659227, -6.9565773010253915],
        "event name": "Halloween pt 2",
        "description": "Kildare Farm Foods! IDK WHY THESE COORDINATES PUT IT IN CLANE? anywho! team rocket was a bit of a slay :) you got to met more of my friends and ride a train! one of the first times we and you went to a party together :) you made it a lot more fun!",
        "image": "teamrocket.jpeg",
    },{
        "coordinates": [53.358888300000004, -6.308530354714592],
        "event name": "ZOO!",
        "description": "ZOO! I am forever grateful you bought me that lightup spiny thing shit was mesmerising. We also did go to see the animals, and I had a blast. I love all the animal facts you have in your pocket.",
        "image": "Zoopt2",
    },{
        "coordinates": [53.23613384108949, -6.6256141662597665],
        "event name": "the Bridge",
        "description": "Shit is a bridge. U lie-end of<3",
        "image": "Bridge.jpg",
    },{
        "coordinates": [53.24365906831265 ,-6.639025211334229],
        "event name": "Quarry",
        "description": "One of your 'spots' that you think is mid. But to me, living in johnstown, this was like the grand Canyon. It was so lovely just sitting with you. I remeber you telling me about viruses and that fact is lodged into my mind now",
        "image": "Quarry.jpg",
    },{
        "coordinates": [53.33720921951305, -6.283240947111138],
        "event name": "BrickWorks",
        "description": "Patch part 2! here you are actually technially allowed into my apartment. It may be really warm (because of you and lack of airconditioning), but I love it when you are here :)",
        "image": "Brickworks.jpg",
    }

]


# Add a marker to the map
#def add_marker(coords: list, name: str, description: str, image_path = None) -> None:
#    marker_popup = f"""
#    
#        <h1 style="size: 300pc;">{name}</h1>
#        <h3 style="size 250pc;">{description}</h3>
#    """
#    if image_path != None:
#        marker_popup += f'<img src="{image_path}">'
#    folium.Marker(location=[coords[0], coords[1]], icon=folium.CustomIcon(icon_image='heart.png', icon_size=(50, 50)), popup=marker_popup).add_to(f_map)
def add_marker(coords: list, name: str, description: str, image_path = None) -> None:
    marker_popup = f"""
    <div class="popup-content">
        <h1 class="popup-title" style="font-size: 18px;">{name}</h1>
        <p  class="popup-description" style="font-size: 16px;">{description}</p>
    </div>
    """
    if image_path:
        marker_popup += f'<img src="{image_path}" style="max-width: 200px; max-height: 150px; height: auto; width: auto;">'
    folium.Marker(location=[coords[0], coords[1]], icon=folium.CustomIcon(icon_image='heart.png', icon_size=(50, 50)), popup=marker_popup).add_to(f_map)

# Generate the map
def generate():
    for point in points:
        add_marker(point["coordinates"], point["event name"], point["description"], f"images/{point['image']}")
    

    # Save the map as an HTML file
    f_map.save('static/map.html')


    # Open the generated map.html file to add custom JavaScript
with open('static/map.html', 'a') as f:
    f.write('''
        <script>
        window.addEventListener('message', function(event) {
            if (event.data.type === 'zoom') {
                var map = window.map_65bb4606acfdb1edb5a5a19656e73d3c;
                map.setView([event.data.lat, event.data.lng], event.data.zoom);
            }
        });
        </script>
    ''')

generate()