from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page
)
import random


author = 'Michael Rose <michael_rose@gmx.de>'

doc = """
otdm provides an easy way of creating experiments to measure the temporal discounting of money
using the Direct Method (DM) [Attema et al., 2016]
"""


class Constants(BaseConstants):
    name_in_url = 'otdm'
    players_per_group = None
    num_attention_check_tries = 2
    num_game_rounds = 3
    num_rounds = num_attention_check_tries + num_game_rounds - 1
    payment_per_correct_answer = 1
    QUESTION_1_TEXT = "Which of the following statements is true?"
    QUESTION_1_ANSWER = "future"

    QUESTION_2_TEXT = "Suppose you are 80% certain that your decisions actually correspond to how much the different choice options are worth to you. Which button should you click in this case?"
    QUESTION_2_ANSWER = "80%"

    QUESTION_3_TEXT = "When we ask you how certain you are about how much different payments are worth to you at different points in time, then which type of uncertainty are we interested in?"
    QUESTION_3_ANSWER = "value"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class AddNumbers(Page):
    form_model = "player"
    form_fields = ["number_entered"]

    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries

    def vars_for_template(self):
        number_1 = random.randint(0,100)
        number_2 = random.randint(0, 100)
        self.player.correct_result = number_1 + number_2
        return {
            "number_1": number_1,
            "number_2": number_2,
        }

    def before_next_page(self):
        if self.player.number_entered == self.player.correct_result:
            self.player.payoff = Constants.payment_per_correct_answer


class Player(BasePlayer):
    age = models.StringField(
        label="How old are you?",
        choices=["Under 18", "18-24 years old", "25-34 years old", "35-44 years old", "45-54 years old", "55-64 years old", "65+ years old"]
    )
    gender = models.StringField(
        label="How do you describe yourself?",
        choices=["Male", "Female", "Non-binary / third gender", "Prefer not to say"]
    )
    education = models.StringField(
        label="What is the highest level of education you have completed?",
        choices=["Some high school or less", "High school diploma or GED", "Some college, but no degree", "Associates or technical degree", "Bachelor’s degree", "Graduate or professional degree (MA, MS, MBA, PhD, JD, MD, DDS etc.)", "Prefer not to say"]
    )
    employment = models.StringField(
        label="What best describes your employment status over the last three months?",
        choices=["Working full-time", "Working part-time", "Unemployed and looking for work", "A homemaker or stay-at-home parent", "Student", "Retired", "Other"]
    )
    income = models.StringField(
        label="What was your total household income before taxes during the past 12 months?",
        choices=["Less than $25,000", "$25,000-$49,999", "$50,000-$74,999", "$75,000-$99,999", "$100,000-$149,999", "$150,000 or more", "Prefer not to say"]
    )
    zipcode = models.IntegerField(label="What is your US Zip Code?")

    question_1_answer = models.StringField(
        choices=[
            ('future',
             'In making my decisions, I am asked to assume that I will actually receive all payments as indicated, regardless of whether they take place now or in the future.'),
            ('less_likely_future',
             'In making my decisions, I am asked to assume that it is less likely that I will actually receive payments that are meant to take place in the future.'),
            ('now',
             'In making my decisions, I am asked to assume that it is less likely that I will actually receive payments that are meant to take place now.')
        ],
        label="",
        widget=widgets.RadioSelect  # Use widgets.RadioSelect here
    )
    question_2_answer = models.StringField(
        choices=[(f"{i}%", f"{i}%") for i in range(0, 101, 5)],
        label="",
        widget=widgets.RadioSelectHorizontal  # 仍然使用 widgets.RadioSelect
    )
    question_3_answer = models.StringField(
        choices=[
            ('receipt', 'Uncertainty about whether I would actually receive the payments.'),
            ('value',
             'Uncertainty about how much I value the payments, assuming that I know I would receive them with certainty.')
        ],
        label="",
        widget=widgets.RadioSelect  # And also here
    )

    attention_check_rounds = models.IntegerField(label="How many rounds dose the experiment have?")
    attention_check_payment = models.FloatField(label="How much are you paid per correct answer?")
    number_entered = models.IntegerField(label="Please enter the result.")
    correct_result = models.IntegerField()


    current_step = models.IntegerField(initial=1)
    """Current step the player is in
    
    Equals the elicitation round, i.e. ranges from 1 (for c12) to 5 (c78).
    """


    # IMPORTANT: DO NOT CHANGE THE VARIABLE NAMES FOR THE c values!

    c12 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/2)"""

    c14 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/4)"""

    c34 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(3/4)"""

    c4 = models.IntegerField(initial=-1)


    c5 = models.IntegerField(initial=-1)


    c6 = models.IntegerField(initial=-1)

    def goto_next_step(self) -> None:
        """Advances the player to the next step

        Should be called after each `ChoiceListPage`
        """
        self.current_step = self.current_step + 1

    def cancel_game(self) -> None:
        """Sets the indicator that an invalid choice occurred"""
        self.current_step = -1

    def get_current_step(self) -> int:
        """Get the current step the player is in
        :return: current step (1-based)
        """
        return self.current_step


class Instructions(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["failed_attention_check"]



class FailedAttentionCheck(Page):
    def is_displayed(self):
        return self.participant.vars["failed_attention_check"]



class Results(Page):
    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries