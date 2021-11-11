import random
random.seed(9472)



class Banger:

  def sendTweet(self):
    tweets = ['mfs be like slenderman. angrier and angrier as i collect more paper', 'women are always cold due to original sin', '17 years olds r running those boba shops like it\'s the navy', 'i am no longer mentally ill', 'be very careful john', '\"are you ok?\" no i need to be cast in a weird ass A24 movie', 'wearing a basic outfit but in a dakota johnson girlboss farmers market alexa chung everlane santal 33 glossier boybrow mid century modern curtain bangs the bell jar in my tote bag kind of way', 'i have faced more peer pressure to drink oat milk than to do drugs', 'Let\'s see Paul Allen\'s Picrew.', 'philosophy sounds so exhausting why do u people wanna think so bad', 'i\'m tired of shows based around high school can we get coming of age 20 something shit...i wanna see a bitches card get declined at trader joe\'s', 'all i want is to post cringe without facing consequences', 'hatsune miku has been cancelled', 'laughing like the joker on the bus', 'has anyone tried making edibles but without weed? like virgin edibles or something', 'wearing airpods in bed feeling like the wife in fahrenheit 451', 'white people love \"getting their steps in\"', 'I\'ve been up for 5 hours. I\'ve already ran 12 miles. I\'ve had 2 protein shakes and done 300 burpees. We are on opposite ends of the spectrum. I\'ll be there at 1045 putting in the work to be the best I can be. Just like I do every single day.', 'And you smell like a roll of nickels', 'Ok girl, can we finally make those darn songs now that Apartheid Clyde is out of the way?','I have been a professional medium for 15 and a half years and am VERY sensitive to all of the energy forces that surround us. The instructors are great and the facility is clean but when I walked into the studio I was ASSAULTED by the dark energy radiating from Monica at the front desk.', 'Exactly 27 years ago I came into this world crying and shitting. Not much has changed']
    j = len(tweets)
    i = random.randint(0, j-1)
    return tweets[i]


