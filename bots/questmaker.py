#QuestGiver/bots/questmaker.py
import logging
import inflect
from random import randint
import nltk
nltk.download('brown')
nltk.download('universal_tagset')

logger = logging.getLogger()
inflector = inflect.engine()

minFreq = 1000

def generate_new_quest():
    """ Returns generated quest dialog.

    Format logic of returned string is:
        [Greeting] [traveller],
        [Please] [verb] for me [number] [adjective] [noun] [preposition] [proper noun]

    Example output:
        Greetings traveller,
        Could you please find for me three golden rocks of Lambert?

    Parameters:
        None

    Returns:
        quest (str): The string of complete quest dialogue to publish.
    
    """
    

    val_amount = randint(1,100)
    num = inflector.number_to_words(val_amount)

    plural_noun = inflector.plural(get_noun(),val_amount)

    quest = get_greeting() + ", "  \
        + get_traveller() + ".\n" \
        + get_please() + " " \
        + get_verb() + " for me " \
        + num + " " \
        + get_adjective() + " " \
        + plural_noun + " " \
        + get_preposition() + " " \
        + get_proper_noun() + "?"
    return quest

# def get_word(word_type):
#     val = rw.get_random_word(hasDictionaryDef="true",includePartOfSpeech=word_type, minCorpusCount=minFreq)
#     return val

# def get_words(word_type,num):
#     vals = rw.get_random_words(hasDictionaryDef="true",includePartOfSpeech=word_type, minCorpusCount=minFreq, limit=num)
#     return vals

class Request(object):
    def get_request(self,style):
        method_name = 'request_'+str(style)
        method = getattr(self,method_name,lambda :'Invalid')
        return method()

    def request_1(self):
        """ Request style with form:
        [Please] [verb] for me [number] [adjective] [noun] [preposition] [proper noun]

        Parameters:
            None

        Returns:
            greeting (str): The string denoting the greeting section of quest dialogue.
    
        """
        val_amount = randint(1,100)
        num = inflector.number_to_words(val_amount)

        verb = ""#get_word("verb")

        adj = ""#get_word("adjective")

        noun = ""#get_word("noun")
        plural_noun = inflector.plural(noun,val_amount)

        request = get_please() + " " \
            + verb + " for me " \
            + num + " " \
            + adj + " " \
            + plural_noun + " " \
            + get_preposition() + " " \
            + get_proper_noun() + "?"
        return request

    def request_2(self):
        """ Request style with form:
        [Please] get [noun], [noun], [noun], ..., and [noun] for me

        Parameters:
            None

        Returns:
            greeting (str): The string denoting the greeting section of quest dialogue.
    
        """
        val_amount = randint(3,8)

        nouns = []
        for x in range(val_amount):
            nouns.append(get_noun())
       
        nounlist = join(nouns)

        request = get_please() + " get " \
            + nounlist + " for me."
        return request

    def request_3(self):
        """ Request style with form:
        [Please] kill [proper noun], [proper noun], ..., and [proper noun] for [pronoun]

        Parameters:
            None

        Returns:
            greeting (str): The string denoting the greeting section of quest dialogue.
    
        """
        val_amount = randint(3,8)

        names = nltk.corpus.names



def get_greeting():
    """ Returns the greeting dialogue component.

    Parameters:
        None

    Returns:
        greeting (str): The string denoting the greeting section of quest dialogue.
    
    """
    greeting = ""
    return greeting

def get_traveller():
    """ Returns the traveller dialogue component between greeting and please.

    Parameters:
        None

    Returns:
        traveller (str): The string denoting the traveller section of quest dialogue.
    
    """
    traveller = ""
    return traveller

def get_please():
    """ Returns the "please" dialogue component between traveller and task.

    Parameters:
        None

    Returns:
        please (str): The string denoting the please section of quest dialogue.
    
    """
    please = ""
    return please

def get_verb():
    """ Returns the "verb" dialogue component between please and num.

    Parameters:
        None

    Returns:
        verb (str): The string denoting the verb section of quest dialogue.
    
    """
    tagged_words = nltk.corpus.brown.tagged_words(tagset="universal")
    verbs = [word for (word, tag) in tagged_words if tag == 'VERB']
    val = randint(0,len(verbs)-1)
    return verbs[val]

def get_num():
    """ Returns the number dialogue component between verb and adjective.

    Parameters:
        None

    Returns:
        num (str): The string denoting the number section of quest dialogue.
    
    """
    val = randint(1,100)
    num = inflector.number_to_words(val)
    return num

def get_adjective():
    """ Returns the adjective dialogue component between number and noun.

    Parameters:
        None

    Returns:
        adj (str): The string denoting the adjective section of quest dialogue.
    
    """
    tagged_words = nltk.corpus.brown.tagged_words(tagset="universal")
    adjs = [word for (word, tag) in tagged_words if tag == 'ADJ']
    val = randint(0,len(adjs)-1)
    return adjs[val]

def get_noun():
    """ Returns the noun dialogue component between adjective and preposition.

    Parameters:
        None

    Returns:
        noun (str): The string denoting the noun section of quest dialogue.
    
    """
    tagged_words = nltk.corpus.brown.tagged_words(tagset="universal")
    nouns = [word for (word, tag) in tagged_words if tag == 'NOUN']
    val = randint(0,len(nouns)-1)
    return nouns[val]

def get_preposition():
    """ Returns the preposition dialogue component between noun and proper noun.

    Parameters:
        None

    Returns:
        prep (str): The string denoting the preposition section of quest dialogue.
    
    """
    prep = ""
    return prep

def get_proper_noun():
    """ Returns the proper noun dialogue component at the end of the quest

    Parameters:
        None

    Returns:
        pnoun (str): The string denoting the proper noun section of quest dialogue.
    
    """
    tagged_words = nltk.corpus.brown.tagged_words(tagset="universal")
    nouns = [word for (word, tag) in tagged_words if tag == 'NOUN']
    val = randint(0,len(nouns)-1)
    return nouns[val]

if __name__ == "__main__":

    print(generate_new_quest())