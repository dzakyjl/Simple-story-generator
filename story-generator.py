import random


when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 27th June']
who = ['a cat', 'a mouse', 'a turtle','a capybara']
name = ['Ali', 'Miriam', 'daniel', 'Houki', 'Dartvader']
residense = ['Barcelona', 'Indonesia', 'Germany', 'England', 'Japan']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'Eats a sate padang','found a treasure', 'solved a mistery', 'wrote a book' ]
print(random.choice(when) + ', ' + random.choice(who), ' that lived in ' + random.choice(residense) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))