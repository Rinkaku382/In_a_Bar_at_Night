define slowfade = Fade(1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)

define y = Character("You")
define g = Character("The Girl")
define gu = Character("The Guy")
define s = Character("The Singer")
define j = Character("The Journalist")
define ow = Character ("The Owner")
define b = Character ("The Body")
define nnm = Character("No Name Man")
define t = Character("Travis")


label start:
    $ idiot = False
    $ expert = False

    $ gtm = 0

    $ gtm = renpy.random.randint(1, 10)

    if gtm == 1:
        jump passage_1

    if gtm == 2:
        jump passage_2

    if gtm == 3:
        jump passage_3

    if gtm == 4:
        jump passage_4

    if gtm == 5:
        jump passage_5

    if gtm == 6:
        jump passage_6

    if gtm == 7:
        jump passage_7

    if gtm == 8:
        jump passage_8

    if gtm == 9:
        jump passage_9

    if gtm == 10:
        jump passage_10

label passage_1:
    show scene1
    with fadehold
    with Pause(4)

    scene backg_1
    with fadehold
    """
    A night like many others.

    You're sitted at a tiny table in a bar, while outside the rain falls continuously.

    All around the few tables are occupied by couples or groups of friends. Only at one table there is a single person, just like you.

    A girl, but you can't see her face completely. Just a glimpse which seems to be so beautiful that you can't do anything but fall in love instantly.

    You notice she's reading a book, and she's completely bended on it.

    Curious to see more, you stick your head towards her, but she's so much concentrated on her book you still can't see anything.

    In this precise moment the bar's door opens and a tall man enters. He reaches the counter, orders something to drink and then turns around.

    His eyes reach the girl's table and find themselves unable to look away.

    As you notice all this, you can't avoid feeling a little angry. You don't like the look in those thin eyes.

    Exactly as your worst fear predicted, he reaches the table and sits at the chair next to her.
    """
    gu "Strange, a girl so beautiful is sitting here, completely alone..."
    "She doesn't say anything. As if he doesn't even exist, she continue to read a book, silently."
    gu "Is it an interesting book?"
    "Still no answer at all."
    gu "Well, you seem like a silent girl...can I offer you something?"
    "She then raise her head, watching his face for a couple of seconds and then she looks around."
    "Your eyes catch hers, she smiles, picks up her things and then gets up."
    g "Sorry, I just saw a very dear friend of mine."
    "The guy doesn't even has the occasion of saying something that she already reached you."
    g "Hi, long time no see, huh?"
    "Her voice is high, as she tries to be listened by the guy, whose look is fixed on you two."
    menu:
        "Uh, yeah, it's been a lot!":
            "her smile is the biggest you've ever seen, as she watches you with a grateful look."
            $ idiot = False
            jump passage1_idiot
        "Sorry, but...who are you?":
            "There seems to be a strong note of disappointment in her face, as she watches you."
            $ idiot = True
            jump passage1_idiot

label passage1_idiot:
    if idiot == False:
        g "Yeah, well, how are you?"
        y "Uhm, I think he's stopped listening to us, you know?"
        g "Thank God! Can you imagine? I just wanted to sit quietly and read for the rest of the evening..."
        y "Well, I guess it happens, sometimes...So, anyway..."
        menu:
            "Who are you?":
                "She doesn't seem intended to answer your question. Her eyes lowers a bit and, then turn towards the window and the street outside."
                jump passage1_who
            "It's a pleasure to meet you!":
                "She doesn't stop smiling, not even for a second. You think she really is the most beautiful girl you ever met."
                jump passage1_pleasure
    elif idiot == True:
        g "...How did I managed to find an idiot, among all these people!"
        y "Excuse me...?"
        g "Oh come on, you've seen that man too, didn't you?"
        y "Oh, yeah...sorry."
        g "You truly are an imbecile."
        y "Hey, I just said I'm sorry!"
        g "Yeah, whatever..."
        y "Well, anyway..."
        menu:
            "Who are you?":
                "She doesn't seem intended to answer your question. Her eyes lowers a bit and, then turn towards the window and the street outside."
                jump passage1_who
            "It's...kind of a pleasure to meet you?":
                "A thin smile comes back on her face. You think she really is the most beautiful girl you ever met."
                jump passage1_pleasure

label passage1_who:
    y "Uhmm, was it an inappropriate question...?"
    g "No, don't worry. I just don't really want to talk about me. Not tonight, at least."
    y "Oh, I understand, don't worry..."
    g "Well, you can talk about yourself, if you want!"
    y "And what do you want to know?"
    g "You choose, I'm good at listening and interested in every kind of story!"
    menu:
        "Well, I work as a comic artist, but I haven't done anything famous.":
            "She seems very interested, and the smile appears again on her face."
            jump passage1_comicartist
        "I really don't know, I'm not that much interesting, sorry...":
            "A kind of melancholic smile appears on her face, as her eyes seem to grasp your soul."
            jump passage1_notinteresting

label passage1_pleasure:
    if idiot == True:
        g "You really are an idiot, then!"
        y "What?"
        g "Don't worry, I'm just joking! But you are funny, that's for sure."
    g "The pleasure is mine, really. And thanks, I think I would have leaved if it wasn't for you."
    y "Oh, you're kidding!"
    g "No, really. There isn't anyone alone, in here! And I don't think that guy would've gone away so easily."
    y "Guess you're right, yeah."
    g "So, what are you doing in here by yourself?"
    menu:
        "Just looking for a quiet place, that's all.":
            "She looks around, studying for a few seconds the couples and the groups of friends at the tables."
            jump passage1_quiet
        "Sincerely I don't know, I just wanted to go out...":
            "She looks sad as she listens to you. But, at the same time, she seems to understand."
            jump passage1_understand

