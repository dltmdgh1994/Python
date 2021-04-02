# -*- ecoding: utf-8 -*-
import hanspell

def checkSpell(reviews):
    review = []
    for r in reviews:
        try:
            result = hanspell.spell_checker.check(r)
            review.append(result.checked)
            print(result.checked)
        except:
            review.append('')

    return review
