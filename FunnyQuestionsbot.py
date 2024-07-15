import telebot
import random

bot = telebot.TeleBot("")

questions = ['Have you ever had a sex😏?', 'How old are you🧐?', 'Do you like russia?💩', 'Do you like Ukraine?', 'What is your favourite country?',
                 'What is your name?', 'What is your less favourite country?', 'How to poop?', 'Do you like go to the toilet for dancing?😂😂😂',
                 'In which countries have you ever been before?', 'Do you have a boyfriend/girlfriend?', 'Have you ever got a kiss?', 'Do you love someone?',
                 'Do you like watching skibidi toilets?😈', 'Have you ever seen a beaver?', 'Have you ever been in zoo?',
                 'Which continents have you ever visited?', 'Which countries did you visit?', 'Which animals did you see?', 'Do you like capybaras?',
                 'How are you?😀', 'What is your hobby?', 'What is your favourite computer game?', 'Who is your best friend?',
                 'How much did you eat poops?', 'How long do you go to the toilet for pooping', 'Where would you like to go?',
                 'Who is Caesar? Salad or commander of Roman army?', 'Where are you from?🗺', 'Who destroyed Arabian army in France?😎',
                 'Who first discovered america?', 'How long do you think you would survive in a zombie apocalypse?',
                 ' What is your favorite smell?', ' Have you ever gone a day without wearing underwear?', 'What do you think will your last words be?',
                 'What is it that you keep wanting to smell despite the fact that it does not smell particularly good?',
                 'What secret conspiracy would you like to actually start letting other people know?',
                 'If you can still remember, what are your funniest childhood memories?', 'What is the best Wi-Fi name you have seen in your entire life?',
                 'If you were a dog, which breed would you want to be?', 'How do you hang toilet paper: over or under?', 'Have you ever gone to a corner store and stolen a candy bar?',
                 'How many beers do you think I would be able to consume?', 'When would you like to have a 🔞?', 
                 'What would you do if you won a million dollars?', 'What is your Wi-Fi password?', 
                 'Why is it that round pizzas come in square boxes?', 'Where was the most embarrassing place you have ever farted?',
                 'Has someone caught you dancing in front of the mirror?', 'If I will fail a driver’s test, in which part will I fail?',
                 'Have you ever tried talking to your dog?', 'What would you do if you could live forever?', 'What would you call a male ladybug?',
                 'Do you like pineapple on your pizza?', ' Have you ever been caught cheating on a test?', 'Who was your first ever crush?',
                 'Do you sleep with lights on or off?', 'What is the silliest thing you have ever seen a stranger do in public?',
                 'If you could have a superpower, what would it be?', 'Do you have an imaginary friend?', ' Have you ever fallen off your bike in front of a huge crowd?',
                 'Are you scared of horror movies?', 'What is your favoutite movie?', 'How long is your 🍆?', 'What is your relationship to flirting',
                 'What is a size of your breast?', 'If you could be any age for the rest of your life, which would you choose?',
                 'What is your favorite animal?', 'What is your favorite family holiday tradition?', 'What is the most hilarious fact you know?',
                 'Do people drink or eat soup?', 'Do you have children?', 'Do you have a family?', 'Do you like breaking a pasta',
                 'Do you like to be alone?', 'In which would you like to live like middle ages, WW2 and etc?', 'Have you ever been arrested?',
                 'Who is your favourite actor', 'What is the wildest fantasy you’ve ever had?', 'What do you think your last meal would be if you were on death row?', 
                 'Which person do you know that totally reminds you of a character in a TV show or movie?', 'Did you once forget to bring your wallet when you’ve been scheduled to pay for a meal?',
                 'Do you still sleep with a stuffed toy?', 'What do you think is the worst thing that a person can put on their bio on a dating app?',
                 'Which species would be the rudest if all animals could talk?', 'What’s your preference: to be buried or be cremated?',
                 'What is the most creative insult you can think of?', 'Have you ever consumed so much alcohol that you passed out?',
                 'Do you think aliens really exist?', 'Do you like our work?', 'Do you want to try other our projects?',
                 'Have you ever been in a secret relationship?', 'Who is the first person on your hit list?',
                 ' Do you think the sea is salty because the shore never waves back at it?', 'Have you ever succeeded in making one of your parents cry?',
                 'Can you tell me the most hilarious joke you’ve heard?', 'What does the word “ok” mean for you?', 'Where would you like to time travel: back to the past or to the future?',
                 'What has been the funniest or strangest thing that has happened to you on a first date?', 'If you could choose any animated character, who would it be?',
                 'What has been the strangest thing a visitor has done at your home?', ' What musical instrument has the most annoying sound to you?',
                 'Have you ever been in a car crash where you were at fault?', 'What’s the biggest lie you have ever told?',
                 'What is the funniest thing you have ever seen in another person\'s house?', 'Have you ever secretly taken money from your parents\' pocket or purse?',
                 'Do you like the avtor of this bot?', 'What\'s your ideology?', 'Between Superman and Goku, who do you think would win?', 
                 'What is your deepest, darkest secret that no one else knows about?', 'What\'s the first thing you wash in the shower?',
                 'Do you have a habit of going for a walk while sleeping?', 'Are you scared about flying on a plane?', 'Have you experienced going skinny-dipping before?',
                 'Why do we say people work like dogs if they work all day, while dogs do nothing but lie around?',
                 'What are some of your clients\' or colleagues\' nicknames?', 'Have you accidentally glued your hands together when doing a craft project?',
                 'Which living individual, outside of your family, do you value the most?', 'Have you ever tried to punch me in the face because of what I\'ve done?',
                 'What do you want to be in your next birth, and why do you want to be that?', 'When was the last time you screwed anything up and no one noticed?',
                 'What\'s the worst tagline you can think of for a wart removal cream company?', 'What will people be nostalgic for in 500 years?',
                 'Have you ever been called out at school for wearing something embarrassing?', 'Are your friends real?',
                 'As a kid, what was your favorite color?',  'n terms of appearance, which athlete do you believe most closely resembles you?',
                 'In all honesty, what are some of your guilty pleasures that you are willing to admit?',
                 'What would you do if you could replace all of the grass on the planet with something else, and why?',
                 ' Who do you wish you could torture for the rest of your life?', 'How do you think who will destroy your life?',
                 'Which aspects of mine do you admire and which do you despise?', 'Would you rather be forced to wear shoes every second of your life or never be able to wear shoes again?',
                 'What would you do if you were an Ilon Mask?', 'Have you ever fired a gun?', 'Who would you appoint as the president of the internet, and why?',
                 'Have you ever offered to help anyone else with their homework in return for something specific?',
                 'If we were to have a boxing match, who do you think would win?', 'What’s the weirdest thing you\'ve given someone as a gift?',
                 'What do you think the first person to milk a cow was actually trying to do?', ' How many ants would it take to lift an elephant?',
                 'Have you ever approached a stranger and said something that later turned out to be your best friend?',
                 'Can you tell me one memory that you’ve never shared with me?', 'Which movie would you want it to be if your life was a movie?',
                 'What is the soundtrack of your life?', 'Do you like watching anime?', 'What\'s your favourite type of music?',
                 'What is your most liked anime?', 'What was the make and model of your first car?', 'If you could to see a person by a secret camera whom would you like to see?',
                 'What\'s your favorite sport to watch?', 'What\'s your dream career?', 'Which unconventional animal do you wish you could have as a pet?',
                 'Do you have a favorite memory?']