label passage1_quiet:
    g "And this place seems quiet, to you?"
    y "Well, it's not the most quiet place on earth for sure, but I like it, somehow."
    g "Guess that's fair enough, then. You know, I feel like there's something of mine in here. Memories, or something like that."
    y "You mean you think of having being here some time ago? And you can't remember it well?"
    g "Something like that, yeah."
    menu:
        "And what do you remember?":
            "She starts thinking about it, looking completely concentrated on remembering."
            jump passage1_whatremember
        "Is it something from yout childhood, maybe?":
            "Her eyes lower with subtle embarassment."
            jump passage1_childhood

label passage1_understand:
    g "I kind of understand what you mean, you know? I feel kind of...trapped, sometimes, and I need to go out."
    y "Trapped? What do you mean?"
    g "Trapped between my house's walls, or between my thoughts. Even my memories, sometimes, make me feel trapped."
    y "Do you have particularly bad memories...?"
    g "Guess you could call them bad, yeah. But they're a lot, for sure."
    y "A lot of sorta bad memories...that seems something heavy to handle, huh?"
    g "In a way, yes."
    $ renpy.pause(2.0)
    g "Have you ever had the impression of...having memories that don't belong to you?"
    menu:
        "Uhm no, not really...":
            "She rapidly passes a hand through her long, dark hair."
            jump passage1_nomemories
        "I don't know, but I've read a comic about something similar.":
            "A new light shines in her eyes. She seems excited."
            jump passage1_comicmemories

label passage1_comicartist:
    g "A comic artist? That's incredible!"
    y "Oh no, it really isn't. It's just a work..."
    g "Come on, I'm sure it's amazing! Can you tell me what you're working on? Or is it top-secret?"
    y "In fact I shouldn't, but it's not that important...I'm working on an action comic."
    g "Oh God! Is it something like Dragon Ball? Or a super hero story?"
    y "No, no! Something more like the old western movies. You know, similar to Sergio Leone's works."
    g "That's incredible, I love those movies! And it really seems like an interesting project!"
    y "Oh, thanks."
    g "Hmm, listen, have you ever worked on stories about memories...?"
    y "Uhmm no, I haven't. Why?"
    g "Nothing, it's just that sometimes I get this...images, that don't seem to be mine at all."
    y "You mean dejà-vus?"
    g "No, they are complete memory passages, but that I haven't lived."
    y "Well, that's strange..."
    g "...you don't believe me, don't you?"
    menu:
        "Well, it truly is a funny story.":
            "She hints a smile, but isn't really happy about what you just said."
            jump passage1_funnystory
        "It's a bit strange, but I guess it could be true.":
            "She slowly rubs her fingers, embarassed, but her face seems strangely happy and relieved."
            jump passage1_couldtrue

label passage1_notinteresting:
    g "I know a thing or two about not being interesting, but I also know that everyone has something interesting to tell about him or herself."
    y "I think you're right, but I really don't know what I could tell you..."
    g "Well, don't you remember anything from your childhood, for example?"
    menu:
        "I remember the smell of my father's ink, but...":
            g "But?"
            y "It seems like a normal thing to me."
            g """
            And yet it's something related to you, and you only, don't you think?

            That smell as he pured it into the inkpot and then started writing his novels must've been truly important.
            """
            y "Yeah, that...that's true. But how did you know about the novels?"
        "I clearly remember my mother's voice when he sang.":
            g "That's a beautiful memory. I'm sure she sang truly beautiful songs, right?"
            y "Yes, absolutely. She used to sing one in particular..."
            g "'Under the sycomore trees'?"
            y "Well, how did you..."
    g "That's my 'something to tell'. Sometimes I see other people's memories..."
    menu:
        "You're joking, right?":
            "She puts up the saddest smile you've ever seen and silently nods."
            jump passage1_jokingright
        "That...that's amazing...":
            "She's surprised by your reaction, just as you are about her story."
            jump passage1_amazing

label passage1_whatremember:
    g "I remember of sitting here, at this same table, waiting for a girl who never came and then...then I met someone and spend the night with her."
    y "And you forgot something like that?"
    g "Not exactly. It's more like it happened to someone else, but it's a part of my memories."
    y "It happened to someone else..."
    g "Yeah, it's something that happens to me quite often...I just have these imagese which belong to other people."
    menu:
        "That really seems like a torture to me.":
            "She laughs with all her voice. Her face is now red and her teeth, white as milk, shine in front of you."
            jump passage1_torture
        "Well, you sure are good at telling creepy stories!":
            "The expression on her face turns all gloomy and sad, as if she regretted telling you that."
            jump passage1_creepystories

label passage1_childhood:
    g "No, not really, it's just that..."
    y "That?"
    g "Well, that sometimes i get these images. Memories that don't belong to me."
    menu:
        "...Are you crazy or what?":
            "She's shocked. For a couple of seconds she doesn't say anything or move at all."
            jump passage1_crazy
        "That really is something!":
            "Surprised, her eyes widens and her smile too, a second later."
            jump passage1_reallysomething

label passage1_nomemories:
    g """
    Well, maybe it'll seem strange to you, but sometimes it happens to me.

    I have these memories that don't feel like mine. And yet they pass through my mind.

    I don't even know why, but it really feels strange...

    And as we talked I thought that maybe you could...understand, but I guess I was  wrong.
    """
    menu:
        "Maybe I can't understand, but...":
            "Curious and anxious about your answer, she turns pale."
            jump passage1_canunderstand
        "Sorry, but...is this a joke?":
            "Somehow sad and disappointed, she lowers her eyes."
            jump passage1_joke

