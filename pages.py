from math import floor

from typing import List
import random
from random import choice

from ._builtin import Page, WaitPage
from .choices import ChoiceManager
from .models import Constants
from .config import GAIN_PER_WEEK, NUM_WEEKS, NUM_DAYS

class AttentionCheck1(Page):
    form_model = 'player'
    form_fields = ['question_1_answer', 'question_2_answer', 'question_3_answer']

    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["failed_attention_check"]

    def vars_for_template(self):
        return {
            'question_1_text': Constants.QUESTION_1_TEXT,
            'question_2_text': Constants.QUESTION_2_TEXT,
            'question_3_text': Constants.QUESTION_3_TEXT,
            'choices_2': [f"{i}%" for i in range(0, 101, 5)]  # 这是第二个问题的选项
        }

    def before_next_page(self):
        # 检查玩家的答案是否正确
        if (self.player.question_1_answer == Constants.QUESTION_1_ANSWER and
                self.player.question_2_answer == Constants.QUESTION_2_ANSWER and
                self.player.question_3_answer == Constants.QUESTION_3_ANSWER):
            self.participant.vars["failed_attention_check"] = False
        else:
            self.participant.vars["failed_attention_check"] = True
            self.participant.vars["attention_check_attempts"] = self.participant.vars.get("attention_check_attempts",
                                                                                          0) + 1


class Checkin(Page):
    pass

class BasicInstruction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["failed_attention_check"]


class DecisionScreen1(Page):
    pass

class DecisionScreen2(Page):
    pass

class Instruction1(Page):
    pass

class Instruction2(Page):
    pass

class Demographic(Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "employment", "income", "zipcode"]

class FailedAttentionCheck(Page):
    def is_displayed(self):
        return self.participant.vars["failed_attention_check"]


class ChoiceList1(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList2(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList3(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList4(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList5(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList6(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList7(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList8(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList9(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList10(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList11(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList12(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList13(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList14(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ChoiceList15(Page):
    """
    Displays a list of choices to the player to elicitate a certain c value.
    """

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Results(Page):
    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries

choicelist_groups = [
    [ChoiceList4, ChoiceList5, ChoiceList6],
    [ChoiceList7, ChoiceList8, ChoiceList9],
    [ChoiceList10, ChoiceList11, ChoiceList12],
]

chosen_group = choice(choicelist_groups)

page_sequence = [
    BasicInstruction,
    DecisionScreen1,
    DecisionScreen2,
    AttentionCheck1,
    FailedAttentionCheck,
    ChoiceList1,
    ChoiceList2,
    ChoiceList3,
    Instruction1,
    *chosen_group,
    Instruction2,
    ChoiceList13,
    ChoiceList14,
    ChoiceList15,
    ResultsWaitPage,
    Results
]

