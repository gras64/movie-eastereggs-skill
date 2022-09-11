from mycroft import MycroftSkill, intent_file_handler


class MovieEastereggs(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('eastereggs.movie.intent')
    def handle_eastereggs_movie(self, message):
        self.speak_dialog('eastereggs.movie')


def create_skill():
    return MovieEastereggs()