label passage1_comicmemories:
    g "A comic, you say?"
    y "Yeah, but I can't remember the name..."
    g "What was it about?"
    y "It was about a girl with no name, but who has the entire human being's memories! The art was really something, I've always admired the man who drew it."
    g "And do you believe in that story?"
    y "Well, it'a a sci-fi comic, so it's only a fantasy."
    "She nods, with a melancholic smile on her face."
    g "Only a fantasy...guess you're right."
    y "Yet, it's an incredibe story. It would be incredible if, out there, there is someone like that, don't you think?"
    g "I'm sure it would. But it's really funny, you know?"
    y "What?"
    g "A girl with no name. No name, just...just like me."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_funnystory:
    g "Yeah, it is, right? A terribly funny story."
    y "Is there something wrong?"
    g "No, not at all, I just realized it's late, you know. I think it's better if I go."
    $ renpy.pause(2.0)
    g "But I'm glad you found that story funny. I really am."
    "She then leaves the bar, casting a sad atmosphere on you and the impression that, maybe, you misunderstood her"

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_couldtrue:
    g "You really think that?"
    y "Well, yeah. This world is so big that we can't always know everything about it, don't you think?"
    g "I'm glad. I really am. Thank you..."
    y "Why are you thanking me?"
    g "For believing me. It really is rare nowadays for someone to completely trust and believe in a stranger."
    y "Especially with a story like yours, huh?"
    g "Yeah."
    y "I don't know, maybe I'm just credulous."
    g "Maybe, yes. But that makes me happy nonetheless."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_jokingright:
    g "Well..."
    y "Sorry, I think...I think it's better if I go. I'm not here to be taken for a stupid."
    g "No wait, please...!"
    y "It's better if I go, really. Goodbye..."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_amazing:
    g "You think it's amazing?"
    y "Of course! It's like a super power, isn't it?"
    g "Sometimes it is, others it feels more like a curse, to be sincere..."
    y "Oh, I imagine it's difficult..."
    g "Yes, it sure is."
    y "...Listen, would you like to drink something? Let's forget about it for now and enjoy the night."
    g "Yeah, thanks, it would be great!"
    "Her smile...it's so beautiful you can't stop staring at it."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_torture:
    g "Yeah, you're absolutely right, it really feels like a torture. But not always."
    y "And what kind of memories do you see?"
    g "Well, it depends. Most of them are sad but others are joyful. The most funny ones, though, happens to be the sex ones!"
    y "What?!"
    g "It's a bit embarassing, because they may happen in a hotel room or in the  middle of a street or in a shop."
    y "Well, that's...unexpected..."
    g "Don't tell me!"
    y "You don't seem to dislike them, though!"
    g "Well, who would ever dislike seeing some sex memories?"

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_creepystories:
    g "Creepy stories, huh...?"
    y "Uhmm, what? Have I said something wrong?"
    g "No, absolutely. You're just a common human being, I guess."
    "With that said she gets up, grabs her things, and gets out of the bar without saying a word."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_crazy:
    g "Well, if I'm crazy you're an asshole, do you know that?"
    y "What? You tell me some strange story and then insult me?"
    g "Does something forbids me to?"
    y "No, it just demonstrate you totally are crazy!"
    g "Yeah, well goodnight, then."
    "Furious she leaves the bar, slamming the door."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_reallysomething:
    g "Really something?"
    y "Yeah, I mean, it's a great story! Never heard something like that."
    g "Well thanks, I guess..."
    y "You truly are special, then?"
    g "If...if you would call it like that yess, guess I am."
    y "To have met someone who sees other people's memories...that really is incredible..."
    g "Don't take it for something too much special, please. It really isn't. It's only strange and difficult."
    y "Oh, I'm sorry."
    g "Don't worry, it happens a lot more than you'd think. It's not something that happens to everyone, after all."
    y "Yes, I imagine. Yet, it truly seems incredible."
    g "...thanks."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_canunderstand:
    g "But...?"
    y """
    But you can never know...I mean, everyone is somehow special, isn't it?

    For example, there are almost three metres tall people, or magicians who can do formidable things.

    So I guess it could be natural for someone in this world to be able to see other people's memories.

    I mean, nobody can never be sure about what humans could be capable of, right?
    """
    g "Uhm, I don't know if I'm following you completely but I guess I understand a little."
    y """
    Let me try to explain better, than...what I mean is that your specialty is wonderful, for me.

    And I think it's something completely human to be able to do something similar, even though t's not an everyday capacity.
    """
    g "W-well, it's the first time that someone tells me something similar..."
    y "Oh...really?"
    g "Yes, and it's beautiful."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

label passage1_joke:
    g "Uh...yeah, of course it is!"
    y """
    What a relief! It could've been so scary, you know?

    I would really be embarassed if, for example, you would've been able to read my memories!
    """
    g "Yeah, it really would have been scary!"
    y "Listen, would you like to go out?"
    g "Oh no, sorry, but it's kinda late, so I have to go."
    y "Yeah, you're right. Well, goodbye then, and thanks."
    g "You're welcome, bye."

    $ persistent.passage_1 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 1 ##########################################################################################################################################################################################################################################

label passage_2:
    show scene2
    with fadehold
    with Pause(4)

    scene backg_2
    with fadehold
    s """
    First of all, we'd like to thank you for being here.

    It's our first concert in this place, so we're glad you all came.

    This song is called 'harlem nocturne' and we think it really is appropriate for tonight so...enjoy.
    """
    """
    The bar is full of people, all sitted at the different tables.

    In their hands they hold big cups of coffee, cigarettes or glasses full of different alchoholics. Mostly beer, though.

    You are sitted in a corner, at a table for two even though you're alone.

    It wouldn't be bad to reachsomeone for some talking, just to better enjoy the night, but you think that being alone it's fine anyway.

    So you don't move an inch. You slowly drink your coffee and listen to the band playing.

    At least, now that they're playing an instrumental, you don't have to focus on lyrics, trying to translate all the japanese words.

    It's tiring, and that's why you had to drink three cups of coffee in a row.

    As you look around, trying to watch the other people's faces in the dark, you notice a man standing not so distant from you.

    He's holding a small notebook and sometimes he writes something on it with a short pencil, than delets it and writes something else.

    He notices you too, after a while, and smiles back. He then points at the other chair at the table, asking if it's occupied.
    """
    j "Thanks, friend, I was starting to think I'd have to stand for the whole concert. It really would've been a torture, don't you think?"
    y "A true torture indeed."
    s """
    When we started playing, nobody listened to us. It still feels strange to see so many people, tonight.

    Since we started, reviews and articles have not been gentle with us.

    Still, you, those who listen to our music and support us, acontinue to fill us with joy.

    Even though we're not so loved by the critics, the so called 'experts', we're loved by you all.

    Thank you for that.
    """
    play music "harlem.ogg"
    j "The experts..."
    y "Sorry, did you say something?"
    j """
    Oh, yes, I was just wondering about the concept of experts, you know.

    You, for example, do you see yourself as an expert in something? As music, for example, or cinema.
    """
    menu:
        "Yes.":
            "He smiles, as if he already knew the answer."
            $ expert = True
            jump passage2_expert
        "No.":
            "For a second, a shadow of surprise appears on his face."
            $ expert = False
            jump passage2_expert