questions_German = ['Hatten Sie jemals Sex😏?', 'Wie alt sind Sie?', 'Magst du Russland? 💩', 'Magst du die Ukraine?', 'Was ist dein Lieblingsland?',
                  'Wie heißt du?', 'Welches ist dein weniger Lieblingsland?', 'Wie kacke ich?', 'Gehst du gerne zum Tanzen auf die Toilette?😂😂😂',
                  'In welchen Ländern warst du schon einmal?', 'Hast du einen Freund/eine Freundin?', 'Hast du jemals einen Kuss bekommen?', 'Liebst du jemanden?',
                  'Schauen Sie gerne Skibidi-Toiletten zu? 😈', 'Haben Sie schon einmal einen Biber gesehen?', 'Waren Sie schon einmal im Zoo?',
                  'Welche Kontinente haben Sie schon einmal besucht?', 'Welche Länder haben Sie besucht?', 'Welche Tiere haben Sie gesehen?', 'Magst du Wasserschweine?',
                  'Wie geht es dir? 😀', 'Was ist dein Hobby?', 'Was ist dein Lieblingscomputerspiel?', 'Wer ist dein bester Freund?',
                  'Wie viel hast du Kacke gegessen?', 'Wie lange gehst du zum Kacken auf die Toilette', 'Wohin würdest du gerne gehen?',
                  'Wer ist Cäsar? Salat oder Befehlshaber der römischen Armee?', 'Woher kommst du?🗺', 'Wer hat die arabische Armee in Frankreich zerstört?😎',
                  'Wer hat Amerika zuerst entdeckt?', 'Wie lange würden Sie Ihrer Meinung nach in einer Zombie-Apokalypse überleben?',
                  'Was ist Ihr Lieblingsgeruch?', 'Haben Sie jemals einen Tag ohne Unterwäsche verbracht?', 'Was werden Ihrer Meinung nach Ihre letzten Worte sein?',
                  'Was möchten Sie immer wieder riechen, obwohl es nicht besonders gut riecht?',
                  'Welche geheime Verschwörung würden Sie gerne anderen Menschen mitteilen?',
                  'Wenn Sie sich noch erinnern können, was sind Ihre lustigsten Kindheitserinnerungen?', 'Was ist der beste Wi-Fi-Name, den Sie in Ihrem ganzen Leben gesehen haben?',
                  'Wenn Sie ein Hund wären, welche Rasse würden Sie gerne haben?', 'Wie hängt man Toilettenpapier auf: darüber oder darunter?', 'Sind Sie jemals in einen Laden um die Ecke gegangen und haben einen Schokoriegel gestohlen?',
                  'Wie viele Biere könnte ich wohl trinken?', 'Wann hättest du gerne ein 🔞?',
                  'Was würden Sie tun, wenn Sie eine Million Dollar gewinnen würden?', 'Wie lautet Ihr WLAN-Passwort?',
                  'Warum gibt es runde Pizzen in quadratischen Schachteln?', 'Wo war der peinlichste Ort, an dem du jemals gefurzt hast?',
                  'Hat dich jemand dabei erwischt, wie du vor dem Spiegel tanzt?', 'Wenn ich bei einer Fahrerprüfung durchfallen werde, in welchem Teil werde ich durchfallen?',
                  'Haben Sie jemals versucht, mit Ihrem Hund zu sprechen?', 'Was würden Sie tun, wenn Sie ewig leben könnten?', 'Wie würden Sie einen männlichen Marienkäfer nennen?',
                  'Mögen Sie Ananas auf Ihrer Pizza?', 'Wurden Sie jemals beim Schummeln bei einem Test erwischt?', 'In wen waren Sie zum ersten Mal verknallt?',
                  'Schlafen Sie mit an- oder ausgeschaltetem Licht?', 'Was ist das Dümmste, was Sie je von einem Fremden in der Öffentlichkeit gesehen haben?',
                  'Wenn du eine Superkraft haben könntest, welche wäre das?', 'Hast du einen imaginären Freund?', 'Bist du jemals vor einer großen Menschenmenge vom Fahrrad gefallen?',
                  'Hast du Angst vor Horrorfilmen?', 'Welcher ist dein Lieblingsfilm?', 'Wie lang ist dein 🍆?', 'Welche Beziehung hast du zum Flirten?',
                  'Wie groß ist Ihre Brust?', 'Wenn Sie für den Rest Ihres Lebens in welchem Alter bleiben könnten, welches würden Sie wählen?',
                  'Welches ist Ihr Lieblingstier?', 'Was ist Ihre liebste Familienurlaubstradition?', 'Was ist die lustigste Tatsache, die Sie kennen?',
                  'Trinken oder essen die Leute Suppe?', 'Haben Sie Kinder?“', 'Haben Sie eine Familie?', 'Brechen Sie gerne Nudeln',
                  'Möchten Sie allein sein?', 'Wo würden Sie gerne leben, etwa im Mittelalter, im Zweiten Weltkrieg usw.?', 'Wurden Sie schon einmal verhaftet?',
                  'Wer ist Ihr Lieblingsschauspieler', 'Was ist die wildeste Fantasie, die Sie je hatten?', 'Was glaubst du, dass deine letzte Mahlzeit wäre, wenn du in der Todeszelle wärst?',
                  'Welche Person kennen Sie, die Sie völlig an eine Figur aus einer Fernsehsendung oder einem Film erinnert?', 'Haben Sie einmal vergessen, Ihr Portemonnaie mitzubringen, als Sie für eine Mahlzeit bezahlen mussten?',
                  'Schläfst du immer noch mit einem Stofftier?', 'Was ist deiner Meinung nach das Schlimmste, was eine Person in einer Dating-App in ihre Biografie aufnehmen kann?',
                  'Welche Tierart wäre die unhöflichste, wenn alle Tiere sprechen könnten?', 'Was bevorzugen Sie: begraben oder eingeäschert zu werden?',
                  'Was ist die kreativste Beleidigung, die Ihnen einfällt?', 'Haben Sie schon einmal so viel Alkohol getrunken, dass Sie ohnmächtig geworden sind?',
                  'Glauben Sie, dass Außerirdische wirklich existieren?', 'Gefällt Ihnen unsere Arbeit?', 'Möchten Sie andere unserer Projekte ausprobieren?',
                  'Waren Sie jemals in einer geheimen Beziehung?', 'Wer ist die erste Person auf Ihrer Abschussliste?',
                  'Glauben Sie, dass das Meer salzig ist, weil das Ufer nie zurückweht?', 'Ist es Ihnen jemals gelungen, einen Ihrer Eltern zum Weinen zu bringen?',
                  'Können Sie mir den lustigsten Witz erzählen', 'den Sie je gehört haben?', 'Was bedeutet das Wort ok für Sie?']

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '<b>Hi</b>, <em>I am a bot where You can send you a funny messages</em>. With this bot you can spend your time funny with your time'+
                     ''' If you want to generate question write: /sendquestion . If you are intrested into how many questions knows write: /showhowmanypharasesknow , to guess number write: /guessnumber, to change langiage write: /changelanguage. Have fun :)''', parse_mode='html')
    
