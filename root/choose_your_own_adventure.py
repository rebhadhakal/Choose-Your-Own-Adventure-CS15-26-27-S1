user_choice = None
story = """You are walking alone at midnight. You are walking home alone until your phone buzzes with a text from an unknown number.

"I know what you did last night. Walk any further, and you will regret it. - A"

While reading the text, you hear footsteps on the path right behind you.

A : Run straight inside the dark, unlocked cabin to hide.

or

B : Turn around and confront the figure following you."""
print(story)

user_choice = input().lower()
if user_choice == "a":
    story = """You go inside the dark cabin and close the heavy wooden doors behind you. As you process whatever just happened, you spot diary

    A: Pick up the diary and read what's inside

    or

    B: Ignore the diary and look around the cabin for another exit"""
    print(story)
    user_choice = input().lower()
    if user_choice == "a":
        story = """You open the diary. It reveals that your best friend has been lying to the police about the night before your friend Alison disappeared.

        Suddenly, a trap door is opened under you, dropping you to the hidden basement.
        A dark figure stands in front of the door. 

        A: Give the figure the diary to save your freedom

        or

        B: Refuse to give the diary and try to push the figure away and make a run for it."""
        print(story)
        user_choice = input().lower()
        if user_choice == "a":
            story = """The figure takes the diary, unlocks the door, and sets you free. You escaped the cabin safely, but 'A' exposes your secret to the public the next morning
            END."""
            print(story)
        else:
            story = """You attack the dark figure, but they trigger the trap door that drops the stone ceiling. The basement seals you underneath the ground before you escape.
            END. (you're dead)"""
            print(story)
    else:
        story = """You climb out using the stairs to the top floor of the cabin, where you find a laptop playing a live stream of your bedroom

        A: Inspect the laptop to see what in the world is going on in your room

        or 

        B: Try to find a way to get out the cabin safely"""
        print(story)
        user_choice = input().lower()
        if user_choice == "a":
            story = """You lean over the laptop and see that a timer hit zero, shutting off all the lights and trapping you inside. Moments later, the police arrive and arrest you because you have been framed by 'A' for a crime you did not commit

            END."""
            print(story)
        else:
            story = """You see a fire escape ladder just a bit out of reach and so you reach for it and make a run to the police station with proof that 'A' had set you up, and you finally take down the A Team

            END."""
            print(story)
else:
    story = """You look around on the sidewalk. Standing under the streetlight is a figure in a black hoodie.

The figure pulls off their hood to revealing your friend Spencer Hastings, who looks terrified

She tells you that you shouldn't be out tonight. She says, "'A' set a trap in the Lost Woods Resort, and we need to stop it."

A : Drive with Spencer to the Lost Woods Resort to investigate.

or

B : Refuse to go and demand she hand over her phone to check for texts."""
    print(story)
    user_choice = input().lower()
    if user_choice == "a":
        story = """You and Spencer arrive at a room in the motel. Inside, the walls are covered with photos of you and your friends, random coordiantes, and old newspaper scraps.
        A hidden door is behind the wardrobe and it sits half open.

        A: Go into the hidden room

        or

        B: Search the motel drawers for room keys and documents"""
        print(story)
        user_choice = input().lower()
        if user_choice == "a":
            story = """You and Spencer step into the room. The wardrobe door suddenly slams shut and is locked from the outside.
            You are trapped inside A's dollhouse and is forced to play their sick games till your last breath.

            END. (you're pretty much dead)"""
            print(story)
        else:
            story = """In the desk drawer, you find a key and a map revealing A's hideout in town. You get out through the back window before the police arrive, while holding the evidence. A gets found and arrested

            END."""
            print(story)
    else:
        story = """Spencer won't give you her phone and goes back into th street. She tells you that if you're not willing to trust her, then you're own your own. 
        Before she walks away, a dark car with tinted windows speeds around the corner towards the both of you.

        A: Push Spencer out of the way and jump into the bushes.

        or 

        B: Stand your ground while flashing your flashlight towards the driver."""
        print(story)
        user_choice = input().lower()
        if user_choice == "a":
            story = """You dive into the bushes safely as the car passes you with speed. Grateful that you saved her life, Spencer trusts you and finally reveals A's identity.

            END."""
            print(story)
        else:
            story = """The beams blinds you, and the car speeds up without slowing down for you. The car strikes right into you, then driving off
            END. (you're dead)"""
            print(story)