label passage2_expert:
    if expert == False:
        j "And why?"
        menu:
            "It's difficult to know everything about something.":
                "A sincere and funny smile appears on his face."
            "I'm just not interested in being an expert.":
                "He seems satisfied, as he turns towards the band."
    elif expert == True:
        j "Why do you considerate yourself an expert?"
        menu:
            "I've spent some years studying cinema...":
                "He seems surprised, but not too much impressed."
            "Well,I listen to a lot of music.":
                "He takes your words with a short laugh, before returning serious."
    j "So, you think your opinion matters?"
    menu:
        "I think every opinion equally matters.":
            j "That's a nice opinion. A little utopian, though."
        "Well, experts' opinions value more.":
            j "I guess you could say that, yes."
    j """
    You know, I've spent years wondering about the concept of opinions.

    How much they value, if they value at all. And, mostly, if experts' opinions really matter.

    Truth is, that they matter and at the same time they don't.

    Everything you think, everything you say and choose, matters only to you.

    By that, I mean thet for me your opinion might not be so much necessary, do you understand that?

    But at the same time, this depends by the conversation'0s atmosphere and by the importance of your knowledge.

    The way you expose your opinion is important just as much as what you are saying. Yet, I can choose to not listen to your opinion.

    Isn't this how internet works? And how social networks abuse and exploit people's thoughts?

    On what truths can you base your experience as an expert? How many movies have you watched, how many songs have you listened?

    You can say 'I am an expert in japanese music' and, yet, not even know who Zazen Boys are.

    In the same way, you can define yourself an expert of european cinema, and talk bad about Von Trier's cinema only because 'you have heard he is a bad person.'

    Oh, sorry, I think I'm being too much personal,now.
    """
    j """
    What I mean is, that true experts does not exist in the art's world.

    If you look around, everyone wants to expose his own opinion, even though most of those people doesn't even have an opinion.

    Sometimes, they don't even have a necessarily open mind in order to comprehend art.

    But art lives in the talking, doesn't it? It truly show its power when people discuss about it.

    Let's say you go to the cinema with some friends: each one of them, as they watch, matures his own idea and experience.

    That happens only with not-straightforward art, though.

    Let's now say that you are a videogames player. The ultimate form of freedom, right?

    You do what you want with the rules that designers have given you. But those rules are made to give you that freedom.

    And the more freedom you have, the more you enjoy the game.

    But what if I, as a designer, take away that freedom and force you to be a spectator?

    What if your freedom and opinions doesn't matter anymore?
    """
    y "But...isn't a dialogue supposed to be an exchange of choices?"
    j "Basically yes. But you're not the owner of the discussion. I could even end it here, if I want."

    stop music fadeout (2)
    show black
    with fadehold

    $ persistent.passage_2 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 2 ##########################################################################################################################################################################################################################################

label passage_3:
    $ conversation1 = False
    $ conversation2 = False
    $ emptycup = False
    $ cigarettelit = False
    $ cigaretteunlit = False
    $ milkpoured = False
    $ coffeepoured = False
    $ trip = False
    $ work = False
    $ appreciation = False
    $ lucille = False

    show scene3
    with fadehold
    with Pause(4)

    scene black
    with fadehold
    play music "eggsandsausage.ogg" fadein(5)
    """
    A night like many others.

     Tom Waits is playing in the background.

    Just one song, in loop, as if the bartender has fallen in love with it and doesn't want to listen to anything else.

    You're sitted at a table, drinking coffee and smoking cigarettes.

    But at one point, a young man who looks like he's been on the street for days, enters in the bar.

    He looks around and then notices you.

    You look at him, greeting him with an open smile as he moves towards your table and then sits.
    """
    scene backg_3
    with slowfade
    y "It's been a long time, Travis! How are you?"
    t "Fine, thanks. What about you? I've heard you've been around."
    menu:
        "Yes, me and Mary have been on a little trip.":
            $ trip = True
            t "A trip? Where?"
            y "We've been to Paris. She has always dreamt of going there so...so I just took her."
            t "You just took her?"
            y "Yes, one day I made up my mind, bought the tickets and told her."
            t "That really should've been great..."

        "Well, you know, work...":
            $ work = True
            t "That's too bad. But i bet it's nice to just travel, even for work."
            y "Yeah, it's nice. You get to see many places."
            t "Travel throughout the wolrd...that must be very interesting. I bet you've seen many things in these years."
            y "Yeah, I did."
            t "Incredible, truly incredible..."
    t "Me...I have to say, I'm not so interesting, these days."
    menu:
        "What do you mean?":
            t "You know, it's always the usual. Nothing happens, nothing changes, all stays the same."
            y "Oh, I understand."
        "Well, sometimes that's good too.":
            t "You're right. Sometimes it is..."
    t "But anyways, have some coffee."
    $ coffeepoured = True
    y "Thanks, Travis."
    t "Here, I've some cigarettes left, if you want to smoke some. They're strong, though."
    "He takes a full pack out of a pocket in his jacket and places it on the table."
