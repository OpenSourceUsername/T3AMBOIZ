import random
answers = ["Coolio","Awesome","Great!","I love that too!","I'm too tired for this, even though im a computer."]
subjects = [
    ["name", "My name is PICKLE RICK! WHAT'S YOURS?"],
    ["food", " My favorite food is those alien eyeballs, they're worth the butt wooping Morty."],
    ["Jerry", "We don't talk abut Jerry, he crossed me, so I made him and the government go away Morty."],
    ["Beth", "She's the best daughter you could ever have."],
    ["Marco", "Marco is the greatest person you will ever meet, he is the GOAT in my opinion."],
    ["FaZe", "We dont talk about FaZe, they vlog and do clickbait pranks."],
    ["Jake Paul", "It's everday bro with that Disney channel flow(not anymore), 5 mil on Youtube been 6 months, neva done before, past all the competition Pewdiepie is next, got that brand new Rolex, and the matching Lambo too, this is Team 10 bish, who the hella flippin you, and you know i kick em out if they aint with tha crew, ya im talking about you, you beggin for attention talking shiz on twitter too, but you still hit my phone last night, it was 4:52 and I got the texts to prove and all the recordings too, dont make me tell them the truth, and i just dropped some merch and its selling like a god churh, Ohio's where I'm from, we shoot it like a gun, the tattooes just for fun Jake Paul is number one!"],
    ["Logan Paul", "YA YEET CHECK OUT MY MERCH LINK IN BIO"],
    ["age","old enough"]
     
    #Add more subject/response texts ltr
]
print("Hi! I'm PICKLE RICK! LETS TALK ABOUT MY DUMB SIDEKICK MORTY!")
print("I bet your talking to a Python implementation of Rick from Rick and Morty becuase you probably love Rick Sanchez or you are a loner who can't initiate a conversation to another fellow human being.")
print("If you ever get the memo that you should stop talking to a computer and go outside and be social, type quit.")

while True:
    text = input()
    if(text == "quit"): #This quits the program
        break
    responded = False
    for s in subjects:
        if(text.find(s[0]) != -1): #Check for subject phrases in text.
           response = s[1]
           print(response)
           responded = True
           break
    if(not responded):
           response = random.choice (answers)
           print(response)
           
print("You finally got the *burp* memo Morty *burp* good-*burp*-bye.")

            