@bot.message_handler(commands=['sendquestion'])
def question(message):
    send = random.choice(questions)

    bot.reply_to(message, f'{send}')


@bot.message_handler(commands=['showhowmanypharasesknow'])
def count(message):
    count = len(questions)
    bot.send_message(message.chat.id, f'This bot knows {count + 1} phrases to ask you')

@bot.message_handler(commands=['changelanguage'])
def languagechange(message):
    pass

@bot.message_handler(commands=['guessnumber'])
def guess_random_num(message):
    pass

@bot.message_handler(commands=['otherbots'])
def other_bots(message):
    bot.send_message(message.chat.id, '''There\'s other our bots: 
There's bots of our partners:
OnlapusTeam🦾:
1.https://t.me/OnlapiaBot - this is an AI bot in telegram in Ukrainian language😎.
2.https://t.me/True_Or_Truee_Bot - is another bot with funny questions but in Ukrainian language too.
    If you want to see what changed in our other programs so subsrcibe to our channel:https://t.me/onlapus
                     
Glory to UKraine!!!-🇺🇦''')
    
@bot.message_handler(commands=['aboutus'])
def about_us(message):
    bot.send_message(message.chat.id , 'The developer of this bot is from Ukraine. More about us is in our news channel: https://t.me/onlapus.')
    

bot.polling(none_stop=True)