label passage3screen1:
    if conversation2 == True:
        call screen passage3screen3
    elif conversation1 == True:
        call screen passage3screen2
    elif conversation1 == False:
        call screen passage3screen1
label passage3_hiscoffee:
    scene backg_3
    if appreciation == True:
        """
        His coffee is dark as the night outside the bar.

        As he drinks it, it seems he enjoys it very much.
        """
    elif appreciation == False:
        $ appreciation = True
        y "You sure like it strong, huh?"
        t "Yeah, strong cigarettes and strong coffee. I just enjoy it."
        y "That's good, truly good."
        t "Oh, you can bet it is."
    jump passage3screen1
label passage3_mycoffee:
    scene backg_3
    if coffeepoured == True:
        menu:
            "Drink":
                $ coffeepoured = False
                $ milkpoured = False
                "In one big sip you empty the entire cup."
            "Don't drink":
                $ coffeepoured = True
                "The coffee is too hot, so you leave it there for some more."
    elif coffeepoured == False:
        "I should pour some coffee."
    jump passage3screen1
label passage3_pourcoffee:
    scene backg_3
    if coffeepoured == True:
        "You've already poured it."
    elif coffeepoured == False:
        menu:
            "Pour coffee.":
                $ coffeepoured = True
                "The black and strong-flavoured liquid flows in your cup."
            "Don't pour coffee.":
                $ coffepoured = False
                "You don't really feel like drinking coffee."
    jump passage3screen1
label passage3_pourmilk:
    scene backg_3
    if milkpoured == True:
        "There's no need to pour more milk."
    elif milkpoured == False:
        menu:
            "Pour milk.":
                $ milkpoured = True
                "You add some milk in your cup."
            "Don't pour milk.":
                $ milkpoured = False
                "You prefer not to add milk."
    jump passage3screen1
label passage3_cigarette:
    scene backg_3
    if cigarettelit == True:
        "There's no need to light another one."
    elif cigarettelit == False:
        menu:
            "Take a cigarette.":
                $ cigarettelit = True
                "You take a cigarette from the pack, and you light it."
            "Don't take it.":
                $ cigarettelit = False
                "Your hand moves closer to the pack of cigarettes, but you decide to not smoke."
    jump passage3screen1
label passage3_tosscigarette:
    scene backg_3
    if cigarettelit == True:
        menu:
            "Toss the cigarette.":
                $ cigarettelit = False
                "You squash the cigarette into the ashtray. Some traces of ash remain on your fingers."
            "Don't toss the cigarette.":
                $ cigarettelit = True
                "You think about tossing the cigarette, but then decide to continue smoking it."
    elif cigarettelit == False:
        "You don't have any cigarette to toss."
    jump passage3screen1

label passage3_discussion1:
    scene backg_3
    $ conversation1 = True
    if trip == True:
        t "So, how was Paris?"
        menu:
            "Everything is just incredible!":
                t "Really? I'm glad to hear that."
                y "You know what? You should go there, once you can. You would like it."
                t "Yeah, you're right. I would..."
            "Not bad, but I wouldn't live there":
                t "Guess I understand. Nowhere is better than home, right?"
                y "Absolutely. There are no places like this, there. And there are no friends."
                t "No friends, huh?"
                y "Nope."
    elif work == True:
        y "And how is work going?"
        menu:
            "Not bad, some new contracts on the way":
                t "That's a good news, right?"
                y "Of course! Lots of places are asking me to play there and the prizes just keep increasing."
                t "You finally made it, then! Oh, that's so good to hear, really."
                y "Thank you."
                t "I really mean it, I'm happy for you."
            "Tiring, as always.":
                t "Too bad, really too bad. No time to rest, huh?"
                y "Absolutely no time, right. As soon as I've finished playing in a place I have to leave for another."
                t "Sorry to hear that..."
                y "Don't worry, it's just how life is."
    jump passage3screen1
label passage3_discussion2:
    scene backg_3
    $ conversation2 = True
    menu:
        "So, what are you doing these days?":
            t "The usual, you know...girls, drinks, some little wandering here and there."
            y "Yeah, the usual indeed. And what about Lucille?"
            t "...Lucille?"
            y "Yeah, your girlfriend."
            t """
            Oh, yeah, right...Lucille...Lucille yeah, well, we left each other.

            She told me I wasn't reliable, I didn't earn too much, I didn't wash the dishes very well, so she left.

            You know, it's the usual.
            """
            y "Uhm not so usual, I guess."
            t "But it doesn't matter! It really doesn't matter."
            $ lucille = True
        "It's nice here.":
            t " Yeah, it is. How did you managed to know about this place?"
            y "Well, a friend of mine told me about it, yet I never came before tonight."
            t "I see. Nice music, too."
            y "Yes, but it would be nice to hear something else from Waits, too."
            t "Guess you're right."
    jump passage3screen1
