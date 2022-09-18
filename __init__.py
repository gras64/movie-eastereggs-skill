from mycroft import MycroftSkill, intent_file_handler


class MovieEastereggs(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

# Game of Thrones

    @intent_file_handler('valar.morgulis.intent')
    def handle_valar_morgulis(self, message):
        self.speak_dialog('valar.dohaeris')

# Harry Potter

    @intent_file_handler('lumus.intent')
    def handle_lumus(self, message):
        self.speak_dialog('lumus')

    @intent_file_handler('obliviate.intent')
    def handle_forgott(self, message):
        self.speak_dialog('obliviate')

    @intent_file_handler('levitation.charm.intent')
    def handle_fly(self, message):
        self.speak_dialog('levitation.charm')

# Rambo III

    @intent_file_handler('What.is.that.intent')
    def handle_what_is_that(self, message):
        favorite_flavor = self.get_response('thats.blue.light', validator=None, on_fail=None, num_retries=- 1)
        self.speak_dialog('it.glows.blue')

# Star wars

    @intent_file_handler('i.love.you.intent')
    def handle_i_love_you(self, message):
        self.speak_dialog('i.konw')

    @intent_file_handler('im.going.to.pee.now.intent')
    def handle_pee_now(self, message):
        self.speak_dialog('to.much.information')

# Lord of the Rings   

    @intent_file_handler('whatever.luck.brings.intent')
    def handle_frinds_with_you(self, message):
        favorite_flavor = self.get_response('your.friends.are.with.you', validator=None, on_fail=None, num_retries=- 1)
        self.speak_dialog('they.too.survive.night')

    @intent_file_handler('i.never.thought.die.intent')
    def handle_side_by_side(self, message):
        self.speak_dialog('side.side.by.frind')

# The Hitchhiker’s Guide to the Galaxy

    @intent_file_handler('hand.towel.intent')
    def handle_hand_towel(self, message):
        self.speak_dialog('hand.towel')

    @intent_file_handler('big.question.intent')
    def handle_big_question(self, message):
        self.speak_dialog('big.question')


def create_skill():
    return MovieEastereggs()