label passage3_discussion3:
    scene backg_3
    if lucille == True:
        t "Well, to be honest...Lucille didn't left for that. She disappeared without saying anything."
        y "At all?"
        t """
        Yeah, at all. From that day, I always feel unconscious. I don't pay attention to nothing, I don't do nothing.

        I'm just a shell, you know? An ugly and empty shell, waiting for her to come back. But she doesn't.
        """
        menu:
            "I'm really sorry.":
                t "I'm sorry too, yeah. But what can we do about it? Nothing, I guess."
                "He's sad as he drinks his coffee. From now, neither of you speaks anymore, you just enjoy the night, the music and the atmosphere."
            "Can I help you in any way?":
                t "I don't know. I really don't know. Maybe...maybe talking about it is already enough."
                y "I understand..."
                t """
                You know, I've been doing...bad things. Treating others like items. Drinking myself to sleep every night.

                Shouting at people, stealing from people, fucking with random people. I don't even feel human anymore.
                """
                if trip == True:
                    t """
                    But you know what? I think seeing you after all this time, knowing things for you are good...

                    It just makes me feel better. Really.

                    Listen, what about a toeast?
                    """
                    call screen passage3goodend
                elif trip == False:
                    t """
                    You know, just talking with you feels nice.

                    Really, I mean it. Even if things are just ok for you, it's good. I guess even old friendships can last in time, huh?
                    """
                    y "Guess you're right, yeah."
                    "He smiles at you, drinking his coffee. From now, neither of you speaks anymore, you just enjoy the night, the music and the atmosphere."
    else:
        t "Well, it's been nice seeing you, but now I really have to go."
        y "Really? Can't you stay a little more?"
        t "No, I'm sorry, I have some unfinished business, you know, and it's better if I take care of it."
        y "That's good, don't worry. See you, then."
        t "Yeah, see you, it has been nice."
        "He leaves the bar, disappearing in the darkness of the night."

label passage3_goodend:
    "Both of you raise your cups of coffee and drink."

    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 3 ##########################################################################################################################################################################################################################################

label passage_4:
    show scene4
    with fadehold
    with Pause(4)

    scene backg_4
    with fadehold
    """
    This is passage 4.
    """
    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 4 ##########################################################################################################################################################################################################################################


label passage_5:
    show scene5
    with fadehold
    with Pause(4)

    scene backg_5
    with fadehold
    play music "zazenbo.ogg"
    """
    This is passage 5.
    """
    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 5 ##########################################################################################################################################################################################################################################

label passage_6:
    show scene6
    with fadehold
    with Pause(4)

    scene backg_6
    with fadehold
    """
    This is passage 6.
    """
label passage6_screen:
    call screen passage6screen
label passage6_coffee:
    "That really is a good coffee."
    jump passage6_screen
label passage6_text:
    "Well, let me tell you about that text..."

    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 6 ##########################################################################################################################################################################################################################################

label passage_7:
    show scene7
    with fadehold
    with Pause(4)

    scene backg_7
    with fadehold
    """
    This is passage 7.
    """
    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 7 ##########################################################################################################################################################################################################################################

label passage_8:
    show scene8
    with fadehold
    with Pause(4)

    scene backg_8
    with fadehold
    """
    This is passage 8.
    """
    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 8 ##########################################################################################################################################################################################################################################

label passage_9:
    $ body_res= 5
    $ mind_res = 5
    show scene9
    with fadehold
    with Pause(4)

    scene backg_9
    with fadehold
    play music "warushawa.ogg" fadein (2.0)
    """
    A bar with dim lights and few people at the tables.

    Nobody talks much, and japanese punk music is playing.

    Your body, a feminine one, is sitted at a table, reading a magazine and drinking coffee.
    """
    menu:
        "Put sugar in the coffee.":
            $ body_res -= 1
            "You start stirring the coffee. The slowmovements and metallic sound of the teaspoon reminds you of a sweet lullaby."
        "Turn the page.":
            $ mind_res -= 1
            "As you turn the page, you start reading a new article. It's about a new gun's features and the impact it had on the weapon's fanatics."
    """
    A new group of clients enter in the bar.

    The owner greets them immediately. It seems like he knows them all very well.

    After taking them to their table, he reaches you. In his hands he holds a coffeepot.
    """
    ow "Do you want some more?"
    menu:
        "Yes, thanks.":
            $ body_res -= 1
            "He pours some more coffee, filling the cup to the edge."
        "No thanks, I still have to finish this.":
            $ mind_res -= 1
            ow "No problem, I'll come back later."
    """
    In a corner of the bar, a couple suddenly starts shouting.

    But then, realizing they're attracting everyone's attention, they lower their voice.

    Still, they continue to argue.
    """
    menu:
        "Drink the coffee.":
            $ body_res -= 1
            "You take a sip from the cup, slowly. The hot liquid warms up your throat."
        "Read the magazine.":
            $ mind_res -= 1
            "This article is about the spreading of new weapony technologies through the world and the consequent proliferation of armed conflicts."
    """
    A drunk man is talking with the owner at the counter.

    He continuously drink shots of alcohol, one after the other.

    The owner listens to him carefully, gently answers to his questions and gives him advices based on his experiencies.

    At one point, the drunk man starts crying and the owner starts preparing him a hot teato calm him.
    """
    menu:
        "Go on drinking.":
            $ body_res -= 1
            "The coffe is starting to get cold. But it's still very good."
        "Go on reading.":
            $ mind_res -= 1
            "An article about the recent bombing of a city in eastern Europe. Photos of the destroyed buildings and the victims are spreaded throughout the article."
    """
    A man, not so far from you, is reading a book.

    He seems really focused on it. As you try to read the title, you realize it's a collection of poems from Arsenij Tarkovskij.

    A smile appears on your face as the memories of his poetry start flowing in your mind.
    """
    menu:
        "Empty the cup.":
            $ body_res -= 1
            jump passage9_coffeeend
        "Finish reading the magazine.":
            $ mind_res -= 1
            jump passage9_magazineend

label passage9_coffeeend:
    if body_res == 0:
        """
        Because of all the coffe you've drunk your stomach starts feeling bad.

        You need to go to the toilet as soon aso possible.

        And as you seat in the toilet, a voice coming from your stomach starts talking.
        """
        b "That's what you get when you drink so much coffee!"
        y "Sorry?"
        b "You heard me very well! It's your body talking. Stop giving me all those stupid orders."
        y "What?"
        b "If you continue, worst things will happen, don't you know? So stop hurting me so much!"
    else:
        """
        The night still is long ahead of you.

        Quietly, most of the clients in the bar start disappear.

        They go away, mixing with the night's darkness. But your place is in there, in the bar, until the dawn's light will appear.
        """

    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_3 = True
    $ renpy.end_replay()

    return

label passage9_magazineend:

    if mind_res == 0:
        """
        You feel tired from all the reading.

        You close your eyes, just for a little moment. Just to relax for a couple of seconds.

        But you actually end up sleeping.
        """
        b "That's what you get by tiring me so much."
        y "What?"
        b "Don't you know you should take more care of me? It's the middle of the night, you should be sleeping now."
        y "Who...who might you be, excuse me?"
        b "I'm your body, of course!"
    else:
        """
        Slightly tired and bored, you look at the few clients, at the owner, at the man reading the collection of poems.

        The night is still long, yet you don't want to go back home.

        It feels like this bar is your home, now. If you could, you'd spend the rest of your life in here, reading magazines and drinking coffee.
        """

    stop music fadeout (2)
    show black
    with fadehold
    $ persistent.passage_9 = True
    $ renpy.end_replay()

    return

##### END PASSAGE 9 ##########################################################################################################################################################################################################################################

label passage_10:
    $ drink = 0
    $ punishment = False
    show scene10
    with fadehold
    with Pause(4)

    scene backg_10
    with fadehold
    play music "nightisover.ogg"
    """
    A tiny room; the walls are gray and so are the floor and the ceiling.

    In front of you, a tired man holds an old rifle.

    He's slowly and silently smoking a cigarette, his eyes fixed on the door and the barred windows.

    From outside the room you can hear strange sounds, similar to a mass of human's cry but distorted.
    """
    nnm "Those fuckers are still out there..."
    y "I don't think they're gonna leave."
    nnm "We can only hope the bodies in the other room don't wake up. If they do it'll be the end for us."
    y "Yes, that's true..."
    "For a couple of seconds he looks at you, than turns again towards the door and the windows."
    nnm """
    I'm sorry. I guess it's not the best thing in the world to end up with someone like me in this kind of situation.

    Still, it's better than being out there, huh?
    """
    y "You're right."
    nnm "Sorry, I was trying to make a joke, but..."
    menu:
        "Don't worry, it's alright.":
            "He quietly nods, smiling at the door and windows."
        "I'm not in the mood for jokes, now.":
            nnm "Yeah, sorry..."
    """
    As the silence returns to surround everything in the room, only to be broken by the sounds from outside, you feel anxious.

    How did you find yourself in this situation? And how can you manage to escape?

    All questions that, even though aren't useful at all, still lingers in your mind.

    And the more you think, the more you feel that anxiety and hopelessness, asking yourself which choices would be the better ones.
    """
    nnm "Listen, you know what?"
    y "What?"
    nnm "I'm tired of looking at the door and the windows."
    "He stops to think for a couple of seconds."
    nnm "Come on, let's drink something. We're at the world's end, so we might at least enjoy our deaths."
    y "Hm,ok. I'm not good at drinking though. I completely loose the ability to speak."
    "He gets up from the floor and takes a bottle from a credenza in the left corner of the room, then sits in front of you at the tiny and metallic table."
    "It's a large bottle of red wine, which he pours in the two paper cups on the table, right before lighting himself a cigarette."
    menu:
        "Drink.":
            $ drink += 1
            "You take the paper cup and empty it in one sip."
            nnm "Well, you sure put a lot of effort in drinking!"
        "Don't drink.":
            $ drink += 0
            nnm "It seems you're not really in the mood, huh?"
    "He gulps all the wine in his paper cup; a satisfied look on his face."
    nnm "You know, I use to think a lot about the unfortunate situation we've found ourselves in."
    jump passage10_drink1

label passage10_drink1:
    if drink == 0:
        y "That's something we have in common, I guess."
        nnm "And to what conclusions do you come?"
        menu:
            "It's all the government's fault.":
                nnm "Heh, yeah..."
            "I think this is our punishment.":
                $ punishment = True
                nnm "I couldn't agree more."
    elif drink == 1:
        y "Oh, you do?"
        nnm "Of course I do! And the more I think about it, the angrier I get."
        y "Angrier? Why?"
        nnm "You know, sometimes I think that those things out there are only victims. Of wars, of government's exploitation but even of life itself, of feelings."
        y "I followed you until life itself..."
    nnm """
    I've always thought of having the possibility to choose for myself, you know. If I want to go out or not, if I want to sleep or not. Things like that.

    What happened to the world now, though...it feels like I've wasted my whole life.

    Can you imagine it? Doing nothing but what you want and then, one day, everything falls in ruins and what can you say about your existence?

    I've never seen myself as a part of society, of it's politic and all that. And now I think that maybe it's my fault. It's people like me who ruined everything.

    Caring about your businesses, about the things that are important only to yourself...it's good, you know, kinda a sacred rule. Yet, that brought me to nothing.

    Nothing, except this room in which we're locked and this rifle. And the wine.
    """
    if drink == 1:
        "He fills both paper cups again."
    elif drink == 0:
        "He fills his paper cup again."
    menu:
        "Drink.":
            $ drink += 1
            y "The wine is actually the only positive thing in this situation."
            nnm "You can bet on that."
            "He smiles at you and then drinks too."
        "Don't drink.":
            $ drink += 0
            y "Maybe too much wine..."
            "He shrugs and then drinks."
    nnm "It seems they're way more savage, tonight."
    "The noises from outside become a mass of howlings."
    nnm "We're just passing the darkest hours of the night. Soon it will be dawn. Their dawn."
    if drink == 0:
        y "Do you think we'll ever get away from here?"
        nnm "I don't know. I really don't know. The others are all dead, you know that too."
        "A short pause of silence between you two. His eyes look sad as they turn towards the nearest window."
        nnm "I don't even know if we can afford to think that we'll be able to survive..."
        y "I don't know either."
        if punishment == True:
            nnm """
            You know, if I try to think about how this all started it's really difficult to remember.

            Before you said that this is our punishment and I think you're right.

            The dead are back for us. Those who gave us birth, who gave us their world hoping we would make it better and then disappointed by our actions...

            They're back to reclaim their possessions, their belongings. The planet itself is theirs.
            """
        else:
            nnm """
            Their howling means they want us. They know we're here.

            That's why, after all, we have to defend ourselves. That's why we have this...dear old rifle, here.

            Yet, it feels like we're the ones standing on the wrong side and not them, you know?
            """
    elif drink >= 1:
        "Your eyes linger to the tiny stripes of sky that are barely visible through the barred windows."
        y "Isn't the sky beautiful, though?"
        nnm """
        Yes, you're right.
        I've seen many nights but let me say this, since they came to life the nights have become more and more beautiful, indeed.
        """
        y "That's absolutle true."
        nnm "You hear them? Their howlings...they're calling us, I think. They want us to be with them outside, in this splendid night."
        y "Really?"
        nnm "Yeah, I guess. Yet, if we go out we'll be dead. It's like the siren's calling, you know? It's beautiful and dangerous at the same time."
        y "A siren's calling..."
        nnm """
        Have you ever heard a beautiful song that hurts you at the same time?

        Like, when you really miss someone whom that song reminds you of.

        You want to listen to it, even though you know it will hurt you.

        I think it's the same thing here. In their howling we hear the relations we had with all those who aren't here anymore.

        We want to join them, in order to be happy again but we know it's dangerous and we'll never come back.
        """
    if drink >= 1:
        "He fills both paper cups again."
    elif drink == 0:
        "He fills his paper cup again."
    menu:
        "Drink.":
            $ drink += 1
            "After drinking he gets up and reaches the nearest window.."
            jump passage10_end1
        "Don't drink.":
            $ drink += 0
            "As he empties his paper cup, he just stares at the emptiness of the room."
            jump passage10_end2

label passage10_end1:
    if drink <= 2:
        nnm "Yeah, we wish to join them..."
        y "Don't tellme you're gonna open it!"
        nnm "Of course not, but still...sometimes I wonder if I did open it. Of course I would die, but..."
        "He pauses himself for a second, his eyes lost on the light seeping in through the boards on the window."
        nnm """
        During the night, I realize how much truth there is in the fact that they're the victims.

        Even though we don't know why they're alive again, even though they want to eat us, they just fall under our bullets.

        And the bullets...we use them to keep us safe. To defend ourselves, because we're unable to understand when it's the moment to accept what we fear, you know?

        This feeling and these thoughts, they become stronger at the passage of time. And at night, when this light shines through the room, I can't keep them inside.

        I just can't.
        """
        """
        You watch that light, cast by the moon on the floor and the furniture.

        It's beauty, as it brightens the room, hypnotize you.
        """
        nnm """
        When I'm surrounded by this beauty, I really realize that, maybe, dying isn't that bad. And accept death becomes normal, natural.

        I ask to myself: why do I have a rifle in my hands? Why do I want to kill? Who do I want to kill?

        I've known the answer for so many time, but now...now it's useless.

        In the moment in which this rifle could save me, I find it to be the greatest evil on the planet.
        """
        jump passage10_end
    if drink == 3:
        nnm "Wine, moon and a rifle. A terrible yet beautiful mix, don't you think?"
        y "Well, I think I'm dead tired."
        nnm "Dead tired? Funny choice of words! A dead tired man surrounded by the deads! It seems a book's or movie's incipit."
        y "Weren't you...saying something, before?"
        nnm "Oh, yes...but actually, I don't remember what it was."
        y "Maybe it wasn't important."
        nnm "Yeah, I don't know, it's just...just..."
        y "It's just...?"
        "A slow tear falls, directed towards the chin."
        nnm """
        All this loneliness...all this life...lost in nothingness.

        Maybe there's my mother out there. Or my father. Or my lover. All dead and then awakened.

        All of them lost in a slow and hungry crowd, howling at the sun and the moon, at us, trapped in this room.

        And this rifle...all these weapons we've created are useless in front of this!

        Who are we?
        What right do we have to decide who has to live and to die?
        Are we gods?
        """
        y "I...I don't think I can answer that...I'm sorry."
        nnm "No, I should be sorry. This anger I feel, directed to the whole world, the whole humanity...it's impossible to control it."
        jump passage10_end

label passage10_end2:
        nnm "In a world on the verge of ruin, our only choice is to kill or to be killed, isn't it?"
        y "It seems that's true..."
        nnm "Then tell me, why is it that I can't use my weapon anymore? Why, everytime I hold it in my hands, I just want to not use it anymore?"
        menu:
            "Maybe it's the desire of dying?":
                nnm "Could be. Maybe I'm tired of killing them and I've finally come to an understanding."
                y "What understanding?"
                nnm """
                That whatever controls this planet has decided that all humans shall disappear.

                You know the old story...we've destroyed nature, killed our similars, ruined ourselves and our spirits.

                Maybe we've reached our end. Our punishment.
                """
            "Cowardice, perhaps.":
                "He smiles, entartained by your answer."
                nnm """
                Cowardice, you say. It could be...yes, it could be. But I must say that, then, I'm happy with being a coward.

                From now on I'll let the killing to the stupid and will try to embrace what the planet, God or whatever controls us has decided to do with humanity.
                """
        menu:
            "That sounds political. Aren't you scared of that?":
                nnm "Sometimes to get political isn't a bad thing. Especially if you've spent your life avoiding all the politic stuff."
                jump passage10_end
            "That...I think you're right.":
                nnm "You can bet I'm right."
                jump passage10_end

label passage10_end:
    y """
    Look!

    It seems that...the night is over, now.
    """
    nnm "It's funny, since the dead's days seem to be only at the beginning."

    stop music fadeout (2)
    show black
    with fadehold

    $ persistent.passage_10 = True
    $ renpy.end_replay()

    return
